from connect import connector
import string as st
import random
import datetime as dt
class event:
    def __init__(self, number_place, code=None, date_event=None):
        self.code = self.generate_unique_code()
        self.date_event = dt.datetime.now()
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
            cursor.execute("insert into event (code, date_event, number_place) values (%s,%s,%s)", (self.code, self.date_event, self.number_place))
            connector.commit()
            print("event created")
        else:
            print("lose operation")
        connector.close()
        
    def edit_event(self):
        pass
    def delete_event(self):
        pass
    
event1 = event(40)
event1.create_event()

