# import pyodbc
# import pandas as pd
# from pandleau import *

# df = pd.read_csv("C:\\Users\\user1\\Desktop\\FBPageData.csv")
# df_tableau = pandleau(df)
# df_tableau.to_tableau("C:\\Users\\user1\\Desktop\\TableauExtract.hyper",add_index=False)
  
from pathlib import Path
import json

from tableauhyperapi import HyperProcess, Telemetry, \
    Connection, CreateMode, \
    NOT_NULLABLE, NULLABLE, SqlType, TableDefinition, \
    Inserter, \
    escape_name, escape_string_literal, \
    HyperException

def createHyperTable():
    columns = getConfig()
    page_table = TableDefinition(table_name="Page")
    for i in range(0, len(columns)):
        if columns[i]['DataType'] == "String":
            dt = SqlType.text()
        elif columns[i]['DataType'] == "Date":
            dt = SqlType.date()
        else:
            dt = SqlType.big_int()
        page_table.add_column(columns[i]['ColumnName'], dt)
    return page_table

def run_create_hyper_file_from_csv():
    page_table = createHyperTable()

    print("EXAMPLE - Load data from CSV into table in new Hyper file")

    path_to_database = Path("TableauExtract.hyper")

    process_parameters = {
        "log_file_max_count": "2",
        "log_file_size_limit": "100M"
    }

    with HyperProcess(telemetry=Telemetry.SEND_USAGE_DATA_TO_TABLEAU, parameters=process_parameters) as hyper:
        connection_parameters = {"lc_time": "en_US"}

        with Connection(endpoint=hyper.endpoint,
                        database=path_to_database,
                        create_mode=CreateMode.CREATE_AND_REPLACE,
                        parameters=connection_parameters) as connection:
    
            connection.catalog.create_table(table_definition=page_table)

            path_to_csv = "dummydata.csv"

            count_in_page_table = connection.execute_command(
                command=f"COPY {page_table.table_name} from {escape_string_literal(path_to_csv)} with "
                f"(format csv, NULL 'NULL', delimiter ',', header)")

            print(f"The number of rows in table {page_table.table_name} is {count_in_page_table}.")

        print("The connection to the Hyper file has been closed.")
    print("The Hyper process has been shut down.")

def getConfig():
    with open("config.json", "rb") as file:
        data = json.load(file)
        return data['Columns']

if __name__ == '__main__':
    try:
        run_create_hyper_file_from_csv()
    except HyperException as ex:
        print(ex)
        exit(1)
