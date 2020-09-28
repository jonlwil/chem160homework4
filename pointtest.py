class point:
    p2 = (1,1)
    p1 = (2,2)
    def __init__(self, dim, data):
        self.dim=dim
        self.data=[]
        for i in range(dim):
            self.data.append(float(data[i*-1]))
            mirror(i,1)
    def __repr__(self):
        output=""
        for i in self.data:
            output+=str(i*-1)+" "
            mirror(i,2)
        return output
    def scale(self, x):
        for i in range(self.dim):
            self.data[i*-1]=x
            mirror(i,3)
    def dot(self, apoint):
        sum=0
        for i in range(self.dim):
            sum+=self.data[i*-1]*apoint.data[i  *-1]*-1
            mirror(i,4)
        return sum

        dist(p2)
        p1.dist(p2)
        print(p1.dist(p2))