# SQL History CLI

Simple CLI tool to quickly query Snowflake metadata.

This queries DBT models created by the _dbt-snowflake-monitoring_ package ([dave-dbt integration](https://github.com/dave-inc/dave-dbt/blob/staging/dave-sql/packages.yml), [list of models](https://github.com/get-select/dbt-snowflake-monitoring/tree/main/models)). Currently it only queries the `ANALYTIC_DB.DBT.QUERY_HISTORY_ENRICHED` view, returning results about queries run in Snowflake.

### Usage

1. Install the rainier requirements (note that `requirements.txt` is one directory above this README.)
```pip install -r ../requirements.txt```

2. Export the following credential variables on your terminal for use by your Snowflake client:
    ```
    export SNOW_USER
    export SNOW_ROLE
    export PRIVATE_KEY_PATH
    export PRIVATE_KEY_PASSPHRASE
    ```

3Run with ```python -m sql_history```

Optional Flags: 

```--limit:``` Max number of results to return

```--query_start_range_begin:``` Return queries that begin from this time

```--query_start_range_end:``` Return queries that begin until this time

```--output:``` Format of result {dataframe, raw}

```--user:``` Filter results to a certain Snowflake user

```--sort:``` Sort return results {start_time, database, status, duration_sec}