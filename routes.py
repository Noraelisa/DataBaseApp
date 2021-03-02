from app import app
from flask import render_template, request, redirect
import reviews, users, restaurants

@app.route("/")
def index():
    list_res = restaurants.get_list_res()
    return render_template("index.html", restaurants=list_res)

@app.route("/restaurant")
def new():
    return render_template("restaurant.html")

@app.route("/restaurantrev/<int:id>")    
def rev(id):
    res_name = restaurants.get_res(id)
    list_rev = reviews.get_list_rev(id)
    return render_template("restaurant_rev.html", count=len(list_rev), reviews=list_rev, restaurants=res_name, id=id)

@app.route("/add") 
def add():
    return render_template("add.html")   

@app.route("/sendrestaurant", methods=["post"])
def send_res():
    restaurant = request.form["restaurant"]
    if restaurants.send_res(restaurant):
        return redirect("/")
    else:
        return render_template("error.html",message="Ravintolan lisäys epäonnistui")

@app.route("/sendreview", methods=["post"])
def send_rev():
    content = request.form["content"]
    restaurant_id = request.form["restaurant_id"]
    if reviews.send_rev(content, restaurant_id):
        return redirect("/restaurantrev/<int:id>")
    else:
        return render_template("error.html",message="Viestin lähetys epäonnistui")

@app.route("/login", methods=["get","post"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["get","post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Rekisteröinti ei onnistunut")