pip3 install Flask-Storage --user
pip3 install Flask-Testigng --user
pip3 install py-postgresql --user
pip3 install psycopg2 --user

#------------------------
sudo apt-get install postgresql libpq-dev postgresql-client postgresql-client-common

# enter to a 'postgres' account
sudo -i -u postgres

# create a new db user
createuser matt -P --interactive 

# create db 'testpython'
createdb testpython

# launch it to edit
psql testpython
#-------------------------
#-------------------------
# create dir venv 
virtualenv venv

# activate venv
source venv/bin/activate

# deactivate venv
deactivate

#------------------------ 
#from scrath installed in venv
pip install pip-tools
pip install flask