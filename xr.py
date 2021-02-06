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

fin = xr.open_dataset('SST_datacube.nc')
print(fin)

sst_values = fin['sst'][0]
print(sst_values)


def test_length_fin():
   assert fin.count() == 1036800
