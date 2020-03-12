from collections import defaultdict
import sys

class Table:
    def __init__(self,name,capacity):
        self.name = name
        self.capacity = capacity
    def get_name(self):
        return self.name
    def get_capacity(self):
        return self.capacity
    def __str__(self):
        return self.name


class Restaurent:
    def __init__(self,name):
        self.name = name
        self.free_table_list = defaultdict(list)
        self.booked_table_list = defaultdict(list)
        self.table_wth_max_cap = -1

    def get_name(self):
        return self.name

    def add_table(self,table):
        self.table_wth_max_cap = max (self.table_wth_max_cap,table.get_capacity())
        self.free_table_list[self.name].append(table) # here false denotes unoccupied
    
    def get_free_tables(self):
        return self.free_table_list[self.name]

    def get_booked_tables(self):
        return self.booked_table_list[self.name]

    def add_booking(self,table):
        self.booked_table_list[self.name].append(table)
            
    def get_max_table_size(self):
        return self.table_wth_max_cap

class Booking:
    def book_restaurent(self,restaurent,capacity):
        free_table_list = restaurent.get_free_tables()
        #find the min size table the fits the capacity
        if capacity>restaurent.get_max_table_size():
            return "Restaurent does not have a table with {} capacity".format(capacity)
        min_diff = sys.maxsize
        max_diff = -sys.maxsize
        selected_table = None
        for table in free_table_list:
            cap = capacity-table.get_capacity()
            if cap <= 0:
                if cap ==0:
                    if table not in restaurent.get_booked_tables():
                        restaurent.add_booking(table)
                        return table
                    else:
                        return "Table already booked"            
                else:
                    if cap>max_diff:
                        max_diff = cap
                        selected_table = table
        if selected_table is not None:
            if selected_table in restaurent.get_booked_tables():
                return "Table already booked"

            restaurent.add_booking(selected_table)
            return selected_table
        else:
            return "No table found with the given capacity"



t1= Table('Victoria', 4)
t2= Table('Elizabeth', 3)
t3= Table('Charles', 2)
t4 = Table('Mozart',8)

r = Restaurent('TajPalace')
r.add_table(t1)
r.add_table(t2)
r.add_table(t3)
r.add_table(t4)

r1 = Restaurent('ITC')
r1.add_table(t2)
r1.add_table(t4)

# print(r.get_free_tables())

b= Booking()
print(b.book_restaurent(r,1))
print(b.book_restaurent(r,2))
print(b.book_restaurent(r,3))
print(b.book_restaurent(r,3))
print(b.book_restaurent(r,4))
print(b.book_restaurent(r,4))
print(b.book_restaurent(r,5))
print(b.book_restaurent(r,6))
print(b.book_restaurent(r,9))

print(b.book_restaurent(r1,4))




# class Booking:
    
#     def book_restaurent(self,restaurent_name,capacity):

        