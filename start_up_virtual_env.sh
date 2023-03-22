#!/bin/bash
: '
You can enter any comments here
'
python3 -m venv <venv_name>
source <venv_name>/bin/activate 
pip install --upgrade pip --proxy <proxy>
pip install --upgrade pip setuptools wheel --proxy <proxy>
pip install -r requirements.txt  --proxy <proxy>
