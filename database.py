import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='python_mk10'
)


def add_pelajar(namapelajar):
    mycursor = mydb.cursor()
    sql = 'INSERT INTO pelajar (namapelajar) VALUES (%s)'
    val = (namapelajar,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(f'{mycursor.rowcount} record inserted.')


def print_hi():
    mycursor = mydb.cursor()
    mycursor.execute('SELECT namapelajar FROM pelajar')
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x[0])


if __name__ == '__main__':
    print_hi()

    # Get user input
    new_pelajar = input('Enter full name (namapelajar): ')

    # Add user input to the database
    add_pelajar(new_pelajar)

    # Print the updated list
    print_hi()
