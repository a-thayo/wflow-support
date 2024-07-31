## this is a fairly niche problem but basically i cannot generate an output with "subcatchment" as the reducer
## thats why i made this script to extract the land runoff into river output

import geopandas as gpd
import rioxarray
from pathlib import Path

gdf = gpd.read_file(Path.cwd() / "PATH TO SUBCATCHMENT MAP").set_crs("EPSG:4326")
xds = rioxarray.open_rasterio(Path.cwd() / "PATH TO NCDF RESULTS MAP)["YOUR VARIABLE"].rio.write_crs("EPSG:4326")
basins = [x for x in gdf["value"]] # get subbasin number
to_river = []
for b in basins:
    subbasin = gdf[gdf["value"]==b]
    xds_sb = xds.rio.clip(subbasin.geometry.values, subbasin.crs)
    sum_to_river = xds_sb.sum(dim="y").sum(dim="x").values
    to_river.append(sum_to_river)
d = dict(zip(basins, to_river))
df = pd.DataFrame.from_dict(d, orient="columns")
df.to_csv("YOUR FILE NAME")
