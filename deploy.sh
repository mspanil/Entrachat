#!/bin/bash

# Install virtualenv
python3 -m pip install --user virtualenv

# Create a virtual environment
python3 -m virtualenv myenv

# Activate the virtual environment
source myenv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install Waitress
pip install waitress

# Run the application
waitress-serve --listen=0.0.0.0:8000 app:app