# Fungsi generator sederhana 
def my_gen(): 
    n = 1 
    print('This is printed first') 

    # Fungsi generator berisi pernyataan yield 
    yield n 

    n += 1 
    print('This is printed second') 
    yield n 

    n += 1 
    print('This is printed at last')
    yield n 

# Menggunakan loop for 
for item in my_gen(): 
    print(item)