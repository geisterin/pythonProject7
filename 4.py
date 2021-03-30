name = input('Как вас зовут?\n')
name2=""
for i in name[::-1]:
    name2+=i
print("новый текст: ",name2)
input("\n\nEnter.")