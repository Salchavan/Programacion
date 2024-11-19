class A:
    def hello(self):
        print("hello in A")
class B (A):
    def hello(self):
        print("hello in B")
class C (B, A):
    def hello(self):
        print("hello in C")
class D (C, B, A):
    def hello(self):
        print("hello in D")
class E (D, C, B, A):
    def hello(self):
        print("hello in E")
class F (E, D, C, B, A):
    pass
class G (F, E, D, C, B, A):
    pass
class H (G, F, E, D, C, B, A):
    pass
    

abc = H()
abc.hello()