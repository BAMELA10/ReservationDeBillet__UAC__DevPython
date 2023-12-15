from connect import connector
import datetime as dt
import random
import string as st

class reservation:
    def __init__(self,id_users,id_event,status_reservation,number_place, code=None, date_reservation=None):
        self.code = self.generate_unique_code()
        self.date_reservation = date_reservation
        self.id_users = id_users
        self.id_event = id_event
        self.status_reservation = status_reservation
        self.number_place = number_place
        
    def code(self):
        character = ''.join(random.choice(st.ascii_letters.upper()) for i in range (5))
        number = ''.join(random.choice(st.digits) for i in range (3))
        return character + '_' + number
    
    def generate_unique_code(self):
        connector.ping()
        code = self.code()
        cursor = connector.cursor()
        cursor.execute("select * from reservation where code = (%s)", (code,))
        result = cursor.fetchall()
        print(result)
        while result != []:
            code = self.code()
        return code        
                
    def create_reservation(self):
        connector.ping()
        cursor = connector.cursor()
        cursor.execute("select * from reservation where code = (%s)", (self.code,))
        result = cursor.fetchone()
        if result is None:
            cursor.execute("insert into reservation (code, status_reservation,number_place, date_reservation, id_users, id_event) values (%s,%s,%s,%s,%s,%s)", (self.code,self.status_reservation, self.number_place, self.date_reservation, self.id_users,self.id_event))
            connector.commit()
            print("reservation created")
            return True
        else:
            print("lose operation")
            return False
        
    def edit_reservation(self, code):
        connector.ping()
        cursor = connector.cursor()
        cursor.execute("select * from reservation where code = %s", (code,))
        result = cursor.fetchone()
        if cursor is not None:
            cursor.execute("update reservation set number_place = %s , id_users = %s, id_event = %s where code = %s" , (self.number_place, self.id_users, self.id_event, code))
            connector.commit()
            print("reservation edited")
            return True
        else:
            print("lose operation")
            return False    
        
        
    def cancel_reservation(self, code):
        connector.ping()
        cursor = connector.cursor()
        cursor.execute("update reservation set status_reservation = %s where code = %s", ("Annulé", code))
        connector.commit()
        print("reservation canceled")
        return True