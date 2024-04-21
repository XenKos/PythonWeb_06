import sqlite3

def create_db():
    # Чтение файла с SQL-скриптом для создания БД
    with open('C:/Users/Денег на комп нету/OneDrive/Робочий стіл/HW_PythonWeb_6/db.sql', 'r') as f:
        sql = f.read()
        
    # Устанавливаем соединение с БД (если файла БД нет, он будет создан)
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        # Выполнение SQL-скрипта из файла для создания таблиц в БД
        cur.executescript(sql)

if __name__ == "__main__":
    create_db()