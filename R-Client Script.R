#@author Judith Becka, https://github.com/a2beckj
#@author Jonas Raabe, https://github.com/jona159

# clean up environment

rm(list=ls())

# Install dependencies 
install.packages("devtools")
library(devtools)
install.packages("tibble")
library(tibble)

#Set up R-Client
devtools::install_github(repo="Open-EO/openeo-r-client",dependencies=TRUE, force=TRUE)
library(openeo)
host_url="http://127.0.0.1"
api_versions(host_url)
con=connect(host=host_url, version="1.0.0")
collections=list_collections()
print(collections)
processes=list_processes()
print(processes)
#print(names(processes))
#print(names(collections))
#ndvi=describe_process("ndvi")
#print(ndvi)
#sst=describe_process("mean_sst")
#print(sst)
#res=describe_process("save_result")
#print(res)
#lc=describe_process("load_collection")
#print(lc)

##INSTALL PACKAGES FOR TESTING##
install.packages("rlang")
library(rlang)
install.packages("testthat")
library(testthat)

###TEST SUITE###
test_that("check description of save_result", {expect_equal(processes$save_result$returns$description, "Returns a boolean which indicates if the save was successfull")})

test_that("check ndvi category", {expect_equal(print(processes$ndvi$categories[[2]][1]), "vegetation indices")})

test_that("check keywords Sentinel2 collection", {expect_length(collections$`Sentinel2-Geosoft2`$keywords, 5)})

test_that("check temporal extent SST", {expect_equal(collections$`SST-Geosoft2`$extent$temporal[[1]][[1]],"1981-09-01T00:00:00Z" )})

test_that("check temporal extent SST", {expect_equal(collections$`SST-Geosoft2`$extent$temporal[[1]][[2]],"2020-12-31T23:59:59Z" )})

test_that("check for correct number of collections", {expect_length(collections, 2)})

test_that("check spatial and temporal extent Sentinel", {expect_equal(collections$`Sentinel2-Geosoft2`$extent$spatial, c(7.531529, 51.363158 , 9.143291, 52.350386))})

test_that("check spatial and temporal extent Sentinel", {expect_equal(collections$`Sentinel2-Geosoft2`$extent$temporal[[1]][[1]], "2020-01-01T00:00:00Z")})

test_that("check spatial and temporal extent Sentinel", {expect_equal(collections$`Sentinel2-Geosoft2`$extent$temporal[[1]][[2]], "2020-12-31T23:59:59Z")})

test_that("check for collections that does not exist", {expect_null(collections$unknown)})

test_that("check for Sentinel invalid spatial extent", {expect_failure(expect_equal(collections$`Sentinel2-Geosoft2`$extent$spatial, c(1,4000, 3, 17)))})

test_that("check for Sentinel invalid temporal extent", {expect_failure(expect_equal(collections$`Sentinel2-Geosoft2`$extent$temporal[[1]][[1]], "1950-01-01T00:00:00Z" ))})

test_that("check for Sentinel invalid temporal extent", {expect_failure(expect_equal(collections$`Sentinel2-Geosoft2`$extent$temporal[[1]][[2]], "2022-01-01T00:00:00Z" ))})

test_that("check for collections to be named", {expect_named(collections)})

test_that("check for processes to be named", {expect_named(processes)})

test_that("check correct dimensions of SST cube", {expect_equal(collections$`SST-Geosoft2`$cube, "dimensions:{x:1424,y:720,z:1,t:'40years',bands:1}")})

test_that("check for version not to be double", {expect_failure(expect_equal(collections$`SST-Geosoft2`$version, 1.0))})

test_that("check that number of processes is higher than 3", {expect_gt(length(processes), 3)})

test_that("check that number of processes is lower than 5", {expect_lt(length(processes), 5)})

test_that("check if description for SST is provided", {expect_output(print(collections$`SST-Geosoft2`$description))})

test_that("check if description for Sentinel is provided", {expect_output(print(collections$`Sentinel2-Geosoft2`$description))})

test_that("check if description for ndvi is provided", {expect_output(print(processes$ndvi$description))})

test_that("check if description for ndvi is provided", {expect_output(print(processes$mean_sst$description))})

test_that("check if description for ndvi is provided", {expect_output(print(processes$save_result$description))})

test_that("check if description for ndvi is provided", {expect_output(print(processes$load_collection$description))})

test_that("check for the stac version to be of type character", {expect_type(collections$`SST-Geosoft2`$stac_version, "character")})

test_that("check for invalid process description", {expect_null(describe_process("unknown"))})

test_that("check for output of describe_process function", {expect_output(print(describe_process("ndvi")))})

