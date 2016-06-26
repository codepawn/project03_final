class A():

    def save(self):
        print("A save call")


class B(A):

    def save(self):
        print("B save call")
        super(B, self).save()


class C(A):

    def save(self):
        print("C save call")
        super(C, self).save()


class D(B, C):

    def save(self):
        print("D save call")
        super(D, self).save()

d = D()
d.save()
