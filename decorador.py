def limite(f):
    def aux(*x,**y):
        try:
            return f(*x,**y)
        except Exception, e:
            return e
    return aux

if __name__ == '__main__':

    def f(x,y):
        return x/y

    g = limite(f)
    print g(3,4.)
    print (3,0)
