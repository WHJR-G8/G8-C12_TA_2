str1="Tom"
str2="my123"
str3="@gmail.com"

string1=str1+str2+str3

print("The string after concatenating is :", string1)

if string1.isupper() == True:
    print("The string is in uppercase")
else:
    string1=string1.upper()
    print("The string after converting to uppercase is :", string1)

if string1.islower() == True:
    print("The string is in lowercase")
else:
    string1=string1.lower()
    print("The string after converting to lowercase is :", string1)
    
if string1.isalnum() == True:
    print("The string contains alphabets and numbers")
else:
    print("The string is not alphanumeric")
