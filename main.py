

a=int(input("what number would you like to decode?"))

def decodingMenu ():
  print("1- hexadecimal")
  print("2- binary")
  print("3- decimal")
decodingMenu()
b=int(input("which number would you like?"))

if b==1:
  print(hex(a))
elif b==2:
  print(bin(a))
else:
  print(int(a))
  