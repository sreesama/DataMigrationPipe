from input import input_db_details, output_db_details
import Transform as tfm
import Load as load
import pyodbc
import Extract as ext
import TweetExtract as twt
import sqlite3


def getConnectionODBC(driver, input_db_details):
    conn_str = (
        driver + ";"
        "DATABASE=" + input_db_details['database'] + ";"
        "UID="+ input_db_details['user']+";"
        "PWD="+input_db_details['pwd']+";"
        "SERVER="+input_db_details['server']+";"
        "PORT="+ input_db_details['port'] + ";"
    )
    error = ''
    try:
        conn = pyodbc.connect(conn_str)
    except pyodbc.Error as err:
        error = 'ERROR'
        conn = err
    return error, conn

def initiateConnection(config_details, type):
    conn = '';
    error = '';
    if (type == 'o' and config_details['dbtype'] == 'tweets'):
        error = 'ERROR'
        conn = 'Un Supported output type'
        return error, conn

    if (config_details['dbtype'] == 'my_sql'):
        driver = 'DRIVER={MySQL ODBC 8.0 ANSI Driver}'
        error, conn = getConnectionODBC(driver, config_details)
    elif(config_details['dbtype'] == 'sql_server'):
        driver = 'DRIVER={ODBC Driver 17 for SQL Server}'
        error, conn = getConnectionODBC(driver, config_details)
    elif(config_details['dbtype'] == 'sqlite'):
         try:
            conn = sqlite3.connect(config_details['database'])
         except sqlite3.Error as err:
             error = 'ERROR'
             conn = err
    elif(config_details['dbtype'] == 'Postgres'):
        driver = 'DRIVER={PostgreSQL ODBC Driver(ANSI)}'
        error, conn = getConnectionODBC(driver, config_details)
    elif (config_details['dbtype'] == 'tweets'):
        conn = ''
    elif(config_details['dbtype'] != 'csv'):
        conn = 'Invalid Input DB Type'
        error = 'ERROR'

    return error, conn;

def startExtract(conn):
    if (input_db_details['dbtype'] == 'csv'):
        rows = ext.processExtractCSV(input_db_details['csvloc'])
        dataDFList = [['csv', rows]]
    elif (input_db_details['dbtype'] == 'tweets'):
        rows = twt.extractTweets(input_db_details['search_words'],input_db_details['date_since'])
        dataDFList = [['tweets', rows]]
    else:
        dataDFList = ext.startExtractProcess(conn)

    return dataDFList
def main():
    error, conn = initiateConnection(input_db_details, 'i')

    if (error == 'ERROR'):
        print('ALERT....'+ str(conn))
        return;

    print('---> Starting Extratcing Process')
    dataDFList = startExtract(conn)

    print('---> Starting Transform Process')
    dataDFListTransform = tfm.processTransform(dataDFList);

    print('---> Starting Load Process')
    error, connL = initiateConnection(output_db_details, 'o')
    if (error == 'ERROR'):
        print('ALERT....' + str(conn))
        return;

    if (output_db_details['dbtype'] == 'csv'):
        load.loadProcessCsv(output_db_details['csvloc'],dataDFListTransform)
    else:
        load.startLoadProcess(connL, dataDFListTransform)


if __name__ == "__main__":
    main()
