# Video Trend Data

Identifying good opportunities for property investors based on a user-defined filter.

## Datasets

Please place all the datasets in the `open_datasets` folder.

### [Housing Sales](https://www.gov.uk/government/collections/price-paid-data)

This single file contains information regarding property sales in the U.K. dating from 1st January 1995; it is updated on a monthly basis. 

### [University Locations](https://get-information-schools.service.gov.uk/Establishments/Search?tok=8TMj138l)

A file containing information on the geographical information of universities around the U.K.

### [University Admissions](https://www.ucas.com/data-and-analysis/undergraduate-statistics-and-reports/ucas-undergraduate-end-cycle-data-resources/applicants-and-acceptances-universities-and-colleges-2018)

Admission data for U.K. universities.

## Development

### Back-end

It is recommended to create a virtual environment in the `back_end` directory. You can do this by using virtualenv, a Python package.

**Creating a virtualenv**: `virtualenv venv`. You may need to add on the parameter `-p python3` if you have multiple Python versions on your machine.

**Activating the virtualenv**: `source venv/bin/activate` (Linux)

**Installing the requirements**: `pip install -r requirements.txt`

**Deactivating the virtualenv**: `source deactivate`

### PYTHONPATH

For Flask to run correctly, PYTHONPATH must be set. This should be set in the top-level folder (this one). 

Please use command `export PYTHONPATH='.'` in the top-level directory if you are receiving any import errors.

### Front-end

See `./front-end/README.md` for information on running the front end.

### Database

We are using PostgreSQL for the database. Postgres runs on a server in which you can interact with.

Postgres can be interacted with using the following command `pg_ctl -D /usr/local/var/postgres`. Ensure that you append one of the following to perform the function that you require:

* `start`: Starts the server
* `stop`: Stops the server
* `status`: Status of the server

E.g. to start the server you would run the command `pg_ctl -D /usr/local/var/postgres start`

`psql postgres` to allow for administrator commands + command line interface.

### Installation

You must install [Node.js](https://nodejs.org/en/download/) for use on the local machine.

### Usage

Please see README.md in `front_end` for information on front-end usage.

## Extensions

Using news sources to further aid estimation of future trends
