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
    
@app.route('/db_insert')
def inserting():
    try:
        conn = psycopg2.connect("postgresql://liam_lab_10_postgresql_db_user:ZPqw3tqzwtOjm6kAVf6EzlKPRjYLaiL1@dpg-cqm0g5qj1k6c73e1h1ig-a/liam_lab_10_postgresql_db")
        cur = conn.cursor()
        
        cur.execute('''
            INSERT INTO Basketball (First, Last, City, Name, Number)
            VALUES
            ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
            ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
            ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
            ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
        conn.commit()
        conn.close()

        return "Basketball Table Successfully Populated"
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/db_select')
def selecting():
    try:
        conn = psycopg2.connect("postgresql://liam_lab_10_postgresql_db_user:ZPqw3tqzwtOjm6kAVf6EzlKPRjYLaiL1@dpg-cqm0g5qj1k6c73e1h1ig-a/liam_lab_10_postgresql_db")
        cur = conn.cursor()
        
        cur.execute('SELECT * FROM Basketball;')
        records = cur.fetchall()
        
        cur.close()
        conn.close()
        
        response_string = ""
        response_string += "<table border='1'>"
        response_string += "<tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr>"
        
        for player in records:
            response_string += "<tr>"
            for info in player:
                response_string += "<td>{}</td>".format(info)
            response_string += "</tr>" 
        response_string += "</table>"
        return response_string
    
    except Exception as e:
        return f"An error occurred: {e}"
    
@app.route('/db_drop')
def dropping():
    try:
        conn = psycopg2.connect("postgresql://liam_lab_10_postgresql_db_user:ZPqw3tqzwtOjm6kAVf6EzlKPRjYLaiL1@dpg-cqm0g5qj1k6c73e1h1ig-a/liam_lab_10_postgresql_db")
        cur = conn.cursor()
        cur.execute('DROP TABLE Basketball;')
        conn.commit()
        cur.close()
        conn.close()
        
        return "Basketball Table Successfully Dropped"
    
    except Exception as e:
        return f"An error occurred: {e}"


if __name__ == '__main__':
    app.run()