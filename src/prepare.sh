#!/bin/bash

if [ ! -d "venv" ]; then
    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
else
    source venv/bin/activate
fi

if [ ! -f "requirements.txt" ]; then
    touch requirements.txt
    pip install tk
    pip install sympy
    pip freeze > requirements.txt
else
    pip install -r requirements.txt
fi

pip install --upgrade pip