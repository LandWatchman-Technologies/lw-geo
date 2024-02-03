from geopy.distance import geodesic

def calc_distance_list(points_list):
    point_0 = points_list[0]
    total_distance = 0

    for i, point in enumerate(points_list):
        if i > 0:
            total_distance += geodesic(
                (float(point_0["lat"]), float(point_0["lon"])),
                (float(point["lat"]), float(point["lon"])),
            ).m
            point_0 = point
    return total_distance

def calc_distance(point_1, point_2):
    return geodesic(
        (float(point_1["lat"]), float(point_1["lon"])),
        (float(point_2["lat"]), float(point_2["lon"])),
    ).m