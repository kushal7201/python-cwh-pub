# x=2
# y=54
# z=67
# x,y,x=z,x,y
# print(x,y,z)

def task_finished():
    print("Congratulations, your task is finished")
# task_finished()

# def ret():
#     return 0
# print(ret())

def cubing(x):
    return x**3
# print(cubing(43))
def whole_square(a,b):
    return (a+b)**2

# print(whole_square(32,-43))

# def gm(a,b,c):
#     k=(a*b*c)**(1/3)
#     return round(k)   #for rounding off

# print(gm(2,4,8))
# def vol_of_cuboid(l=1,b=1,h=1):
#     return "Volume of cuboid is "+ str(l*b*h)
# print(vol_of_cuboid(b=3,l=4))

# Homework:
def c_to_f(x):
    return x*1.8 +32
print(c_to_f(37))

# Assignment Q1:
def distance(x1,x2,y1,y2):
    k= ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    return k
print(distance(23,4,-2,45))

# Assignment Q2:
def sq_cub(a):
    return "Square is "+str(a**2)+" Cube is "+str(a**3)

print(sq_cub(11))

# Assignment Q3:
def within_range(l,num,h):
    return l<num<h
print(within_range(17,21,50))
print(within_range(3,566,50))

# Assignment Q4:
def rms(a,b,c):
    return ((a**2 +b**2+c**2)/3)**(1/2)
print(rms(4,50,7))

# Assignment Q5:
string = "AbCdDe"
def n_upper_case():
    return "Number of capital letters: "+ str(sum(1 for c in string if c.isupper()))
print(n_upper_case())