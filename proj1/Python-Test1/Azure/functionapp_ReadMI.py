import pyodbc
import collections
import json
def connectMI(server: str, database: str, user: str, password: str):
    conn = pyodbc.connect(
        server=f"{server}",
        database=f"{database}",
        user=f'{user}',
        tds_version='7.4',
        password=f"{password}",
        port=1433,
        driver='FreeTDS'
    )
    return conn



def getdata(server: str, database: str, user: str, password: str):
    conn = connectMI (f'{server}', f'{database}', f'{user}', f'{password}')
    crsr = conn.cursor()
    rows = crsr.execute(" Select top 1 @@ServerName as InstanceName,RowID,DateTimeUTC,Memory_Grants_Pending\
,SessionCount,TempDB_Data_Size_GB,TempDB_Log_Size_GB,InMemoryOLTP_MB,Log_IOPS,Log_ThroughPut_BytesPerSec\
,Log_IOStallPerSec,Data_IOPS,Data_ThroughPut_BytesPerSec,Data_IOStallPerSec,FileCount,Data_Size_GB\
,Log_Size_GB from Metric_Instance").fetchall()

    for row in rows:
        d = {}
        for i, col in enumerate(crsr.description):
            d[f'{col[0]}'] = str(row[i])
            object_json=d
        j = json.dumps(object_json)

    print(object_json)
    crsr.close()
    conn.close()

getdata ('mi-useast-mcdatatier-poc1.76db9e6f952f.database.windows.net', 'utility', 'mcadmin', 'mcdtTestPassword1')
