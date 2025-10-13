from flask import Flask, render_template
from data import fake_data

app = Flask(__name__)

@app.get('/')
def index():
    orders = fake_data.get_orders()
    return render_template("index.html", orders=orders)

if __name__ == '__main__':
    app.run()
