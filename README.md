# unemployment-inclass-2022


## Setup
Create and activate a virtual environment

'''sh
conda create -n unemployment-env python=3.8
'''

Install the necessary packages

'''sh
pip install -r requirements.txt
'''


##Configuration

Obtain an API Key from ALPHAVANTAGE.

Then create a local ".env" file and provide the key like this:
'''sh
ALPHAVANTAGE_API_KEY = "abc123"
'''

Then create a .gitignore file of the python flavor to help hide the .env file

## Usage



Run the unemplyment report:

'''sh
python app/unemployment.py
'''


