#******************************************************************

# Input/output Db Detail:
#   db details  - Postgres, my_sql, sql_server, sqlite, csv, tweets (for Twitter API )
#   user        - database user id
#   pwd         - database user password
#   server      - database server
#   database    - database name
#   port        - database connection port
#   csvloc      - location of input csv file

#.... for csv db type, only db type and csv location are mandatory.
#.... for sqlite db type, only dbtype, database are mandatory.

# in SQLList.py - update extract queries and load queries.
#*******************************************************************


input_db_details = {
    'dbtype': 'tweets',
    'user': 'postgres',
    'pwd': 'root',
    'server': 'localhost',
    'database': 'test',
    'port': '5432',
    'csvloc': 'C:\\Users\\userid\\Downloads\\students-data.csv',
    'search_words': '#halloween -filter:retweets',
    'date_since': '2018-11-16'
}

output_db_details = {
    'dbtype': 'csv',
    'user': 'postgres',
    'pwd': 'root',
    'server': 'localhost',
    'database': 'testsch',
    'port': '5432',
    'csvloc': 'C:\\Users\\userid\\Downloads\\'
}
