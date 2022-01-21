# qgz_repointer
 
This is a simple python command line tool for repointing the database connections within a [QGIS](https://qgis.org/en/site/) project.

An example usage would be `python .\qgz_repointer.py --port 1234 --hostname localhost --username 'grclague' --dbname 'mydatabase' --password 'supersecret' 'MyOriginalMap.qgz' 'MyRepointedMap.qgz'` which will repoint all the database connections in MyOriginalMap.qgz and create a new project MyRepointedMap.qgz.

There is also a folder flag (-f) that will repoint all of the .qgz files within a given folder. Now the input and output arguments are the directory to look in, and the directory to output to.

Eventually I plan to expand this a bit so that you can specify which connection you would like to remap. Also, to allow the remapping of directories for shapefiles and geopackages contained within your .qgz file.
