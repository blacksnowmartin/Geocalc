import geopandas as gpd

# Load the KML file
kml_file = "path/to/your/exported.kml"
gdf = gpd.read_file(kml_file)

# Calculate the area
area_sq_meters = gdf.geometry.area.sum()
area_sq_km = area_sq_meters / 1e6  # Convert square meters to square kilometers

print(f"Approximate Area: {area_sq_km:.2f} square kilometers")

# BEFORE YOU START THE PROGRAM ENSURE YOU RUN THIS CODE AT BASH pip install geopandas
