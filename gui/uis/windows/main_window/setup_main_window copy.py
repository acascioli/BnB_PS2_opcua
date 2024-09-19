# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from numpy.random.mtrand import f
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from . functions_main_window import *
import sys
import os

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import *

# MAIN FUNCTIONS
# ///////////////////////////////////////////////////////////////
from . functions_main_window import *

# PY WINDOW
# ///////////////////////////////////////////////////////////////


class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon": "icon_home.svg",
            "btn_id": "btn_home",
            "btn_text": "Home",
            "btn_tooltip": "Home page",
            "show_top": True,
            "is_active": True
        },
        {
            "btn_icon": "icon_exclamation_triangle.svg",
            "btn_id": "btn_alert",
            "btn_text": "Alerts",
            "btn_tooltip": "Show alert's details",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_table.svg",
            "btn_id": "btn_variables",
            "btn_text": "Variables",
            "btn_tooltip": "Show variables",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_graph_up.svg",
            "btn_id": "btn_charts",
            "btn_text": "Charts",
            "btn_tooltip": "Open charts",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_folder_open.svg",
            "btn_id": "btn_open_file",
            "btn_text": "Open File",
            "btn_tooltip": "Open file",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_save.svg",
            "btn_id": "btn_save",
            "btn_text": "Save File",
            "btn_tooltip": "Save file",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_info.svg",
            "btn_id": "btn_info",
            "btn_text": "Information",
            "btn_tooltip": "Open information",
            "show_top": False,
            "is_active": False
        },
        {
            "btn_icon": "icon_close.svg",
            "btn_id": "btn_exit",
            "btn_text": "Exit",
            "btn_tooltip": "Close the session",
            "show_top": False,
            "is_active": False
        }
    ]

    # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        {
            "btn_icon": "icon_search.svg",
            "btn_id": "btn_search",
            "btn_tooltip": "Search",
            "is_active": False
        },
        {
            "btn_icon": "icon_settings.svg",
            "btn_id": "btn_top_settings",
            "btn_tooltip": "Top settings",
            "is_active": False
        }
    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self, uaclient):
        self.uaclient = uaclient
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])

        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(
                self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(
                self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD TITLE
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to PyOneDark")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.synoptic_page)
        MainFunctions.set_left_column_menu(
            self,
            menu=self.ui.left_column.menus.menu_1,
            title="Settings Left Column",
            icon_path=Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # ///////////////////////////////////////////////////////////////
        # OBJECTS FOR LOAD PAGES, LEFT AND RIGHT COLUMNS
        # You can access objects inside Qt Designer projects using
        # the objects below:
        #
        # <OBJECTS>
        # LEFT COLUMN: self.ui.left_column.menus
        # RIGHT COLUMN: self.ui.right_column
        # LOAD PAGES: self.ui.load_pages
        # </OBJECTS>
        # ///////////////////////////////////////////////////////////////

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # LEFT COLUMN
        # ///////////////////////////////////////////////////////////////

        # BTN 1
        self.left_btn_1 = PyPushButton(
            text="Btn 1",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.left_btn_1.setMaximumHeight(40)
        self.ui.left_column.menus.btn_1_layout.addWidget(self.left_btn_1)

        # BTN 2
        self.left_btn_2 = PyPushButton(
            text="Btn With Icon",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("icon_settings.svg"))
        self.left_btn_2.setIcon(self.icon)
        self.left_btn_2.setMaximumHeight(40)
        self.ui.left_column.menus.btn_2_layout.addWidget(self.left_btn_2)

        # BTN 3 - Default QPushButton
        self.left_btn_3 = QPushButton("Default QPushButton")
        self.left_btn_3.setMaximumHeight(40)
        self.ui.left_column.menus.btn_3_layout.addWidget(self.left_btn_3)

        # PAGES
        # ///////////////////////////////////////////////////////////////

        # ///////////////////////////////////////////////////////////////
        # PAGE HOME
        # ///////////////////////////////////////////////////////////////

        # FORM UP 1
        # ///////////////////////////////////////////////////////////////

        # TOGGLE BUTTON MAIN
        self.toggle_button_Power = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["bg_one"],
            active_color=self.themes["app_color"]["green"]
        )

        self.toggle_button_Power.setCheckState(
            self.uaclient.get_power('MachineMng1.sEnableMainContact'))

        def toggleMainpower():
            self.uaclient.set_Main_power(
                MainPower_toggle=self.toggle_button_Power.isChecked())

        self.toggle_button_Power.toggled.connect(toggleMainpower)
        # self.toggle_button_Power.toggle()

        # TOGGLE BUTTON AIR
        self.toggle_button_AirValve = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["bg_one"],
            active_color=self.themes["app_color"]["green"]
        )

        self.toggle_button_AirValve.setCheckState(
            self.uaclient.get_power('MachineMng1.sStartAirValveV2_scaricoCondensatore'))

        def toggleAIRpower():
            self.uaclient.set_AIR_power(
                AIR_toggle=self.toggle_button_AirValve.isChecked())

        self.toggle_button_AirValve.toggled.connect(toggleAIRpower)

        # TOGGLE BUTTON HEATERS
        self.toggle_button_Heaters = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["bg_one"],
            active_color=self.themes["app_color"]["green"]
        )

        self.toggle_button_Heaters.setCheckState(
            self.uaclient.get_power('MachineMng1.sStartHeater'))

        def toggleHeaterspower():
            self.uaclient.set_Heaters_power(
                Heaters_toggle=self.toggle_button_Heaters.isChecked())

        self.toggle_button_Heaters.toggled.connect(toggleHeaterspower)

        # TOGGLE BUTTON PUMP
        self.toggle_button_Pump = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["bg_one"],
            active_color=self.themes["app_color"]["green"]
        )

        self.toggle_button_Pump.setCheckState(
            self.uaclient.get_power('MachineMng1.sStartPump'))

        def togglePumppower():
            self.uaclient.set_Pump_power(
                Pump_toggle=self.toggle_button_Pump.isChecked())

        self.toggle_button_Pump.toggled.connect(togglePumppower)

        # TOGGLE BUTTON BPR
        self.toggle_button_BPR = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["bg_one"],
            active_color=self.themes["app_color"]["green"]
        )

        self.toggle_button_BPR.setCheckState(
            self.uaclient.get_power('MachineMng1.sStartValveFlowCompensation'))

        def toggleBPRpower_1():
            self.uaclient.set_BPR_power_1(
                BPR_toggle_1=self.toggle_button_BPR.isChecked())

        self.toggle_button_BPR.toggled.connect(toggleBPRpower_1)

        self.ui.load_pages.formLayout.addRow(
            self.tr("&Power:"), self.toggle_button_Power)
        self.ui.load_pages.formLayout.addRow(
            self.tr("&Air Valve V2:"), self.toggle_button_AirValve)
        self.ui.load_pages.formLayout.addRow(
            self.tr("&Heaters:"), self.toggle_button_Heaters)
        self.ui.load_pages.formLayout.addRow(
            self.tr("&Pump:"), self.toggle_button_Pump)
        self.ui.load_pages.formLayout.addRow(
            self.tr("&BPR:"), self.toggle_button_BPR)

        # FORM UP 2
        # ///////////////////////////////////////////////////////////////

        # TOGGLE BUTTON IND
        self.toggle_button_Induction = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["bg_one"],
            active_color=self.themes["app_color"]["green"]
        )

        self.toggle_button_Induction.setCheckState(
            self.uaclient.get_power('PID_Regulator_3_PreHeater2.sStartRegualtion'))

        def toggleINDpower():
            self.uaclient.set_IND_power_2(
                IND_toggle_2=self.toggle_button_Induction.isChecked())

        self.toggle_button_Induction.toggled.connect(toggleINDpower)

        # PY LINE EDIT
        self.line_edit_IndsetT = PyLineEdit(
            text="",
            place_holder_text="0 °C",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["bg_two"],
            bg_color_active=self.themes["app_color"]["bg_two"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_edit_IndsetT.setMinimumHeight(30)
        self.line_edit_IndsetT.setMaximumWidth(80)

        self.label_IND_T = QLabel()
        self.uaclient.stream_IND_T(label=self.label_IND_T)
        self.label_IND_ctrlPower = QLabel()
        self.uaclient.stream_IND_ctrlPower(label=self.label_IND_ctrlPower)
        self.label_IND_auxStep = QLabel()
        self.uaclient.stream_PFR_auxStep(label=self.label_IND_auxStep)

        def line_edit_IND_changed():
            self.uaclient.set_IND_T(Tset=self.line_edit_IndsetT.text())

        self.line_edit_IndsetT.returnPressed.connect(line_edit_IND_changed)

        self.ui.load_pages.formLayout_2.addRow(
            self.tr("&Induction:"), self.toggle_button_Induction)
        self.ui.load_pages.formLayout_2.addRow(
            self.tr("&Induction T:"), self.label_IND_T)
        self.ui.load_pages.formLayout_2.addRow(
            self.tr("&Induction Power:"), self.label_IND_ctrlPower)
        self.ui.load_pages.formLayout_2.addRow(
            self.tr("&Induction setT:"), self.line_edit_IndsetT)
        self.ui.load_pages.formLayout_2.addRow(
            self.tr("&Induction aux step:"), self.label_IND_auxStep)

        # FORM UP 3
        # ///////////////////////////////////////////////////////////////

        # TOGGLE BUTTON PFR
        self.toggle_button_PFR = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["bg_one"],
            active_color=self.themes["app_color"]["green"]
        )

        self.toggle_button_PFR.setCheckState(
            self.uaclient.get_power('PID_Regulator_1_PFR.sStartRegualtion'))

        def togglePFRpower():
            self.uaclient.set_PFR_power_2(
                PFR_toggle_2=self.toggle_button_PFR.isChecked())

        self.toggle_button_PFR.toggled.connect(togglePFRpower)

        # PY LINE EDIT
        self.line_edit_PFR = PyLineEdit(
            text="",
            place_holder_text="0 °C",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["bg_two"],
            bg_color_active=self.themes["app_color"]["bg_two"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_edit_PFR.setMinimumHeight(30)
        self.line_edit_PFR.setMaximumWidth(80)

        def line_edit_PFR_changed():
            self.uaclient.set_PFR_T(Tset=self.line_edit_PFR.text())

        self.line_edit_PFR.returnPressed.connect(line_edit_PFR_changed)

        self.label_PFR_T = QLabel()
        self.uaclient.stream_PFR_T(label=self.label_PFR_T)
        self.label_PFR_ctrlPower = QLabel()
        self.uaclient.stream_PFR_ctrlPower(label=self.label_PFR_ctrlPower)
        self.label_PFR_auxStep = QLabel()
        self.uaclient.stream_PFR_auxStep(label=self.label_PFR_auxStep)

        self.ui.load_pages.formLayout_3.addRow(
            self.tr("&PFR:"), self.toggle_button_PFR)
        self.ui.load_pages.formLayout_3.addRow(
            self.tr("&PFR T:"), self.label_PFR_T)
        self.ui.load_pages.formLayout_3.addRow(
            self.tr("&PFR Power:"), self.label_PFR_ctrlPower)
        self.ui.load_pages.formLayout_3.addRow(
            self.tr("&PFR setT:"), self.line_edit_PFR)
        self.ui.load_pages.formLayout_3.addRow(
            self.tr("&PFR aux step:"), self.label_PFR_auxStep)

        # FORM UP 4
        # ///////////////////////////////////////////////////////////////

        self.label_HE_T_in = QLabel('0 °C')
        self.uaclient.stream_HE_T_in(label=self.label_HE_T_in)
        self.label_HE_T_out = QLabel('0 °C')
        self.uaclient.stream_HE_T_out(label=self.label_HE_T_out)
        self.label_Slurry_T_in = QLabel('0 °C')
        self.uaclient.stream_Slurry_T_in(label=self.label_Slurry_T_in)
        self.label_SafetyV_T = QLabel('0 °C')
        self.uaclient.stream_SafetyV_T(label=self.label_SafetyV_T)

        self.ui.load_pages.formLayout_4.addRow(
            self.tr("&H.E. out T:"), self.label_HE_T_in)
        self.ui.load_pages.formLayout_4.addRow(
            self.tr("&H.E. in T:"), self.label_HE_T_out)
        self.ui.load_pages.formLayout_4.addRow(
            self.tr("&Slurry in T:"), self.label_Slurry_T_in)
        self.ui.load_pages.formLayout_4.addRow(
            self.tr("&Safety Valve T:"), self.label_SafetyV_T)

        # FORM UP 5
        # ///////////////////////////////////////////////////////////////

        # TOGGLE BUTTON SEP
        self.toggle_button_Sep = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["bg_one"],
            active_color=self.themes["app_color"]["green"]
        )

        self.toggle_button_Sep.setCheckState(
            self.uaclient.get_power('PID_Regulator_5_Pipe2.sStartRegualtion'))

        def toggleSEPpower():
            self.uaclient.set_SEP_power_2(
                SEP_toggle_2=self.toggle_button_Sep.isChecked())

        self.toggle_button_Sep.toggled.connect(toggleSEPpower)

        # PY LINE EDIT
        self.line_edit_Sep = PyLineEdit(
            text="",
            place_holder_text="0 °C",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["bg_two"],
            bg_color_active=self.themes["app_color"]["bg_two"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_edit_Sep.setMinimumHeight(30)
        self.line_edit_Sep.setMaximumWidth(80)

        self.label_Sep_T = QLabel()
        self.uaclient.stream_SEP_T(label=self.label_Sep_T)
        self.label_Sep_ctrlPower = QLabel('0 %')
        self.uaclient.stream_SEP_ctrlPower(label=self.label_Sep_ctrlPower)
        self.label_Sep_auxStep = QLabel('0 °C')
        self.uaclient.stream_SEP_auxStep(label=self.label_Sep_auxStep)

        def line_edit_SEP_changed():
            self.uaclient.set_SEP_T(Tset=self.line_edit_Sep.text())

        self.line_edit_Sep.returnPressed.connect(line_edit_SEP_changed)

        self.ui.load_pages.formLayout_5.addRow(
            self.tr("&SEP:"), self.toggle_button_Sep)
        self.ui.load_pages.formLayout_5.addRow(
            self.tr("&SEP T:"), self.label_Sep_T)
        self.ui.load_pages.formLayout_5.addRow(
            self.tr("&SEP Power:"), self.label_Sep_ctrlPower)
        self.ui.load_pages.formLayout_5.addRow(
            self.tr("&SEP setT:"), self.line_edit_Sep)
        self.ui.load_pages.formLayout_5.addRow(
            self.tr("&SEP aux step:"), self.label_Sep_auxStep)

        # SYNOPTIC IMAGE & LEDs
        # ///////////////////////////////////////////////////////////////

        self.PnI = QLabel(self)
        self.pixmap = QPixmap(Functions.set_image("PnI_HTL.png"))
        # # self.pixmap = self.pixmap.scaled(self.ui.load_pages.synoptic_page.width(), self.PnI.height(), Qt.KeepAspectRatio)
        # self.ui.load_pages.label_PnI.setPixmap(self.pixmap)
        self.PnI.setPixmap(self.pixmap)
        self.PnI.setScaledContents(True)
        self.PnI.resize(self.pixmap.width(), self.pixmap.height())
        self.ui.load_pages.verticalLayout_charts_synoptic.addWidget(
            self.PnI, Qt.AlignCenter, Qt.AlignCenter)

        self.pixmap1 = QPixmap(Functions.set_svg_icon("icon_signal.svg"))
        self.ui.load_pages.label_4.setPixmap(self.pixmap1)

        self.uaclient.stream_LED_green(label=self.ui.load_pages.label_green)
        self.uaclient.stream_LED_yellow(label=self.ui.load_pages.label_yellow)
        self.uaclient.stream_LED_red(label=self.ui.load_pages.label_red)

        # FORM DOWN 1
        # ///////////////////////////////////////////////////////////////

        # TOGGLE BUTTON
        self.toggle_button_PumpStart = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["bg_one"],
            active_color=self.themes["app_color"]["green"]
        )

        self.toggle_button_PumpStart.setCheckState(
            self.uaclient.get_power('PumpMng1.sStartPump'))

        def togglePUMPpower_2():
            self.uaclient.set_Pump_power_2(
                Pump_toggle_2=self.toggle_button_PumpStart.isChecked())

        self.toggle_button_PumpStart.toggled.connect(togglePUMPpower_2)

        # TOGGLE BUTTON
        self.toggle_button_ResetError = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["bg_one"],
            active_color=self.themes["app_color"]["green"]
        )

        self.toggle_button_PumpStart.setCheckState(Qt.Unchecked)
        
        def togglePUMPreset():
            self.uaclient.reset_Pump_error()
            self.toggle_button_ResetError.toggle()

        self.toggle_button_ResetError.toggled.connect(togglePUMPreset)

        # PY LINE EDIT
        self.line_edit_SafetyP_A = PyLineEdit(
            text="",
            place_holder_text="0 bar",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["bg_two"],
            bg_color_active=self.themes["app_color"]["bg_two"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_edit_SafetyP_A.setMinimumHeight(30)
        self.line_edit_SafetyP_A.setMaximumWidth(120)

        def line_edit_SafetyP_A_changed():
            self.uaclient.set_SafetyP_A(Pset_A=self.line_edit_SafetyP_A.text())

        self.line_edit_SafetyP_A.returnPressed.connect(line_edit_SafetyP_A_changed)

        # PY LINE EDIT
        self.line_edit_SafetyP_B = PyLineEdit(
            text="",
            place_holder_text="0 bar",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["bg_two"],
            bg_color_active=self.themes["app_color"]["bg_two"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_edit_SafetyP_B.setMinimumHeight(30)
        self.line_edit_SafetyP_B.setMaximumWidth(120)

        def line_edit_SafetyP_B_changed():
            self.uaclient.set_SafetyP_B(Pset_B=self.line_edit_SafetyP_B.text())

        self.line_edit_SafetyP_B.returnPressed.connect(line_edit_SafetyP_B_changed)

        # PY LINE EDIT
        self.line_edit_Flow_A = PyLineEdit(
            text="",
            place_holder_text="0 ml/min",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["bg_two"],
            bg_color_active=self.themes["app_color"]["bg_two"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_edit_Flow_A.setMinimumHeight(30)
        self.line_edit_Flow_A.setMaximumWidth(120)

        def line_edit_Flow_A_changed():
            self.uaclient.set_Flow_A(Flow_A=self.line_edit_Flow_A.text())

        self.line_edit_Flow_A.returnPressed.connect(line_edit_Flow_A_changed)


        # PY LINE EDIT
        self.line_edit_Flow_B = PyLineEdit(
            text="",
            place_holder_text="0 ml/min",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["bg_two"],
            bg_color_active=self.themes["app_color"]["bg_two"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_edit_Flow_B.setMinimumHeight(30)
        self.line_edit_Flow_B.setMaximumWidth(120)

        def line_edit_Flow_B_changed():
            self.uaclient.set_Flow_B(Flow_B=self.line_edit_Flow_B.text())

        self.line_edit_Flow_B.returnPressed.connect(line_edit_Flow_B_changed)

        self.ui.load_pages.formLayout_7.addRow(
            self.tr("&Start Pump:"), self.toggle_button_PumpStart)
        self.ui.load_pages.formLayout_7.addRow(
            self.tr("&Reset Error:"), self.toggle_button_ResetError)
        self.ui.load_pages.formLayout_7.addRow(
            self.tr("&Set Safety P A:"), self.line_edit_SafetyP_A)
        self.ui.load_pages.formLayout_7.addRow(
            self.tr("&Set Safety P B:"), self.line_edit_SafetyP_B)
        self.ui.load_pages.formLayout_7.addRow(
            self.tr("&Set Flow A:"), self.line_edit_Flow_A)
        self.ui.load_pages.formLayout_7.addRow(
            self.tr("&Set Flow B:"), self.line_edit_Flow_B)

        # FORM DOWN 2
        # ///////////////////////////////////////////////////////////////

        self.label_Flow_A = QLabel("0 ml/min")
        self.uaclient.stream_Flow_A(label=self.label_Flow_A)
        self.label_Flow_B = QLabel("0 ml/min")
        self.uaclient.stream_Flow_B(label=self.label_Flow_B)
        self.label_Flow_tot = QLabel("0 ml/min")
        self.uaclient.stream_Flow_tot(label=self.label_Flow_tot)
        self.label_Pump_P_out = QLabel("0 bar")
        self.uaclient.stream_Pump_P_out(label=self.label_Pump_P_out)
        self.label_Pump_V_out = QLabel("0 ml")
        self.uaclient.stream_Pump_V_out(label=self.label_Pump_V_out)
        self.label_Pump_P_A = QLabel("0 bar")
        self.uaclient.stream_Pump_P_A(label=self.label_Pump_P_A)
        self.label_Pump_P_B = QLabel("0 bar")
        self.uaclient.stream_Pump_P_B(label=self.label_Pump_P_B)

        self.ui.load_pages.formLayout_8.addRow(
            self.tr("&Flow Cyl A:"), self.label_Flow_A)
        self.ui.load_pages.formLayout_8.addRow(
            self.tr("&Flow Cyl B:"), self.label_Flow_B)
        self.ui.load_pages.formLayout_8.addRow(
            self.tr("&Flow top:"), self.label_Flow_tot)
        self.ui.load_pages.formLayout_8.addRow(
            self.tr("&P out:"), self.label_Pump_P_out)
        self.ui.load_pages.formLayout_8.addRow(
            self.tr("&V tot:"), self.label_Pump_V_out)
        self.ui.load_pages.formLayout_8.addRow(
            self.tr("&P Cyl A:"), self.label_Pump_P_A)
        self.ui.load_pages.formLayout_8.addRow(
            self.tr("&P Cyl B:"), self.label_Pump_P_B)

        # FORM DOWN 3
        # ///////////////////////////////////////////////////////////////

        self.label_Pump_SafetyP_A_2 = QLabel("0 bar")
        self.uaclient.stream_Pump_SafetyP_A_2(label=self.label_Pump_SafetyP_A_2)
        self.label_Pump_SafetyP_B_2 = QLabel("0 bar")
        self.uaclient.stream_Pump_SafetyP_B_2(label=self.label_Pump_SafetyP_B_2)

        self.ui.load_pages.formLayout_9.addRow(
            self.tr("&Safety P A:"), self.label_Pump_SafetyP_A_2)
        self.ui.load_pages.formLayout_9.addRow(
            self.tr("&Safety P B:"), self.label_Pump_SafetyP_B_2)

        # FORM DOWN 4
        # ///////////////////////////////////////////////////////////////

        # TOGGLE BUTTON
        self.toggle_button_FILT = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["bg_one"],
            active_color=self.themes["app_color"]["green"]
        )

        self.toggle_button_FILT.setCheckState(
            self.uaclient.get_power('PID_Regulator_4_Pipe1.sStartRegualtion'))

        def toggleFILTpower():
            self.uaclient.set_FILT_power(
                FILT_toggle=self.toggle_button_FILT.isChecked())

        self.toggle_button_FILT.toggled.connect(toggleFILTpower)

        # PY LINE EDIT
        self.line_edit_FILT = PyLineEdit(
            text="",
            place_holder_text="0 °C",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["bg_two"],
            bg_color_active=self.themes["app_color"]["bg_two"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_edit_FILT.setMinimumHeight(30)
        self.line_edit_FILT.setMaximumWidth(120)

        def line_edit_FILT_changed():
            self.uaclient.set_FILT_T(Tset=self.line_edit_FILT.text())

        self.line_edit_FILT.returnPressed.connect(line_edit_FILT_changed)

        self.label_FILT_T = QLabel('0 °C')
        self.uaclient.stream_FILT_T(label=self.label_FILT_T)
        self.label_FILT_ctrlPower = QLabel('0 %')
        self.uaclient.stream_FILT_ctrlPower(label=self.label_FILT_ctrlPower)
        self.label_FILT_T_in = QLabel('0 °C')
        self.uaclient.stream_FILT_T_in(label=self.label_FILT_T_in)
        self.label_FILT_auxStep = QLabel('0 °C')
        self.uaclient.stream_FILT_auxStep(label=self.label_FILT_auxStep)
        self.label_FILT_P_in = QLabel('0 bar')
        self.uaclient.stream_FILT_P_in(label=self.label_FILT_P_in)

        self.ui.load_pages.formLayout_10.addRow(
            self.tr("&Filter:"), self.toggle_button_FILT)
        self.ui.load_pages.formLayout_10.addRow(
            self.tr("&Filter T:"), self.label_FILT_T)
        self.ui.load_pages.formLayout_10.addRow(
            self.tr("&Filter Power:"), self.label_FILT_ctrlPower)
        self.ui.load_pages.formLayout_10.addRow(
            self.tr("&Filter setT:"), self.line_edit_FILT)
        self.ui.load_pages.formLayout_10.addRow(
            self.tr("&Filter in T:"), self.label_FILT_T_in)
        self.ui.load_pages.formLayout_10.addRow(
            self.tr("&Filter aux step:"), self.label_FILT_auxStep)
        self.ui.load_pages.formLayout_10.addRow(
            self.tr("&Filter upstream P:"), self.label_FILT_P_in)
            
        # FORM DOWN 5
        # ///////////////////////////////////////////////////////////////

        self.label_BPR_P = QLabel('0 bar')
        self.uaclient.stream_BPR_P(label=self.label_BPR_P)
        self.label_BPR_ctrlPower = QLabel('0 %')
        self.uaclient.stream_BPR_ctrlPower(label=self.label_BPR_ctrlPower)
        self.label_BPR_T = QLabel('0 °C')
        self.uaclient.stream_BPR_T(label=self.label_BPR_T)

        # TOGGLE BUTTON
        self.toggle_button_BPR_Mng = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["bg_one"],
            active_color=self.themes["app_color"]["green"]
        )

        self.toggle_button_BPR_Mng.setCheckState(
            self.uaclient.get_power('DuplicateSetPointGradient1.sStartRegualtion'))

        def toggleBPRpower_2():
            self.uaclient.set_BPR_power_2(
                BPR_toggle_2=self.toggle_button_BPR_Mng.isChecked())

        self.toggle_button_BPR_Mng.toggled.connect(toggleBPRpower_2)

        # PY LINE EDIT
        self.line_edit_BPR_P = PyLineEdit(
            text="",
            place_holder_text="0 bar",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["bg_two"],
            bg_color_active=self.themes["app_color"]["bg_two"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_edit_BPR_P.setMinimumHeight(30)
        self.line_edit_BPR_P.setMaximumWidth(120)

        def line_edit_BPR_P_changed():
            self.uaclient.set_BPR_P(Pset=self.line_edit_BPR_P.text())

        self.line_edit_BPR_P.returnPressed.connect(line_edit_BPR_P_changed)

        # PY LINE EDIT
        self.line_edit_BPR_Grad = PyLineEdit(
            text="",
            place_holder_text="0 bar/s",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["bg_two"],
            bg_color_active=self.themes["app_color"]["bg_two"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_edit_BPR_Grad.setMinimumHeight(30)
        self.line_edit_BPR_Grad.setMaximumWidth(120)

        def line_edit_BPR_grad_changed():
            self.uaclient.set_BPR_grad(grad=self.line_edit_BPR_Grad.text())

        self.line_edit_BPR_Grad.returnPressed.connect(line_edit_BPR_grad_changed)

        self.ui.load_pages.formLayout_11.addRow(
            self.tr("&BPR Mng:"), self.toggle_button_BPR_Mng)
        self.ui.load_pages.formLayout_11.addRow(
            self.tr("&BPR actual P:"), self.label_BPR_P)
        self.ui.load_pages.formLayout_11.addRow(
            self.tr("&BPR set P:"), self.line_edit_BPR_P)
        self.ui.load_pages.formLayout_11.addRow(
            self.tr("&BPR gradient:"), self.line_edit_BPR_Grad)
        self.ui.load_pages.formLayout_11.addRow(
            self.tr("&BPR %:"), self.label_BPR_ctrlPower)
        self.ui.load_pages.formLayout_11.addRow(
            self.tr("&BPR T:"), self.label_BPR_T)

        # FORM DOWN 6
        # ///////////////////////////////////////////////////////////////

        # TOGGLE BUTTON
        self.toggle_button_DrainValve = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["bg_one"],
            active_color=self.themes["app_color"]["green"]
        )

        self.toggle_button_DrainValve.setCheckState(
            self.uaclient.get_power('AirMng1.sEnable'))

        def toggleDVpower():
            self.uaclient.set_DRAIN_V_power(
                toggle=self.toggle_button_DrainValve.isChecked())

        self.toggle_button_DrainValve.toggled.connect(toggleDVpower)

        self.label_DV = QLabel('0')
        self.uaclient.stream_DV(label=self.label_DV)

        self.label_DV_TimeOn = QLabel('10 s')
        self.uaclient.stream_DV_On(label=self.label_DV)

        self.label_DV_TimeOff = QLabel('10 s')
        self.uaclient.stream_DV_Off(label=self.label_DV)

        self.ui.load_pages.formLayout_12.addRow(
            self.tr("&Drain Valve:"), self.toggle_button_DrainValve)
        self.ui.load_pages.formLayout_12.addRow(
            self.tr("&Valve On:"), self.label_DV)
        self.ui.load_pages.formLayout_12.addRow(
            self.tr("&Time On:"), self.label_DV_TimeOn)
        self.ui.load_pages.formLayout_12.addRow(
            self.tr("&Time Off:"), self.label_DV_TimeOff)

        # ///////////////////////////////////////////////////////////////
        # PAGE ALERTS
        # ///////////////////////////////////////////////////////////////

        # FORM UP 1
        # ///////////////////////////////////////////////////////////////

        # ///////////////////////////////////////////////////////////////
        # PAGE VARIABLES
        # ///////////////////////////////////////////////////////////////

        # LOAD VARIABLES
        df = self.uaclient.loadVariables()

        # ICON BUTTON SEARCH
        self.icon_button_SearchVariable = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_search.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Search variable",
            width=40,
            height=40,
            radius=20,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_active"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["context_pressed"]
        )

        # PY LINE EDIT
        self.line_edit_SearchVariable = PyLineEdit(
            text="",
            place_holder_text="Search...",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["bg_two"],
            bg_color_active=self.themes["app_color"]["bg_two"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_edit_SearchVariable.setMinimumHeight(30)

        self.ui.load_pages.horizontalLayout_search.addWidget(
            self.icon_button_SearchVariable)
        self.ui.load_pages.horizontalLayout_search.addWidget(
            self.line_edit_SearchVariable)

        # TABLE WIDGETS
        self.variables_table = QTableWidget()
        self.variables_table.setColumnCount(10)
        self.variables_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.variables_table.setSelectionMode(
            QAbstractItemView.SingleSelection)
        # self.variables_table.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Columns / Header
        self.variables_table_column_1 = QTableWidgetItem()
        self.variables_table_column_1.setTextAlignment(Qt.AlignCenter)
        self.variables_table_column_1.setText("Group")

        self.variables_table_column_2 = QTableWidgetItem()
        self.variables_table_column_2.setTextAlignment(Qt.AlignCenter)
        self.variables_table_column_2.setText("Alias")

        self.variables_table_column_3 = QTableWidgetItem()
        self.variables_table_column_3.setTextAlignment(Qt.AlignCenter)
        self.variables_table_column_3.setText("Name")

        self.variables_table_column_4 = QTableWidgetItem()
        self.variables_table_column_4.setTextAlignment(Qt.AlignCenter)
        self.variables_table_column_4.setText("Description")

        self.variables_table_column_5 = QTableWidgetItem()
        self.variables_table_column_5.setTextAlignment(Qt.AlignCenter)
        self.variables_table_column_5.setText("Type")

        self.variables_table_column_6 = QTableWidgetItem()
        self.variables_table_column_6.setTextAlignment(Qt.AlignCenter)
        self.variables_table_column_6.setText("Write")

        self.variables_table_column_7 = QTableWidgetItem()
        self.variables_table_column_7.setTextAlignment(Qt.AlignCenter)
        self.variables_table_column_7.setText("Min")

        self.variables_table_column_8 = QTableWidgetItem()
        self.variables_table_column_8.setTextAlignment(Qt.AlignCenter)
        self.variables_table_column_8.setText("Max")

        self.variables_table_column_9 = QTableWidgetItem()
        self.variables_table_column_9.setTextAlignment(Qt.AlignCenter)
        self.variables_table_column_9.setText("Value")

        self.variables_table_column_10 = QTableWidgetItem()
        self.variables_table_column_10.setTextAlignment(Qt.AlignCenter)
        self.variables_table_column_10.setText("M.U.")

        # Set column
        self.variables_table.setHorizontalHeaderItem(
            0, self.variables_table_column_1)
        self.variables_table.setHorizontalHeaderItem(
            1, self.variables_table_column_2)
        self.variables_table.setHorizontalHeaderItem(
            2, self.variables_table_column_3)
        self.variables_table.setHorizontalHeaderItem(
            3, self.variables_table_column_4)
        self.variables_table.setHorizontalHeaderItem(
            4, self.variables_table_column_5)
        self.variables_table.setHorizontalHeaderItem(
            5, self.variables_table_column_6)
        self.variables_table.setHorizontalHeaderItem(
            6, self.variables_table_column_7)
        self.variables_table.setHorizontalHeaderItem(
            7, self.variables_table_column_8)
        self.variables_table.setHorizontalHeaderItem(
            8, self.variables_table_column_9)
        self.variables_table.setHorizontalHeaderItem(
            9, self.variables_table_column_10)

        # Adjust width
        self.header = self.variables_table.horizontalHeader()
        self.header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(3, QHeaderView.Stretch)
        self.header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(6, QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(7, QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(8, QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(9, QHeaderView.ResizeToContents)

        for id, row in df.iterrows():
            row_number = self.variables_table.rowCount()
            self.variables_table.insertRow(row_number)  # Insert row
            # 0
            self.group = QTableWidgetItem()
            self.group.setTextAlignment(Qt.AlignCenter)
            self.group.setText(str(row['Group']))
            self.variables_table.setItem(
                row_number, 0, self.group)
            # 1
            self.alias = QTableWidgetItem()
            self.alias.setTextAlignment(Qt.AlignLeft)
            self.alias.setText(str(row['ALIAS']))
            self.variables_table.setItem(
                row_number, 1, self.alias)
            # 2
            self.visname = QTableWidgetItem()
            self.visname.setTextAlignment(Qt.AlignLeft)
            self.visname.setText(str(row['VISUALIZATION NAME']))
            self.variables_table.setItem(
                row_number, 2, self.visname)
            # 3
            self.descr = QTableWidgetItem()
            self.descr.setTextAlignment(Qt.AlignLeft)
            self.descr.setText(str(row['DESCRIPTION']))
            self.variables_table.setItem(
                row_number, 3, self.descr)
            # 4
            self.inType = QTableWidgetItem()
            self.inType.setTextAlignment(Qt.AlignCenter)
            self.inType.setText(str(row['INPUT TYPE']))
            self.variables_table.setItem(
                row_number, 4, self.inType)
            # 5
            self.inProt = QTableWidgetItem()
            self.inProt.setTextAlignment(Qt.AlignCenter)
            self.inProt.setText(str(row['INPUT PROTECTION']))
            self.variables_table.setItem(
                row_number, 5, self.inProt)
            # 6
            self.min = QTableWidgetItem()
            self.min.setTextAlignment(Qt.AlignCenter)
            self.min.setText(str(row['MIN']))
            self.variables_table.setItem(
                row_number, 6, self.min)
            # 7
            self.max = QTableWidgetItem()
            self.max.setTextAlignment(Qt.AlignCenter)
            self.max.setText(str(row['MAX']))
            self.variables_table.setItem(
                row_number, 7, self.max)
            # 8
            self.actVal = QTableWidgetItem()
            self.actVal.setTextAlignment(Qt.AlignCenter)
            self.actVal.setText('Value')
            myFont=QFont()
            myFont.setBold(True)
            self.actVal.setFont(myFont)
            self.variables_table.setItem(
                row_number, 8, self.actVal)
            # 9
            self.um = QTableWidgetItem()
            self.um.setTextAlignment(Qt.AlignCenter)
            self.um.setText(str(row['U.M.']))
            self.variables_table.setItem(
                row_number, 9, self.um)

            # self.variables_table.setRowHeight(row_number, 22)

        self.variables_table.resizeColumnsToContents()
        self.variables_table.resizeRowsToContents()
        self.ui.load_pages.verticalLayout_table.addWidget(self.variables_table)

        # PUSH BUTTON PUMP
        self.push_button_Pump = QPushButton("Pump")
        self.push_button_Pump.setStyleSheet("")
        self.push_button_Pump.setMinimumHeight(40)

        # PUSH BUTTON PID
        self.push_button_PID = QPushButton("PID")
        self.push_button_PID.setMinimumHeight(40)

        # PUSH BUTTON T
        self.push_button_Temp = QPushButton("Temperature")
        self.push_button_Temp.setMinimumHeight(40)

        # PUSH BUTTON SYS
        self.push_button_System = QPushButton("System")
        self.push_button_System.setMinimumHeight(40)

        self.ui.load_pages.horizontalLayout_varCategory.addWidget(
            self.push_button_Pump)
        self.ui.load_pages.horizontalLayout_varCategory.addWidget(
            self.push_button_PID)
        self.ui.load_pages.horizontalLayout_varCategory.addWidget(
            self.push_button_Temp)
        self.ui.load_pages.horizontalLayout_varCategory.addWidget(
            self.push_button_System)

        # FUNCTIONS
        def search(s):
            # clear current selection.
            self.variables_table.setCurrentItem(None)

            if not s:
                # Empty string, don't search.
                return

            matching_items = self.variables_table.findItems(s, Qt.MatchContains)
            if matching_items:
                # we have found something
                item = matching_items[0]  # take the first
                self.variables_table.setCurrentItem(item)

        self.line_edit_SearchVariable.textChanged.connect(search)

        # ///////////////////////////////////////////////////////////////
        # PAGE CHARTS
        # ///////////////////////////////////////////////////////////////

        # # PUSH CHART
        # self.push_button_Chart = PyPushButton(
        #     text="Start",
        #     radius=8,
        #     color=self.themes["app_color"]["text_foreground"],
        #     bg_color=self.themes["app_color"]["dark_one"],
        #     bg_color_hover=self.themes["app_color"]["dark_three"],
        #     bg_color_pressed=self.themes["app_color"]["dark_four"]
        # )
        # self.push_button_Chart.setMinimumHeight(40)
        # self.ui.load_pages.verticalLayout_charts.addWidget(self.push_button_Chart)

        # TOGGLE BUTTON
        self.toggle_button_Stream = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["bg_one"],
            active_color=self.themes["app_color"]["green"]
        )
        self.ui.load_pages.verticalLayout_charts.addWidget(
            self.toggle_button_Stream)

        from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
        import matplotlib.animation as mplanimation

        self.chart = RandomDataWidget()

        self.uaclient.update_plt(chart=self.chart)

        self.toolbar = NavigationToolbar(self.chart, self)
        self.ui.load_pages.verticalLayout_charts.addWidget(self.chart)
        self.ui.load_pages.verticalLayout_charts.addWidget(self.toolbar)

        def updateStream():
            self.chart.set_stram(self.toggle_button_Stream.isChecked())

        self.toggle_button_Stream.toggled.connect(updateStream)
        self.toggle_button_Stream.toggle()

        def updateTwin1():
            if self.toggle_twin1.checkState() == Qt.Checked:
                self.chart.set_plt_twin_1(True)
                print(self.toggle_twin1.checkState())
                print(Qt.Checked)
                print('True')
            else:
                self.chart.set_plt_twin_1(False)
                print('False')

        def updateTwin2():
            if self.toggle_twin2.checkState() == Qt.Checked:
                self.chart.set_plt_twin_2(True)
                print(self.toggle_twin2.checkState())
                print(Qt.Checked)
                print('True')
            else:
                self.chart.set_plt_twin_2(False)
                print('False')

        # TABLE WIDGETS
        self.charts_table = PyTableWidget(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["context_color"],
            bg_color=self.themes["app_color"]["bg_two"],
            header_horizontal_color=self.themes["app_color"]["dark_two"],
            header_vertical_color=self.themes["app_color"]["bg_three"],
            bottom_line_color=self.themes["app_color"]["bg_three"],
            grid_line_color=self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.charts_table.setColumnCount(4)
        self.charts_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.charts_table.setSelectionMode(
            QAbstractItemView.ExtendedSelection)
        self.charts_table.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Columns / Header
        self.charts_table_column_0 = QTableWidgetItem()
        self.charts_table_column_0.setTextAlignment(Qt.AlignCenter)
        self.charts_table_column_0.setText("Check")

        self.charts_table_column_1 = QTableWidgetItem()
        self.charts_table_column_1.setTextAlignment(Qt.AlignCenter)
        self.charts_table_column_1.setText("Group")

        self.charts_table_column_2 = QTableWidgetItem()
        self.charts_table_column_2.setTextAlignment(Qt.AlignCenter)
        self.charts_table_column_2.setText("Alias")

        self.charts_table_column_3 = QTableWidgetItem()
        self.charts_table_column_3.setTextAlignment(Qt.AlignCenter)
        self.charts_table_column_3.setText("Name")

        # Set column
        self.charts_table.setHorizontalHeaderItem(
            0, self.charts_table_column_0)
        self.charts_table.setHorizontalHeaderItem(
            1, self.charts_table_column_1)
        self.charts_table.setHorizontalHeaderItem(
            2, self.charts_table_column_2)
        self.charts_table.setHorizontalHeaderItem(
            3, self.charts_table_column_3)

        row_number = self.charts_table.rowCount()
        self.charts_table.insertRow(row_number)  # Insert row
        self.toggle_twin1 = QTableWidgetItem()
        self.toggle_twin1.setFlags(Qt.ItemIsUserCheckable |
                                   Qt.ItemIsEnabled)
        self.toggle_twin1.setCheckState(Qt.Checked)
        self.charts_table.setItem(row_number, 0, self.toggle_twin1)
        self.charts_table.itemClicked.connect(updateTwin1)
        self.charts_table.setItem(
            row_number, 1, QTableWidgetItem(str("Twin 1")))  # Add name
        self.charts_table.setItem(row_number, 2, QTableWidgetItem(
            str("vfx_on_fire_" + str(1))))  # Add nick
        self.pass_text = QTableWidgetItem()
        self.pass_text.setTextAlignment(Qt.AlignCenter)
        self.pass_text.setText("12345" + str(1))
        self.charts_table.setItem(
            row_number, 3, self.pass_text)  # Add pass
        self.charts_table.insertRow(row_number)  # Insert row
        self.toggle_twin2 = QTableWidgetItem()
        self.toggle_twin2.setFlags(Qt.ItemIsUserCheckable |
                                   Qt.ItemIsEnabled)
        self.toggle_twin2.setCheckState(Qt.Checked)
        self.charts_table.setItem(row_number, 0, self.toggle_twin2)
        self.charts_table.itemClicked.connect(updateTwin2)
        self.charts_table.setItem(
            row_number, 1, QTableWidgetItem(str("Twin 2")))  # Add name
        self.charts_table.setItem(row_number, 2, QTableWidgetItem(
            str("vfx_on_fire_" + str(1))))  # Add nick
        self.pass_text = QTableWidgetItem()
        self.pass_text.setTextAlignment(Qt.AlignCenter)
        self.pass_text.setText("12345" + str(1))
        self.charts_table.setItem(
            row_number, 3, self.pass_text)  # Add pass

        self.ui.load_pages.verticalLayout_charts.addWidget(self.charts_table)

        # ///////////////////////////////////////////////////////////////
        # END - EXAMPLE CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////

    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(
                self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(
                5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(
                self.width() - 20, self.height() - 20, 15, 15)
