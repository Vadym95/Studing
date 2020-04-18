name = input("Please enter your name: ")
print(name)

num1 = input("Enter x: ")
num2 = input("Enter y: ")

summa = int(num1) + int(num2)
print(summa)

massage = ""
while massage != 'sekret':
    massage = input("Enter password: ")
    if massage == "sekret": break
    print(massage + " Password Not Correct")

print("Password was:" + massage)


mylist = []

msg = ""
while msg != 'stop'.upper():
    msg = input("Enter new item: ")
    mylist.append(msg)

print(msg)