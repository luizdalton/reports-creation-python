import database_connect as db

if __name__ == "__main__":
    print('Trying to connect to the database...')

try:
    db = db.MySQLConnection()
    print('Connection successful!')
    db._close()
    print('Connection closed.')

except ConnectionError as error:
    raise "Error during the connection. Message: {error}"

