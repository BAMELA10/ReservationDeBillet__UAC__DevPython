from connect import connector
import string as st
import random
import datetime as dt
class event:
    def __init__(self, intitule, number_place, code=None, date_event=None):
        self.intitule = intitule
        self.code = self.generate_unique_code()
        self.date_event = date_event
        self.number_place = number_place
    def code(self):
        character = ''.join(random.choice(st.ascii_letters.upper()) for i in range (4))
        number = ''.join(random.choice(st.digits) for i in range (3))
        return character + '-' + number
    
    def generate_unique_code(self):
        connector.ping()
        code = self.code()
        cursor = connector.cursor()
        cursor.execute("select * from event where code = (%s)", (code,))
        result = cursor.fetchall()
        print(result)
        while result != []:
            code = self.code()
        return code       
    
    def create_event(self):
        connector.ping()
        cursor = connector.cursor()
        cursor.execute("select * from event where code = (%s)", (self.code,))
        result = cursor.fetchone()
        if result is None:
            cursor.execute("insert into event (code, intitulé, date_event, number_place) values (%s,%s,%s,%s)", (self.code, self.intitule, self.date_event, self.number_place))
            connector.commit()
            print("event created")
            return True
        else:
            print("lose operation")
            return False 
        connector.close()
        
    def edit_event(self, intitule):
        connector.ping()
        cursor = connector.cursor()
        cursor.execute("select * from event where intitulé = %s", (intitule,))
        result = cursor.fetchone()
        if cursor is not None:
            cursor.execute("update event set intitulé = %s, date_event = %s, number_place = %s where intitulé = %s", (self.intitule, self.date_event, self.number_place, intitule))
            connector.commit()
            print("edit_event edited")
            return True
        else:
            print("lose operation")
            return False    
        
    def delete_event(self):
        connector.ping()
        cursor = connector.cursor()
        cursor.execute("select * from event where intitulé = %s", (self.intitule,))
        result = cursor.fetchone()
        if result is not None:
            cursor.execute("delete from event where intitulé = %s", (self.intitule,))
            connector.commit()
            print("user deleted")
            return True
            
        else:
            print("lose operation")
            return False



event1 = event("event4", 450, "", '2023-12-12')
event1.edit_event("event1")

