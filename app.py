from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'sql2.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql2371484'
app.config['MYSQL_PASSWORD'] = 'iX2!mJ3*'
app.config['MYSQL_DB'] = 'sql2371484'

mysql = MySQL(app)



@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM `DATA`")
    data = cur.fetchall()
    cur.close()




    return render_template('index2.html', DATA=data )




@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        id = request.form['id']
        name = request.form['name']
        brand_name = request.form['brand_name']
        regular_price_value = request.form['regular_price_value']
        offer_price_value = request.form['offer_price_value']
        currency = request.form['currency']
        classification_l1 = request.form['classification_l1']
        classification_l2 = request.form['classification_l2']
        classification_l3 = request.form['classification_l3']
        classification_l4 = request.form['classification_l4']
        image_url = request.form['image_url']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO DATA (id,name, brand_name, regular_price_value,offer_price_value,currency,classification_l1,classification_l2,classification_l3,classification_l4,image_url) VALUES (%s,%s,%s, %s, %s,%s, %s, %s,%s, %s, %s)", (id,name, brand_name, regular_price_value,offer_price_value,currency,classification_l1,classification_l2,classification_l3,classification_l4,image_url))
        mysql.connection.commit()
        return redirect(url_for('Index'))




@app.route('/delete/<string:id>', methods = ['GET'])
def delete(id):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM DATA WHERE id=%s", (id,))
    mysql.connection.commit()
    return redirect(url_for('Index'))





@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        brand_name = request.form['brand_name']
        regular_price_value = request.form['regular_price_value']
        offer_price_value = request.form['offer_price_value']
        currency = request.form['currency']
        classification_l1 = request.form['classification_l1']
        classification_l2 = request.form['classification_l2']
        classification_l3 = request.form['classification_l3']
        classification_l4 = request.form['classification_l4']
        image_url = request.form['image_url']
        cur = mysql.connection.cursor()
        
        cur.execute("""
               UPDATE DATA
               SET name=%s, brand_name=%s, regular_price_value=%s,
               offer_price_value=%s, currency=%s, classification_l1=%s,
               classifica   tion_l2=%s, classification_l3=%s, classification_l4=%s,image_url=%s
               WHERE id=%s
            """, (name, brand_name, regular_price_value,offer_price_value,currency,classification_l1,classification_l2,classification_l3,classification_l4 ,image_url, id,))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))









if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80,debug=True)
