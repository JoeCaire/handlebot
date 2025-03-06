import psycopg2

def delete_user(discord_id):
    try:
        connection = psycopg2.connect(user="your_user",
                                      password="your_password",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="your_database")
        cursor = connection.cursor()
        delete_query = """DELETE FROM users WHERE discord_id = %s"""
        cursor.execute(delete_query, (discord_id,))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully from users table")
    except (Exception, psycopg2.Error) as error:
        print("Error while deleting record from users table", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def delete_organization(sid):
    try:
        connection = psycopg2.connect(user="your_user",
                                      password="your_password",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="your_database")
        cursor = connection.cursor()
        delete_query = """DELETE FROM organizations WHERE sid = %s"""
        cursor.execute(delete_query, (sid,))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully from organizations table")
    except (Exception, psycopg2.Error) as error:
        print("Error while deleting record from organizations table", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def delete_guild(guild_id):
    try:
        connection = psycopg2.connect(user="your_user",
                                      password="your_password",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="your_database")
        cursor = connection.cursor()
        delete_query = """DELETE FROM Server WHERE guildID = %s"""
        cursor.execute(delete_query, (guild_id,))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully from Server table")
    except (Exception, psycopg2.Error) as error:
        print("Error while deleting record from Server table", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
