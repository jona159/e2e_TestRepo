import xarray as xr

fin = xr.open_dataset('SST_datacube.nc')
print(fin)
