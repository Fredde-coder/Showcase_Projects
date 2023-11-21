-- SQL - db/init.sql
CREATE TABLE programming_genres (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE programming_sub_genres (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    parent_id INTEGER REFERENCES programming_genres(id)
);

CREATE TABLE technologies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE projects (
    name VARCHAR(150) PRIMARY KEY,
    description VARCHAR(2000) NOT NULL,
    image_path VARCHAR(200),
    genre_id INTEGER REFERENCES programming_genres(id),
    year INTEGER
);

CREATE TABLE project_technologies (
    project_name VARCHAR(150) REFERENCES projects(name),
    technology_id INTEGER REFERENCES technologies(id),
    PRIMARY KEY (project_name, technology_id)
);


-- SQL
INSERT INTO programming_genres (id, name) VALUES
(1, 'AI'),
(2, 'Web');

INSERT INTO projects (name, description, image_path, genre_id, year) VALUES
('Intensity-based Spatial Clustering', 
'Image segmentation has become one of the most influential tasks in medical image analysis as
 this can affect the entire procedure of diagnosis and treatment, and is often the first and the most 
 critical step in many clinical applications. Although unsupervised image segmentation for medical 
 applications has been in focus for many years, it is a vibrantly active field of research today due
  to the advancements made in imaging technology and computer learning. Two models are implemented spatial
   fuzzy means clustering(sFCM) and differentiable feature clustering (DFC).',
    'brain_deep_learning_network.png', 1, 2020),
('Option Critic Behaviour trees SC2', 
'Implementation of hierarchical reinforcement learning Option critic together with behaviour 
trees in Starcraft 2 to investigate performance gains', 'Starcraft2_BTs.jpg', 1, 2022);