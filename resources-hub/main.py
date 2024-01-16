from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="***",
    database="resources"
)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/search')
def search_index():
   cursor = mydb.cursor()
   cursor.execute("SELECT * FROM resources_list")
   resources_list = cursor.fetchall()
   cursor.close()

   return render_template('search.html', resources_list=resources_list)

@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['search_query']
    selected_option = request.form.getlist('tag[]')

    query = "SELECT * FROM resources_list WHERE 1 = 1"
    placeholders = []

    if selected_option:
        for tag in selected_option:
            query += " AND tags LIKE %s"
            placeholders.append(f"%{tag}%")
    
    if search_query:
        query += " AND title LIKE %s"
        placeholders.append(f"%{search_query}%")

    cursor = mydb.cursor()
    cursor.execute(query, tuple(placeholders))
    result = cursor.fetchall()
    cursor.execute("SELECT * FROM resources_list")
    resources_list = cursor.fetchall()
    cursor.close()

    if not result:
        return render_template('search.html', resources_list=resources_list)
    else:
        return render_template('search.html', resources_list=result)

@app.route('/resource_submissions')
def resource_submissions():
   return render_template('resource_submissions.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        title = request.form['name']
        url = request.form['url']
        description = request.form['description']
        tags = request.form.getlist('tag[]')
        concatenated_tags = ','.join(tags)


        # Insert data into MySQL
        cursor = mydb.cursor()
        sql = "INSERT INTO resources_list (title, url, description, tags) VALUES (%s, %s, %s, %s)"
        val = (title, url, description, concatenated_tags)
        cursor.execute(sql, val)
        mydb.commit()
        cursor.close()
        
        return "Data successfully inserted into the database."
    return "Invalid request."

if __name__ == '__main__':
   app.run(debug=True)