#!/bin/bash
python manage.py migrate
python manage.py flush --no-inputbox
