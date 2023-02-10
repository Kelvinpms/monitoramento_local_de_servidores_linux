-- Criar um banco de dados
CREATE DATABASE mydatabase;

-- Conecte-se ao banco de dados
\c mydatabase;

-- Criar uma tabela
CREATE TABLE monitoring (
  id INTEGER PRIMARY KEY,
  monitoring_id VARCHAR(255),
  monitor_id VARCHAR(255),
  total INTEGER,
  mem_available INTEGER,
  mem_percent INTEGER
);
