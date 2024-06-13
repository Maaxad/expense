import sqlite3

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def save(self):
        conn = sqlite3.connect('db/expense_tracker.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO user(
                username,
                password
            )
            VALUES (?, ?)
        ''', (self.username, self.password))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect('db/expense_tracker.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM user')
        users = cursor.fetchall()
        conn.close()
        return users

    @classmethod
    def find_by_id(cls, user_id):
        conn = sqlite3.connect('db/expense_tracker.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM user WHERE id = ?', (user_id,))
        user = cursor.fetchone()
        conn.close()
        return user

    @classmethod
    def delete(cls, user_id):
        conn = sqlite3.connect('db/expense_tracker.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM user WHERE id = ?', (user_id,))
        conn.commit()
        conn.close()
