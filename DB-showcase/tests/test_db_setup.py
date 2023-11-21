"""
This file contains unit tests for setting up the database.
"""
import time
import os
import unittest
import docker
import mysql.connector


class TestDatabaseSetup(unittest.TestCase):
    """
    This class contains unit tests for setting up the database.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment by starting a
        Docker container with MySQL image,
        waiting for the MySQL server to start,
        running the init.sql script to set up the database,
        and connecting to the MySQL server.
        """
        try:
            cls.client = docker.from_env()
            cls.container = cls.client.containers.run(
                'mysql',
                detach=True,
                ports={'3306/tcp': 3306},
                environment={
                    "MYSQL_DATABASE": "mydatabase",
                    "MYSQL_ALLOW_EMPTY_PASSWORD": "yes"
                }
            )
            # Wait for the MySQL server to start
            for _ in range(30):  # try for 30 seconds
                exit_code, output = cls.container.exec_run(
                    'mysql -uroot -e "SHOW DATABASES"'
                )
                if "mydatabase" in output.decode():
                    break
                time.sleep(1)
            else:
                cls.tearDownClass()
                raise RuntimeError(
                    'MySQL server did not start or "mydatabase" not found'
                )

            # Run the init.sql script to set up the database
            script_path = os.path.join(
                os.path.dirname(__file__), '..', 'models', 'init.sql'
            )
            with open(script_path, 'r', encoding='UTF-8') as file:
                sql_command = ''
                for line in file:
                    # Skip comments
                    if not line.strip().startswith('--'):
                        sql_command += line.strip()
                        # If the line ends with a semicolon,
                        # execute the SQL command
                        if sql_command.endswith(';'):
                            command = (
                                f'mysql -uroot -Dmydatabase '
                                f'-e "{sql_command}"'
                            )
                            exit_code, output = cls.container.exec_run(command)
                            if exit_code != 0:
                                raise RuntimeError(
                                    f'Failed to execute SQL command: {output}'
                                )
                            sql_command = ''
            # Connect to the MySQL server
            cls.connection = mysql.connector.connect(
                host='localhost',
                database='mydatabase',
                user='root'
            )
            cls.cursor = cls.connection.cursor()
        except Exception as e:
            print(f"Setup failed: {e}")
            cls.tearDownClass()
            raise

    @classmethod
    def tearDownClass(cls):
        """
        Clean up the test environment by stopping the Docker container.
        """
        cls.connection.close()
        cls.container.stop()
        cls.container.remove()

    def test_database_exists(cls):
        """
        Test if the 'mydatabase' exists in the MySQL server.
        """
        cls.cursor.execute('SHOW DATABASES')
        databases = cls.cursor.fetchall()
        cls.assertIn(('mydatabase',), databases)

    def test_database_setup(cls):
        """
        Test if the required tables were created correctly in the database.
        """
        cls.cursor.execute('SHOW TABLES')
        tables = cls.cursor.fetchall()
        cls.assertIn(('programming_genres',), tables)
        cls.assertIn(('programming_sub_genres',), tables)
        cls.assertIn(('technologies',), tables)
        cls.assertIn(('projects',), tables)
        cls.assertIn(('project_technologies',), tables)

    def test_inserted_programming_genres_present(cls):
        """
        Test if the inserted programming genres
        are present in the 'programming_genres' table.
        """
        cls.cursor.execute('SELECT name FROM programming_genres')
        rows = cls.cursor.fetchall()
        cls.assertIn(('AI',), rows)
        cls.assertIn(('Web',), rows)

    def test_inserted_projects_present(cls):
        """
        Test if the inserted projects are present in the 'projects' table.
        """
        cls.cursor.execute('SELECT name FROM projects')
        rows = cls.cursor.fetchall()
        cls.assertIn(('Intensity-based Spatial Clustering',), rows)
        cls.assertIn(('Option Critic Behaviour trees SC2',), rows)


if __name__ == '__main__':
    unittest.main()
