import os

from dotenv import load_dotenv

import psycopg2

load_dotenv()


def init_db():
    dsn = os.environ.get('DATABASE_URL')
    print(dsn)
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()

    with open('schema.sql', encoding="utf-8") as f:
        sql = f.read()
        cur.execute(sql)
    conn.commit()

    conn.close()


def all_users():
    dsn = os.environ.get('DATABASE_URL')
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    sql = "SELECT * FROM users;"
    cur.execute(sql)
    users = cur.fetchall()
    conn.commit()
    conn.close()
    return users


def register_user(name, age):
    dsn = os.environ.get('DATABASE_URL')

    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    sql = "INSERT INTO users (name, age) VALUES (%(name)s, %(age)s)"
    cur.execute(sql, {'name': name, 'age': age})
    conn.commit()
    conn.close()


def main():
    init_db()

    welcome_message = "===== Welcome to CRM Application =====\n" \
                      "[S]how: Show all users info\n" \
                      "[A]dd: Add new user\n" \
                      "[Q]uit: Quit The Application\n" \
                      "======================================"
    print(welcome_message)
    while True:
        print()
        command = input('Your command > ')
        if command == 'S':
            users = all_users()
            for user in users:
                print(f"Name: {user[0]} | Age: {user[1]}")

        elif command == 'A':
            name = input('New user name > ')
            age = input('New user age > ')
            print(f"Add new user: {name}")
            register_user(name, age)

        elif command == 'Q':
            print("Bye!")
            break

        else:
            print(f"{command}: command not found")


if __name__ == '__main__':
    main()
