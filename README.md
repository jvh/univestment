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

### Front-end

### Installation

You must install [Node.js](https://nodejs.org/en/download/) for use on the local machine.

### Usage

Please see README.md in `front_end` for information on front-end usage.

## Extensions

Using news sources to further aid estimation of future trends
