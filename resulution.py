class A:
    def show(self): #nama show sama dengan class B
        print("Ini adalah show A")

class B:
    def show(self): #nama show sama dengan class A
        print("Ini adalah show B")

class C(A,B):
    pass

objek = C()

objek.show() 