from db import db
import users, restaurants

def get_list_rev(id):
    sql = "SELECT R.content, U.username, R.sent_at, R.stars FROM reviews R, users U WHERE R.restaurant_id=:id AND R.user_id=U.id ORDER BY R.id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def get_stars(id):
    sql = "SELECT AVG(stars)::numeric(10,2) FROM reviews WHERE restaurant_id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()[0]

def send_rev(content, restaurant_id, stars):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO reviews (content, user_id, sent_at, restaurant_id, stars) VALUES (:content, :user_id, NOW(), :restaurant_id, :stars)" 
    db.session.execute(sql, {"content":content, "user_id":user_id, "restaurant_id":restaurant_id, "stars":stars}) 
    db.session.commit()
    return True 
