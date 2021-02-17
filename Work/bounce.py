# bounce.py
#
# Exercise 1.5
starting_height = 100
height_lost = 0.6
bounce_height = 0
nr_bounce = 0

for i in range(0,11):
    print('Bounce: ', nr_bounce)
    print('Height: ', round(starting_height,4))
    nr_bounce = nr_bounce + 1
    starting_height = starting_height *  height_lost




