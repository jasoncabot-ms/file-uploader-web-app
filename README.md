# Data Collector - Web App Version

A Python Flask Web App that demonstrates how to receive data and upload to a storage account on the server side

## Get Started

You can deploy straight to your Azure subscription

[![Deploy to Azure](https://azuredeploy.net/deploybutton.png)](https://azuredeploy.net/)

Alternatively you can **fork** this repository on GitHub and deploy from there instead.

## Run Locally

To build and run this locally, you can execute the following, assuming you have python installed

```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
DATACOLLECTOR_SETTINGS_PATH=./config/development.cfg FLASK_APP=datacollector flask run
```

# Customisation

You can change the data fields and how they are uploaded from `./datacollector/forms.py` and `./datacollector/templates/upload.html`

Processing of the uploaded form takes place in the `upload` method of `./datacollector/frontend.py`

# Appendix

You don't have to run the following, it's how the project was initially created

```
python3 -m venv venv
. venv/bin/activate
pip install flask
pip install flask_wtf
pip install email-validator
pip freeze > requirements.txt

# Generate a secret key
python -c 'import os; print(os.urandom(24))' > datacollector/config/development.cfg
````
    
