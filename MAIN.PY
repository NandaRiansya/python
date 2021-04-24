a = 4
b = 2

# lebih besar dari > 
print ('========lebih besar dari(>)')
hasil = a > 3 
print(a,'>',3,'=',hasil)
hasil = b > 3 
print(b,'>',3,'=',hasil)
hasil = b > 2 
print(b,'>',2,'=',hasil)


# kurang dari <
print ('======== kurang dari dari(<)')
hasil = a < 3 
print(a,'<',3,'=',hasil)
hasil = b < 3 
print(b,'<',3,'=',hasil) 
hasil = b < 2 
print(b,'<',2,'=',hasil) 

#lebih besar dari SAMA DENGAN >= 
print ('========lebih besar dari sama dengan (>=)')
hasil = a >= 3 
print(a,'>=',3,'=',hasil)
hasil = b >= 3 
print(b,'>=',3,'=',hasil)
hasil = b >= 2 
print(b,'>=',2,'=',hasil)

#kurang dari SAMA DENGAN <= 
print ('======== kurang dari sama dengan (<=)')
hasil = a <= 3 
print(a,'<=',3,'=',hasil)
hasil = b <= 3 
print(b,'<=',3,'=',hasil)
hasil = b <= 2 
print(b,'<  =',2,'=',hasil)

#sama dengan (==)
print ('======== sama dengan (==)')
hasil = a == 4 
print(a,'==',4,'=',hasil)
hasil = b == 4 
print(b,'==',4,'=',hasil)

# tidak sama dengan (!=)
print ('======== sama dengan (!=)')
hasil = a != 4 
print(a,'!=',4,'=',hasil)
hasil = b != 4 
print(b,'!=',4,'=',hasil)

#object identity (is)
print ('======== object identity(is)')
x = 5
y = 5
print('nilai x =',x,',id = ', hex(id(x)))
print('nilai x =',x,',id = ', hex(id(y)))
hasil = x is y
print ('x is y =', hasil)

x = 5
y = 6
print('nilai x =',x,',id = ', hex(id(x)))
print('nilai x =',x,',id = ', hex(id(y)))
hasil = x is y
print ('x is y =', hasil)