## Getting started
These instructions will get you a copy of the project up and running in your local machine for development and testing purposes.

## Prerequisites
- [Git](https://git-scm.com/download/)
- [Python 3.6 and above](https://www.python.org/downloads/)
- [Postgresql](https://www.postgresql.org/)
- [Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html)

## Installing

### Setting up and Activating a Virtual Environment
- Create a working space in your local machine and create your database
- Clone this [repository](https://github.com/nicksonlangat/fold_money_assignment.git) `git clone https://github.com/nicksonlangat/fold_money_assignment.git`
- Navigate to the project directory
- Create a virtual environment `python3 -m venv name_of_your_virtual_environment` and activate it `source name_of_your_virtual_environment/bin/activate`
- Create a .env file in root directory and put these key=values in it:
```
DEBUG=on
SECRET_KEY='u)$fi2g)y)*2nv%85t)=**4b_7v6pubtxfxs*h!-_2)ewjux7o'
DB_NAME="your_db_name"
DB_USER="your_db_user"
DB_PASSWORD="your_db_password"
DB_PORT="your_db_port"
DB_HOST="localhost"
```
- Install dependencies to your virtual environment `pip install -r requirements.txt`
- Migrate changes to the newly created database `python manage.py migrate`

## Elastisearch Setup
- New terminal tab Install and run Elasticsearch in the background `docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.14.0`
- Build and populate index `python manage.py search_index --rebuild`
- Ready to go :)

## Starting the server
- Ensure you are in the project directory on the same level with `manage.py` and the virtual environment is activated
- Run the server `python manage.py runserver`

## Create some data
- Create test user (http://localhost:8000/register), payload `{'email': '', 'name': '', 'password': ''}`.
- Create test hashtag (http://localhost:8000/hashtags), payload shown in the browsable API
- Create test project (http://localhost:8000/projects), payload shown in the browsable API
- Create as many projects, hashtags to test next

## PROJECT MODULES,
- The project configs and settings is in the folder `mysite`
- Users app is `accounts`
- Main app is `core`.
- Search app is `search`

## Search Endpoints
- Search for projects created by a particular user via (http://localhost:8000/search/project/user/<query>/)
- Search for projects that use specific hashtags via (http://localhost:8000/search/project/hashtag/<query>/)
- Full-text fuzzy search for projects via (http://localhost:8000/search/project/slug/<query>/)

## Running tests
- Tests can be run by using  `python manage.py test `
