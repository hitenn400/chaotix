# Django Celery Stability AI Image Generator

This Django application integrates with the Stability AI API to generate images based on predefined or dynamically provided text using Celery for asynchronous task management.

## Setup

1. **Clone the repository:**
git clone https://github.com/hitenn400/chaotix.git

2. **Install dependencies:**
create virtual env and install all dependicies

3. **Configure Django:**

- Set up your Django settings, including database configuration, API authentication details, and any other necessary settings. Ensure you have your Stability AI API credentials configured properly.

4. **Configure Celery:**
- run redis :
- redis-server
- run celery command :
- celery -A chaotix worker --loglevel=info

5. **Run migrations:**
6. 
7. command : python3 manage.py migrate
8. run server
9. python3 manage.py runserver
