from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.order import Order

@app.route('/')
def index():
    all_orders = Order.get_all()
    return render_template("orders.html", orders = all_orders)

@app.route('/new_order')
def new_order():
    return render_template('new_order.html')

@app.route('/update_order', methods=["POST"])
def update_order():
    if Order.validate_order(request.form):
        Order.save(request.form)
    return redirect('/')

@app.route('/create_order', methods=["POST"])
def create_order():
    print(request.form)
    if Order.validate_order(request.form):
        Order.save(request.form)
        return redirect('/')
    return redirect('/new_order')

@app.route('/edit_order/<order_id>')
def edit_order(order_id):
    cookie_order = Order.get_one(order_id)
    return render_template('edit_order.html', cookie_order = order)