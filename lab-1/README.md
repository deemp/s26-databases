# Try Postgres

## Run `Postgres` and `pgAdmin`

- Install [Docker](https://docs.docker.com/engine/install/).
- Change the directory to `lab-1`.

  ```console
  cd compose
  ```

- Create a `.env` file from the example.

    ```console
    cp .env.example .env
    ```

- Edit the `.env` file as necessary.
- Run `Postgres` and `pgAdmin`:
  
  ```console
  docker compose up
  ```

## Connect `pgAdmin` to the database

- [Run `Postgres` and `pgAdmin`](#run-postgres-and-pgadmin).
- Open `pgAdmin` at `localhost:45050`.
- Log in with `PGADMIN_DEFAULT_EMAIL` and `PGADMIN_DEFAULT_PASSWORD` (defined in `.env`)
- Click `Add New Server`.
  - In `General`, set:
    - `Name`: `postgres`
  - In `Connection`, set:
    - `Host name/address`: `postgres` (service name created by `Docker`)
    - `Port`: `5432` (the value of `POSTGRES_PORT` defined in `.env`)
    - `Maintenance database`: `postgres` (the value of `POSTGRES_DB` defined in `.env`)
    - `Username`: `postgres` (the value of `POSTGRES_USER` defined in `.env`)
    - `Password`: `postgres` (the value of `POSTGRES_PASSWORD` defined in `.env`)
- Click `Save`.

## Run queries via `pgAdmin`

- [Connect `pgAdmin` to the database](#connect-pgadmin-to-the-database).
- In `Default Workspace` -> `Object Explorer` -> `Servers` -> `postgres` -> `Databases`, right-click `postgres` and then click `Query Tool`.
- Write `SQL`.
- Click `Execute Script`

## Connect to the database via `VS Code`

- [Run `Postgres`](#run-postgres-and-pgadmin).
- [Install](https://code.visualstudio.com/download) `VS Code`.

## Connect `VS Code` to the database using `ms-ossdata.vscode-pgsql`

- Install the [`ms-ossdata.vscode-pgsql`](https://marketplace.visualstudio.com/items?itemName=ms-ossdata.vscode-pgsql) extension.
- In `VS Code` -> `Activity Bar`, click `PostgreSQL`.
- Click `Add Connection`.
- In `CONNECT VIA:` -> `Parameters`, set:
  - `SERVER NAME`: `postgres`
  - `USER NAME`: `postgres` (the value of `POSTGRES_USER` defined in `.env`)
  - `PASSWORD`: `postgres` (the value of `POSTGRES_PASSWORD` defined in `.env`)
  - `DATABASE NAME`: `postgres` (the value of `POSTGRES_DB` defined in `.env`)
  - `CONNECTION NAME`: `postgres` (arbitrary name)
- Click `Advanced`.
- In `Advanced Connection Settings`:
  - set `PORT`: `45432` (the value of `POSTGRES_HOST_PORT` defined in `.env`)
  - in `Server`, set:
    - `HOST IP ADDRESS`: `127.0.0.1` (the value of `POSTGRES_HOST_ADDRESS` defined in `.env`)
  - in `SSL`, set:
    - `SSL MODE`: `Disable`
- Click `Save and connect`.

## Connect `VS Code` to the database using `mtxr.sqltools`

- Install the [`mtxr.sqltools`](https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools) extension.
- In `VS Code` -> `Activity Bar`, click `SQLTools`.
- Click `Add New Connection`.
- In `Connection Settings`, set:
  - `Connection name`: `postgres` (arbitrary name)
  - `Connection group`: `Servers` (arbitrary name)
  - `Connect using`: `Server and Port`
  - `Server Address`: `127.0.0.1` (the value of `POSTGRES_HOST_ADDRESS` defined in `.env`)
  - `Port`: `45432` (the value of `POSTGRES_HOST_PORT` defined in `.env`)
  - `Database`: `postgres` (the value of `POSTGRES_DB` defined in `.env`)
  - `Username`: `postgres` (the value of `POSTGRES_USER` defined in `.env`)
  - `SSL`: `Disabled`
- Click `TEST CONNECTION`.
- Click `Allow`.
- Enter password.
- Click `SAVE CONNECTION`.
- Click `CONNECT NOW`.
