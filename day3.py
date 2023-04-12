'''x=1

while x<=10:
        print(x)
        x=x+1

print(x)
x=1
while x<=5:
    print('varsha')
    x=x+1
x=int(input('enter a number'))
i=1
while i<=x:
    if i==15:
      i=i+1
      continue 
      
    print(i)
    i=i+1
for i in range (1,10,2):
    print(i)

a=['mango','orange','apple']
for i in a:
    print(i)

name='python'
for i in name:
    print(i)


adj=['red','big','tasty']
fruits=['apple','banana','cherry']
for x in adj:
    for y in fruits:
        print(x,y)

a=[]
for i in range (1,10):
    a.append(i)
print(a)'''


numbers = []
evens = []

for i in range(0,101):
    numbers.append(i)
    

for i in numbers:
    if i % 2 == 0:
        evens.append(i)

print(evens)
