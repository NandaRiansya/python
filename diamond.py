class A:
    def show(self):
        print("Ini adalah fungsi A")

class B(A):
    def show(self):
        print("Ini adalah method B")

class C(A):
    def show(self):
        print("Ini adalah method B")

class D(B,C):
    pass

# BENTUK HUBUNGAN CLASS DIATAS ADALAH MEMBENTUK DIAMOND
# SEHINGGA URUTAN EKSEKUSI UNTUK OBJECT DALAM D ADALAH

objek = D()
objek.show()