class A:
    def method(self):
        print('This is class A')
    pass
class B(A):
    def method(self):
        print('This is class B')
    pass
class C(A):
    def method(self):
        print('This is class C')
    pass
class D(C,B):
    # def method(self):
    #     print('This is class D')
    pass

d = D()
d.method()
#basically that class is fetched by this diamond problem here which comes first in the class D