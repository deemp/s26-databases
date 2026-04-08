# `Neo4j`

## Run using `Docker Compose`

1. [Set up the environment](#set-up-the-environment).
2. [Run `Docker Compose` services](#run-docker-compose-services).
3. [Set up the database](#set-up-the-database).
4. [Query the database](#query-the-database).

### Set up the environment

1. Create the env file:

   ```terminal
   cp .env.example .env
   ```

2. Edit `NEO4J_PASSWORD` and `NEO4J_USER`.

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
