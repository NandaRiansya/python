def print_msg(msg):
    # Ini adalah fungsi pembungkus luar

    def printer():
    # Ini adalah fungsi bersarang
        print(msg)
    printer()

# Eksekusi fungsi
# Output: Hello
print_msg("Hello")