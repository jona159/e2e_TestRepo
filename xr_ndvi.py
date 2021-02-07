import requests
import json
import time
import sys
import re
import urllib.request
import os
import xarray as xr
import netCDF4
import scipy.io.netcdf
import pytest
from netCDF4 import Dataset
import h5py

   
fin_ndvi = xr.open_dataset('Sentinel_datacube.nc')
print(fin_ndvi)   
   
#print(fin_ndvi['__xarray_dataarray_variable__'][:])

print(" \n END OF NDVI NETCDF FILE \n")

# Test to assert that the xarray Dataset contains the correct number of values
def test_length_fin_ndvi():
  assert fin_ndvi.count() == 2303604   
   
