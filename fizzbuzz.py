# sexy fizzbuzz code in two lines p
# don't use if-else
n = int(input())
print('\n'.join('Fizz' * (i%3==0) + 'Buzz' * (i%5==0) or str(i) for i in range(1, n)))
# another method
# for i in range(1, n): print('FizzBuzz'[i*i%3*4:8--i**4%5] or i) 