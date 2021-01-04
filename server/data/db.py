import mysql.connector

class Database():
    def __init__(self):
        self.mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="root",
                        database="iGarden"
                    )
        self.cursor = self.mydb.cursor(dictionary=True,buffered=True)

    def select_luminities(self):
        self.cursor.execute("SELECT * FROM luminities")
        myresult = self.cursor.fetchall()
        return myresult

    def select_humidity(self):
        self.cursor.execute("SELECT * FROM humidities")
        myresult = self.cursor.fetchall()
        return myresult
        
    def select_temperatures(self):
        self.cursor.execute("SELECT * FROM temperatures")
        myresult = self.cursor.fetchall()
        return myresult
        

    def save_state(self,humid,temp,light,time):
        sql="INSERT INTO humidities (value,time) VALUES (%s,%s)"
        values=(humid,time)
        self.cursor.execute(sql,values)

        sql="INSERT INTO luminities (value,time) VALUES (%s,%s)"
        values=(light,time)
        self.cursor.execute(sql,values)

        sql="INSERT INTO temperatures (value,time) VALUES (%s,%s)"
        values=(temp,time)
        self.cursor.execute(sql,values)
                    
        self.mydb.commit()
        print(self.cursor.rowcount, "was inserted.")

    
