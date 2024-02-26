from geopy.distance import geodesic
from typing import List, Optional

def calc_distance_list(points_list: List[dict]) -> float:
    """
    Calculate the total distance traversed by a list of points using the geodesic distance formula.
    
    Args:
        points_list (List[dict]): A list of dictionaries representing points with 'lat' and 'lon' keys.
        
    Returns:
        float: The total distance traversed by the list of points.
    """
    
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

def calc_distance(point_1: dict, point_2: dict) -> float:
    return geodesic(
        (float(point_1["lat"]), float(point_1["lon"])),
        (float(point_2["lat"]), float(point_2["lon"])),
    ).m
    
def filter_points(points_list: List[dict], lower_bound: Optional[float]=2, upper_bound: Optional[float]=200)-> List[dict]:
    filtered_points = [points_list[0]]  # Start with the first point
    for i in range(1, len(points_list)):
        distance = calc_distance(points_list[i - 1], points_list[i], )
        if lower_bound <= distance <= upper_bound:
            filtered_points.append(points_list[i])
    return filtered_points