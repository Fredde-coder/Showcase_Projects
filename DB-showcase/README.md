# Database server for the showcase projects

## Prerequisite
Configure the .env file with the following values according to your desire for the database:
- `MYSQL_USER=your_mysql_user`
- `MYSQL_PASSWORD=your_mysql_password`
- `MYSQL_ROOT_PASSWORD=your_mysql_root_password`
- `MYSQL_DATABASE=your_mysql_database`

## Database structure
/**
 * The database initializes with the following tables:
 * 
 * - programming_genres: Stores programming genres with their IDs and names.
 * - programming_sub_genres: Stores programming sub-genres with their IDs, names, and parent genre IDs.
 * - technologies: Stores technologies with their IDs and names.
 * - projects: Stores projects with their names, descriptions, image paths, genre IDs, and years.
 * - project_technologies: Stores the relationship between projects and technologies.
 * 
 * The script also inserts initial projects into the programming_genres and projects tables.
 * 
 * @file db/init.sql
 */

## Running the project with Docker

To build the Docker image, navigate to the project root directory and run the following command:

```bash
docker build -t your-image-name .
docker run --env-file .env -p 3306:3306 your-image-name
```


