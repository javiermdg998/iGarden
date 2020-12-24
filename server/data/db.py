import mysql.connector

class Database():
    def __init__(self):
        self.mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="root",
                        database="iGarden"
                    )
        self.cursor = self.mydb.cursor(dictionary=True)

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
        

