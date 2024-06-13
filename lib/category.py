import sqlite3

class Category:
    def __init__(self, name):
        self.name = name

    def save(self):
        conn = sqlite3.connect('db/expense_tracker.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO category(name)
            VALUES (?)
        ''', (self.name,))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect('db/expense_tracker.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM category')
        categories = cursor.fetchall()
        conn.close()
        return categories

    @classmethod
    def find_by_id(cls, category_id):
        conn = sqlite3.connect('db/expense_tracker.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM category WHERE id = ?', (category_id,))
        category = cursor.fetchone()
        conn.close()
        return category

    @classmethod
    def delete(cls, category_id):
        conn = sqlite3.connect('db/expense_tracker.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM category WHERE id = ?', (category_id,))
        conn.commit()
        conn.close()
