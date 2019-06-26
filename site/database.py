import psycopg2
import sys
import os
import json
sys.path.append(os.path.abspath('../code'))
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
      c_campaign_name VARCHAR(50) NOT NULL,
      c_user_id integer NOT NULL,
      character_name VARCHAR(50) NOT NULL,
      c_race VARCHAR(50) NOT NULL,
      c_subrace VARCHAR(50) NOT NULL,
      c_class VARCHAR(50) NOT NULL,
      c_subclass VARCHAR(50),
      c_level SMALLINT NOT NULL,
      PRIMARY KEY(c_campaign_name, c_user_id, character_name),
      CONSTRAINT c_user_id_user_id FOREIGN KEY (c_user_id)
        REFERENCES users(user_id) ON UPDATE NO ACTION ON DELETE NO ACTION,
      CONSTRAINT c_campaign_name_campaign_name FOREIGN KEY (c_campaign_name)
        REFERENCES campaigns(campaign_name) ON UPDATE NO ACTION ON DELETE NO ACTION
    );
    """
  )
  # close communication with the PostgreSQL database server
  cur.close()
  # commit the changes
  conn.commit()

def grab_all_campaign_names(conn):
  cur = conn.cursor()
  cur.execute(
    """
    SELECT campaign_name FROM campaigns;
    """
  )
  answer = cur.fetchall()
  cur.close()
  return answer

def grab_all_usernames(conn):
  cur = conn.cursor()
  cur.execute(
    """
    SELECT username FROM users;
    """
  )
  users = cur.fetchall()
  cur.close()
  return users

def grab_all_characters(conn):
  cur = conn.cursor()
  cur.execute(
    """
    SELECT * FROM characters;
    """
  )
  characters = cur.fetchall()
  cur.close()
  return characters

def grab_all_characters_for_user(conn, user):
  cur = conn.cursor()
  cur.execute(
    """
    SELECT * FROM characters WHERE c_user_id = 
      (SELECT user_id FROM users as u WHERE u.username = (%s) );
    """, (user,)
  )
  users = cur.fetchall()
  cur.close()
  return users

def get_userid_for_username(conn, username):
  cur = conn.cursor()
  cur.execute(
  """
  SELECT user_id from users WHERE username = (%s);
  """, (username,)
  )

  user_id = cur.fetchall()
  cur.close()
  return None if len(user_id) == 0 else user_id[0]

def verify_user_exists(conn, username):
  return len(get_userid_for_username(username)) > 0


def insert_a_campaign(conn, campaign_name, poohbah_name):
  cur = conn.cursor()
  #p_id = get_userid_for_username(conn, poohbah_name)
  #Create users table
  cur.execute(
    """
    INSERT INTO campaigns (campaign_name, poohbah_id)
      SELECT (%s), ( SELECT user_id FROM users WHERE username = (%s) )
    WHERE NOT EXISTS(
      SELECT 1 FROM campaigns WHERE campaign_name = (%s)
    );
    """, (campaign_name, poohbah_name, campaign_name)
  )
  cur.close()
  conn.commit()
  return None

def insert_new_user(conn, username):
  cur = conn.cursor()
  cur.execute(
    """
    INSERT INTO users (username)
      SELECT (%s)
    WHERE NOT EXISTS(
      SELECT 1 FROM users WHERE username = (%s)
    );
    """, (username, username)
  )
  cur.close()
  conn.commit()
  return None

def insert_new_character(conn, campaign_name, username, character_name, rnr_race, rnr_subrace, rnr_class, rnr_subclass, level):
  cur = conn.cursor()
  user_id = get_userid_for_username(conn, username)
  if user_id is None:
    raise "ERROR: Bad username {0}".format(username)
  #Create users table
  cur.execute(
    """
    INSERT INTO characters (c_campaign_name, c_user_id, character_name, c_race, c_subrace, c_class, c_subclass, c_level)
      SELECT (%s), (%s), (%s), (%s), (%s), (%s), (%s), (%s) 
    WHERE NOT EXISTS(
      SELECT 1 FROM characters WHERE c_campaign_name = (%s) AND c_user_id = (%s) AND character_name = (%s)
    );
    """, (campaign_name, user_id, character_name, rnr_race, rnr_subrace, rnr_class, rnr_subclass, level, campaign_name, user_id, character_name)
  )
  cur.close()
  conn.commit()
  return None

def initialize_database_connection():
  db_user = input("Please enter your database username. ")
  db_password = input("Please enter your database password. ")
  connect_str = "dbname='rangers_and_ruffians' user='{0}' host='localhost' password='{1}'".format(db_user, db_password)
  conn = psycopg2.connect(connect_str)
  create_rnr_tables(conn)
  return conn

def db_to_rnr_load_characters_for_user(conn, user):
  rows = grab_all_characters_for_user(conn, user)
  characters = dict()
  for campaign, _, character_name, race, subrace, rnr_class, subclass, level in rows:
    if not campaign in characters:
      characters[campaign] = list()
    c = rnr_utils.rnr_character(character_name, race, subrace, rnr_class, level, subclass=subclass)
    characters[campaign].append(c.serialize())
  return characters

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
  conn = initialize_database_connection()
  print(grab_all_usernames(conn))
  insert_new_user(conn, "Evan")
  insert_new_user(conn, "Jeremy")
  insert_new_user(conn, "Zack")
  print(grab_all_campaign_names(conn))
  print(grab_all_usernames(conn))
  print(get_userid_for_username(conn,"Evan"))
  print(get_userid_for_username(conn,"Bobby Flay"))
  print(get_userid_for_username(conn,"Jeremy"))
  insert_a_campaign(conn, "The Curse of Strahd", "Evan")
  insert_a_campaign(conn, "The Abyss", "Jeremy")
  insert_a_campaign(conn, "Untitled Campaign", "Zack")
  print(grab_all_campaign_names(conn))
  print(grab_all_characters(conn))
  print(grab_all_characters_for_user(conn, "Evan"))
  insert_new_character(conn, "The Abyss", "Evan", "Archibold", "Human", "Human", "Wizard", None, 4)
  insert_new_character(conn, "The Curse of Strahd", "Jeremy", "Gillthunder", "Human", "Human", "Knight", None, 5)
  insert_new_character(conn, "The Abyss", "Zack", "Orcenshield", "Orc", "Orc", "Archer", None, 4)
  insert_new_character(conn, "The Curse of Strahd", "Zack", "Orcenshield", "Orc", "Orc", "Archer", None, 5)
  print(grab_all_characters(conn))
  print(grab_all_characters_for_user(conn, "Evan"))
  print(grab_all_characters_for_user(conn, "Zack"))
  print(grab_all_characters_for_user(conn, "Jeremy"))
  print(json.dumps(db_to_rnr_load_characters_for_user(conn, "Zack"), indent=4))