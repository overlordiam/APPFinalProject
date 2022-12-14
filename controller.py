from utils import *
from flask import Flask, jsonify, request
import json
import os
from flask_cors import CORS, cross_origin
from app import Products, Controller, Users, Orders
from utils import getDataFromAPI

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['POST'])
@cross_origin()
def WebsiteData():
    Controller.connectToDB(database_name="APP2.db")
    PutProductsInDatabase(getDataFromAPI("https://dummyjson.com/", "products"))
    products = Products.objects.select("id, title, description, price, brand, category, thumbnail")
    print(products)
    return jsonify(products)

@app.route("/products", methods=["POST"])
@cross_origin()
def getProducts():
    return jsonify(getDataFromAPI("https://dummyjson.com/","products"))

@app.route("/emptyCart", methods=["POST"])
@cross_origin()
def emptyCart():
    Controller.connectToDB(database_name="APP2.db")
    Orders.objects.delete()
    return "Done"

@app.route("/signUp", methods=["POST"])
@cross_origin()
def SignUp():
    Controller.connectToDB(database_name="APP2.db")
    email = request.json["email"]
    firstName = request.json["firstName"]
    lastName = request.json["lastName"]
    age = request.json["age"]
    gender = request.json["gender"]
    obj = [{"id": f"{100}", "firstName": f"{firstName}", "lastName": f"{lastName}", "gender": f"{gender}", "age": f"{age}", "email": f"{email}"}]
    Users.objects.insert(obj)
    return "done"

@app.route("/addOrders", methods=["POST"])
@cross_origin()
def addOrders():
    id = request.json["id"]
    userName = request.json["userName"]
    productName = request.json["productName"]
    quantity = request.json["quantity"]
    

if __name__ == "__main__":
    Controller.connectToDB(database_name="APP2.db")
    app.run(host='0.0.0.0', port=5000, debug=True)
