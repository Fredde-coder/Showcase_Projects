# Flask application
This is a Flask app that serves as a basic web server.


## Prerequisite
Configure the .env file with the following values according to the configuration of the database:
- `DB_PASSWORD=YOUR_DB_PASSWORD`
- `DB_NAME=YOUR_DB_NAME`
- `DB_USER=YOUR_DB_USER`
- `DB_PORT=YOUR_DB_PORT`
- `DB_HOST=YOUR_DB_HOST`
- `PYTHONPATH=${PYTHONPATH}:.`






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

