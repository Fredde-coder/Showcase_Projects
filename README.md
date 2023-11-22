# Showcase_Projects
This project aims to create a web page that showcases my projects. It sets up three services a react frontend, a flask restful API backend and a MySQL server for it to query for data.
It could of course be simpler and only use react, but there is some advanced functionality to be deployed later on that would be more difficult and this project is also a showcase
in itself and therefore aims to include multiple components to showcase my competencies.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Showcase_Project.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Showcase_Project
    ```
3. You need to configure all of the environment variables in .env described in the Readme.md of each service folder
4. Build and run the Docker containers:
    ```bash
    docker-compose up --build
    ```

The application should now be running at `http://localhost`.

## Running the Tests

To run all the tests in all the services, you can use the following command:

### Linux
```bash
bash run_all_tests.sh
```
### Windows
```bash
run_all_tests.bat
```
