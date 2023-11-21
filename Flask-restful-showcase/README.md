# Flask application
This is a Flask app that serves as a basic web server.

## Usage
### Python:
- Run the app using the `flask run` command.
- Access the home page at http://localhost:5000/.
- The app supports only one route currently:
    - /projects: Returns a list of projects inside the connected database

### Docker
```bash
docker build -t your-image-name .
docker run --env-file .env -p 5000:5000 your-image-name
```

