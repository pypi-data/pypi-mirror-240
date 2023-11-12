import pandas as pd
from geopy.distance import geodesic
from datetime import datetime, timedelta
import plotly.express as px
import os

def calculate_distance(lat, lon, df_deviceid_file_path, distance, row_lat='lat', row_lon='lon', deviceid='device_id'):
    # Read the device data from the CSV file
    df_deviceid = pd.read_csv(df_deviceid_file_path)
    
    # Drop rows with missing lat or lon values
    df_deviceid = df_deviceid.dropna(subset=[row_lat, row_lon], how='all')
    
    # Ensure latitude and longitude values are within valid ranges
    min_lat = -90
    max_lat = 90
    min_lon = -180
    max_lon = 180
    df_deviceid[row_lat] = df_deviceid[row_lat].apply(lambda x: min(max(min_lat, x), max_lat))
    df_deviceid[row_lon] = df_deviceid[row_lon].apply(lambda x: min(max(min_lon, x), max_lon))

    # Create a function to calculate the distance
    def calculate_distance_row(row):
        device_location = (row[row_lat], row[row_lon])
        target_location = (lat, lon)
        distance = geodesic(device_location, target_location).kilometers
        return distance

    # Add a column to store the distances
    df_deviceid['distance_km'] = df_deviceid.apply(calculate_distance_row, axis=1)

    # Filter out data within one kilometer
    filtered_df = df_deviceid[df_deviceid['distance_km'] <= distance]

    # Get the list of device IDs
    lst_device_id = filtered_df[deviceid].to_list()

    return lst_device_id

def filter_data_for_device(result_lst_device_id, time, df_device_file_path, row_time='localTime', row_deviceid='deviceId',sensor='PM2.5'):
    def get_date_hour_min(time2minus, now, str_time):
        str_date = str_time.split(' ')[0]
        str_hour = str_time.split(' ')[1].split(':')[0]
        str_minute = str_time.split(' ')[1].split(':')[1][0]
        if str_minute == '0':
            if str_hour == '00':
                str_time = now - timedelta(minutes=time2minus + 10)
                str_time = str_time.strftime("%Y-%m-%d %H:%M:%S")
                str_date = str_time.split(' ')[0]
                str_hour = str_time.split(' ')[1].split(':')[0]
                str_minute = str_time.split(' ')[1].split(':')[1][0]
            else:
                str_hour = str(int(str_hour) - 1).zfill(2)
                str_minute = '5'
        else:
            str_minute = str(int(str_minute) - 1)

        return str_date, str_hour, str_minute
    
    def filter_time(df, time):
        user_input_time = pd.to_datetime(time)
        half_hour_offset = pd.DateOffset(minutes=30)
        start_time = user_input_time - half_hour_offset
        end_time = user_input_time + half_hour_offset
        df[row_time] = pd.to_datetime(df[row_time])
        filtered_data = df[(df[row_time] >= start_time) & (df[row_time] <= end_time)].reset_index(drop = True)
        return filtered_data
    
    def filter_deviceid(df, result_lst_device_id):
        df = df[df[row_deviceid].isin(result_lst_device_id)].reset_index(drop = True)
        return df
    
    df_all = pd.DataFrame()

    get_time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')

    for i in range(-40, 40, 10):
        str_time = get_time - timedelta(minutes=i)
        str_time = str_time.strftime("%Y-%m-%d %H:%M:%S")
        str_date, str_hour, str_minute = get_date_hour_min(i, time, str_time)
        str_url = f'{df_device_file_path}/{str_date}/10mins_{str_date} {str_hour}_{str_minute}.csv.gz'
        try:
            str_url = f'{df_device_file_path}/{str_date}/10mins_{str_date} {str_hour}_{str_minute}.csv.gz'
            df = pd.read_csv(str_url, compression='gzip')
            df_all = df_all.append(df, ignore_index=True)
        except:
            pass
    df_all = filter_time(df_all, time)
    df_all = filter_deviceid(df_all, result_lst_device_id)
    df_all = df_all[df_all['sensorId']=='pm2_5'].reset_index(drop = True)
    
    return df_all

def create_pm25_map(df,lat, lon, file_name, row_value='value', row_deviceId='deviceId', row_lat='lat', row_lon='lon', row_time='localTime'):
    # Filter data
    df[row_value] = df[row_value].astype(float)
    df = df.loc[df.groupby(row_deviceId)[row_value].idxmax()]

    # Create scatter mapbox
    fig = px.scatter_mapbox(df, lat=row_lat, lon=row_lon, color=row_value,
                            color_continuous_scale='turbo', range_color=(0, 300),
                            hover_data=[row_time, row_deviceId, row_value],
                            zoom=7, height=600)

    fig.update_layout(mapbox_style='open-street-map')

    initial_center = {"lat": lat, "lon": lon}  # Example coordinates
    initial_zoom = 13  # Example zoom level
    fig.update_layout(mapbox_center=initial_center, mapbox_zoom=initial_zoom)

    fig.update_layout(margin={'r': 0, 't': 0, 'l': 0, 'b': 0})

    # Save to html
    output_path = f'./code/{file_name}.html'
    fig.write_html(output_path, include_plotlyjs=True)
    
    return output_path


if __name__ == '__main__':
    # Example of calculate_distance usage:
    lon = 121.4471
    lat = 25.0669
    df_deviceid_file_path = '/Users/apple/Downloads/project_device_table_20231017.csv'
    result_lst_device_id = calculate_distance(lat, lon, df_deviceid_file_path, 1)
    print(result_lst_device_id)
    
    # Example of filter_data_for_device_time usage:
    df_device_file_path = '/Users/apple/Desktop/iot_data'
    time = '2023-11-03 08:35:00'
    df = filter_data_for_device(result_lst_device_id, time,df_device_file_path)
    print(df.localTime.min())
    print(df.localTime.max())
