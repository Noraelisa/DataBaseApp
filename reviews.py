from db import db
import users, restaurants

def get_res(id):
    sql = "SELECT Res.restaurant FROM reviews R, restaurants Res WHERE R.id=:restaurant_id AND Res.id=R.restaurant_id"
    result = db.session(sql, {"id":id})
    return result.fetchall()

def get_list_rev(id):
    sql = "SELECT R.content, U.username, R.sent_at, R.restaurant_id FROM reviews R, users U WHERE R.user_id=U.id AND R.id=:R.restaurant_id ORDER BY R.id"
    result = db.session.execute(sql)
    return result.fetchall()

def send_rev(content, restaurant_id):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO reviews (content, user_id, sent_at, restaurant_id) VALUES (:content, :user_id, NOW(), :restaurant_id)"
    db.session.execute(sql, {"content":content, "user_id":user_id, "restaurant_id":restaurant_id})
    db.session.commit()
    return True 