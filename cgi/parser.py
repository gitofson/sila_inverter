import json
import crc16
from collections import OrderedDict

batteryTypes = {'0': 'AGM', '1': 'FLA', '2': 'User Defined'}
voltageRanges = {'0': 'Appliance', '1': 'UPS'}
outputSources = {'0': 'Utility first', '1': 'Solar first', '2': 'SBU'}
chargerSources = {'0': 'Utility first', '1': 'Solar first', '2': 'Solar + Utility', '3': 'Solar only'}
deviceTypes = {'00': 'Grid tie', '01': 'Off grid', '10': 'Hybrid',
               '11': 'Off Grid, 2 trackers', '20': 'Off grid, 3 trackers'}
topologies = {'0': 'transformerless', '1': 'transformer'}
outputModes = {'0': 'Single', '1': 'Parallel', '2': 'Phase 1', '3': 'Phase 2', '4': 'Phase 3'}
pvStatuses = {'0': 'On one OK', '1': 'On all OK'}
balances = {'0': 'PV max current', '1': 'PV max power'}


def QPIGS(a):
    # len 112
    data = {}
#    data['command'] = 'QPIGS'
    if len(a) >= 110:
        nums = a[1:].split()
        data["Grid_voltage"] = float(nums[0])
        data["Grid_frequency"] = float(nums[1])
        data["AC_output_voltage"] = float(nums[2])
        data["AC_output_frequency"] = float(nums[3])
        data["AC_output_apparent_power"] = float(nums[4])
        data["AC_output_active_power"] = float(nums[5])
        data["Output_Load_Percent"] = float(nums[6])
        data["Bus_voltage"] = float(nums[7])
        data["Battery_voltage"] = float(nums[8])
        data["Battery_charging_current"] = float(nums[9])
        data["Battery_capacity"] = float(nums[10])
        data["Inverter_heatsink_temperature"] = float(nums[11])
        data["PV_input_current_for_battery"] = float(nums[12])
        data["PV_Input_Voltage"] = float(nums[13])
        data["Battery_voltage_from_SCC"] = float(nums[14])
        data["Battery_discharge_current"] = float(nums[15])
        data["Device_status"] = nums[16]
 #       data['error'] = False
    else:
        data['error'] = True
    return data
#    return json.dumps(data, indent=2)


def QPIRI(a):
    # len 104
    data = {}
    data['command'] = 'QPIRI'
    if len(a) >= 97:
        r = a[1:].split()
        data['error'] = False
        data['Utility_voltage'] = r[0]
        data['Utility_current'] = r[1]
        data['Output_voltage'] = r[2]
        data['Output_frequency'] = r[3]
        data['Output_current'] = r[4]
        data['Output_va'] = r[5]
        data['output_watts'] = r[6]
        data['Battery_voltage'] = r[7]
        data['Battery_bulk_charge_voltage'] = r[8]
        data['Battery_cutoff_voltage'] = r[9]
        data['Battery_bulk_charge_voltage'] = r[10]
        data['Battery_float_charge_voltage'] = r[11]
        data['Battery_type'] = r[12]
        data['Baximum_utility_charge_current'] = r[13]
        data['Baximum_charge_current'] = r[14]
        data['Bnput_voltage_sensitivity'] = r[15]
        data['Output_source_priority'] = r[16]
        data['Charger_source_priority'] = r[17]
        data['Maximum_parallel_units'] = r[18]
        data['Device_type'] = r[19]
        data['Device_topology'] = r[20]
        data['Output_mode'] = r[21]
        data['Battery_float_charge_voltage'] = r[22]
        data['PV_parallel_ok_mode'] = r[23]
        data['PV_power_balance_mode'] = r[24][:1]
    else:
        data['error'] = True
    return data
#    return json.dumps(data, indent=2)


def QMOD(a):
    data = {}
    data['command'] = 'QMOD'
    if len(a) >= 5:

        data['error'] = False
        a = a[1:2]
        if a == 'P':
            res = 'power'
        elif a == 'S':
            res = 'standby'
        elif a == 'L':
            res = 'line'
        elif a == 'B':
            res = 'battery'
        elif a == 'F':
            res = 'fault'
        elif a == 'H':
            res = 'power_savig'
        else:
            res = 'unknown'
        data['state'] = res
    else:
        data['error'] = True
    return data
#    return json.dumps(data)


def QDI(a):
    # len 80
    data = {}

    data['command'] = 'QDI'
    if len(a) >= 79:
        r = a[1:].split()
        data['error'] = False
        data['Output_voltage'] = r[0]
        data['Output_frequency'] = r[1]
        data['Maximum_ac_charge_current'] = r[2]
        data['Battery_cutoff_voltage'] = r[3]
        data['Battery_float_charge_voltage'] = r[4]
        data['Battery_bulk_charge_voltage'] = r[5]
        data['Battery_bulk_charge_voltage'] = r[6]
        data['Maximum_charge_current'] = r[7]
        data['Input_voltage_sensitivity'] = r[8]
        data['Output_source_priority'] = r[9]
        data['Charger_source_priority'] = r[10]
        data['Battery_type'] = r[11]
        data['Enable_power_saving'] = r[13]
        data['Enable_overload_restart'] = r[14]
        data['Enable_over_temperature_restart'] = r[15]
        data['Enable_lcd_backlight'] = r[16]
        data['Enable_primary_source_interrupt_alarm'] = r[17]
        data['Enable_fault_code_recording'] = r[18]
        data['Enable_bypass_to_utility_on_overload'] = r[19]
        data['Enable_lcd_timeout_escape_to_default_page'] = r[20]
        data['Output_mode'] = r[21]
        data['Battery_float_charge_voltage'] = r[22]
        data['PV_parallel_ok_mode'] = r[23]
        data['PV_power_balance_mode'] = r[24][:1]
    else:
        data['error'] = True
    return data
#    return json.dumps(data, indent=2)


def parse_resp(command, resp):
    if command == 'QDI':
        return QDI(resp)
    elif command == 'QMOD':
        return QMOD(resp)
    elif command == 'QPIGS':
        return QPIGS(resp)
    elif command == 'QPIRI':
        return QPIRI(resp)
    else:
        data = {}
        data['resp'] = 'unknown'

        return json.dumps(data)
