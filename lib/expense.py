import sqlite3

class Expense:
    def __init__(self, description, amount, date, category_id, user_id):
        self.description = description
        self.amount = amount
        self.date = date
        self.category_id = category_id
        self.user_id = user_id
  
    def save(self):
        conn = sqlite3.connect('db/expense_tracker.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO expense(
                description,
                amount,
                date,
                category_id,
                user_id
            )
            VALUES (?, ?, ?, ?, ?)
        ''', (self.description, self.amount, self.date, self.category_id, self.user_id))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect('db/expense_tracker.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM expense')
        expenses = cursor.fetchall()
        conn.close()
        return expenses

    @classmethod
    def find_by_id(cls, expense_id):
        conn = sqlite3.connect('db/expense_tracker.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM expense WHERE id = ?', (expense_id,))
        expense = cursor.fetchone()
        conn.close()
        return expense

    @classmethod
    def delete(cls, expense_id):
        conn = sqlite3.connect('db/expense_tracker.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM expense WHERE id = ?', (expense_id,))
        conn.commit()
        conn.close()