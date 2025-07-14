import psycopg2
import pandas as pd

# เชื่อมต่อ PostgreSQL
conn = psycopg2.connect(
    dbname="farm_info",
    user="farm_info_user",
    password="42o5yORjVMXllaQADlSquxcpaCk6dYR8",
    host="dpg-cusvme0gph6c73atupg0-a.singapore-postgres.render.com",
    port="5432"
)
# postgresql://farm_info_user:42o5yORjVMXllaQADlSquxcpaCk6dYR8@dpg-cusvme0gph6c73atupg0-a.singapore-postgres.render.com/farm_info
cursor = conn.cursor()

df = pd.read_excel("Data.xlsx", engine="openpyxl")
#
# for index, row in df.iterrows():
#     sql = "INSERT INTO sensor_datas (timestamp, temperature, humidity, ph, rainfall, soil_moisture, sunlight_exposure, wind_speed, co2_concentration, frost_risk, water_usage_efficiency) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#     values = (row["Timestamp"], row["Temperature"], row["Humidity"], row["PH"], row["Rainfall"], row["Soil_moisture"], row["Sunlight_exposure"], row["Wind_speed"], row["CO2_concentration"], row["Frost_risk"], row["Water_usage_efficiency"])
#
#     cursor.execute(sql, values)
# # #
# for index, row in df.iterrows():
#     sql = "INSERT INTO crop_infos (plant, growth_stage, plantation_area, pest_pressure, crop_density) VALUES (%s, %s, %s, %s, %s)"
#     values = (row["Plant"], row["Growth_stage"], row["Plantation_area"], row["Pest_pressure"], row["Crop_density"])
#     cursor.execute(sql, values)
# #
#
# for index, row in df.iterrows():
#     sql = "INSERT INTO geo_environmentals (urban_area_proximity) values (%s)"
#     values = (row["Urban_area_proximity"],)
#     cursor.execute(sql, values)
#
# for index, row in df.iterrows():
#     sql = "INSERT INTO soil_compositions(nitrogen, phosphorus, potassium, organic_matter, soil_type) values (%s, %s, %s, %s, %s)"
#     values = (row["Nitrogen"], row["Phosphorus"], row["Potassium"], row["Organic_matter"], row["Soil_type"])
#     cursor.execute(sql, values)

# for index, row in df.iterrows():
#     sql = "INSERT INTO irrigation_fertilizations (timestamp, irrigation_frequency, fertilizer_usage, water_source_type) values (%s, %s, %s, %s)"
#     values = (row["Timestamp"], row["Irrigation_frequency (times/week)"], row["Fertilizer_usage"], row["Water_source_type"])
#     cursor.execute(sql, values)


# a = 1
# for index, row in df.iterrows():
#     sql = """
#     INSERT INTO farm_datas(
#         "sensor_datasId",
#         "soil_compositionsId",
#         "irrigation_fertilizationsId",
#         "crop_infosId",
#         "geo_environmentalsId"
#     ) values (%s, %s, %s, %s, %s)
#     """
#     values = (a, a, a, a, a)
#     cursor.execute(sql, values)
#     a += 1

# a =1
# for index, row in df.iterrows():
#     sql = "UPDATE irrigation_fertilizations SET water_usage_efficiency = %s WHERE id = %s"
#     values = (row["Water_usage_efficiency"], a)
#
#     cursor.execute(sql, values)
#
#     a += 1

import random

a = 1
def is_valid_coordinate(lat, lon):
    return (5.61 <= lat <= 20.46) and (97.35 <= lon <= 105.63)

regions = {
    "North": {"lat": [16.0, 20.5], "lon": [97.3, 100.9]},
    "Center": {"lat": [13.0, 16.0], "lon": [99.0, 101.5]},
    "South": {"lat": [6.0, 13.0], "lon": [98.5, 101.5]},
}

for index, row in df.iterrows():
    sql = "SELECT plantation_area FROM crop_infos WHERE id = %s"
    values = (a,)
    cursor.execute(sql, values)
    result = cursor.fetchone()

    if result:
        plantation_area = result[0]

        if plantation_area in regions:
            lat_range = regions[plantation_area]["lat"]
            lon_range = regions[plantation_area]["lon"]

            while True:  # 🔄 สุ่มซ้ำจนกว่าจะได้ค่าที่ถูกต้อง
                latitude = round(random.uniform(lat_range[0], lat_range[1]), 6)
                longitude = round(random.uniform(lon_range[0], lon_range[1]), 6)
                if is_valid_coordinate(latitude, longitude):
                    break

            sql = "UPDATE crop_infos SET latitude = %s, longitude = %s WHERE id = %s"
            values = (latitude, longitude, a)
            cursor.execute(sql, values)

    a += 1

conn.commit()
cursor.close()
conn.close()

print("Data imported successfully!")
