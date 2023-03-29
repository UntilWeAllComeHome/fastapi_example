from fastapi import FastAPI
import geopandas as gpd

app = FastAPI()

@app.get('/ping')
async def ping_pong():
    return 'pong'

@app.get('/calculate_center/{filepath:path}')
async def calculate_center(filepath):
    """Calculates the center of a passed geosjon file."""

    try:
        gdf = gpd.read_file(('/' + filepath))
        center = gdf.dissolve().centroid
        return(str(center.to_json()))
    except:
        return("Error: File not found or file is not a spatial file.")

@app.get('/calculate_bounds/{filepath:path}')
async def calculate_bounds(filepath):
    """Calculates the total bounds of a passed geosjon file."""

    try:
        gdf = gpd.read_file(('/' + filepath))
        t_bounds = gdf.total_bounds
        return(str(t_bounds))
    except:
        return("Error: File not found or file is not a spatial file.")

@app.get('/calculate_boundry/{filepath:path}')
async def calculate_boundry(filepath):
    """Calculates the total bounds of a passed geosjon file."""

    try:
        gdf = gpd.read_file(('/' + filepath))
        bound = gdf.boundary
        return(str(bound.to_json()))
    except:
        return("Error: File not found or file is not a spatial file.")

@app.get('/calculate_area/{filepath:path}')
async def calculate_area(filepath):
    """Calculates the total bounds of a passed geosjon file."""
    
    try:
        gdf = gpd.read_file(('/' + filepath))
        area = gdf.area
        return(str(area))
    except:
        return("Error: File not found or file is not a spatial file.")