import xarray as xr

fin = xr.open_dataset('netCDF_sst.nc')
print(fin)
