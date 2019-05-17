# Video Trend Data

Identifying good opportunities for property investors based on a user-defined filter.

## Datasets

Please place all the datasets in the `open_datasets` folder.

### [Housing Sales](https://www.gov.uk/government/collections/price-paid-data)

This single file contains information regarding property sales in the U.K. dating from 1st January 1995; it is updated on a monthly basis. 

### [University Locations](https://get-information-schools.service.gov.uk/Establishments/Search?tok=8TMj138l)

A file containing information on the geographical information of universities around the U.K.

### [University Admissions](https://www.hesa.ac.uk/data-and-analysis/students/where-study)

University enrolment and graduation statistics for admission data.

### [University Logos and Coordinates](https://equipment.data.ac.uk/)

Logo URL's for university's and their (latitude, longitude) coordinates.

## Quick Start

You can either visit [univestment.co.uk](http://univestment.co.uk/) or attempt to deploy this locally. Keep in mind, deplying this project locally is not an easy undertaking given the number of requirements. Furthermore, price data is a large file which is unable to be stored on git, this must be stored locally under `/open_datasets.nosync/price_paid_data`. We highly recommend you visit our site for the easiest and best experience. Although uptime is over 99%, this server is privately hosted so may be down at times due to internet outages, please contact Jack Tarbox (jt7g15@soton.ac.uk) if you are experiencing any difficulties.

### Installation on local machine

You will need [Python3.7](https://www.python.org/downloads/release/python-370/), [NodeJS](https://nodejs.org/en/), [npm install](https://www.npmjs.com/), and [PostgreSQL](https://www.postgresql.org/).

More thorough and specific installation instructions are given below the Quick-Start guide.

#### Database

* Ensure postgres is running on port 5432 on localhost.
* Create a postgres user using command `\createuser`. The user should be called postgres with the password the same as seen in `back_end/src/__init__.py` under the `POSTGRES_PASSWORD` constant.
* Create a database called `housing_data`.

#### Backend

* Navigate to the top level directory and type `pip install -r back_end/requirements.txt` in order to install Python libraries.
* (Ensure you have database setup first) Create relevant tables using `python back_end/src/database/database_main.py`.
* Run python Flask (API service) using `python back_end/src/app.py`.

#### Frontend 

* Navigate to the `front_end/` directory.
* Run command `npm ci`.
* Run command `npm start`.

## Development

Connect to the deployment server using SSH: `ssh -p 9922 odi13@jacktarbox.co.uk`.

### Server

The application is currently running on our company's own server. This is due to the small nature of our application for the time being until our userbase becomes larger. The following are some commands to interact with the server.

`sudo supervisorctl restart odi_flask`: Restarts the flask server.

`sudo supervisorctl status`: Views the status of the services running.

`cat /var/log/odi_server/odi-flask.err.log`: View error log for flask.

`cat /var/log/odi_server/odi-flask.out.log`: View out log for flask.

### Back-end

The back-end is written primarily in Python.

#### Python Virtual Environment

It is recommended to create a virtual environment in the `back_end` directory. You can do this by using virtualenv, a Python package.

**Creating a virtualenv**: `virtualenv venv`. You may need to add on the parameter `-p python3` if you have multiple Python versions on your machine.

**Activating the virtualenv**: `source venv/bin/activate` (Linux)

**Installing the requirements**: `pip install -r requirements.txt`

**Deactivating the virtualenv**: `source deactivate`

#### API Keys

For full usage, API keys are necessary. The following commands **must** be run from the main working directory:

* `export GOOGLE_APPLICATION_CREDENTIALS="api/google_key.json"` 

#### PYTHONPATH

For Flask to run correctly, PYTHONPATH must be set. This should be set in the top-level folder (this one). 

Please use command `export PYTHONPATH='.'` in the top-level directory if you are receiving any import errors.

### Front-end

See `./front-end/README.md` for information on running the front end.

### Database

We are using PostgreSQL for the database. Postgres runs on a server in which you can interact with. Use [this tutorial](https://www.codementor.io/engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb) to configure.

Postgres can be interacted with using the following command `pg_ctl -D /usr/local/var/postgres`. Ensure that you append one of the following to perform the function that you require:

* `start`: Starts the server
* `stop`: Stops the server
* `status`: Status of the server

E.g. to start the server you would run the command `pg_ctl -D /usr/local/var/postgres start`

`psql postgres` to allow for administrator commands + command line interface.

#### On the Server

Run `sudo su - postgres` to access the user for postgres.

Command `psql` to login to postgres server.

`\connect housing_data` to connect to housing_data database.

`\dt` to view all relations (tables).

`\d+ table_name` to view schema of table_name.

`SELECT * FROM table_name;` view contents of table_name.

`DROP TABLE table_name;` remove table_name.

### Installation

You must install [Node.js](https://nodejs.org/en/download/) for use on the local machine.

### Usage

Please see README.md in `front_end` for information on front-end usage.

We are using the Adzuna API in order to access current property listings. An example of the Adzuna API is as follows: `https://api.adzuna.com/v1/api/property/gb/search/1/?app_id=INSERT_APP_ID&app_key=INSERT_APP_KEY&category=for-sale&results_per_page=10&where=SO173RZ`
