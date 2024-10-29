from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Order:
    db = "cookie_orders"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.cookie_name = data['cookie_name']
        self.num_boxes = data['num_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
       all_orders_list = []
       query = "SELECT * FROM cookie_orders"
       all_orders = connectToMySQL('cookie_orders').query_db(query)
       for order in all_orders:
           new_order_object = Order(order)
           all_orders_list.append(new_order_object)
       return all_orders_list
    
    @classmethod
    def get_one(cls, order_id):
        query = """
                SELECT * FROM cookie_orders WHERE id = %(id)s
                """
        order_dictionary = connectToMySQL("cookie_orders").query_db(query, {"id" : order_id})
        order = Order(order_dictionary[0])
        return order



    @classmethod
    def save(cls, data):
        query = "INSERT into cookie_orders(name, cookie_name, num_boxes) VALUES( %(name)s, %(cookie_name)s, %(num_boxes)s );"
        result = connectToMySQL('cookie_orders').query_db(query, data)
        return result
    
    @classmethod
    def edit(cls, data):
        query = """
                UPDATE cookie_orders SET name = %(name)s,
                cookie_type = %(cookie_type)s,
                num_boxes = %(num_boxes)s
                WHERE id = %(id)s;
                """
        results = connectToMySQL('cookie_orders').query_db(query, data)
        return results
    
    @staticmethod
    def validate_order(data):
        is_valid = True
        if len(data["name"]) == 0:
            flash("Name is required.")
            is_valid = False
        if len(data["cookie_name"]) == 0:
            flash("Type of cookie is required.")
            is_valid = False
        if len(data["num_boxes"]) == 0:
            flash("Number of boxes is required.")
            is_valid = False
        elif int(data["num_boxes"]) <= 0:
            flash("Number of boxes must be a positive number.")
            is_valid = False
        
        return is_valid
