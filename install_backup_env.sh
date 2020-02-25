#! /bin/bash

python -m pip install venv
python3 -m venv ./venv

chmod +x ./venv/bin/activate
source ./venv/bin/activate

pip3 install -r requirements.txt

deactivate