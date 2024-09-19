from numpy.core.fromnumeric import mean
from opcua.crypto import uacrypto
from qt_core import *
from opcua import Client
import datetime
import time
import sys
import os
import pathlib as plib

import logging
import pandas as pd

from opcua import ua
from opcua.common import events


class SubHandler(QObject):
    val_changed = Signal(int, str)

    def datachange_notification(self, node, val, data):
        self.val_changed.emit(val, str(node))
        self.nv = val
        # print("Python: New data change event", node, val)

    def event_notification(self, event):
        print("Python: New event", event)


# ///////////////////////////////////////////////////////////////
# UACLIENT
# ///////////////////////////////////////////////////////////////

class UaClient(object):
    """
    OPC-Ua client specialized for the need of GUI client
    return exactly what GUI needs, no customization possible
    """

    def __init__(self):
        self.client = Client("opc.tcp://192.168.0.5:4842")
        self.valPFR_T = 0
        self.valBPR_P = 0

    def loadVariables(self):
        base = plib.Path(__file__).parents[0]
        file = plib.Path(base, 'Variables_PLC.csv')
        self.df = pd.read_csv(file)
        self.usedNodes = []
        types = []
        for i in self.handle_lst:
            node = i.nodeid.to_string()[7:].replace(".", "_")
            self.usedNodes.append(node)
        indx = self.df['OPC/UA_DISPLAYNAME'].isin(self.usedNodes)
        self.subdf = self.df[indx]
        alias = self.subdf['ALIAS'].str.split(pat="_", expand=True)[0]
        self.values = [0.0]*len(self.subdf)
        self.subdf = self.subdf.assign(Group=alias, Values=self.values)
        self.subdf.reset_index(drop=True, inplace=True)
        self.init_dataLog()

    def startSubscription(self):
        self.PFR_T = self.client.get_node(
            "ns=2;s=PID_Regulator_1_PFR.sActTemperature")
        # "ns=2;s=Read2chTemperature_1_PFR.sActTemperature")
        self.PFR_ctrlPower = self.client.get_node(
            "ns=2;s=PID_Regulator_1_PFR.sControlPowerOut")
        self.PFR_auxStep = self.client.get_node(
            "ns=2;s=PID_Regulator_1_PFR.sAuxStepSetpoint")
        self.Ind_T = self.client.get_node(
            "ns=2;s=PID_Regulator_3_PreHeater2.sActTemperature")
        self.Ind_T_ctrlPower = self.client.get_node(
            "ns=2;s=PID_Regulator_3_PreHeater2.sControlPowerOut")
        self.Ind_T_auxStep = self.client.get_node(
            "ns=2;s=PID_Regulator_3_PreHeater2.sAuxStepSetpoint")
        self.Sep_T = self.client.get_node(
            "ns=2;s=PID_Regulator_5_Pipe2.sActTemperature")
        self.Sep_T_ctrlPower = self.client.get_node(
            "ns=2;s=PID_Regulator_5_Pipe2.sControlPowerOut")
        self.Sep_T_auxStep = self.client.get_node(
            "ns=2;s=PID_Regulator_5_Pipe2.sAuxStepSetpoint")
        self.BPR_P = self.client.get_node(
            "ns=2;s=MY_PID_PUMP_REGULATOR_V31.sActValue")
        self.BPR_ctrlPower = self.client.get_node(
            "ns=2;s=MY_PID_PUMP_REGULATOR_V31.ControlValuePercent")
        self.BPR_T = self.client.get_node(
            "ns=2;s=BackPressureRegulatorTempMonitor.sActTemperature")
        self.HE_T_in = self.client.get_node(
            "ns=2;s=InletCoolingWaterTempMonitor.sActTemperature")
        self.HE_T_out = self.client.get_node(
            "ns=2;s=OutletCoolingWaterTempMonitor.sActTemperature")
        self.Slurry_T_in = self.client.get_node(
            "ns=2;s=InjectedFluidTemperatureMonitor.sActTemperature")
        self.SafetyV_T = self.client.get_node(
            "ns=2;s=SafetyValveTempMonitor.sActTemperature")
        self.LED_green = self.client.get_node(
            "ns=2;s=MachineMng1.cLightGREENVisu")
        self.LED_yellow = self.client.get_node(
            "ns=2;s=MachineMng1.cLightYELLOWVisu")
        self.LED_red = self.client.get_node(
            "ns=2;s=MachineMng1.cLightREDVisu")
        self.Flow_A = self.client.get_node(
            "ns=2;s=_ReadInputRegister1.SFlowCylinderA")
        self.Flow_B = self.client.get_node(
            "ns=2;s=_ReadInputRegister1.SflowCylinderB")  # Errore del programmatore...
        self.Flow_tot = self.client.get_node(
            "ns=2;s=_ReadInputRegister1.SFlowTotal")
        self.Pump_P_out = self.client.get_node(
            "ns=2;s=_ReadInputRegister1.sPressure_OUT")
        self.Pump_P_A = self.client.get_node(
            "ns=2;s=_ReadInputRegister1.sPressureCylinderA")
        self.Pump_P_B = self.client.get_node(
            "ns=2;s=_ReadInputRegister1.sPressureCylinderB")
        self.Pump_V_out = self.client.get_node(
            "ns=2;s=_ReadInputRegister1.sVolumeTotal")
        self.Pump_SafetyP_A_2 = self.client.get_node(
            "ns=2;s=_ReadInputRegister1.sSafetyPressureA_Bar")
        self.Pump_SafetyP_B_2 = self.client.get_node(
            "ns=2;s=_ReadInputRegister1.sSafetyPressureB_Bar")
        self.FILT_T = self.client.get_node(
            "ns=2;s=PID_Regulator_4_Pipe1.sActTemperature")
        self.FILT_ctrlPower = self.client.get_node(
            "ns=2;s=PID_Regulator_4_Pipe1.sControlPowerOut")
        self.FILT_auxStep = self.client.get_node(
            "ns=2;s=PID_Regulator_4_Pipe1.sAuxStepSetpoint")
        self.FILT_T_in = self.client.get_node(
            "ns=2;s=InletFilterTempMonitor.sActTemperature")
        self.FILT_P_in = self.client.get_node(
            "ns=2;s=ScaleInputPressure_filterIN.outValue")
        self.DV = self.client.get_node(
            "ns=2;s=AirMng1.sValveActive")
        self.DV_On = self.client.get_node(
            "ns=2;s=AirMng1.T_On")
        self.DV_Off = self.client.get_node(
            "ns=2;s=AirMng1.T_Off")

        self.handler = SubHandler()
        self.sub = self.client.create_subscription(2000, self.handler)
        self.handle_lst = [self.PFR_T, self.Ind_T,
                           self.PFR_ctrlPower, self.PFR_auxStep,
                           self.BPR_P, self.BPR_ctrlPower, self.BPR_T,
                           self.Sep_T, self.Sep_T_auxStep, self.Sep_T_ctrlPower,
                           self.HE_T_in, self.HE_T_out, self.Slurry_T_in, self.SafetyV_T,
                           self.LED_green, self.LED_yellow, self.LED_red,
                           self.Flow_A, self.Flow_B, self.Flow_tot, self.Pump_V_out,
                           self.Pump_P_out, self.Pump_P_A, self.Pump_P_B,
                           self.Pump_SafetyP_A_2, self.Pump_SafetyP_B_2,
                           self.FILT_T, self.FILT_ctrlPower, self.FILT_auxStep,
                           self.FILT_T_in, self.FILT_P_in,
                           self.DV, self.DV_On, self.DV_Off,
                           ]
        self.handle = self.sub.subscribe_data_change(self.handle_lst)
        self.sub.subscribe_events()

    def stream_PLC_status_label(self, label):
        self.label_PLC_status = label

    def stream_table_values(self, model):
        self.var_model = model

    def stream_chart_table_values(self, model):
        self.chart_model = model

    def connectClient(self):
        try:
            self.client.connect()
            self.startSubscription()
            self._connected = True
            self.label_PLC_status.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
                                                "color: rgb(0, 0, 0);\n"
                                                "border: 1px solid black;")
            self.label_PLC_status.setText('Connected!')

        except Exception as e:
            print(e)
            self._connected = False

    def disconnectClient(self):
        try:
            self.sub.delete()
            self.client.disconnect()
            self._connected = False
        except Exception as e:
            print(e)
            self._connected = True

    # ///////////////////////////////////////////////////////////////
    # MAIN
    # ///////////////////////////////////////////////////////////////

    def get_power(self, node):
        power = self.client.get_node(
            "ns=2;s="+node)
        power_val = power.get_value()
        if power_val:
            powerChecked = Qt.Checked
        else:
            powerChecked = Qt.Unchecked
        return powerChecked

    def set_Main_power(self, MainPower_toggle):
        if MainPower_toggle:
            val = 1
        else:
            val = 0
        power = self.client.get_node(
            "ns=2;s=MachineMng1.sEnableMainContact")
        dv = ua.DataValue(ua.Variant(val, ua.VariantType.Int32))
        dv.ServerTimestamp = None
        dv.SourceTimestap = None
        power.set_value(dv)

    def set_AIR_power(self, AIR_toggle):
        if AIR_toggle:
            val = 1
        else:
            val = 0
        AIRpower = self.client.get_node(
            "ns=2;s=MachineMng1.sStartAirValveV2_scaricoCondensatore")
        dv = ua.DataValue(ua.Variant(val, ua.VariantType.Int32))
        dv.ServerTimestamp = None
        dv.SourceTimestap = None
        AIRpower.set_value(dv)

    def set_Heaters_power(self, Heaters_toggle):
        if Heaters_toggle:
            val = 1
        else:
            val = 0
        powerHeaters = self.client.get_node(
            "ns=2;s=MachineMng1.sStartHeater")
        dv = ua.DataValue(ua.Variant(val, ua.VariantType.Int32))
        dv.ServerTimestamp = None
        dv.SourceTimestap = None
        powerHeaters.set_value(dv)

    def set_Pump_power(self, Pump_toggle):
        if Pump_toggle:
            val = 1
        else:
            val = 0
        powerPump = self.client.get_node(
            "ns=2;s=MachineMng1.sStartPump")
        dv = ua.DataValue(ua.Variant(val, ua.VariantType.Int32))
        dv.ServerTimestamp = None
        dv.SourceTimestap = None
        powerPump.set_value(dv)

    def set_Pump_power_2(self, Pump_toggle_2):
        if Pump_toggle_2:
            val = 1
        else:
            val = 0
        powerPump = self.client.get_node(
            "ns=2;s=PumpMng1.sStartPump")
        dv = ua.DataValue(ua.Variant(val, ua.VariantType.Int32))
        dv.ServerTimestamp = None
        dv.SourceTimestap = None
        powerPump.set_value(dv)

    def set_FILT_power(self, FILT_toggle):
        if FILT_toggle:
            val = 1
        else:
            val = 0
        power = self.client.get_node(
            "ns=2;s=PID_Regulator_4_Pipe1.sStartRegualtion")
        dv = ua.DataValue(ua.Variant(val, ua.VariantType.Int32))
        dv.ServerTimestamp = None
        dv.SourceTimestap = None
        power.set_value(dv)

    def set_DRAIN_V_power(self, toggle):
        if toggle:
            val = 1
        else:
            val = 0
        power = self.client.get_node(
            "ns=2;s=AirMng1.sEnable")
        dv = ua.DataValue(ua.Variant(val, ua.VariantType.Int32))
        dv.ServerTimestamp = None
        dv.SourceTimestap = None
        power.set_value(dv)

    def reset_Pump_error(self):
        pass
        # resetPump = self.client.get_node(
        #     "ns=2;s=PumpMng1.sQuitError")

        # toggle_button_ResetError.toggle()

        # TODO
        # try:
        #     val = 1
        #     dv = ua.DataValue(ua.Variant(val, ua.VariantType.Int32))
        #     dv.ServerTimestamp = None
        #     dv.SourceTimestap = None
        #     resetPump.set_value(dv)
        #     # time.sleep(1)
        #     toggle_button_ResetError.toggle()
        #     val = 0
        #     dv = ua.DataValue(ua.Variant(val, ua.VariantType.Int32))
        #     dv.ServerTimestamp = None
        #     dv.SourceTimestap = None
        #     resetPump.set_value(dv)
        # except Exception as e:
        #     print(e)

    def set_BPR_power_1(self, BPR_toggle_1):
        if BPR_toggle_1:
            val = 1
        else:
            val = 0
        powerBPR = self.client.get_node(
            "ns=2;s=MachineMng1.sStartValveFlowCompensation")
        dv = ua.DataValue(ua.Variant(val, ua.VariantType.Int32))
        dv.ServerTimestamp = None
        dv.SourceTimestap = None
        powerBPR.set_value(dv)

    @Slot(int, str)
    def changeHandler(self, val, node):
        if str(node) == self.PFR_T.nodeid.to_string():
            self.valPFR_T = val  # to avoid UnboundLocalError firstly defined in __init__
            self.get_label_PFR_T(val, str(node))
        elif str(node) == self.PFR_ctrlPower.nodeid.to_string():
            self.get_label_PFR_ctrlPower(val, str(node))
        elif str(node) == self.PFR_auxStep.nodeid.to_string():
            self.get_label_PFR_auxStep(val, str(node))
        elif str(node) == self.Ind_T.nodeid.to_string():
            self.get_label_IND_T(val, str(node))
        elif str(node) == self.Ind_T_ctrlPower.nodeid.to_string():
            self.get_label_IND_ctrlPower(val, str(node))
        elif str(node) == self.Ind_T_auxStep.nodeid.to_string():
            self.get_label_IND_auxStep(val, str(node))
        elif str(node) == self.Sep_T.nodeid.to_string():
            self.get_label_SEP_T(val, str(node))
        elif str(node) == self.Sep_T_ctrlPower.nodeid.to_string():
            self.get_label_SEP_ctrlPower(val, str(node))
        elif str(node) == self.Sep_T_auxStep.nodeid.to_string():
            self.get_label_SEP_auxStep(val, str(node))
        elif str(node) == self.BPR_P.nodeid.to_string():
            self.valBPR_P = val
            self.get_label_BPR_P(val, str(node))
        elif str(node) == self.BPR_ctrlPower.nodeid.to_string():
            self.get_label_BPR_ctrlPower(val, str(node))
        elif str(node) == self.BPR_T.nodeid.to_string():
            self.get_label_BPR_T(val, str(node))
        elif str(node) == self.HE_T_in.nodeid.to_string():
            self.get_label_HE_T_in(val, str(node))
        elif str(node) == self.HE_T_out.nodeid.to_string():
            self.get_label_HE_T_out(val, str(node))
        elif str(node) == self.Slurry_T_in.nodeid.to_string():
            self.get_label_Slurry_T_in(val, str(node))
        elif str(node) == self.SafetyV_T.nodeid.to_string():
            self.get_label_SafetyV_T(val, str(node))
        elif str(node) == self.LED_green.nodeid.to_string():
            self.get_label_LED_green(val, str(node))
        elif str(node) == self.LED_yellow.nodeid.to_string():
            self.get_label_LED_yellow(val, str(node))
        elif str(node) == self.LED_red.nodeid.to_string():
            self.get_label_LED_red(val, str(node))
        elif str(node) == self.Flow_A.nodeid.to_string():
            self.get_label_Flow_A(val, str(node))
        elif str(node) == self.Flow_B.nodeid.to_string():
            self.get_label_Flow_B(val, str(node))
        elif str(node) == self.Flow_tot.nodeid.to_string():
            self.get_label_Flow_tot(val, str(node))
        elif str(node) == self.Pump_V_out.nodeid.to_string():
            self.get_label_Pump_V_out(val, str(node))
        elif str(node) == self.Pump_P_out.nodeid.to_string():
            self.get_label_Pump_P_out(val, str(node))
        elif str(node) == self.Pump_P_A.nodeid.to_string():
            self.get_label_Pump_P_A(val, str(node))
        elif str(node) == self.Pump_P_B.nodeid.to_string():
            self.get_label_Pump_P_B(val, str(node))
        elif str(node) == self.Pump_SafetyP_A_2.nodeid.to_string():
            self.get_label_Pump_SafetyP_A_2(val, str(node))
        elif str(node) == self.Pump_SafetyP_B_2.nodeid.to_string():
            self.get_label_Pump_SafetyP_B_2(val, str(node))
        elif str(node) == self.FILT_T.nodeid.to_string():
            self.get_label_FILT_T(val, str(node))
        elif str(node) == self.FILT_auxStep.nodeid.to_string():
            self.get_label_FILT_auxStep(val, str(node))
        elif str(node) == self.FILT_ctrlPower.nodeid.to_string():
            self.get_label_FILT_ctrlPower(val, str(node))
        elif str(node) == self.FILT_T_in.nodeid.to_string():
            self.get_label_FILT_T_in(val, str(node))
        elif str(node) == self.FILT_P_in.nodeid.to_string():
            self.get_label_FILT_P_in(val, str(node))
        elif str(node) == self.DV.nodeid.to_string():
            self.get_label_DV(val, str(node))
        elif str(node) == self.DV_On.nodeid.to_string():
            self.get_label_DV_On(val, str(node))
        elif str(node) == self.DV_Off.nodeid.to_string():
            self.get_label_DV_Off(val, str(node))
        self.plt_vals(self.subdf)
        self.write_data()

    # ///////////////////////////////////////////////////////////////
    # DATA LOG
    # ///////////////////////////////////////////////////////////////

    def init_dataLog(self, custom=False, logcount_label=None):
        self.custom = custom
        if logcount_label !=None:
            self.logcount_label = logcount_label
            self.count = 0
        current_time = datetime.datetime.now()
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/logs/"+current_time.strftime('%Y_%m_%d')+'/'
        self.log_path = os.path.join(app_path, folder)
        os.makedirs(self.log_path, exist_ok=True)
        if custom:
            self.file_name_custom='dataLog_'+current_time.strftime('%Y%m%d_%H_%M_%S')+'.txt'
            self.dataLog = os.path.join(self.log_path, self.file_name_custom)
            with open(self.dataLog, 'w') as f:
                for entry in self.subdf['VISUALIZATION NAME']:
                    f.write(entry+',')
                f.write('t\n')
        else:
            self.file_name_base='dataLog.txt'
            self.dataLog = os.path.join(self.log_path, self.file_name_base)
            with open(self.dataLog, 'a') as f:
                for entry in self.subdf['VISUALIZATION NAME']:
                    f.write(entry+',')
                f.write('t\n')
    
    def write_data(self):
        if self.custom:
            if self.logcount_label != None:
                self.count += 1
                self.logcount_label.setText(str(self.count))
            else:
                pass
            self.dataLog = os.path.join(self.log_path, self.file_name_custom)
            with open(self.dataLog, 'a') as f:
                for entry in self.subdf['Values']:
                    f.write(str(entry)+',')
                f.write(str(self.dataDict['t'][-1])+'\n')
            self.dataLog = os.path.join(self.log_path, self.file_name_base)
            with open(self.dataLog, 'a') as f1:
                for entry in self.subdf['Values']:
                    f1.write(str(entry)+',')
                f1.write(str(self.dataDict['t'][-1])+'\n')
        else:
            self.count = 0
            self.dataLog = os.path.join(self.log_path, self.file_name_base)
            with open(self.dataLog, 'a') as f1:
                for entry in self.subdf['Values']:
                    f1.write(str(entry)+',')
                f1.write(str(self.dataDict['t'][-1])+'\n')
        


    # ///////////////////////////////////////////////////////////////
    # CHART
    # ///////////////////////////////////////////////////////////////

    def update_plt(self, chart):
        self.chart = chart

    def plt_vals(self, subdf):
        self.dataDict = self.chart.plt_vals(subdf=subdf)


    # ///////////////////////////////////////////////////////////////
    # LEDs
    # ///////////////////////////////////////////////////////////////

    def stream_LED_green(self, label):
        self.label_green = label

    def get_label_LED_green(self, val, node):
        if val:
            self.label_green.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
                                           "border: 1px solid black;")
        else:
            self.label_green.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
                                           "border: 1px solid black;")
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(str(val))
        self.chart_model.item(id[0], 5).setText(str(val))
        self.subdf.at[id[0], 'Values'] = val

        # .setStyleSheet(u"background: transparent;")

    def stream_LED_yellow(self, label):
        self.label_yellow = label

    def get_label_LED_yellow(self, val, node):
        if val:
            self.label_yellow.setStyleSheet(u"background-color: rgb(255, 255, 0);\n"
                                            "border: 1px solid black;")
        else:
            self.label_yellow.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
                                            "border: 1px solid black;")
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(str(val))
        self.chart_model.item(id[0], 5).setText(str(val))
        self.subdf.at[id[0], 'Values'] = val

    def stream_LED_red(self, label):
        self.label_red = label

    def get_label_LED_red(self, val, node):
        if val:
            self.label_red.setStyleSheet(u"background-color: rgb(255, 85, 0);\n"
                                         "border: 1px solid black;")
        else:
            self.label_red.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
                                         "border: 1px solid black;")
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(str(val))
        self.chart_model.item(id[0], 5).setText(str(val))
        self.subdf.at[id[0], 'Values'] = val

    # ///////////////////////////////////////////////////////////////
    # PFR
    # ///////////////////////////////////////////////////////////////

    def get_PFR_T(self):
        PFR_T = self.client.get_node(
            "ns=2;s=Read2chTemperature_1_PFR.sActTemperature")
        return PFR_T.get_value()

    def get_label_PFR_T(self, val, node):
        n_val = val/10
        val = str(val/10)+' °C'
        self.label_PFR_T.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        try:
            lst = self.dataDict[self.subdf.iloc[id[0]]['VISUALIZATION NAME']]
            self.chart_model.item(id[0], 4).setText(str(min(lst))+' °C')
            self.chart_model.item(id[0], 6).setText(str(max(lst))+' °C')
            self.chart_model.item(id[0], 8).setText(
                str(round(mean(lst), 1))+' °C')
        except AttributeError:
            pass
        self.chart_model.item(id[0], 5).setText(val)
        self.subdf.at[id[0], 'Values'] = n_val

    def stream_PFR_T(self, label):
        self.label_PFR_T = label
        self.handler.val_changed.connect(self.changeHandler)  # required!!!

    def get_label_PFR_ctrlPower(self, val, node):
        n_val = val/10
        val = str(val/10)+' %'
        self.label_PFR_ctrlPower.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        try:
            lst = self.dataDict[self.subdf.iloc[id[0]]['VISUALIZATION NAME']]
            self.chart_model.item(id[0], 4).setText(str(min(lst))+' %')
            self.chart_model.item(id[0], 6).setText(str(max(lst))+' %')
            self.chart_model.item(id[0], 8).setText(
                str(round(mean(lst), 1))+' %')
        except AttributeError:
            pass
        self.chart_model.item(id[0], 5).setText(val)
        self.subdf.at[id[0], 'Values'] = n_val

    def stream_PFR_ctrlPower(self, label):
        self.label_PFR_ctrlPower = label

    def get_label_PFR_auxStep(self, val, node):
        n_val = val/10
        val = str(val/10)+' °C'
        self.label_PFR_auxStep.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        try:
            lst = self.dataDict[self.subdf.iloc[id[0]]['VISUALIZATION NAME']]
            self.chart_model.item(id[0], 4).setText(str(min(lst))+' °C')
            self.chart_model.item(id[0], 6).setText(str(max(lst))+' °C')
            self.chart_model.item(id[0], 8).setText(
                str(round(mean(lst), 1))+' °C')
        except AttributeError:
            pass
        self.chart_model.item(id[0], 5).setText(val)
        self.subdf.at[id[0], 'Values'] = n_val

    def stream_PFR_auxStep(self, label):
        self.label_PFR_auxStep = label

    def set_PFR_power_2(self, PFR_toggle_2):
        if PFR_toggle_2:
            val = 1
        else:
            val = 0
        powerPFR = self.client.get_node(
            "ns=2;s=PID_Regulator_1_PFR.sStartRegualtion")
        dv = ua.DataValue(ua.Variant(val, ua.VariantType.Int32))
        dv.ServerTimestamp = None
        dv.SourceTimestap = None
        powerPFR.set_value(dv)

    def set_PFR_T(self, Tset):
        try:
            Tset = int(Tset)*10
        except ValueError:
            Tset = 0
        except Exception as e:
            print(e)
            Tset = int(Tset[:-4])*10
        PFR_T = self.client.get_node(
            "ns=2;s=PID_Regulator_1_PFR.sFinalSetPoint")
        dv = ua.DataValue(ua.Variant(Tset, ua.VariantType.Int32))
        dv.ServerTimestamp = None
        dv.SourceTimestap = None
        PFR_T.set_value(dv)

    # ///////////////////////////////////////////////////////////////
    # IND
    # ///////////////////////////////////////////////////////////////

    def get_label_IND_T(self, val, node):
        n_val = val/10
        val = str(val/10)+' °C'
        self.label_IND_T.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)
        self.subdf.at[id[0], 'Values'] = n_val

    def stream_IND_T(self, label):
        self.label_IND_T = label

    def get_label_IND_ctrlPower(self, val, node):
        n_val = val/10
        val = str(val/10)+' %'
        self.label_IND_ctrlPower.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)
        self.subdf.at[id[0], 'Values'] = n_val

    def stream_IND_ctrlPower(self, label):
        self.label_IND_ctrlPower = label

    def get_label_IND_auxStep(self, val, node):
        n_val = val/10
        val = str(val/10)+' °C'
        self.label_IND_auxStep.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)
        self.subdf.at[id[0], 'Values'] = n_val

    def stream_IND_auxStep(self, label):
        self.label_IND_auxStep = label

    def set_IND_power_2(self, IND_toggle_2):
        if IND_toggle_2:
            val = 1
        else:
            val = 0
        powerIND = self.client.get_node(
            "ns=2;s=PID_Regulator_3_PreHeater2.sStartRegualtion")
        dv = ua.DataValue(ua.Variant(val, ua.VariantType.Int32))
        dv.ServerTimestamp = None
        dv.SourceTimestap = None
        powerIND.set_value(dv)

    def set_IND_T(self, Tset):
        try:
            Tset = int(Tset)*10
        except ValueError:
            Tset = 0
        except Exception as e:
            print(e)
            Tset = int(Tset[:-4])*10
        dv = ua.DataValue(ua.Variant(Tset, ua.VariantType.Int32))
        dv.ServerTimestamp = None
        dv.SourceTimestap = None
        self.Ind_T.set_value(dv)

    # ///////////////////////////////////////////////////////////////
    # WATER AND SLURRY
    # ///////////////////////////////////////////////////////////////

    def stream_HE_T_in(self, label):
        self.label_HE_T_in = label

    def get_label_HE_T_in(self, val, node):
        val = str(val/10)+' °C'
        self.label_HE_T_in.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)

    def stream_HE_T_out(self, label):
        self.label_HE_T_out = label

    def get_label_HE_T_out(self, val, node):
        val = str(val/10)+' °C'
        self.label_HE_T_out.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)

    def stream_Slurry_T_in(self, label):
        self.label_Slurry_T_in = label

    def get_label_Slurry_T_in(self, val, node):
        val = str(val/10)+' °C'
        self.label_Slurry_T_in.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)

    def stream_SafetyV_T(self, label):
        self.label_SafetyV_T = label

    def get_label_SafetyV_T(self, val, node):
        val = str(val/10)+' °C'
        self.label_SafetyV_T.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)

    # ///////////////////////////////////////////////////////////////
    # SEP
    # ///////////////////////////////////////////////////////////////

    def set_SEP_power_2(self, SEP_toggle_2):
        if SEP_toggle_2:
            val = 1
        else:
            val = 0
        powerSEP = self.client.get_node(
            "ns=2;s=PID_Regulator_5_Pipe2.sStartRegualtion")
        dv = ua.DataValue(ua.Variant(val, ua.VariantType.Int32))
        dv.ServerTimestamp = None
        dv.SourceTimestap = None
        powerSEP.set_value(dv)

    def stream_SEP_T(self, label):
        self.label_SEP_T = label

    def get_label_SEP_T(self, val, node):
        val = str(round(val/10, 2))+' °C'
        self.label_SEP_T.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)

    def set_SEP_T(self, Tset):
        try:
            Tset = int(Tset)*10
        except ValueError:
            Tset = 0
        except Exception as e:
            print(e)
            Tset = int(Tset[:-4])*10
        dv = ua.DataValue(ua.Variant(Tset, ua.VariantType.Int32))
        dv.ServerTimestamp = None
        dv.SourceTimestap = None
        Sep_Tset = self.client.get_node(
            "ns=2;s=PID_Regulator_5_Pipe2.sFinalSetPoint")
        Sep_Tset.set_value(dv)

    def stream_SEP_ctrlPower(self, label):
        self.label_SEP_ctrlPower = label

    def get_label_SEP_ctrlPower(self, val, node):
        val = str(round(val/10, 2))+' %'
        self.label_SEP_ctrlPower.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)

    def stream_SEP_auxStep(self, label):
        self.label_SEP_auxStep = label

    def get_label_SEP_auxStep(self, val, node):
        val = str(round(val/10, 2))+' °C'
        self.label_SEP_auxStep.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)

    # ///////////////////////////////////////////////////////////////
    # BPR
    # ///////////////////////////////////////////////////////////////

    def set_BPR_power_2(self, BPR_toggle_2):
        if BPR_toggle_2:
            val = 1
        else:
            val = 0
        powerBPR = self.client.get_node(
            "ns=2;s=DuplicateSetPointGradient1.sStartRegualtion")
        dv = ua.DataValue(ua.Variant(val, ua.VariantType.Int32))
        dv.ServerTimestamp = None
        dv.SourceTimestap = None
        powerBPR.set_value(dv)
        print(powerBPR.get_value())

    def get_label_BPR_P(self, val, node):
        val = str(round(val/1000, 2))+' bar'
        self.label_BPR_P.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)

    def stream_BPR_P(self, label):
        self.label_BPR_P = label

    def set_BPR_P(self, Pset):
        try:
            Pset = int(Pset)*1000
        except ValueError:
            Pset = 15000
        except Exception as e:
            print(e)
            Pset = int(Pset[:-4])*1000
        BPR_P = self.client.get_node(
            "ns=2;s=DuplicateSetPointGradient1.sFinalSetPoint")
        dv = ua.DataValue(ua.Variant(Pset, ua.VariantType.Int32))
        dv.ServerTimestamp = None
        dv.SourceTimestap = None
        BPR_P.set_value(dv)

    def set_BPR_grad(self, grad):
        try:
            grad = float(grad)*1000
            grad = int(grad)
        except ValueError:
            grad = 15000
        except Exception as e:
            print(e)
            grad = int(grad[:-4])*1000
        BPR_grad = self.client.get_node(
            "ns=2;s=DuplicateSetPointGradient1.sGradient_unit_Sec")
        dv = ua.DataValue(ua.Variant(grad, ua.VariantType.Int32))
        dv.ServerTimestamp = None
        dv.SourceTimestap = None
        BPR_grad.set_value(dv)

    def stream_BPR_ctrlPower(self, label):
        self.label_BPR_ctrlPower = label

    def get_label_BPR_ctrlPower(self, val, node):
        val = str(round(val/1000, 2))+' %'
        self.label_BPR_ctrlPower.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)

    def stream_BPR_T(self, label):
        self.label_BPR_T = label

    def get_label_BPR_T(self, val, node):
        val = str(round(val/10, 2))+' °C'
        self.label_BPR_T.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)

    # ///////////////////////////////////////////////////////////////
    # PUMP
    # ///////////////////////////////////////////////////////////////

    def set_SafetyP_A(self, Pset_A):
        try:
            Pset = int(Pset_A)*100
        except ValueError:
            Pset = 1500
        except Exception as e:
            print(e)
            Pset = int(Pset_A[:-4])*100
        SafetyP_A = self.client.get_node(
            "ns=2;s=_ReadWriteHoldingRegister1.sSetSafetyPressureA")
        # "ns=2;s=_ReadInputRegister1.sSafetyPressureA_Bar")
        dv = ua.DataValue(ua.Variant(Pset, ua.VariantType.Int32))
        dv.ServerTimestamp = None
        dv.SourceTimestap = None
        SafetyP_A.set_value(dv)

    def set_SafetyP_B(self, Pset_B):
        try:
            Pset = int(Pset_B)*100
        except ValueError:
            Pset = 1500
        except Exception as e:
            print(e)
            Pset = int(Pset_B[:-4])*100
        SafetyP_B = self.client.get_node(
            "ns=2;s=_ReadWriteHoldingRegister1.sSetSafetyPressureB")
        # "ns=2;s=_ReadInputRegister1.sSafetyPressureA_Bar")
        dv = ua.DataValue(ua.Variant(Pset, ua.VariantType.Int32))
        dv.ServerTimestamp = None
        dv.SourceTimestap = None
        SafetyP_B.set_value(dv)

    def set_Flow_A(self, Flow_A):
        try:
            Pset = int(Flow_A)*100000
        except ValueError:
            Pset = 1500
        except Exception as e:
            print(e)
            Pset = int(Flow_A[:-4])*100000
        nFlow_A = self.client.get_node(
            "ns=2;s=_ReadWriteHoldingRegister1.sSetRateA")
        # "ns=2;s=_ReadInputRegister1.sSafetyPressureA_Bar")
        dv = ua.DataValue(ua.Variant(Pset, ua.VariantType.Int32))
        dv.ServerTimestamp = None
        dv.SourceTimestap = None
        nFlow_A.set_value(dv)

    def set_Flow_B(self, Flow_B):
        try:
            Pset = int(Flow_B)*100000
        except ValueError:
            Pset = 1500
        except Exception as e:
            print(e)
            Pset = int(Flow_B[:-4])*100000
        nFlow_B = self.client.get_node(
            "ns=2;s=_ReadWriteHoldingRegister1.sSetRateB")
        # "ns=2;s=_ReadInputRegister1.sSafetyPressureA_Bar")
        dv = ua.DataValue(ua.Variant(Pset, ua.VariantType.Int32))
        dv.ServerTimestamp = None
        dv.SourceTimestap = None
        nFlow_B.set_value(dv)

    def stream_Flow_A(self, label):
        self.label_Flow_A = label

    def get_label_Flow_A(self, val, node):
        val = str(round(val/1000000, 6))+' ml/min'
        self.label_Flow_A.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)

    def stream_Flow_B(self, label):
        self.label_Flow_B = label

    def get_label_Flow_B(self, val, node):
        val = str(round(val/1000000, 6))+' ml/min'
        self.label_Flow_B.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)

    def stream_Flow_tot(self, label):
        self.label_Flow_tot = label

    def get_label_Flow_tot(self, val, node):
        val = str(round(val/1000000, 6))+' ml/min'
        self.label_Flow_tot.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)

    def stream_Pump_V_out(self, label):
        self.label_Pump_V_out = label

    def get_label_Pump_V_out(self, val, node):
        val = str(round(val, 2))+' ml'
        self.label_Pump_V_out.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)

    def stream_Pump_P_out(self, label):
        self.label_Pump_P_out = label

    def get_label_Pump_P_out(self, val, node):
        val = str(round(val/1000, 2))+' bar'
        self.label_Pump_P_out.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)

    def stream_Pump_P_A(self, label):
        self.label_Pump_P_A = label

    def get_label_Pump_P_A(self, val, node):
        val = str(round(val/1000, 2))+' bar'
        self.label_Pump_P_A.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)

    def stream_Pump_P_B(self, label):
        self.label_Pump_P_B = label

    def get_label_Pump_P_B(self, val, node):
        val = str(round(val/1000, 2))+' bar'
        self.label_Pump_P_B.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)

    def stream_Pump_SafetyP_A_2(self, label):
        self.label_Pump_SafetyP_A_2 = label

    def get_label_Pump_SafetyP_A_2(self, val, node):
        val = str(round(val/100, 2))+' bar'
        self.label_Pump_SafetyP_A_2.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)

    def stream_Pump_SafetyP_B_2(self, label):
        self.label_Pump_SafetyP_B_2 = label

    def get_label_Pump_SafetyP_B_2(self, val, node):
        val = str(round(val/100, 2))+' bar'
        self.label_Pump_SafetyP_B_2.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)

    # ///////////////////////////////////////////////////////////////
    # FILTER
    # ///////////////////////////////////////////////////////////////

    def set_FILT_T(self, Tset):
        try:
            Tset = int(Tset)*10
        except ValueError:
            Tset = 0
        except Exception as e:
            print(e)
            Tset = int(Tset[:-4])*10
        dv = ua.DataValue(ua.Variant(Tset, ua.VariantType.Int32))
        dv.ServerTimestamp = None
        dv.SourceTimestap = None
        Sep_Tset = self.client.get_node(
            "ns=2;s=PID_Regulator_4_Pipe1.sFinalSetPoint")
        Sep_Tset.set_value(dv)

    def stream_FILT_T(self, label):
        self.label_FILT_T = label

    def get_label_FILT_T(self, val, node):
        val = str(round(val/10, 2))+' °C'
        self.label_FILT_T.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)

    def stream_FILT_ctrlPower(self, label):
        self.label_FILT_ctrlPower = label

    def get_label_FILT_ctrlPower(self, val, node):
        val = str(round(val/10, 2))+' %'
        self.label_FILT_ctrlPower.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)

    def stream_FILT_auxStep(self, label):
        self.label_FILT_auxStep = label

    def get_label_FILT_auxStep(self, val, node):
        val = str(round(val/10, 2))+' °C'
        self.label_FILT_auxStep.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)

    def stream_FILT_T_in(self, label):
        self.label_FILT_T_in = label

    def get_label_FILT_T_in(self, val, node):
        val = str(round(val/10, 2))+' °C'
        self.label_FILT_T_in.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)

    def stream_FILT_P_in(self, label):
        self.label_FILT_P_in = label

    def get_label_FILT_P_in(self, val, node):
        val = str(round(val/100, 2))+' bar'
        self.label_FILT_P_in.setText(val)
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(val)
        self.chart_model.item(id[0], 5).setText(val)

    # ///////////////////////////////////////////////////////////////
    # DRAIN VALVE
    # ///////////////////////////////////////////////////////////////

    def stream_DV(self, label):
        self.label_DV = label

    def get_label_DV(self, val, node):
        self.label_DV.setText(str(val))
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(str(val))
        self.chart_model.item(id[0], 5).setText(str(val))

    def stream_DV_On(self, label):
        self.label_DV_TimeOn = label

    def get_label_DV_On(self, val, node):
        self.label_DV_TimeOn.setText(str(val))
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(str(val))
        self.chart_model.item(id[0], 5).setText(str(val))

    def stream_DV_Off(self, label):
        self.label_DV_TimeOff = label

    def get_label_DV_Off(self, val, node):
        self.label_DV_TimeOff.setText(str(val))
        node = node[7:].replace(".", "_")
        id = self.subdf[self.subdf['OPC/UA_DISPLAYNAME'] == node].index
        self.var_model.item(id[0], 8).setText(str(val))
        self.chart_model.item(id[0], 5).setText(str(val))
