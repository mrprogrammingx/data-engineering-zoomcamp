import pandas as pd

def load_data():
    yellow_tripdata = pd.read_parquet('data/green_tripdata_2025-11.parquet')
    taxi_zones_data = pd.read_csv('data/taxi_zone_lookup.csv')
    return yellow_tripdata, taxi_zones_data

def count_short_trips(df):
    return len(df.query(
        "trip_distance <= 1 and '2025-11-01' <= lpep_pickup_datetime < '2025-12-01'"
    ))

def main():
    trips, zones = load_data()
    short_trip_count = count_short_trips(trips)
    print("Short trips:", short_trip_count)

if __name__ == "__main__":
    main()
