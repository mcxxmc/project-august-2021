CREATE TABLE picture (
id INTEGER NOT NULL AUTO_INCREMENT,
name VARCHAR(100) UNIQUE NOT NULL,
path VARCHAR(200) NOT NULL,
prediction BOOLEAN,
label BOOLEAN,
PRIMARY KEY(id),
UNIQUE (name));