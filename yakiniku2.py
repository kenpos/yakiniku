#please get cowsay command.
#apt-get install cowsay
import os

print ("please input  a number value.")
while True:
 i =float(raw_input())
 i
 if  ( i%2 ) == 0:
  if  ( i%9 )  == 0:
   os.system('cowsay -f turkey omg...sorry...please Do not eat...please my god...')
  else:
   os.system('cowsay i want to eat YA KI NI KU ')
 else:
   if (i%9)==0:
    os.system('cowsay -f turkey I can not eat ')
   else:
    print  i
