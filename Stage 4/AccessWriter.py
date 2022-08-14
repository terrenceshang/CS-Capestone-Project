import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\Stage 4\\TrainSchedule.accdb;')
cursor = conn.cursor()
sql = "INSERT INTO AreaCentral VALUES (9501,'Cape Town','Kapteinsklip','05:00',16,'MF')"
cursor.execute(sql)
conn.commit() 
"""  
for row in cursor.fetchall():
    print (row)
"""