# crud-operation-using-glask


Installation
For this article first you need to install flask, and after that you need to install flask_mysqldb.


1
pip install Flask
pip install Flask-MySQL

OK after the installation first you need to create a database, i have used https://www.freemysqlhosting.net/ 
You will receive a username and password for the database server and login to that server and import the csv file.

create a REST API that allows the user to do basic CRUD operations on the data. You will have to use the python library of the database to perform these operations on the objects.
You can find the solution in app.py the connection and code for the same


# Package with Docker

  The next stage is where we will create a Docker image.For that first we need to download Docker Destop https://docs.docker.com/docker-for-windows/install/ and login using the registered user id and password once that is done and Docker Destop is running we need to create 2 files one is a Dockerfile and the other is requirement.txt file.
  Requirement.txt file will contain all the libraries that are needed and Dockerfile will contain the build instruction for the creation of the image.
  
  
  After creating these two files we need to execute these 2 following commands
  
 1) docker build -t friendlyhello .
 2) docker run -p 4000:80 friendlyhello
 
 After executing these two commands our api will start running in port 80 and you can  Confirm that the app works on your local machine by running the image and navigating to localhost:4000 in your browser.
