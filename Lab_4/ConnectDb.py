import sqlite3


class ConnDB:
    # Функция подключения к БД
    def conn_db(self, namebd):
        # Создание БД и установка соединения с ней
        connection = sqlite3.connect("%s" % namebd)
        # cursor позволяет нам взаимодействовать с базой данных и добавлять записи
        cursor = connection.cursor()
        return connection, cursor

    # Функция закрытия соединения с БД
    def close_db(self, conn):
        conn.close()
