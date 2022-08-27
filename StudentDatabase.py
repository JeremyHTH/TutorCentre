import mysql.connector
import csv

class Database:

    def __init__(self):
        self.database =  mysql.connector.connect(host="localhost", user="root", password="51128414", database ="tutcentre")
        self.Cursor = self.database.cursor()
        self.SQLCommandKey = []
        self.SQLCommand = {}
        try:
            with open('command.csv', 'r') as data:
                reader = csv.reader(data)
                for row in reader:
                    print (row)
                    self.SQLCommand[row[0]] = str(row[1])
                self.SQLCommandKey = list(self.SQLCommand.keys())
        except:
            print("try error ")

    def ShowTable(self):
        self.Cursor.execute("Show Tables")
        data = self.Cursor.fetchall()
        for x in data:
            print(x)

    def ShowCommandList (self):
        print(self.SQLCommandKey)

    def ExecuteSQLCommand(self, id : int):
        try:
            self.Cursor.execute()
            return self.Cursor.fetchall()
        except:
            print("error")
            return None

    def ExecuteSQLCommand(self, key: str):
        try:
            self.Cursor.execute(self.SQLCommand[key])
            return self.Cursor.fetchall()
        except:
            print("error")
            return None

        