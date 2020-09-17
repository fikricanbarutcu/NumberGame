import random
number = random.randint(1,30)
right = 7
counter = 0
point = 100
loop_point = 100 / 7
while (right > 0):
  counter += 1
  guess = int(input('Your guess (from 1 to 30): '))
  if (guess > number):
    print('Go down')
  elif (guess < number):
    print('Go up')
  elif (guess == number):
    print(f'Correct. You knewn at {counter}. time and your point is {100 - (loop_point * (counter -1))}.')
    break
  right -= 1
if (right == 0):
    print('Your right over...')