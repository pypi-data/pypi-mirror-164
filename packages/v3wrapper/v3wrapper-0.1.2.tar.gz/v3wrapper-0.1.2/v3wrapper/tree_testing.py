import pandas as pd
from functions_sensor_tree import Node,create_tree, SensorData
from v3wrapper import retrieve_multiple_telemetries_flex_schedule
from functions_aux import list_results
pd.set_option('display.max_columns', None)
import matplotlib.pyplot as plt

configuration_df=pd.read_csv("area_classification.csv")
selection_attributes=["desk_or_area"]
levels=["building","group","application_type","level_01","level_02","level_03"]
roots = create_tree(configuration_df=configuration_df,levels=levels,initial_depth=0,add_sensor_names=False)
for root in roots:
    root.render()

r1 = root.search("Hive",partial_match=False,first_result=True, verbose=True)

h8 = root.search("Hive 8")

user='API-USER-ACCENTURE-JUAN'
pwd='67DFEC0B-C3E3-4C54-989D-B22DA602DB38'

telemetries = ['AREA_COUNT']
frequency_minutes='1'   #frequency of the data retrieved
resample_freq_minutes = 5  #display frequency

#SPECIFY EVERYTHNG IN LOCAL TIME INTERVAL
from_local_time = '2022-08-22T00:00:00'
to_local_time =   '2022-08-23T23:59:00'
schedule = {1: ('00:00', '23:59'),
            2: ('00:00', '23:59'),
            3: ('00:00', '23:59'),
            4: ('00:00', '23:59'),
            5: ('00:00', '23:59'),
            6: ('00:00', '23:59'),
            7: ('00:00', '23:59')
            }

tz_code = "Europe/London"
exclude_holidays_country_region=[]
operation = 'max'
output_directory = ''

s = SensorData(h8)
df = retrieve_multiple_telemetries_flex_schedule(
user =user,
pwd=pwd,
# id_list=[str(x) for x in s.sensor_ids],
id_list=['125083', '125078', '125077', '125095'],
id_to_name_dictionary=None,telemetry_list=telemetries,interval_minutes=frequency_minutes,
from_local_time=from_local_time,to_local_time=to_local_time,max_days_per_call=31,tz_code=tz_code,
schedule=schedule,exclude_holidays_country_region=exclude_holidays_country_region,operation=operation,
group_by="asset",na_fill="ffill")


params_dict={"max_num_sensors_per_call":10,"user":user,"pwd":pwd,
             "id_list":[str(x) for x in s.sensor_ids],
             "id_to_name_dictionary":None,
             "telemetry_list":telemetries,"interval_minutes":frequency_minutes,"from_local_time":from_local_time,"to_local_time":to_local_time,
             "max_days_per_call":31,"tz_code":tz_code,"schedule":schedule,"exclude_holidays_country_region":exclude_holidays_country_region,
             "operation":operation,
             "group_by":"asset","na_fill":"ffill"}

s = SensorData(h8)
s.load_params(params_dict)
s.load_data()
df2 = s.merge_data("AREA_COUNT",transform_function="plain",use_sensor_names=True)
df3 = s.merge_data("AREA_COUNT","sum",True)

#IAQ example

iaq = root.search("IAQ",partial_match=False,first_result=True, verbose=True)
iaq_sensors = SensorData(iaq)
params_dict["telemetry_list"]=["TEMPERATURE","HUMIDITY"]
iaq_sensors.load_params(params_dict)

temperature = iaq_sensors.merge_data("TEMPERATURE")
mean_temperature = iaq_sensors.merge_data("TEMPERATURE",transform_function="mean",use_sensor_names=False)