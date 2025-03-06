import psycopg2

def get_user_by_discord_id(discord_id):
    try:
        connection = psycopg2.connect(user="your_user",
                                      password="your_password",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="your_database")
        cursor = connection.cursor()
        select_query = """SELECT * FROM users WHERE discord_id = %s"""
        cursor.execute(select_query, (discord_id,))
        user = cursor.fetchone()
        return user
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching user from users table", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def get_organization_by_sid(sid):
    try:
        connection = psycopg2.connect(user="your_user",
                                      password="your_password",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="your_database")
        cursor = connection.cursor()
        select_query = """SELECT * FROM organizations WHERE sid = %s"""
        cursor.execute(select_query, (sid,))
        organization = cursor.fetchone()
        return organization
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching organization from organizations table", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def get_guild_prefix(guild_id):
    try:
        connection = psycopg2.connect(user="your_user",
                                      password="your_password",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="your_database")
        cursor = connection.cursor()
        select_query = """SELECT prefix FROM Server WHERE guildID = %s"""
        cursor.execute(select_query, (guild_id,))
        prefix = cursor.fetchone()
        return prefix
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching prefix from Server table", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def is_user_registered(discord_id):
    try:
        connection = psycopg2.connect(user="your_user",
                                      password="your_password",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="your_database")
        cursor = connection.cursor()
        select_query = """SELECT EXISTS(SELECT 1 FROM users WHERE discord_id = %s)"""
        cursor.execute(select_query, (discord_id,))
        is_registered = cursor.fetchone()[0]
        return is_registered
    except (Exception, psycopg2.Error) as error:
        print("Error while checking user registration in users table", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def is_organization_registered(sid):
    try:
        connection = psycopg2.connect(user="your_user",
                                      password="your_password",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="your_database")
        cursor = connection.cursor()
        select_query = """SELECT EXISTS(SELECT 1 FROM organizations WHERE sid = %s)"""
        cursor.execute(select_query, (sid,))
        is_registered = cursor.fetchone()[0]
        return is_registered
    except (Exception, psycopg2.Error) as error:
        print("Error while checking organization registration in organizations table", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
