from config import config
import psycopg2

class DataBase(object):
    '''
    Atributes:
        params: 
        comands:
        conn:
        curr:
    '''
    self.params = None
    self.comands = None
    self.conn = None
    self.curr = None

    def __init__(self, **params):

        '''Set params for the PostgreSQL database and create a user-jokes table
        Note: Type timestamp equals timestamp with time zone
        '''
        self.commands = (
            '''
           CREATE TABLE users_jokes(
                user_id SERIAL PRIMARY KEY,
                password hstore NOT NULL,
                jokes ARRAY,
                ip INET NOT NULL,
                request_timedate TIMESTAMP,
            )
            '''
        )
        # read the connection parameters
        try:
            self.params = config(section='postgresql')
        except (Exception, psycopg2.DatabaseError) as e:
            print(e)

    def create_table(self):
        if self.conn:
            try:
                for command in self.commands:
                    self.cur.execute(command)
            except (Exception, psycopg2.DatabaseError) as e:
                print(e)
        else:
            Exception("No connection to a database...")

    def connect(self):
        try:
            self.conn = psycopg2.connect(self.params)
            self.cur = self.conn.cursor()   
        except (Exception, psycopg2.DatabaseError) as e:
                print(e)
    
    def save(self):
        try:
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as e:
            print(e)

    
    def close(self):
        try:
            self.close()
            conn.close()
        except (Exception, psycopg2.DatabaseError) as e:
            print(e)

 
db = DataBase()
db.create_table()
