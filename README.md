# vk-friends
Simple app for vk authorisation and showing friends.

Usage:

python -m venv env

env\Scripts\activate.bat

pip install -r requirements.txt

python vk-friends\manage.py migrate
python vk-friends\manage.py runserver
