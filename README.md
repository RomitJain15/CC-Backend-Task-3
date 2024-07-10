# CC-Backend-Task-3
 
## Creating a files API for hosting and storing files on PostgreSQL Docker.

The task required hosting a PostgreSQL database using the official PostgreSQL Docker image and creating an API for adding, deleting and retrieving files, along with their contents. 

The steps I took for the task are the following:-
* Started a postgres instance by running the command on the Docker Hub and added port 5432 to host it.
* Created a PGAdmin container and linked to my database to keep track of the data.
* Used 'psycopg2' python module to connect to the database and create a cursor to interact with the database.
* Created 'init.sql' and defined my database schema in that. Then copied and executed it in the Docker container.
* Used 'FastAPI' to create a server for API calls.
* Used POST, DELETE, and GET requests for adding, deleting and retrieving files.
* Used 'UploadFile', a module provided by FastAPI, to recieve a file input and used its read(), filename, and content_type methods to extract the required data from the file.
* Tested the functionality of the APIs using 'curl' command in the command prompt