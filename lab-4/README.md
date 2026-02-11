# Try Postgres

## Run `Postgres` and `pgAdmin`

1. Install [Docker](https://docs.docker.com/engine/install/).
2. Change the directory to `lab-1`.

    ```console
    cd compose
    ```

3. Create a `.env` file from the example.

    ```console
    cp .env.example .env
    ```

4. Edit the `.env` file as necessary.
5. Run `Postgres` and `pgAdmin`:
  
  ```console
  docker compose up
  ```

## Connect `pgAdmin` to the database

1. [Run `Postgres` and `pgAdmin`](#run-postgres-and-pgadmin).
1. Open `pgAdmin` at `localhost:45050`.
1. Log in with `PGADMIN_DEFAULT_EMAIL` and `PGADMIN_DEFAULT_PASSWORD` (defined in `.env`)
1. Click `Add New Server`.
1. In `General`, set:
   - `Name`: `postgres`
1. In `Connection`, set:
   - `Host name/address`: `postgres` (service name created by `Docker`)
   - `Port`: `5432` (the value of `POSTGRES_PORT` defined in `.env`)
   - `Maintenance database`: `postgres` (the value of `POSTGRES_DB` defined in `.env`)
   - `Username`: `postgres` (the value of `POSTGRES_USER` defined in `.env`)
   - `Password`: `postgres` (the value of `POSTGRES_PASSWORD` defined in `.env`)
1. Click `Save`.

## Run queries via `pgAdmin`

1. [Connect `pgAdmin` to the database](#connect-pgadmin-to-the-database).
2. In `Default Workspace` -> `Object Explorer` -> `Servers` -> `postgres` -> `Databases`, right-click `postgres` and then click `Query Tool`.
3. Write `SQL`.
4. Click `Execute Script`

## Connect to the database via `VS Code`

1. [Run `Postgres`](#run-postgres-and-pgadmin).
2. [Install](https://code.visualstudio.com/download) `VS Code`.

## Connect `VS Code` to the database using `ms-ossdata.vscode-pgsql`

1. Install the [`ms-ossdata.vscode-pgsql`](https://marketplace.visualstudio.com/items?itemName=ms-ossdata.vscode-pgsql) extension.
2. In `VS Code` -> `Activity Bar`, click `PostgreSQL`.
3. Click `Add Connection`.
4. In `CONNECT VIA:` -> `Parameters`, set:
   - `SERVER NAME`: `postgres`
   - `USER NAME`: `postgres` (the value of `POSTGRES_USER` defined in `.env`)
   - `PASSWORD`: `postgres` (the value of `POSTGRES_PASSWORD` defined in `.env`)
   - `DATABASE NAME`: `postgres` (the value of `POSTGRES_DB` defined in `.env`)
   - `CONNECTION NAME`: `postgres` (arbitrary name)
5. Click `Advanced`.
6. In `Advanced Connection Settings`:
   - Set `PORT`: `45432` (the value of `POSTGRES_HOST_PORT` defined in `.env`)
   - In `Server`, set:
     - `HOST IP ADDRESS`: `127.0.0.1` (the value of `POSTGRES_HOST_ADDRESS` defined in `.env`)
   - In `SSL`, set:
     - `SSL MODE`: `Disable`
7. Click `Save and connect`.

## Connect `VS Code` to the database using `mtxr.sqltools`

1. Install the [`mtxr.sqltools`](https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools) extension.
2. Open `VS Code`.
3. Go to the `Activity Bar`.
4. Click the `SQLTools` icon.
5. Click `Add New Connection`.
6. In `Connection Settings`, set:
   - `Connection name`: `postgres` (arbitrary name)
   - `Connection group`: `Servers` (arbitrary name)
   - `Connect using`: `Server and Port`
   - `Server Address`: `127.0.0.1` (the value of `POSTGRES_HOST_ADDRESS` defined in `.env`)
   - `Port`: `45432` (the value of `POSTGRES_HOST_PORT` defined in `.env`)
   - `Database`: `postgres` (the value of `POSTGRES_DB` defined in `.env`)
   - `Username`: `postgres` (the value of `POSTGRES_USER` defined in `.env`)
   - `SSL`: `Disabled`
7. Click `TEST CONNECTION`.
8. Click `Allow`.
9. Enter password.
10. Click `SAVE CONNECTION`.
11. Click `CONNECT NOW`.
