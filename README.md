# DataMigrationPipe

This project provides an automated approach for Data migration from multiple sources to multiple sources:

Supported Data Sources:

Input :
  MY SQL
  SQL SERVER
  SQLITE
  POSTGRES
  CSV
  Twitter
  
  
Output:
  MY SQL
  SQL SERVER
  SQLITE
  POSTGRES
  CSV
  
Input.py accepts the input/output config detais:
 
 Input/output Db Detail:
   db details  - Postgres, my_sql, sql_server, sqlite, csv, tweets (for Twitter API , only for input)
   user        - database user id
   pwd         - database user password
   server      - database server
   database    - database name
   port        - database connection port
   csvloc      - location of input csv file

.... for csv db type, only db type and csv location are mandatory.
.... for sqlite db type, only dbtype, database are mandatory.
.... for tweets db type, no other input is required in input db details.


SQLList.py - update extract queries and load queries
