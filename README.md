# qgz_repointer
 
This is a simple python command line tool for repointing the database connections within a [QGIS](https://qgis.org/en/site/) project.

An example usage would be `python .\qgz_repointer.py --port 1234 --hostname localhost --username 'grclague' --dbname 'mydatabase' --password 'supersecret' 'MyOriginalMap.qgz' 'MyRepointedMap.qgz'` which will repoint all the database connections in MyOriginalMap.qgz and create a new project MyRepointedMap.qgz.
