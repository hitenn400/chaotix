# Django Celery Stability AI Image Generator

This Django application integrates with the Stability AI API to generate images based on predefined or dynamically provided text using Celery for asynchronous task management.

## Setup

#Clone the GitHub Repository:
git clone https://github.com/hitenn400/chaotix

#Create .env File:

#Create a .env file in the project directory and add the necessary credentials.

#Navigate to Project Directory:
cd chaotix

#Create Conda Environment:
conda create --name chaotix python=3.8

#Activate Conda Environment:
conda activate chaotix

#Install Dependencies:
pip install -r requirements.txt

#Install Pillow Independently:
pip install pillow==10.3.0

#Make Migrations:
python manage.py makemigrations

#Migrate Database:
python manage.py migrate

#Run Redis Server (in a new terminal):
redis-server

#Run Celery Worker (in a new terminal):
celery -A chaotix worker --loglevel=info

#Run Server:
python manage.py runserver
