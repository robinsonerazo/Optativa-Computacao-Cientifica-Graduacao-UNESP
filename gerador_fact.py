def fact():
    x,y = 1,1
    while 1:
        y *= x
        yield x,y
        x += 1

def factorial(n):
    for item in gf.fact():
        if item[0] == n:
            res = item[1]
            break
        return res

if __name__ == '__main__':

    for item in fact(100):
        print item
        
    
