# `Neo4j`

## Set up `Neo4j` using `Sandbox`

> [CAUTION]
> The sandbox lives only up to 3 days.

1. [Create a `Neo4j` instance](#create-a-neo4j-instance).
2. [Connect to the instance](#connect-to-the-instance).
3. [Run a query or a script in the `Neo4j Browser`](#run-a-query-or-a-script-in-the-neo4j-browser).

### Create a `Neo4j` instance

1. Open <https://sandbox.neo4j.com/> in the browser.

2. Sign up.

3. Go to <https://sandbox.neo4j.com/>.

4. Click `New Project`.

5. Select `Blank Sandbox - Graph Data Science`.

6. Click `Create and Download credentials`.

   Credentials should be downloaded in a `.txt` file.

### Connect to the instance

1. Go to <https://sandbox.neo4j.com/>.

2. Click `Open`

   <img alt="Open the Blank Sandbox" src="./images/open-blank-sandbox.png" style="width:400px"/>

3. Set the values using the values of variables in the downloaded credentials file:

   - `Database user`: `NEO4J_USERNAME`

   - `Password`: `NEO4J_PASSWORD`

4. Click `Connect`.

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

## (Optional) Connect from `VS Code`

> [IMPORTANT]
> Assumption: you run using `Docker Compose`.

1. [Connect to the database](#connect-to-the-database).
2. [Run a query](#run-a-query).
3. [Run all queries](#run-all-queries).

### Connect to the database

1. Install the `VS Code` extension `neo4j-extensions.neo4j-for-vscode`.

2. Run using the `Command Palette`: `Neo4j: Create new connection`.

3. Set the values:

   - `Display name`: `Movies`

   - `Scheme`: `neo4j://`

   Use the values from `.env`:

   - `Host`: `NEO4J_HOST_ADDRESS`

   - `Port`: `NEO4J_BOLT_PORT`

   - `User`: `NEO4J_USER`

   - `Password`: `NEO4J_PASSWORD`

4. Click `Save & Connect`.

### Run a query

1. Open [`cypher/examples.cypher`](./cypher/examples.cypher).

2. Select the `Example 1` query.

3. To run the selected query, press `Ctrl+Enter`.

### Run all queries

1. To run all queries in the file, press `Ctrl+Alt+Enter`.
