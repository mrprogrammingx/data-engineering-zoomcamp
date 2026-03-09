import pandas as pd

def load_data():
    yellow_tripdata = pd.read_parquet('data/green_tripdata_2025-11.parquet')
    taxi_zones_data = pd.read_csv('data/taxi_zone_lookup.csv')
    return yellow_tripdata, taxi_zones_data

# count short trips in November 2025
def count_short_trips(df):
    return len(df.query(
        "trip_distance <= 1 and '2025-11-01' <= lpep_pickup_datetime < '2025-12-01'"
    ))

# longest trip day with distance less than 100 miles
def longest_trip_day(df):
    return df.query(
        "trip_distance <= 100"
    ).sort_values('trip_distance', ascending=False).head(1)['lpep_pickup_datetime']

# longest trip per zone for November 18, 2025
def longest_trip_zone(df, zones):
    return df.query(
        "'2025-11-18' <= lpep_pickup_datetime < '2025-11-19'"
    ).groupby(
        'PULocationID'
        )['total_amount'].sum().reset_index(name='total_amount').sort_values(
            'total_amount', ascending=False
        ).head(1).merge(
            zones[['LocationID', 'Zone']],
            left_on='PULocationID',
            right_on='LocationID',
            how='left'
        )[['Zone']]['Zone']

# largest tip for trips starting in East Harlem North in November 2025
def largest_tip(df, zones):
    east_harlem_north_id = zones.query("Zone == 'East Harlem North'")['LocationID'].values[0]
    return df.query(
        "'2025-11-01' <= lpep_pickup_datetime < '2025-12-01' and PULocationID == @east_harlem_north_id"
    ).sort_values('tip_amount', ascending=False).head(1).merge(
        zones[['LocationID','Zone']],
        left_on='DOLocationID',
        right_on='LocationID',
        how='left'
    )['Zone'].values[0]

def main():
    trips, zones = load_data()
    short_trip_count = count_short_trips(trips)
    longest_day = longest_trip_day(trips)
    longest_zone = longest_trip_zone(trips, zones)

if __name__ == "__main__":
    main()
