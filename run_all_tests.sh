#!/bin/bash

# Navigate to the db service directory and run its tests
cd db
python -m unittest discover

# Navigate to the web backend service directory and run its tests
cd ../Flask_Restful
python -m unittest discover

# Navigate to the showcase-projects directory and run npm test
cd ../showcase-projects
npm test -- --watchAll=false