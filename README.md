# Video Trend Data

Identifying trends in video (both Youtube and movies) in order to better facilitate choices made by amateur directors.

## Datasets

Please place all the datasets in the `open_datasets` folder.

### [Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset)

These files contain metadata for all 45,000 movies listed in the Full MovieLens Dataset. The dataset consists of movies released on or before July 2017. Data points include cast, crew, plot keywords, budget, revenue, posters, release dates, languages, production companies, countries, TMDB vote counts and vote averages.

This dataset also has files containing 26 million ratings from 270,000 users for all 45,000 movies. Ratings are on a scale of 1-5 and have been obtained from the official GroupLens website.

### [BoxOffice Alltime Domestic Data](https://www.kaggle.com/eliasdabbas/boxofficemojo-alltime-domestic-data)

Data scraped from BoxofficeMojo's listing of the lifetime gross, ranking and production year of hollywood movies. All is based on domestic gross (does NOT account for inflation).

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

### Installation

You must install [Node.js](https://nodejs.org/en/download/) for use on the local machine.

### Usage

Please see README.md in `front_end` for information on front-end usage.

## Extensions

Using news sources to further aid estimation of future trends
