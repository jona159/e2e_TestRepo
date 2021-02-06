import xarray as xr
import netCDF4
import scipy.io.netcdf
import pytest

fin = xr.open_dataset('SST_datacube.nc')
print(fin)

def test_length_fin():
   assert fin.count() == 1036800
