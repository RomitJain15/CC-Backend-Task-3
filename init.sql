CREATE TABLE IF NOT EXISTS files (
    id SERIAL PRIMARY KEY,
    file_name VARCHAR(255) NOT NULL,
    content BYTEA NOT NULL,
    media_type VARCHAR(255) NOT NULL DEFAULT 'application/octet-stream'
);


-- Use the following two lines in the terminal to create the TABLE
-- docker cp init.sql PostgreSQL:/docker-entrypoint-initdb.d/init.sql
-- docker exec -it PostgreSQL psql -U postgres -f /docker-entrypoint-initdb.d/init.sql
