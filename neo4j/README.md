# `Neo4j`

## Run using `Docker Compose`

1. [Enter the `neo4j` directory](#enter-the-neo4j-directory).
2. [Set up the environment](#set-up-the-environment).
3. [Run `Docker Compose` services](#run-docker-compose-services).
4. [Set up the database](#set-up-the-database).
5. [Query the database](#query-the-database).

### Enter the `neo4j` directory

1. Clone this repository:

   ```terminal
   git clone https://github.com/deemp/s26-databases
   ```

2. Enter the `neo4j` directory:

   ```terminal
   cd s26-databases/neo4j
   ```

### Set up the environment

1. Create the env file:

   ```terminal
   cp .env.example .env
   ```

2. Set `NEO4J_PASSWORD` in `.env`.

### Run `Docker Compose` services

1. Start `Docker Desktop`.

2. Start the services.

   ```terminal
   docker compose up -d
   ```

### Set up the database

1. Open `http://localhost:7474` in the browser.

2. Copy the text from [`movies.cypher`](./cypher/movies.cypher).

   Source: [`AhmadTaha96/movies.cypher`](https://gist.github.com/AhmadTaha96/b3e3c033a462a37a582ec80213f42ae7)

3. Paste it into the query field (`neo4j$`) in the browser.

4. To run the script, press `Enter` or click the `Run` button in the top right corner.

### Query the database

1. Paste into the query field (`neo4j$`):

   ```cypher
   MATCH (m:Movie) RETURN m.title, m.released ORDER BY m.released
   ```

2. To execute the query, press `Enter` or click the `Run` button in the top right corner.
