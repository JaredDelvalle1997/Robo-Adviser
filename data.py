a = range(20,85,5)
age = []

#iterate through the range provided by a, and append the ages to the "age" list.
for x in a: 
 age.append(x)

b = range(25, 77, 2)
stock = []

#iterate throught the range provided by b, and append the allocation to the "stock" list.
for i in b:
    stock.append(i)
print(stock)



allocation = {
    "age": age,
    "Stock": stock
}


print(allocation['age'], allociation['stock')
