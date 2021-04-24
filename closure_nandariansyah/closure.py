def print_msg(msg): 
# Ini adalah fungsi pembungkus 

    def printer(): 
    # Ini adalah fungsi bersarang 
        print(msg) 

    return printer # baris ini diubah dari yang sebelumnya

# Mari kita panggil fungsinya 
# Output: Hello 
another = print_msg("Hello") 
another() 