from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

# Config from config.py
from config import connection_string

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/available')
def available_gadgets():
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()

    # Get available gadgets
    cursor.execute("SELECT gadget_id, name, description, price_per_day, status FROM Gadgets WHERE status = %s", ('Available',))
    available_gadgets = cursor.fetchall()

    # Get rented gadgets
    cursor.execute("SELECT gadget_id, name, description, price_per_day, status FROM Gadgets WHERE status = %s", ('Rented',))
    rented_gadgets = cursor.fetchall()

    conn.close()

    return render_template('Available.html', available_gadgets=available_gadgets, rented_gadgets=rented_gadgets)

@app.route('/rent/<int:gadget_id>', methods=['GET', 'POST'])
def rent_gadget(gadget_id):
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()

    # Get gadget details
    cursor.execute("SELECT * FROM Gadgets WHERE gadget_id = %s", (gadget_id,))
    gadget = cursor.fetchone()

    if request.method == 'POST':
        # Get the number of days from the form
        days = int(request.form['days'])

        # Update gadget status to 'Rented'
        cursor.execute("UPDATE Gadgets SET status = %s WHERE gadget_id = %s", ('Rented', gadget_id))

        # Insert rental details into Rentals table
        cursor.execute("""
            INSERT INTO Rentals (customer_id, gadget_id, rental_date, return_date, total_cost)
            VALUES (%s, %s, CURRENT_TIMESTAMP, 
                    CURRENT_TIMESTAMP + (%s * INTERVAL '1 day'),
                    (SELECT price_per_day FROM Gadgets WHERE gadget_id = %s) * %s)
        """, (1, gadget_id, days, gadget_id, days))

        conn.commit()
        conn.close()

        return redirect('/available')

    return render_template('rent.html', gadget=gadget)

@app.route('/confirm_return/<int:gadget_id>')
def confirm_return(gadget_id):
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Gadgets WHERE gadget_id = %s", (gadget_id,))
    gadget = cursor.fetchone()
    conn.close()
    return render_template('confirm_return.html', gadget=gadget)

@app.route('/return/<int:gadget_id>')
def return_gadget(gadget_id):
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()

    cursor.execute("UPDATE Gadgets SET status = %s WHERE gadget_id = %s", ('Available', gadget_id))

    conn.commit()
    conn.close()

    return redirect('/available')

if __name__ == '__main__':
    app.run(debug=True)
