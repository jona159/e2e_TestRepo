#@author Judith Becka, https://github.com/a2beckj
#@author Jonas Raabe, https://github.com/jona159

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

# open xarray dataset
fin_sst = xr.open_dataset('SST_datacube.nc')
print(fin_sst)


sst_values = fin_sst['sst'][0]
print(sst_values)

# Test correct amount of values in xarray dataset
def test_length_fin_sst():
   assert fin_sst.count() == 1036800
