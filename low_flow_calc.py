import geopandas as gpd

catch = gpd.read_file(r"PATH TO YOUR BASIN/SUBCATCH FILE")
catch = catch.to_crs(epsg=3414) # change to CRS with meter instead of degrees (in this case i used SVY21)
catch["area in km2"] = catch.area/1000000

catch["lowQ"] = 0.22*3.157*10**(-11)*catch["area in km2"]**0.986*2681**2.562 # low flow equation for 30-day scenario, feel free to adjust
