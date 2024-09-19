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
            self.toggle_button_PFR.setCheckState(
                self.uaclient.get_power('PID_Regulator_1_PFR.sStartRegualtion'))
            self.toggle_button_Sep.setCheckState(
                self.uaclient.get_power('PID_Regulator_5_Pipe2.sStartRegualtion'))
            self.toggle_button_FILT.setCheckState(
                self.uaclient.get_power('PID_Regulator_4_Pipe1.sStartRegualtion'))
            
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

        self.line_edit_SafetyP_A.returnPressed.connect(
            line_edit_SafetyP_A_changed)

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

        self.line_edit_SafetyP_B.returnPressed.connect(
            line_edit_SafetyP_B_changed)

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
        self.uaclient.stream_Pump_SafetyP_A_2(
            label=self.label_Pump_SafetyP_A_2)
        self.label_Pump_SafetyP_B_2 = QLabel("0 bar")
        self.uaclient.stream_Pump_SafetyP_B_2(
            label=self.label_Pump_SafetyP_B_2)

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

        self.line_edit_BPR_Grad.returnPressed.connect(
            line_edit_BPR_grad_changed)

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
        self.uaclient.loadVariables()

        # ICON BUTTON SEARCH
        self.icon_button_SearchVariable = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_search.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Show all",
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

        # standard item model
        headers = ['Group', 'Alias', 'Name', 'Description',
                   'Type', 'Write', 'Min', 'Max', 'Value', 'M.U.']
        model = QStandardItemModel(len(self.uaclient.subdf), len(headers))
        model.setHorizontalHeaderLabels(headers)

        for id, row in self.uaclient.subdf.iterrows():
            # 0
            self.group = QStandardItem()
            self.group.setTextAlignment(Qt.AlignCenter)
            self.group.setText(str(row['Group']))
            model.setItem(
                id, 0, self.group)
            # 1
            self.alias = QStandardItem()
            self.alias.setTextAlignment(Qt.AlignLeft)
            self.alias.setText(str(row['ALIAS']))
            model.setItem(
                id, 1, self.alias)
            # 2
            self.visname = QStandardItem()
            self.visname.setTextAlignment(Qt.AlignLeft)
            self.visname.setText(str(row['VISUALIZATION NAME']))
            model.setItem(
                id, 2, self.visname)
            # 3
            self.descr = QStandardItem()
            self.descr.setTextAlignment(Qt.AlignLeft)
            self.descr.setText(str(row['DESCRIPTION']))
            model.setItem(
                id, 3, self.descr)
            # 4
            self.inType = QStandardItem()
            self.inType.setTextAlignment(Qt.AlignCenter)
            self.inType.setText(str(row['INPUT TYPE']))
            model.setItem(
                id, 4, self.inType)
            # 5
            self.inProt = QStandardItem()
            self.inProt.setTextAlignment(Qt.AlignCenter)
            self.inProt.setText(str(row['INPUT PROTECTION']))
            model.setItem(
                id, 5, self.inProt)
            # 6
            self.min = QStandardItem()
            self.min.setTextAlignment(Qt.AlignCenter)
            self.min.setText(str(row['MIN']))
            model.setItem(
                id, 6, self.min)
            # 7
            self.max = QStandardItem()
            self.max.setTextAlignment(Qt.AlignCenter)
            self.max.setText(str(row['MAX']))
            model.setItem(
                id, 7, self.max)
            # 8
            self.actVal = QStandardItem()
            self.actVal.setTextAlignment(Qt.AlignCenter)
            self.actVal.setText('Value')
            myFont = QFont()
            myFont.setBold(True)
            self.actVal.setFont(myFont)
            model.setItem(
                id, 8, self.actVal)
            # 9
            self.um = QStandardItem()
            self.um.setTextAlignment(Qt.AlignCenter)
            self.um.setText(str(row['U.M.']))
            model.setItem(
                id, 9, self.um)

        # filter proxy model
        filter_proxy_model = QSortFilterProxyModel()
        filter_proxy_model.setSourceModel(model)
        filter_proxy_model.setFilterKeyColumn(1)  # second column

        # table view
        self.variables_table = QTableView()
        self.ui.load_pages.verticalLayout_table.addWidget(self.variables_table)

        self.variables_table.setModel(filter_proxy_model)

        self.variables_table.resizeColumnsToContents()

        headerView = QHeaderView(Qt.Horizontal, self.variables_table)
        self.variables_table.setHorizontalHeader(headerView)
        headerView.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        headerView.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        headerView.setSectionResizeMode(3, QHeaderView.Stretch)
        headerView.setSectionsClickable(True)

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

            matching_items = self.variables_table.findItems(
                s, Qt.MatchContains)
            if matching_items:
                # we have found something
                item = matching_items[0]  # take the first
                self.variables_table.setCurrentItem(item)

        # self.line_edit_SearchVariable.textChanged.connect(search)
        self.line_edit_SearchVariable.textChanged.connect(
            filter_proxy_model.setFilterRegExp)

        def proxyPID():
            filter_proxy_model.setFilterKeyColumn(0)
            filter_proxy_model.setFilterRegExp(QRegExp('PID'))
            filter_proxy_model.setFilterKeyColumn(1)

        def proxyPump():
            filter_proxy_model.setFilterKeyColumn(0)
            filter_proxy_model.setFilterRegExp(QRegExp('Pump'))
            filter_proxy_model.setFilterKeyColumn(1)

        def proxyTemp():
            filter_proxy_model.setFilterKeyColumn(0)
            filter_proxy_model.setFilterRegExp(QRegExp('Temp'))
            filter_proxy_model.setFilterKeyColumn(1)

        def proxySystem():
            filter_proxy_model.setFilterKeyColumn(0)
            filter_proxy_model.setFilterRegExp(QRegExp('System'))
            filter_proxy_model.setFilterKeyColumn(1)

        def proxyReset():
            filter_proxy_model.setFilterKeyColumn(0)
            filter_proxy_model.setFilterRegExp(QRegExp(''))
            filter_proxy_model.setFilterKeyColumn(1)

        self.push_button_PID.clicked.connect(proxyPID)
        self.push_button_Pump.clicked.connect(proxyPump)
        self.push_button_Temp.clicked.connect(proxyTemp)
        self.push_button_System.clicked.connect(proxySystem)
        self.icon_button_SearchVariable.clicked.connect(proxyReset)

        self.uaclient.stream_table_values(model=model)

        # ///////////////////////////////////////////////////////////////
        # PAGE CHARTS
        # ///////////////////////////////////////////////////////////////

        self.chart_commands_HL = QHBoxLayout()
        self.chart_commands_HL.setAlignment(Qt.AlignCenter)
        self.ui.load_pages.verticalLayout_charts.addLayout(self.chart_commands_HL)
        
        self.chart_label = QLabel('Toggle plotting: ')
        self.chart_commands_HL.addWidget(self.chart_label)

        # TOGGLE BUTTON
        self.toggle_button_Stream = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["bg_one"],
            active_color=self.themes["app_color"]["green"]
        )
        self.chart_commands_HL.addWidget(
            self.toggle_button_Stream)

        spacerItem = QSpacerItem(150, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.chart_commands_HL.addItem(spacerItem)

        self.log_label = QLabel('Toggle logging: ')
        self.chart_commands_HL.addWidget(self.log_label)

        # TOGGLE BUTTON
        self.toggle_button_logging = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["bg_one"],
            active_color=self.themes["app_color"]["context_color"]
        )
        self.chart_commands_HL.addWidget(
            self.toggle_button_logging)

        spacerItem = QSpacerItem(50, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.chart_commands_HL.addItem(spacerItem)

        self.log_label_count = QLabel('Count: ')
        self.chart_commands_HL.addWidget(self.log_label_count)
        self.count = QLabel('0')
        self.chart_commands_HL.addWidget(self.count)

        self.custom = False
        def startLog():
            self.custom = not self.custom
            self.uaclient.init_dataLog(custom=self.custom, logcount_label=self.count)

        self.toggle_button_logging.toggled.connect(startLog)

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

        # standard item model
        headers = ['Check', 'Group', 'Alias', 'Name', 'Min',
                   'Actual', 'Max', 'Max Scale', 'Average', 'M.U.']
        model_chart = QStandardItemModel(
            len(self.uaclient.subdf), len(headers))
        model_chart.setHorizontalHeaderLabels(headers)

        self.plot = []

        for id, row in self.uaclient.subdf.iterrows():
            # 0
            self.toggle = QStandardItem()
            self.toggle.setFlags(Qt.ItemIsUserCheckable |
                                 Qt.ItemIsEnabled)
            self.toggle.setTextAlignment(Qt.AlignCenter)
            if row['OPC/UA_DISPLAYNAME'] == 'PID_Regulator_1_PFR_sActTemperature':
                self.toggle.setCheckState(Qt.Checked)
                self.plot.append(True)
            elif row['OPC/UA_DISPLAYNAME'] == 'MY_PID_PUMP_REGULATOR_V31_sActValue':
                self.toggle.setCheckState(Qt.Checked)
                self.plot.append(True)
            elif row['OPC/UA_DISPLAYNAME'] == '_ReadInputRegister1_SFlowTotal':
                self.toggle.setCheckState(Qt.Checked)
                self.plot.append(True)
            else:
                self.toggle.setCheckState(Qt.Unchecked)
                self.plot.append(False)
            model_chart.setItem(
                id, 0, self.toggle)
            # 1
            self.group_cahrt = QStandardItem()
            self.group_cahrt.setTextAlignment(Qt.AlignCenter)
            self.group_cahrt.setText(str(row['Group']))
            model_chart.setItem(
                id, 1, self.group_cahrt)
            # 2
            self.alias_chart = QStandardItem()
            self.alias_chart.setTextAlignment(Qt.AlignLeft)
            self.alias_chart.setText(str(row['ALIAS']))
            model_chart.setItem(
                id, 2, self.alias_chart)
            # 3
            self.visname_chart = QStandardItem()
            self.visname_chart.setTextAlignment(Qt.AlignLeft)
            self.visname_chart.setText(str(row['VISUALIZATION NAME']))
            model_chart.setItem(
                id, 3, self.visname_chart)
            # 4
            self.min_chart = QStandardItem()
            self.min_chart.setTextAlignment(Qt.AlignCenter)
            self.min_chart.setText('min')
            model_chart.setItem(
                id, 4, self.min_chart)
            # 5
            self.act_chart = QStandardItem()
            self.act_chart.setTextAlignment(Qt.AlignCenter)
            self.act_chart.setText('Value')
            model_chart.setItem(
                id, 5, self.act_chart)
            # 6
            self.max_chart = QStandardItem()
            self.max_chart.setTextAlignment(Qt.AlignCenter)
            self.max_chart.setText('max')
            model_chart.setItem(
                id, 6, self.max_chart)
            # 7
            self.max_scale_chart = QStandardItem()
            self.max_scale_chart.setTextAlignment(Qt.AlignCenter)
            self.max_scale_chart.setText(str(row['MAX']))
            model_chart.setItem(
                id, 7, self.max_scale_chart)
            # 8
            self.ave_chart = QStandardItem()
            self.ave_chart.setTextAlignment(Qt.AlignCenter)
            self.ave_chart.setText('ave')
            model_chart.setItem(
                id, 8, self.ave_chart)
            # 9
            self.mu_chart = QStandardItem()
            self.mu_chart.setTextAlignment(Qt.AlignCenter)
            self.mu_chart.setText(str(row['U.M.']))
            model_chart.setItem(
                id, 9, self.mu_chart)

        self.uaclient.subdf = self.uaclient.subdf.assign(Plot=self.plot)

        self.chart.init_dict(self.uaclient.subdf)

        # filter proxy model
        filter_proxy_model_chart = QSortFilterProxyModel()
        filter_proxy_model_chart.setSourceModel(model_chart)
        filter_proxy_model_chart.setFilterKeyColumn(1)  # second column

        # table view
        self.charts_table = QTableView()
        self.ui.load_pages.verticalLayout_charts.addWidget(self.charts_table)

        self.charts_table.setModel(filter_proxy_model_chart)

        self.charts_table.resizeColumnsToContents()

        headerView = QHeaderView(Qt.Horizontal, self.charts_table)
        self.charts_table.setHorizontalHeader(headerView)
        headerView.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        headerView.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        headerView.setSectionResizeMode(3, QHeaderView.Stretch)
        headerView.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        headerView.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        headerView.setSectionResizeMode(6, QHeaderView.ResizeToContents)
        headerView.setSectionResizeMode(7, QHeaderView.ResizeToContents)
        headerView.setSectionResizeMode(8, QHeaderView.ResizeToContents)
        headerView.setSectionResizeMode(9, QHeaderView.ResizeToContents)
        headerView.setSectionsClickable(True)

        def clicked(index):
            self.uaclient.subdf.at[index.row(
            ), 'Plot'] = not self.uaclient.subdf.at[index.row(), 'Plot']

        self.charts_table.clicked[QModelIndex].connect(clicked)

        self.uaclient.stream_chart_table_values(model_chart)

        # ///////////////////////////////////////////////////////////////
        # END
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
