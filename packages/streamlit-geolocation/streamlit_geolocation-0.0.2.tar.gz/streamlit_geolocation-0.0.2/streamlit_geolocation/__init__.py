import streamlit.components.v1 as components
import os

absolute_path = os.path.dirname(os.path.abspath(__file__))
frontend_path = absolute_path

streamlit_geolocation = components.declare_component(
    "streamlit_geolocation", path=frontend_path
)

def geolocate():
    return streamlit_geolocation()

