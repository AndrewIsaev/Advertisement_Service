# Advertisement_Service
Back-end for Advertisement application
***
## Features
- Authorization/Authentication users
- Distribution of roles between users
- CRUD for advertisement
- Search advertisement
- Comments for advertisement
***
## Technology stack
- Python 3.10.6
- Django 3.2.6
- Django REST Framework 3.13.1
- PostgreSQL
- Docker
- Docker-compose
- Djoser 2.1.0
- mypy
- Pillow 9.0.0
***
## Start app
1. Clone project
   ```
   git clone https://github.com/AndrewIsaev/Advertisement_Service.git
2. Run app
   ```
    ./manage.py runserver
***
## Project structure
- `frontend_react/`: frontend
- `market_postgres/`: database
- `skymarket/`: advertisement API
    - `ads/`: advertisement application
    - `fixtures/`: data to upload in database
    - `goals/`: goals application   
    - `users/`: authorization/authentication users
    - `skymarket/`: Django settings
    - `manage.py`: Django app management
