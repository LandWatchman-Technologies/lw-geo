import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def generate_linemap(points_list):
    for point in points_list:
        point["lat"] = float(point["lat"])
        point["lon"] = float(point["lon"])
    df = pd.DataFrame(points_list, columns=['lon', 'lat', 'time'])
    fig = px.line_mapbox(
        points_list,
        lat="lat",
        lon="lon",
        hover_data={"lat": True, "lon": True, "time": True},
        color_discrete_sequence=['blue'],
        zoom=12,
        center={"lat": sum(float(point["lat"]) for point in points_list) / len(points_list),
                "lon": sum(float(point["lon"]) for point in points_list) / len(points_list)}
    )
    
    fig.update_layout(mapbox_style="open-street-map")

    # Update line traces
    fig.update_traces(line=dict(color='blue', width=5))

    # Add markers for start and end points
    fig.add_trace(go.Scattermapbox(
        lat=[points_list[0]["lat"], points_list[-1]["lat"]],
        lon=[points_list[0]["lon"], points_list[-1]["lon"]],
        mode='markers',
        marker=dict(
            size=12,
            color='red',
        ),
        hoverinfo='text',
        text=[f"Start Point: Time: {points_list[0]['time']}", f"End Point: Time: {points_list[-1]['time']}"]
    ))
    fig.show()
    html_fig = fig.to_html(config={'displaylogo': False},include_plotlyjs='cdn', full_html=False)
    return html_fig