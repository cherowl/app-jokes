# Web-project template

This repository has base structure for the web projects and includes:
- Frontend (node react app)
- Backend (python flask app)
- Database (postgresql)
- Docker-compose configuration for deployment


## Requirements
In order to run the project, you should pre-install the following:

**Note:** using `apt-get` package manager and `bash` shell for example, 
adjust according to the system you are using

- python3 + pip3
```
apt-get install python3 python3-pip
```

- (optional) python virtual environment
```
pip3 install virtualenv
virtualenv -v python3 venv

# Activate: 
source venv/bin/activate
# Deactivate: 
deactivate 
```

- Node.js
```
Check on the official website: https://nodejs.org/en/download/package-manager/
```

- Postgresql
```
apt-get install postgresql postgresql-contrib
service postgresql start
```

- (optional) Docker + docker-compose
```
Check on the official website:
Docker: https://docs.docker.com/install
Docker-compose: https://docs.docker.com/compose/install/
```


## Frontend

This project was created with **create-react-app** build tool provided by Facebook. 
It also depends on **react-scripts** library which 
provides it with all functionality concerning *webpack*, *Babel* and so on.

**Notes:** 

- If at some point manual configuration will be required 
  it's possible to get these dependencies with **eject** script
- Facebook provides a pretty big README file (renamed to **FACEBOOK_TIPS**) 
  which is located in **frontend** folder. It provides a lot of useful information.
  
### Starting frontend

1. Navigate to `frontend` folder
1. Install dependencies
1. Run project
1. Navigate to http://localhost:3000/ in the browser

```
cd frontend
npm install
npm run start
```


## Backend
**Note:** Configuration files are located in `backend/config`
There are 3 configurations present:

- `development.py` - used for development
- `testing.py` - used for running tests
- `production.py` - configuration with dummy data for production

Please keep `production.py` up-to-date with other configurations,
but avoid pushing any actual password/keys/secrets to the repository

### Preparing database
**Note:** users, database names and passwords come from configuration files

1. Create databases: `test_db` and `dev_db` 
1. Create `test_user` and `dev_user`
1. Grant permission to the users 
1. Change users passwords

```
createuser test_user
createuser dev_user
createdb test_db
createdb development_db

# login to psql
psql
# in psql:
GRANT ALL ON DATABASE test_db TO test_user;
GRANT ALL ON DATABASE dev_db TO dev_user;
ALTER USER test_user PASSWORD 'test';
ALTER USER dev_db PASSWORD 'development';
```

### Starting backend

1. Navigate to `backend` folder
1. (optional) Init database with testing data
1. (optional) Activate virtual environment
1. Install dependencies
1. Run project (runs under http://localhost:8000/)

```
cd backend
CONFIG=../config/development.py python3 -m db_operations.add_test_data
pip3 install -r requiremens.txt
CONFIG=../config/development.py python3 run.py
```

### Running tests
Tests are present in `backend/tests` folder.

1. Navigate to `backend` folder *(see above)*
1. (optional) Activate virtual environment *(see above)*

After that you can either run **all** tests:
```
CONFIG=../config/testing.py python3 run_tests.py
```
Or run **individual** tests:
```
CONFIG=../config/testing.py python3 -m unittest tests.<test_module>.<test_class>.<test_name>

for example:
CONFIG=../config/testing.py python3 -m unittest tests.test_socketio_connection.TestSocketIOConnection.test_connection_not_authenticated
```

### Database migration
Every time the database schema is changed via the **sqlachemy models**
it should be updated on the **postgresql server**

Instead of recreating the whole database, migration script should be used.
It migrates the current data in the database to the new structure.

This step is optional during development, but **a must** on production server. 

**Notes:**

- All commands should be executed from the `backend` folder
- All commands start with `PYTHONPATH=$(pwd) CONFIG=../config/production.py python3 db_operations/migration_manager.py`

#### Initialisation
Command: `... migration_manager.py db init`

It will create `migrations` folder in your `backend` folder

#### Migration
Command: `... migration_manager.py db migrate`

Creates a new version file for the database containing all the changes from previos version. 

Doesn't upgrade database right away, so at this point it's possible
to review the changes that will be applied to the database (check the newest created version in migrations/versions)

#### Upgrade
Command: `... migration_manager.py db upgrade`

Upgrades the database to the next version

#### Downgrade
Command: `... migration_manager.py db downgrade`

Downgrades the database to the previous version

#### Other commands
All the commands can be checked by running `... migration_manager.py db`

Complete documentation can be found [here](https://flask-migrate.readthedocs.io/en/latest/)

#### Manual revision
In cases when migrate script can't automatically find changes
(e.g. column was renamed, column type was changed, foreign key was added)
it can be done manually.

First run `... migration_manager.py db revision`.

This command will create a new revision file in migrations/versions
with empty **upgrade** and **downgrade** functions,
which can be manually edited to achieve the necessary goal.

Below there is an example which:

- renames **test** column to **test_new**
- changes **test** column type to String (from Integer)
- adds a foreign key constraint to the existing column/table
- in case of downgrading reverts everything to previous state

```python
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1f289239c5cf'
down_revision = '2ddfc219bc02'
branch_labels = None
depends_on = None

def upgrade():
    op.alter_column('funds', 'test', new_column_name='test_new', type_=sa.String())
    op.create_foreign_key('fk_trader_tasks_duration_currency', 'trader_tasks', 'currencies', ['duration'], ['id'])

def downgrade():
    op.alter_column('funds', 'test_new', new_column_name='test', type_=sa.Integer(), postgresql_using='test_new::integer')
    op.drop_constraint('fk_trader_tasks_duration_currency', 'trader_tasks')
```

Complete documentation on all alembic operations can be found [here](http://alembic.zzzcomputing.com/en/latest/ops.html)

## Deployment
The project is deployed via Docker-compose.

First the volumes structure should be prepared on the server and initial database migration version created.

It may happen, that paths to volumes will need to be adjusted in `docker-compose.yml` file.

Initially, the following volumes are needed:

- `~/volumes/certificates/` - should contain ssl certificate for nginx: files `nginx.key` and `nginx.crt`
- `~/volumes/backend_configs/` - should contain `production.py` file with backend configuration 
- `~/volumes/db_data/` - initially empty folder where database will be kept
- `~/volumes/migrations/` - should contain initialised `migrations` folder

The last volume folder `migrations` can be tricky, 
as migration script doesn't allow to init migrations when folder already exists.

Below is an approximate algorithm how to deploy project for the first time:

1. Create volumes folders and populate them accordingly (leave `migrations` folder empty)
1. Change `docker-compose.yml`, so that migrations volume folder was linked to some other path
1. Execute `run_production.sh`
1. Enter the backend container `docker-compose exec backend bash`
1. Init migrations folder (see above)
1. Copy the content of newly created migrations folder into volumes and exit the container
1. Change `docker-compose.yml` back to original and execute `docker-compose restart`  
