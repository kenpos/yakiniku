fb = ''
i = 1
for i in range(1,100) :
 if  ( i%3 ) == 0:
  if  ( i%5 )  == 0:
   fb += 'fizzbuzz\n'
  else:
   fb += 'fizz\n'
  else :
    if (i%5)==0:
     fb += 'buzz\n'
    else:
     fb += str (i) + '\n'
print  fb
