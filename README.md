# Rocks-and-Stuff
This program uses flask, html and sql to create a database for geologists. It is possible to add a locality and country to begin with. It is also possible to add a rock type, including name, type and age. Together the user can figure out where rocks are found and which type they have. Further more the user can add samples, which have an id, rock type, etc. All attributes can be viewed in the ERD.<br />

The SQL and Python_SQL are used to instantiate the databse and can be deleted through them. It is up to user if they want to use the python console or SQL commands to do this.

The static folder contains a css file, which has not been implemented yet.
The templates folder contains the html files, which create the homepage and lets the user interact with the database. <br />

The program runs from the app.py file and uses sqlUtils to post and get information to/from the database.

## How to run the project
Install the requirements using the following:
pip install -r requirements.txt

To initialise the database using python, first make sure to change the values for psycopg, so it can connect to the database.
This includes using the correct port as well as the password for your database. 
- Python_SQL
- sqlUtils
- app

All of these files has this module, where it has to be changed for it to work correctly. 

When this is done, you can now initialise the database using the following commands in this order:
# Python
- python Tables.py
- python localities.py
- python rockTypes.py
- python localityRockTypes.py

# SQL
- psql < tables.sql
- psql < localities.sql
- psql < rock_types.sql
- psql < locality_rock_types.sql

Either way should work, and creates the database. Now to run the app, use the following:
- python app.py

Click the ip-link which will be created in the terminal, and the website is up and running. 
Explore the different options, such as adding rocks, searching for rocks and so forth.

To delete the tables from your database, use:
- python DropAllTables.py
