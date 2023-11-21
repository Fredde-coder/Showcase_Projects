

# Frontend for showcase projects

## Prerequisite
Configure the .env file with the following values:
    - REACT_APP_API_TOKEN: Replace with your API token.
    - REACT_APP_API_ENDPOINT: Replace with the endpoint URL of the Flask_API.


## Getting Started

To get started the react app, follow the steps below:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the dependencies by running `npm install`.
4. Start the development server by running `npm start`.

## Available Scripts

In the project directory, you can run the following scripts:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

### `npm test`

Launches the test runner in the interactive watch mode.

### `npm run build`

Builds the app for production to the `build` folder.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

## Usage

### NPM
```bash
npm run
```

### Docker
```bash
docker build -t your-image-name .
docker run --env-file .env -p 5000:5000 your-image-name
```
