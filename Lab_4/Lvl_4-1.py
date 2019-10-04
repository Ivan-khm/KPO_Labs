from ConnectDb import ConnDB
from CreateTb import CreateTables
from NumbQuer import NumbQuery
import os


if __name__ == "__main__":
    name_db = input("Имя БД: ")+".db"

    # Если БД не существует
    if not os.path.exists(name_db):
        connect_db = ConnDB()
        # Создаем и подключаемся к БД
        connection, curs = connect_db.conn_db(name_db)
        create_tab = CreateTables()
        # Создаем таблицы и добавляем данные
        create_tab.create_table(connection, curs)
        create_tab.adding_data(connection, curs)
    # Если БД существует
    else:
        # Подключаемся к БД
        connect_db = ConnDB()
        connection, curs = connect_db.conn_db(name_db)

    number_query = int(input("Введите номер желаемого запроса (1-4): "))
    numb_q = NumbQuery()
    if number_query == 1:
        print(numb_q.first_query(curs))
    if number_query == 2:
        print(numb_q.second_query(curs))
    if number_query == 3:
        print(numb_q.third_query(curs))
    if number_query == 4:
        print(numb_q.fourth_query(curs))

    connect_db.close_db(connection)
 
