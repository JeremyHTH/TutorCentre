from StudentDatabase import Database
def main(): 
    database = Database()

    database.ShowTable()
    database.ShowCommandList()
    print(database.ExecuteSQLCommand("ShowClass"))


if __name__ == '__main__':
    main()