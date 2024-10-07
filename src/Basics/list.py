fruits=["apple","kiwi","banana","cherry"]
fruits[1:]='watermelon'
print(fruits)

fruits.append("orange")
print(fruits)

student={"name":"arhaan","age":21,"city":"San Francisco"}
for value in student.values():
    print(value)

for key,value in student.items():
    print(f"{key}: {value}")


#dictinoary comprehension
sq={x:x**2 for x in range(10+1)}
print(sq)