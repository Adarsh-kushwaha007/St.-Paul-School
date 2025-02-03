x = float(input("enter the vlaue of x :"))
w = float(input("enter the value of w :"))
b = float(input("enter the vlaue of bias :"))

net = (x*w+b)
if(net<0):
    out = 0
elif((net>=0) & (net <=1)):
    out = net
else:
    out = 1
print("net:",net)
print("output:",out)
