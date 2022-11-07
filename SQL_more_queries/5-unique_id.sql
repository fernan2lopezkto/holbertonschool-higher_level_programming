-- UNIQUE

CREATE TABLE IF NOT EXISTS unique_id (
    id int DEFAULT 1 INCREMENTAL,
    name varchar(256)
);