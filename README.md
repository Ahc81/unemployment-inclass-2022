# unemployment-inclass-2022


## Setup
Create and activate a virtual environment

```sh
conda create -n unemployment-env python=3.8
```

Activate environment 
```sh
conda activate unemployment-env
```

Install the necessary packages

```sh
pip install -r requirements.txt
```


##Configuration

Obtain an API Key from ALPHAVANTAGE.

Then create a local ".env" file and provide the key like this:
```sh
ALPHAVANTAGE_API_KEY = "..."
```

Then create a .gitignore file of the python flavor to help hide the .env file

## Usage



Run the unemplyment report:

```sh
python -m app.unemployment
```


Run stocks report:

```sh
python -m app.stocks
```

#testing
Run tests:

``` sh
pytest
```

### Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```