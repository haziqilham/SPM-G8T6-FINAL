# SPM-G8T6-FINAL
G8T6 source codes 

This repository contains source codes for G8T6 project. 


Folder Directory:

public --> Storage of HTML, JS files  [Frontend]

sql --> Storage of SQL scripts for database 

test --> test case codes with app.py inside

Deployment Guide:

For Local Deploymnent:

-Database:
    Ensure a MySQL databasee server is running. 
    1) Upload SQL script to local database 

- Backend:
    2) run "pip3 install -r requirements.txt" to download dependencies
    3) Run "flask run --host'0.0.0.0' --port=5000" or "python app.py" to execute flask app

-Frontend:
    Navigate to /public for index.html


For Online Deployment:
    (Online deployment is currently hosted by G8T6 SPM please contact one of the members for further enquiries)

-Database:
    - Ensure RDS is running on server (You can also create and upload the sql file to your own RDS)

-Backend:
    - Ensure flask app is running on EC2 instance (run a flask service on either EC2 instance or beanstalk)

Frontend:
    - Create and Connect to Amplifly link to access the service.  e.g. https://main.d2rxpx2m0x6r1l.amplifyapp.com/
