import os

import pyqtgraph as pg
from bec_lib.core import MessageEndpoints
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QWidget
from pyqtgraph import mkPen, mkBrush
from PyQt5 import uic

from bec_widgets.bec_dispatcher import bec_dispatcher
from bec_widgets.qt_utils import Crosshair, Colors

# just for demonstration purposes is script run directly
config_simple = {
    "plot_settings": {
        "background_color": "black",
        "num_columns": 2,
        "colormap": "plasma",
        "scan_types": False,
    },
    "plot_data": [
        {
            "plot_name": "BPM4i plots vs samx",
            "x": {
                "label": "Motor Y",
                "signals": [{"name": "samx", "entry": "samx"}],
            },
            "y": {
                "label": "bpm4i",
                "signals": [{"name": "bpm4i", "entry": "bpm4i"}],
            },
        },
        {
            "plot_name": "Gauss plots vs samx",
            "x": {
                "label": "Motor X",
                "signals": [{"name": "samx", "entry": "samx"}],
            },
            "y": {
                "label": "Gauss",
                "signals": [{"name": "gauss_bpm", "entry": "gauss_bpm"}],
            },
        },
    ],
}


class BECMonitor(pg.GraphicsLayoutWidget):
    update_signal = pyqtSignal()

    def __init__(
        self, parent=None, client=None, config: dict = None, enable_crosshair: bool = False
    ):
        super(BECMonitor, self).__init__(parent=parent)

        # Client and device manager from BEC
        self.client = bec_dispatcher.client if client is None else client
        self.dev = self.client.device_manager.devices

        # Connect slots dispatcher
        bec_dispatcher.connect_slot(self.on_scan_segment, MessageEndpoints.scan_segment())

        # Current configuration
        self.config = config

        # Enable crosshair
        self.enable_crosshair = enable_crosshair

        # Displayed Data
        self.data = {}

        self.crosshairs = None
        self.plots = None
        self.curves_data = None
        self.grid_coordinates = None
        self.scanID = None

        self.user_colors = {}  # key: (plot_name, y_name, y_entry), value: color

        # Connect the update signal to the update plot method #TODO enable when update is fixed
        self.proxy_update_plot = pg.SignalProxy(
            self.update_signal, rateLimit=25, slot=self.update_plot
        )

        # Init UI
        if self.config is None:
            print("No initial config found for BECDeviceMonitor")
        else:
            self.update_config(self.config)

    def _init_config(self):
        """
        Initializes or update the configuration settings for the PlotApp.
        """

        # Separate configs
        self.plot_settings = self.config.get("plot_settings", {})
        self.plot_data_config = self.config.get("plot_data", {})
        self.scan_types = self.plot_settings.get("scan_types", False)

        if self.scan_types is False:  # Device tracking mode
            self.plot_data = self.plot_data_config  # TODO logic has to be improved
        else:  # without incoming data setup the first configuration to the first scan type sorted alphabetically by name
            self.plot_data = self.plot_data_config[min(list(self.plot_data_config.keys()))]

        # TODO init plot background -> so far not used, I don't like how it is done in extreme.py

        # Initialize the UI
        self._init_ui(self.plot_settings["num_columns"])

    def _init_ui(self, num_columns: int = 3) -> None:
        """
        Initialize the UI components, create plots and store their grid positions.

        Args:
            num_columns (int): Number of columns to wrap the layout.

        This method initializes a dictionary `self.plots` to store the plot objects
        along with their corresponding x and y signal names. It dynamically arranges
        the plots in a grid layout based on the given number of columns and dynamically
        stretches the last plots to fit the remaining space.
        """
        self.clear()
        self.plots = {}
        self.grid_coordinates = []

        num_plots = len(self.plot_data)

        # Check if num_columns exceeds the number of plots
        if num_columns >= num_plots:
            num_columns = num_plots
            self.plot_settings["num_columns"] = num_columns  # Update the settings
            print(
                f"Warning: num_columns in the YAML file was greater than the number of plots. Resetting num_columns to number of plots:{num_columns}."
            )
        else:
            self.plot_settings["num_columns"] = num_columns  # Update the settings

        num_rows = num_plots // num_columns
        last_row_cols = num_plots % num_columns
        remaining_space = num_columns - last_row_cols

        for i, plot_config in enumerate(self.plot_data):
            row, col = i // num_columns, i % num_columns
            colspan = 1

            if row == num_rows and remaining_space > 0:
                if last_row_cols == 1:
                    colspan = num_columns
                else:
                    colspan = remaining_space // last_row_cols + 1
                    remaining_space -= colspan - 1
                    last_row_cols -= 1

            plot_name = plot_config.get("plot_name", "")
            x_label = plot_config["x"].get("label", "")
            y_label = plot_config["y"].get("label", "")

            plot = self.addPlot(row=row, col=col, colspan=colspan, title=plot_name)
            plot.setLabel("bottom", x_label)
            plot.setLabel("left", y_label)
            plot.addLegend()

            self.plots[plot_name] = plot
            self.grid_coordinates.append((row, col))

        self.init_curves()

    def init_curves(self) -> None:
        """
        Initialize curve data and properties, and update table row labels.

        This method initializes a nested dictionary `self.curves_data` to store
        the curve objects for each x and y signal pair. It also updates the row labels
        in `self.tableWidget_crosshair` to include the grid position for each y-value.
        """
        self.curves_data = {}
        row_labels = []

        for idx, plot_config in enumerate(self.plot_data):
            plot_name = plot_config.get("plot_name", "")
            plot = self.plots[plot_name]
            plot.clear()

            y_configs = plot_config["y"]["signals"]
            colors_ys = Colors.golden_angle_color(
                colormap=self.plot_settings["colormap"], num=len(y_configs)
            )

            curve_list = []
            for i, (y_config, color) in enumerate(zip(y_configs, colors_ys)):
                y_name = y_config["name"]
                y_entries = y_config.get("entry", [y_name])

                if not isinstance(y_entries, list):
                    y_entries = [y_entries]

                for y_entry in y_entries:
                    user_color = self.user_colors.get((plot_name, y_name, y_entry), None)
                    color_to_use = user_color if user_color else color

                    pen_curve = mkPen(color=color_to_use, width=2, style=QtCore.Qt.DashLine)
                    brush_curve = mkBrush(color=color_to_use)

                    curve_data = pg.PlotDataItem(
                        symbolSize=5,
                        symbolBrush=brush_curve,
                        pen=pen_curve,
                        skipFiniteCheck=True,
                        name=f"{y_name} ({y_entry})",
                    )

                    curve_list.append((y_name, y_entry, curve_data))
                    plot.addItem(curve_data)
                    row_labels.append(f"{y_name} ({y_entry}) - {plot_name}")

            self.curves_data[plot_name] = curve_list

        # Hook Crosshair
        if self.enable_crosshair == True:
            self.hook_crosshair()

    def hook_crosshair(self) -> None:
        """Hook the crosshair to all plots."""
        # TODO can be extended to hook crosshair signal for mouse move/clicked
        self.crosshairs = {}
        for plot_name, plot in self.plots.items():
            crosshair = Crosshair(plot, precision=3)
            self.crosshairs[plot_name] = crosshair

    def update_plot(self) -> None:
        """Update the plot data based on the stored data dictionary."""
        for plot_name, curve_list in self.curves_data.items():
            for y_name, y_entry, curve in curve_list:
                x_config = next(
                    (pc["x"] for pc in self.plot_data if pc.get("plot_name") == plot_name), {}
                )
                x_signal_config = x_config["signals"][0]
                x_name = x_signal_config.get("name", "")
                x_entry = x_signal_config.get("entry", x_name)

                key = (x_name, x_entry, y_name, y_entry)
                data_x = self.data.get(key, {}).get("x", [])
                data_y = self.data.get(key, {}).get("y", [])

                curve.setData(data_x, data_y)

    def get_config(self):
        """Return the current configuration settings."""
        return self.config

    def show_config_dialog(self):
        """Show the configuration dialog."""
        from .config_dialog import ConfigDialog

        dialog = ConfigDialog(default_config=self.config)
        dialog.config_updated.connect(self.update_config)
        dialog.show()

    def update_client(self, client) -> None:
        """Update the client and device manager from BEC.
        Args:
            client: BEC client
        """
        self.client = client
        self.dev = self.client.device_manager.devices

    @pyqtSlot(dict)
    def update_config(self, config: dict) -> None:
        """
        Update the configuration settings for the PlotApp.
        Args:
            config(dict): Configuration settings
        """
        self.config = config
        self._init_config()

    @pyqtSlot(dict, dict)
    def on_scan_segment(self, msg, metadata):
        """
        Handle new scan segments and saves data to a dictionary. Linked through bec_dispatcher.

        Args:
            msg (dict): Message received with scan data.
            metadata (dict): Metadata of the scan.
        """
        # TODO logic can be separated into different methods or there could be separate class for scan data handling
        # TODO for scan mode, if there are same names for different plots, the data are assigned multiple times
        current_scanID = msg.get("scanID", None)
        if current_scanID is None:
            return

        if current_scanID != self.scanID:
            if self.scan_types is False:
                self.plot_data = self.plot_data_config
            elif self.scan_types is True:
                currentName = metadata.get("scan_name")
                if currentName is None:
                    raise ValueError(
                        f"Scan name not found in metadata. Please check the scan_name in the YAML config or in bec "
                        f"configuration."
                    )
                self.plot_data = self.plot_data_config.get(currentName, [])
                if self.plot_data == []:
                    raise ValueError(
                        f"Scan name {currentName} not found in the YAML config. Please check the scan_name in the "
                        f"YAML config or in bec configuration."
                    )

                # Init UI
                self._init_ui(self.plot_settings["num_columns"])

            self.scanID = current_scanID
            self.data = {}
            self.init_curves()

        for plot_config in self.plot_data:
            plot_name = plot_config.get("plot_name", "Unnamed Plot")
            x_config = plot_config["x"]
            x_signal_config = x_config["signals"][0]  # Assuming there's at least one signal for x

            x_name = x_signal_config.get("name", "")
            if not x_name:
                raise ValueError(f"Name for x signal must be specified in plot: {plot_name}.")

            x_entry_list = x_signal_config.get("entry", [])
            if not x_entry_list:
                x_entry_list = (
                    self.dev[x_name]._hints if hasattr(self.dev[x_name], "_hints") else [x_name]
                )

            if not isinstance(x_entry_list, list):
                x_entry_list = [x_entry_list]

            y_configs = plot_config["y"]["signals"]

            for x_entry in x_entry_list:
                for y_config in y_configs:
                    y_name = y_config.get("name", "")
                    if not y_name:
                        raise ValueError(
                            f"Name for y signal must be specified in plot: {plot_name}."
                        )

                    y_entry_list = y_config.get("entry", [])
                    if not y_entry_list:
                        y_entry_list = (
                            self.dev[y_name]._hints
                            if hasattr(self.dev[y_name], "_hints")
                            else [y_name]
                        )

                    if not isinstance(y_entry_list, list):
                        y_entry_list = [y_entry_list]

                    for y_entry in y_entry_list:
                        key = (x_name, x_entry, y_name, y_entry)

                        data_x = msg["data"].get(x_name, {}).get(x_entry, {}).get("value", None)
                        data_y = msg["data"].get(y_name, {}).get(y_entry, {}).get("value", None)

                        if data_x is None:
                            raise ValueError(
                                f"Incorrect entry '{x_entry}' specified for x in plot: {plot_name}, x name: {x_name}"
                            )

                        if data_y is None:
                            if hasattr(self.dev[y_name], "_hints"):
                                raise ValueError(
                                    f"Incorrect entry '{y_entry}' specified for y in plot: {plot_name}, y name: {y_name}"
                                )
                            else:
                                raise ValueError(
                                    f"No hints available for y in plot: {plot_name}, and name '{y_name}' did not work as entry"
                                )

                        if data_x is not None:
                            self.data.setdefault(key, {}).setdefault("x", []).append(data_x)

                        if data_y is not None:
                            self.data.setdefault(key, {}).setdefault("y", []).append(data_y)

        self.update_signal.emit()


if __name__ == "__main__":  # pragma: no cover
    import sys
    from bec_widgets.bec_dispatcher import bec_dispatcher

    client = bec_dispatcher.client
    client.start()

    app = QApplication(sys.argv)
    monitor = BECMonitor()
    monitor.show()
    sys.exit(app.exec_())
