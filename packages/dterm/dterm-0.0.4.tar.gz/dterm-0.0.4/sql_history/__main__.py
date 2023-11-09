import argparse
from datetime import datetime, timedelta

import snowflake.snowpark.functions as F

from common import get_session

parser = argparse.ArgumentParser("sql_history", description="Snowflake Query History Lookup")

parser.add_argument(
    "--limit",
    type=int,
    required=False,
    default=1000,
    help="Number of results to return (default == 1000)"
)

parser.add_argument(
    "--query_start_range_begin",
    type=str,
    required=False,
    help="Return queries that started beginning with this time (default to (now - 14) days). Format as MM/DD/YYYY."
)

parser.add_argument(
    "--query_start_range_end",
    type=str,
    required=False,
    help="Return queries that started ending with this time (default == now). Format as MM/DD/YYYY."
)

parser.add_argument(
    "--output",
    choices=['dataframe', 'raw'],
    default='dataframe',
    help="Output format for results: {dataframe, json}"
)

parser.add_argument(
    "--user",
    type=str,
    required=False,
    help="Filter query history to specific user"
)

parser.add_argument(
    "--schema",
    type=str,
    required=False,
    help="Filter query history to specific schema"
)

parser.add_argument(
    "--sort",
    choices=['start_time', 'database', 'status', 'duration_sec'],
    default='start_time',
    help="Sort order of results: {start_time, database, status, duration_sec}"
)

args = parser.parse_args()


if __name__ == '__main__':

    if args.query_start_range_begin:
        query_start_begin = datetime.strptime(args.query_start_range_begin, '%m/%d/%y')
    else:
        query_start_begin = datetime.today() - timedelta(days=14)

    if args.query_start_range_end:
        query_start_end = datetime.strptime(args.query_start_range_end, '%m/%d/%y')
    else:
        query_start_end = datetime.today()

    with get_session(query_tag={"job": "sql-history"}) as session:

        df = session.table("ANALYTIC_DB.DBT.QUERY_HISTORY_ENRICHED").select(
            F.col("EXECUTION_START_TIME").alias("START_TIME"),
            F.col("TOTAL_ELAPSED_TIME_S").alias("DURATION_SEC"),
            F.col("WAREHOUSE_NAME").alias("WAREHOUSE"),
            F.col("SCHEMA_NAME").alias("SCHEMA"),
            F.col("DATABASE_NAME").alias("DATABASE"),
            F.col("USER_NAME"),
            F.col("EXECUTION_STATUS").alias("STATUS"),
            F.col("QUERY_ID"),
            F.col("QUERY_TEXT").alias("SQL")
        )

        if args.user:
            df = df.filter(F.col("USER_NAME") == args.user)

        if args.schema:
            df = df.filter(F.col("SCHEMA") == args.schema)

        # This comes after column aliasing, so it's "START_TIME", not "EXECUTION_START_TIME"
        df = df.filter(F.col("START_TIME").between(query_start_begin, query_start_end))

        if args.sort:
            df = df.sort(args.sort.upper())

        df = df.limit(args.limit)

        if args.output == 'raw':
            for i in df.collect():
                print(i['START_TIME'], i['DURATION_SEC'], i['WAREHOUSE'], i['SCHEMA'], i['DATABASE'], i['USER_NAME'],
                      i['STATUS'], i['QUERY_ID'], i['SQL'], sep='\t')
        elif args.output == 'dataframe':
            df.show()


