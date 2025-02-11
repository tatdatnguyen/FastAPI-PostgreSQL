# FastAPI-PostgreSQL
## Installation
**In terminal**

``
pip install fastapi[all] sqlalchemy databases psycopg2
``

**Install the database**

``
sudo apt update

sudo apt install postgresql postgresql-contrib
``

## Run the code
**Start the database**

``
sudo systemctl start postgresql
``

**Run the server**

``
uvicorn main:app --reload
``
