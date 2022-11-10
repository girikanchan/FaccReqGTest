import pymysql

global cursor
connection = pymysql.connect(host='localhost', user='root', password='', db='manually_fill_attendance')
cursor = connection.cursor()
db_table

sql = "CREATE TABLE " + DB_table_name + """
                        (ID INT NOT NULL AUTO_INCREMENT,
                         ENROLLMENT varchar(100) NOT NULL,
                         NAME VARCHAR(50) NOT NULL,
                         DATE VARCHAR(20) NOT NULL,
                         TIME VARCHAR(20) NOT NULL,
                             PRIMARY KEY (ID)
                             );
                        """
try:
    cursor.execute(sql)  #for create a table
    connection.commit()
except Exception as ex:
        print(ex)

