"""
Test module for the Projects class.
"""

import unittest
from unittest.mock import Mock, patch
from flask import Flask
from flask_testing import TestCase
from app.run import Projects


class TestProjects(TestCase):
    """
    Test case for the Projects class.
    """

    def create_app(self):
        """
        Create a Flask application for testing.
        """
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    @patch('app.run.get_db_connection')
    def test_get_projects(self, mock_get_db_connection):
        """
        Test the get method of the Projects resource.
        """
        # Mock the database connection and cursor
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [
            ('Test Project', 'Test Description', 'Test Image Path', 1, 2022)
        ]

        # Test the get method of the Projects resource
        projects_resource = Projects()
        response = projects_resource.get()
        expected_response = [
            {
                'name': 'Test Project',
                'description': 'Test Description',
                'image_path': 'Test Image Path',
                'genre_id': 1,
                'year': 2022
            }
        ]

        self.assertEqual(response.get_json(), expected_response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_response)


if __name__ == '__main__':
    unittest.main()
