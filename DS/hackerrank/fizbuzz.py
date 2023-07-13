def fizzBuzz(n):
    l=['FizzBuzz' if i%3==0 and i%5==0 else  'Fizz' if i%3==0 and i%5!=0 else 'Buzz'  if i%3!=0 and i%5==0 else i   for i in range(1,n+1)]
    for i in l:
        print(i)

fizzBuzz(65)