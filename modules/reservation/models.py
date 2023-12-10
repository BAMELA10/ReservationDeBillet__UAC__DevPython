from connect import connector
import datetime as dt
import random
import string as st

class reservation_ticket:
    def __init__(self, id_event, id_reservation,quantity_ticket):
        self.id_event = id_event
        self.id_reservation = id_reservation
        self.quantity_ticket = quantity_ticket   

    def create_reservation_ticket(self):
        connector.ping()
        cursor = connector.cursor()
        cursor.execute("insert into reservation_ticket (id_event, id_reservation, quantity_ticket) values (%s,%s,%s)", (self.id_event, self.id_reservation, self.quantity_ticket))
        connector.commit()
        print("reservation created")
        connector.close()
    def edit_reservation_ticket(self):
        pass
    def delete_reservation_ticket(self):
        pass


class reservation:
    def __init__(self,id_users, code=None, date_reservation=None):
        self.code = self.generate_unique_code()
        self.date_reservation = dt.datetime.now()
        self.id_users = id_users
        
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
            cursor.execute("insert into reservation (code, date_reservation, id_users) values (%s,%s,%s)", (self.code, self.date_reservation, self.id_users))
            connector.commit()
            print("reservation created")
        else:
            print("lose operation")
        
    def edit_reservation(**args):
        connector.ping()
        pass
    def delete_reservation(**args):
        connector.ping()
        pass

class reservation_final:
    def create_reservation_final(self):
        connector.ping()
        cursor = connector.cursor()
        reservation1 = reservation(1)
        reservation1.create_reservation()
        cursor.execute("select id from reservation order by id desc limit 1")
        result = cursor.fetchone()
        reservation_ticket1 = reservation_ticket(1, int(result[0]), 40)
        reservation_ticket1.create_reservation_ticket()
        print("creation complet")
        
    def edit_reservation_final(self):
        pass
    def edit_reservation_final(self):
        pass
    def delete_reservation_final(self):
        pass




''' reservation_ticket1 = reservation_ticket(1, 2, 40)
reservation_ticket1.create_reservation_ticket() '''