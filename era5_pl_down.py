# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 15:53:27 2024

@author: sun-jc
"""

import cdsapi
import os

c = cdsapi.Client()

# 指定目标文件夹
output_folder = r"E:\wrf_era5\Hinnamnor_pressure"

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
    output_filename = f"ERA5-{year}-{month}-{day}_pl.grib"
    output_path = os.path.join(output_folder, output_filename)

    c.retrieve(
        'reanalysis-era5-pressure-levels',
        {
            'product_type': 'reanalysis',
            'format': 'grib',
            'variable': [
                'geopotential', 'relative_humidity', 'temperature', 'specific_humidity',
                'u_component_of_wind', 'v_component_of_wind', 'vertical_velocity'
            ],
            'pressure_level': [
                '1', '2', '3', '5', '7', '10', '20', '30', '50', '70', '100', '125',
                '150', '175', '200', '225', '250', '300', '350', '400', '450', '500',
                '550', '600', '650', '700', '750', '775', '800', '825', '850', '875',
                '900', '925', '950', '975', '1000',
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
