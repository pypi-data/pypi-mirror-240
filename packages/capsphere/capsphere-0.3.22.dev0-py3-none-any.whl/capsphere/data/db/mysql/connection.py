from capsphere.data.db.exception import DatabaseConnectionError, DatabaseExecutionError
from capsphere.data.db.interface import BaseDBConnection

import mysql.connector
from mysql.connector import Error as MySQLError
import os
import logging


class Connector(BaseDBConnection):
    def __init__(self, ssl_cert_path=None):
        self.logger = logging.getLogger(__name__)

        env_vars = ['MYSQL_DB_HOST', 'MYSQL_DB_NAME', 'MYSQL_DB_USER', 'MYSQL_DB_PASSWORD', 'MYSQL_DB_PORT']
        for var in env_vars:
            if os.getenv(var) is None:
                message = f"The environment variable {var} is not set. It is required for MySQL database connection."
                self.logger.error(message)
                raise EnvironmentError(message)

        super().__init__(
            host=os.getenv('MYSQL_DB_HOST'),
            database=os.getenv('MYSQL_DB_NAME'),
            user=os.getenv('MYSQL_DB_USER'),
            password=os.getenv('MYSQL_DB_PASSWORD'),
            port=int(os.getenv('MYSQL_DB_PORT', 3306))
        )
        self.ssl_cert_path = ssl_cert_path

    def connect(self):
        if not self.connection:
            try:
                connection_args = {
                    "host": self.host,
                    "database": self.database,
                    "user": self.user,
                    "password": self.password,
                    "port": self.port
                }
                if self.ssl_cert_path:
                    connection_args['ssl_ca'] = self.ssl_cert_path
                    connection_args['ssl_verify_cert'] = True

                self.connection = mysql.connector.connect(**connection_args)
            except MySQLError as e:
                self.logger.error(f"Database connection failed: {e}")
                raise DatabaseConnectionError(e)
        return self.connection

    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def execute_query(self, query, fetch_results=True):
        connection = self.connect()
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            connection.commit()
            if fetch_results:
                result = cursor.fetchall()
        except MySQLError as e:
            connection.rollback()
            self.logger.error(f"Query execution failed: {e}")
            raise DatabaseExecutionError(e)
        finally:
            cursor.close()
            self.disconnect()
        return result
