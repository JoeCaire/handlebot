import psycopg2
from psycopg2 import sql

class PostgresHelper:
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def connect(self):
        try:
            connection = psycopg2.connect(user=self.user,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port,
                                          database=self.database)
            return connection
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
            return None

    def execute_query(self, query, params=None):
        connection = self.connect()
        if connection is None:
            return None
        try:
            cursor = connection.cursor()
            cursor.execute(query, params)
            connection.commit()
            return cursor
        except (Exception, psycopg2.Error) as error:
            print("Error while executing query", error)
            return None
        finally:
            if connection:
                cursor.close()
                connection.close()

    def fetch_one(self, query, params=None):
        cursor = self.execute_query(query, params)
        if cursor is None:
            return None
        return cursor.fetchone()

    def fetch_all(self, query, params=None):
        cursor = self.execute_query(query, params)
        if cursor is None:
            return None
        return cursor.fetchall()

    def insert(self, table, data):
        columns = data.keys()
        values = [data[column] for column in columns]
        insert_query = sql.SQL("INSERT INTO {table} ({fields}) VALUES ({values})").format(
            table=sql.Identifier(table),
            fields=sql.SQL(', ').join(map(sql.Identifier, columns)),
            values=sql.SQL(', ').join(sql.Placeholder() * len(values))
        )
        self.execute_query(insert_query, values)

    def update(self, table, data, condition):
        columns = data.keys()
        values = [data[column] for column in columns]
        set_clause = sql.SQL(', ').join(
            sql.SQL("{} = {}").format(sql.Identifier(column), sql.Placeholder()) for column in columns
        )
        condition_clause = sql.SQL(' AND ').join(
            sql.SQL("{} = {}").format(sql.Identifier(key), sql.Placeholder()) for key in condition.keys()
        )
        update_query = sql.SQL("UPDATE {table} SET {set_clause} WHERE {condition_clause}").format(
            table=sql.Identifier(table),
            set_clause=set_clause,
            condition_clause=condition_clause
        )
        self.execute_query(update_query, values + list(condition.values()))

    def delete(self, table, condition):
        condition_clause = sql.SQL(' AND ').join(
            sql.SQL("{} = {}").format(sql.Identifier(key), sql.Placeholder()) for key in condition.keys()
        )
        delete_query = sql.SQL("DELETE FROM {table} WHERE {condition_clause}").format(
            table=sql.Identifier(table),
            condition_clause=condition_clause
        )
        self.execute_query(delete_query, list(condition.values()))
