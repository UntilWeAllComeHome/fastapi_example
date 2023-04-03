# fastapi_example
Simple example of a FastAPI app. This app is focused on delivering key metadata about a geospatial file through an API call. This simple example currently requires geojson files to properly work, but could easily be adapted to work with any spatial file Geopandas is compatible with. The app could also be paired with a PostGIS container, have a POST request added that can insert spatial data, and execute spatial queries using SQL to return information about data in the database.

# Setup
Setup your environment using pyenv.

Install Python:

    pyenv install 3.11.1

Create a new pyenv environment:

    pyenv virtualenv 3.11.1 fastapi_example

Activate the new environment:

    pyenv activate fastapi_example

Install the required modules:

    pip install -r requirements.txt

Run the application

    uvicorn main:app --reload
