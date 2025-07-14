import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="coe64-241"
)
cursor = conn.cursor()

df = pd.read_excel("Data.xlsx", engine="openpyxl")

# for index, row in df.iterrows():
#     sql = "INSERT INTO sensor_datas (timestamp, temperature, humidity, ph, rainfall, soil_moisture, sunlight_exposure, wind_speed, co2_concentration, frost_risk, water_usage_efficiency) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#     values = (row["Timestamp"], row["Temperature"], row["Humidity"], row["PH"], row["Rainfall"], row["Soil_moisture"], row["Sunlight_exposure"], row["Wind_speed"], row["CO2_concentration"], row["Frost_risk"], row["Water_usage_efficiency"])
#
#     cursor.execute(sql, values)
#
# for index, row in df.iterrows():
#     sql = "INSERT INTO crop_infos (plant, growth_stage, plantation_area, pest_pressure, crop_density) VALUES (%s, %s, %s, %s, %s)"
#     values = (row["Plant"], row["Growth_stage"], row["Plantation_area"], row["Pest_pressure"], row["Crop_density"])
#     cursor.execute(sql, values)
#
# for index, row in df.iterrows():
#     sql = "INSERT INTO geo_environmentals (urban_area_proximity) values (%s)"
#     values = (row["Urban_area_proximity"],)
#     cursor.execute(sql, values)

# for index, row in df.iterrows():
#     sql = "INSERT INTO soil_compositions(nitrogen, phosphorus, potassium, organic_matter, soil_type) values (%s, %s, %s, %s, %s)"
#     values = (row["Nitrogen"], row["Phosphorus"], row["Potassium"], row["Organic_matter"], row["Soil_type"])
#     cursor.execute(sql, values)

# a = 1
# for index, row in df.iterrows():
#     sql = "INSERT INTO farm_datas(sensor_datasId, soil_compositionsId, irrigation_fertilizationsId, crop_infosId, geo_environmentalsId) values (%s, %s, %s, %s, %s)"
#     values = (a, a, a, a, a)
#     cursor.execute(sql, values)
#     a += 1



conn.commit()
cursor.close()
conn.close()

print("Data imported successfully!")
