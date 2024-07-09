import pandas as pd
import xarray as xr

excel = r"PATH TO EXCEL FILE"
sheet_dict = pd.read_excel(excel, sheet_name=None, header=0, names=["time", "precip"])

# bounding box
lats = [1.26, 2.08]
lons = [103.34, 104.30]

for sheet_name, df in sheet_dict.items():
  pairs = [(x,y) for x in lats for y in lons]
  df["time"] = pd.to_datetime(df["time"], format="%Y-%m-%d %H:%M:%S") # adjust to your own datetime format
  copy = ext.copy()
  for pair in pairs:
      if pairs[0]==pair:
          df["lat"] = pair[0]
          df["lon"] = pair[1]
      else:
          df1 = copy.copy()
          df1["lat"] = pair[0]
          df1["lon"] = pair[1]
          df = pd.concat([df, df1])
  ext = ext.set_index(['time', 'lat', 'lon'])
  exr = ext.to_xarray()
	output = r"PATH TO OUTPUT/{sheet_name}.ncdf"
  ext_nc = exr.to_netcdf(output)
