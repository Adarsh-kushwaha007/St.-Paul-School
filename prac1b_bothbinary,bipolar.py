n = int(input("enter the number of inputs:"))
inputs=[]
print("enter the inputs")
for i in range(0,n):
    elements = float(input())
    inputs.append(elements)
print(inputs)

print("enter the weights :")
weights =[]
for i in range(0,n):
    weight = float(input())
    weights.append(weight)
print(weights)

b = float(input("enter the bias value :"))
print("The net input can be calculated as Yin = x1w1+x2w2+x3w3")
Yin = []
for i in range(0,n):
    Yin.append((inputs[i]*weights[i]))

#print(round(sum(Yin),3))
print(round((sum(Yin)+b),1))
