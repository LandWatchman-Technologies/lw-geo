import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import math
import os


def generate_linemap(points_list):
    for point in points_list:
        point["lat"] = float(point["lat"])
        point["lon"] = float(point["lon"])
    lats = [point["lat"] for point in points_list]
    lons = [point["lon"] for point in points_list]
    lat_min, lat_max = min(lats), max(lats)
    lon_min, lon_max = min(lons), max(lons)

    # Calculate center
    center_lat = (lat_min + lat_max) / 2
    center_lon = (lon_min + lon_max) / 2

    # Calculate zoom level
    lat_dist = lat_max - lat_min
    lon_dist = lon_max - lon_min
    zoom_lat = math.log(360 / lat_dist) / math.log(2)
    zoom_lon = math.log(360 / lon_dist) / math.log(2)
    px.set_mapbox_access_token(os.environ.get("MAPBOX_TOKEN"))
    zoom = math.floor(min(zoom_lat, zoom_lon))
    fig = px.line_mapbox(
        points_list,
        lat="lat",
        lon="lon",
        hover_data={"lat": False, "lon": False, "time": True, "location_name": True},
        color_discrete_sequence=['blue'],
        zoom=zoom,
        center={"lat": center_lat, "lon": center_lon},
    )
    
    fig.update_layout(mapbox=dict(accesstoken=os.environ.get("MAPBOX_TOKEN")))
    fig.update_layout(mapbox_style="streets")
    # Update line traces
    fig.update_traces(line=dict(color='blue', width=5))

    # Add markers for start and end points
    fig.add_trace(go.Scattermapbox(
        lat=[points_list[0]["lat"], points_list[-1]["lat"]],
        lon=[points_list[0]["lon"], points_list[-1]["lon"]],
        mode='markers+text',
        marker=dict(color='red', size=20),
        text=['S', 'E'],
        textposition="middle center",
        hoverinfo='text',
        textfont = dict(color='white', size=18),
        hovertext=[f"<b>{points_list[0]['location_name']}</b><br>Time: {points_list[0]['time']}", f"<b>{points_list[-1]['location_name']}</b><br>Time: {points_list[-1]['time']}"],
        
    ))
    fig.update_layout(coloraxis_showscale=False, mapbox_accesstoken=os.environ.get("MAPBOX_TOKEN"))
    fig.layout.showlegend=False
    fig.update_layout(margin={"r":2,"t":2,"l":2,"b":2})
    fig.update_layout(paper_bgcolor="black")
    html_fig = fig.to_html(config={'displaylogo': False, 'modeBarButtonsToRemove': ['select', 'lasso2d', 'pan']},include_plotlyjs='cdn', full_html=False, div_id='map_location', default_width='85%', default_height='85%')
    return html_fig