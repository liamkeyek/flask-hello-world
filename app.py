from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world from Liam in 3308!'
    
@app.route('/db_test')
def db_test():
    try:
        conn = psycopg2.connect("postgresql://liam_lab_10_postgresql_db_user:ZPqw3tqzwtOjm6kAVf6EzlKPRjYLaiL1@dpg-cqm0g5qj1k6c73e1h1ig-a/liam_lab_10_postgresql_db")
        conn.close()
        return "Database connection successful!"
    except Exception as e:
        return f"An error occurred: {e}"
    
@app.route('/db_create')
def creating():
    try:
        conn = psycopg2.connect("postgresql://liam_lab_10_postgresql_db_user:ZPqw3tqzwtOjm6kAVf6EzlKPRjYLaiL1@dpg-cqm0g5qj1k6c73e1h1ig-a/liam_lab_10_postgresql_db")
        cur = conn.cursor()
        
        cur.execute('''
            CREATE TABLE IF NOT EXISTS Basketball (
                First varchar(255),
                Last varchar(255),
                City varchar(255),
                Name varchar(255),
                Number int
            );
        ''')
        conn.commit()
        conn.close()

        return "Basketball Table Successfully Created"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run()