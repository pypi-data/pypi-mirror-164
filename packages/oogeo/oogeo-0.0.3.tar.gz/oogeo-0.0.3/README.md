# Models API Examples

This repository contains several Jupyter Notebooks that demonstrate the `Models` API which I wrote for [Envelope](https://www.envelope.city/). The API contains many powerful functions for processing GIS data and is built entirely on open-source libraries.

## About the Models API

The Models API is a library for processing GIS data, and was originally designed to mimic functions found in Esri's "Geoprocessing" toolbox (a part of their ModelBuilder product). At the API's inception, [Envelope](https://www.envelope.city/) was using Esri-based products to perform geoprocessing, but the company had a long-term goal of transitioning to open-source products that were less expensive and more in line with the company's other technology stacks. The Models API was designed to ease the transition to open-source libraries by creating a conceptual layer between the GIS processing logic and the underlying GIS function calls. 

The Models API was originally based on Esri's ArcPy library, but once the API had been used to segregate the application's business logic from the GIS processing functions the application could then be transitioned from ArcPy to open-source libraries with a minimum amount of effort. The Models API is now based entirely on open-source libraries, primarily:

* PostgreSQL and PostGIS
* Python
    * `psycopg2`
    * `sqlAlchemy` and `geoAlchemy`
    * `pandas` and `geopandas`
    * `shapely`
    * `matplotlib`

## About the Examples

This repository contains several examples of how the Models API can be used to process geographic data. The work performed in each example is described below:

### The Basics

#### [Geometry Manipulation Example](https://github.com/bmlott27/oogeo/blob/main/notebooks/Geometry%20Manipulation%20Examples.ipynb)

The Geometry Manipulation Example demonstrates the basics of creating and manipulating geometries using the Models API, as well as some simple examples of comparing geometries spatially. This example only contains a small sample of the wide variety of functions available in the Models API for creating, comparing, and manipulating geometries. 

The API's geometry objects (`Point()`, `Line()`, and `Polygon()`) are based primarily on `shapely` geometry objects, with additional support from `matplotlib` for plotting geometries in Jupyter Notebooks.

#### [Geodatabase Manipulation Example](https://github.com/bmlott27/oogeo/blob/main/notebooks/Geodatabase%20Manipulation%20Examples.ipynb)

The Geodatabase Manipulation Example demonstrates how to use the Models API to connect to and manipulate PostGIS geodatabases. The example includes how to create geodatabases, tables, rows, and columns, as well as a few advanced geoprocessing functions such as identity overlays and dissolve functions. This example contains only a small sample of the many methods available in the Models API to query, manipulate, and compare geographic data between PostGIS datasets.

The API's geodatabase objects (`Workspace()`, `Table()`, and `Layer()`) are designed to work with PostGIS databases and are based primarily on the `psycopg2` and `geoAlchemy` libraries, with some support from `geopandas`. Internally the API uses PostGIS `ST_Geometry` functions to create spatial queries for comparing datasets and manipulating data.

#### [Data Migration Example](https://github.com/bmlott27/oogeo/blob/main/notebooks/Data%20Migration%20Example.ipynb)

The Data Migration Example demonstrates how the Models API can be used to perform common migration and transformation tasks on spatial datasets. The example shows how an existing dataset can be filtered (both spatially and by attribute) and reprojected to a new coordinate system. The example also shows how columns can be added, renamed, or dropped using the API.

### Case Studies

#### [Bus Stop Distance Example](https://github.com/bmlott27/oogeo/blob/main/notebooks/Bus%20Stop%20Example.ipynb)

The Bus Stop Distance Example shows how the Models API can be used to find the distance between geometries in two different datasets. The example modifies a parcels dataset by adding columns to the table and populating the columns with the name of and distance to the nearest bus stop. The bus stop data is stored in a separate dataset and PostGIS functions are used to help compare the data between the tables.

#### [CitiBike JSON Import Example](https://github.com/bmlott27/oogeo/blob/main/notebooks/CitiBike%20JSON%20Import%20Example.ipynb)

The CitiBike JSON Import Example demonstrates how the Models API can be used to import JSON into a PostGIS geodatabase. The example creates a new geodatabase to house the imported data, creates a table based on the data found in the JSON file, and loads the table with the JSON data. The data is also projected to a new coordinate system to be consistent with other datasets in our process.

#### [Street Label Points Example](https://github.com/bmlott27/oogeo/blob/main/notebooks/Street%20Label%20Points%20Example.ipynb)

The Street Label Points Example demonstrates how the Models API was used to find the best locations for street labels based on their proximity to city blocks. The example finds the location points for each label and also determines the ideal rotation angle for the text (this was done to help support displaying the labels in reports and other projects).

#### [Subway Stations Example](https://github.com/bmlott27/oogeo/blob/main/notebooks/Subway%20Stations%20Example.ipynb)

The Subway Stations Example demonstrates how the Models API can be used to extract data from one dataset and apply it to another based on spatial attributes. The example uses a points dataset containing subway names to associate subway names with polygons in a subway stations polygon dataset. The spatial relationships between the points and polygons are used to determine the names for the station polygons.
