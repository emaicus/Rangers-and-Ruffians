import psycopg2
import rnr_utils

def create_rnr_tables(conn):
  print('working.')
  cur = conn.cursor()
  #Create users table
  cur.execute(
    """
    CREATE TABLE IF NOT EXISTS users
    (
      user_id serial PRIMARY KEY,
      username VARCHAR(50) UNIQUE NOT NULL
    );
    """
  )
  print('created table users')
  #Create campaigns table
  cur.execute(
    """
    CREATE TABLE IF NOT EXISTS campaigns
    (
      poohbah_id integer UNIQUE NOT NULL, 
      campaign_name VARCHAR(50) UNIQUE PRIMARY KEY,
      CONSTRAINT poohbah_id_user_id FOREIGN KEY (poohbah_id)
        REFERENCES users(user_id) ON UPDATE NO ACTION ON DELETE NO ACTION
    );
    """
  )

  #Create campaigns table
  cur.execute(
    """
    CREATE TABLE IF NOT EXISTS characters
    (
      c_campampaign_name VARCHAR(50) NOT NULL,
      c_user_id integer NOT NULL,
      character_name VARCHAR(50) NOT NULL,
      c_race VARCHAR(50) NOT NULL,
      c_class VARCHAR(50) NOT NULL,
      c_subclass VARCHAR(50),
      c_level SMALLINT NOT NULL,
      PRIMARY KEY(c_campampaign_name, c_user_id, character_name),
      CONSTRAINT c_user_id_user_id FOREIGN KEY (c_user_id)
        REFERENCES users(user_id) ON UPDATE NO ACTION ON DELETE NO ACTION,
      CONSTRAINT c_campaign_name_campaign_name FOREIGN KEY (c_campampaign_name)
        REFERENCES campaigns(campaign_name) ON UPDATE NO ACTION ON DELETE NO ACTION
    );
    """
  )
  # close communication with the PostgreSQL database server
  cur.close()
  # commit the changes
  conn.commit()

if __name__ == '__main__':
  
  print("Booting up the database! Before running this script make sure to:\n\
    1) Install postgres\n\
    2) Create a rangers and ruffians database\n\
      sudo -u postgres createdb rangers_and_ruffians\n\
    3) Set up a database user and password\n\
      sudo -u postgres createuser YOUR_USERNAME\n\
      sudo -u postgres psql\n\
      alter user YOUR_USERNAME with encrypted password 'YOUR_PASSWORD'\n\
      grant all privileges on database rangers_and_ruffians to YOUR_USERNAME\n\
    \n\
    Database user and password is not stored by this application, so re-authentication is necessary upon each invokation.") 

  db_user = input("Please enter your database username. ")
  db_password = input("Please enter your database password. ")
  connect_str = "dbname='rangers_and_ruffians' user='{0}' host='localhost' password='{1}'".format(db_user, db_password)
  conn = psycopg2.connect(connect_str)
  create_rnr_tables(conn)