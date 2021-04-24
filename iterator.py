# mendefinisikan list 
my_list = [4, 7, 0, 3] 

# membuat iterator dengan iter() 
my_iter = iter(my_list) 

# iterasi pada my_iter menggunakan next() 
# print 4 
print(next(my_iter)) 

# print 7 
print(next(my_iter)) 

# next(obj) sama dengan obj.__next__() 
# print 0 
print(my_iter.__next__()) 

# print 3 
print(my_iter.__next__()) 

# Berikut ini akan memunculkan error karena item sudah habis
next(my_iter) 