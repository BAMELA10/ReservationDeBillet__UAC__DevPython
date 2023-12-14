from .connect import connector
import hashlib
from hmac import compare_digest
import mysql.connector as myc
class users:
    def __init__(self, username, password=None, status=None, email=None, phone=None):
        self.username = username
        self.email = email
        self.password = self._encrypt_password(password)
        self.phone = phone
        self.status = status
    
    def _encrypt_password(self, password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    def verify_password(self, password):
        return self.password == self._encrypt_password(password)
        
    def create_users(self):
        connector.ping()
        cursor = connector.cursor()
        cursor.execute("select * from users where username = (%s)", (self.username,))
        result = cursor.fetchone()
        if result is None:
            cursor.execute("insert into users (username, status, password, email, phone) values(%s,%s,%s,%s,%s)", (self.username, self.status, self.password, self.email, self.phone))
            connector.commit()
            print("user created")
        else:
            print("lose operation")
        connector.close()

    def edit_users(self,username):
        connector.ping()
        cursor = connector.cursor()
        cursor.execute("select * from users where username = %s", (username,))
        result = cursor.fetchone()
        if cursor is not None:
            cursor.execute("update users set username = %s, status = %s, password = %s, email =%s, phone= %s where username =%s", (self.username, self.status, self.password, self.email, self.phone, username))
            connector.commit()
            print("user edited")
            return True
        else:
            print("lose operation")
            return False    
    def delete_users(self):
        connector.ping()
        cursor = connector.cursor()
        cursor.execute("select * from users where username = %s", (self.username,))
        result = cursor.fetchone()
        if result is not None:
            cursor.execute("delete from users where username = %s", (self.username,))
            connector.commit()
            print("user deleted")
            return True
            
        else:
            print("lose operation")
            return False
    
    def login_user(self):
        connector.ping()
        cursor = connector.cursor()
        cursor.execute("select password from users where username = %s", (self.username,))
        result = cursor.fetchone()
        if result is None:
            print("incorrect username or password")
            return False
        else:
            if self.password == result[0]:
                print("user connected")
                return True
            else:
                print("incorrect username or password")
                return False 
    
    
    
    
'''     
var1 = input("username")
var2 = input("new_password")
var3 = input("new_status")

var4 = input("new_email")
var5 = input("new_phone")  '''
'''
var6 = input("new_username")

user = users(var1, var3, var2)
print(user.password)
#user.create_users()
user.delete_users()'''
#user.edit_users(var1)
"""
banzet
123
tyury
jfhgj
464564
"""

