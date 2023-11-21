
"""
This file contains the implementation of a Flask-Restful API for
serving different information about the projects.
"""
import os
import mysql.connector
from flask_cors import CORS
from flask import Flask, jsonify
from flask_restful import Api, Resource


def get_db_connection():
    """
    Connects to the database and returns the connection object.
    Returns:
        MySQLConnection: connection object
    """
    conn = mysql.connector.connect(
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=int(os.getenv('DB_PORT'))
        )
    return conn


class Projects(Resource):
    """
    A class representing the /projects endpoint.
    """

    def get(self):
        """
        Retrieves projects from the database
        and returns them as a JSON response.

        Returns:
            Response: A JSON response containing the list of projects.
        """
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM projects")
        rows = cursor.fetchall()

        projects = []
        for row in rows:
            project = {
                'name': row[0],
                'description': row[1],
                'image_path': row[2],
                'genre_id': row[3],
                'year': row[4]
            }
            projects.append(project)

        return jsonify(projects)


if __name__ == '__main__':
    app = Flask(__name__)
    CORS(app)

    api = Api(app)
    api.add_resource(Projects, '/projects')

    app.run("0.0.0.0")
