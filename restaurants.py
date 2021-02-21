from db import db

def get_list_res():
    sql = "SELECT restaurant FROM restaurants ORDER BY restaurant ASC"
    result = db.session.execute(sql)
    return result.fetchall()

def sendRes(restaurant):
    sql = "INSERT INTO restaurants (restaurant) VALUES (:restaurant)"
    db.session.execute(sql, {"restaurant":restaurant})
    db.session.commit()
    return True

def get_restaurant(restaurant_id):
    sql = "SELECT restaurant FROM restaurants WHERE id=:restaurant_id"
    result = db.session.execute(sql, {"restaurant_id":restaurant_id})
    name = result.fetchone()[0]
    return name

