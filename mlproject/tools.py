from mlproject.distance import haversine


if __name__ == "__main__":
    # Le Wagon location
        lat1, lon1 = 48.865070, 2.380009
    #Insert your coordinates from google maps here
    #lat2, lon2 = x, y
        distance = haversine(lon1, lat1, lon2, lat2)
        print(distance)
