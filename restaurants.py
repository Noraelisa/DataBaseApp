from db import db

def get_list_res():
    sql = "SELECT restaurant, id FROM restaurants ORDER BY restaurant ASC"
    result = db.session.execute(sql)
    return result.fetchall()

def send_res(restaurant):
    sql = "INSERT INTO restaurants (restaurant) VALUES (:restaurant)"
    db.session.execute(sql, {"restaurant":restaurant})
    db.session.commit()
    return True

def get_res(id):
    sql = "SELECT restaurant from restaurants where id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()