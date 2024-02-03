# lw-geo

# Geo-Distance API

## Setup
### Environment

1. Create `Python>=3.10` Virtual Environment.


2. Install Requirements
```
pip install -r requirements.txt
```

### Deployment
Deploy on a specific port eg 8501. Default port is 8501

```
python -m geo_distance.flask_geo_distance <port>
```

For Example
```
python -m geo_distance.flask_geo_distance 8501
```

# API Documentation
## Calculate Distance for a List of Points
### Endpoint: `/distance_list`
#### Method: `POST`

Calculate the total distance for a list of geographical points.

#### Request Body:
- **Format:** JSON
- **Field:** `points` (list of dictionaries)
  - Each dictionary should have:
    - `lat` (float): Latitude of the point.
    - `lon` (float): Longitude of the point.

#### Response:
- **Status Code:** 200 OK
- **Body:** JSON object containing the following fields:
  - `distance_metres` (float): Total distance in meters.
  - `distance_kilometres` (float): Total distance in kilometers.
  - `distance_miles` (float): Total distance in miles.

#### Error Response:
- **Status Code:** 400 Bad Request
- **Body:** JSON object with the following field:
  - `error` (string): Error message indicating invalid JSON format or insufficient points.


## Calculate Distance
### Endpoint: `/distance`
#### Method: `GET`

Calculate the distance between two geographical points.

#### Parameters:
- `lat1` (float): Latitude of the first point.
- `lon1` (float): Longitude of the first point.
- `lat2` (float): Latitude of the second point.
- `lon2` (float): Longitude of the second point.

#### Response:
- **Status Code:** 200 OK
- **Body:** JSON object containing the following fields:
  - `distance_meters` (float): Distance in meters.
  - `distance_kilometres` (float): Distance in kilometers.
  - `distance_miles` (float): Distance in miles.

#### Error Response:
- **Status Code:** 400 Bad Request
- **Body:** JSON object with the following field:
  - `error` (string): Error message indicating invalid parameters.

