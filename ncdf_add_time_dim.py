import xarray as xr
import pathlib

nc_folder = r"PATH TO FOLDER CONTAINING ALL NETCDF FILES"
def add_time(ds):
    ds = ds.expand_dims({"time": [datetime.datetime.strptime(ds.attrs["EndDate"]+"T"+ds.attrs["EndTime"], "%Y-%m-%dT%H:%M:%S.%fZ")]})
    return ds
trmm_concat = xr.open_mfdataset(nc_folder.glob("*.nc4"), preprocess=add_time)
trmm_concat.to_netcdf(f"{filename}.nc4")
