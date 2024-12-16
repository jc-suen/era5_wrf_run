# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 18:47:24 2024

@author: sun-jc
"""

import cdsapi
import os

c = cdsapi.Client()

# 指定目标文件夹
output_folder = r"E:\wrf_era5\ERA5_data"

# 确保目标文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 定义日期范围
year = "2022"
month = "09"
days = [
    "01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
    "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
    "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"
]

for day in days:
    output_filename = f"ERA5-{year}-{month}-{day}_2D.grib"
    output_path = os.path.join(output_folder, output_filename)

    c.retrieve(
        'reanalysis-era5-single-levels',
        {
            'product_type': 'reanalysis',
            'format': 'grib',
            'variable': [
                '10m_u_component_of_wind', '10m_v_component_of_wind', '2m_dewpoint_temperature',
                '2m_temperature', 'forecast_albedo', 'forecast_logarithm_of_surface_roughness_for_heat',
                'high_cloud_cover', 'land_sea_mask', 'low_cloud_cover',
                'mean_sea_level_pressure', 'medium_cloud_cover', 'sea_ice_cover',
                'sea_surface_temperature', 'skin_temperature', 'snow_albedo',
                'snow_depth', 'snowfall', 'soil_temperature_level_1',
                'soil_temperature_level_2', 'soil_temperature_level_3', 'soil_temperature_level_4',
                'soil_type', 'surface_pressure', 'total_cloud_cover',
                'total_column_water', 'total_column_water_vapour', 'total_precipitation',
                'volumetric_soil_water_layer_1', 'volumetric_soil_water_layer_2', 'volumetric_soil_water_layer_3',
                'volumetric_soil_water_layer_4',
            ],
            'year': year,
            'month': month,
            'day': day,
            'time': [
                '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00',
                '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00',
                '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00',
            ],
            'area': [80.00, 80.00, -10.00, 170.00],
        },
    ).download(output_path)

    print(f"Downloaded data for {year}-{month}-{day} to {output_path}")