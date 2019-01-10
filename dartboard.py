# Kai
# The longest walk I can take in order to be within walking distance from home 50% of the time is 15-19 steps, according to my written algorithm. My program goes from 0 to 50 steps, and runs each number of steps 1000 times and calculates how often walking home is possible. When it reaches a number of steps whose walk home rate after 1000 trials is less than 50%, the loop breaks. So far the highest number of steps is 19.
# Monte Carlo simulations, named after Monte Carlo in Monaco which is known for its casinos, are algorithms that calculate possible outcomes for any phenomenons that include randomness. Since outcomes that involve random factors are generally very difficult to predict, Monte Carlo Simulations offer an autonomous alternative. Since they do, however, involve elements of randomness, results will often be inconsistent, but this is usually resolved by increasing the number of iterations performed in the calculations. While there is no specific way that Monte Carlo simulations work as they can be applied to any random situation, every Monte Carlo simulation revolves around randomly generating outcomes and applying the outcomes in a predefined manner to produce conclusions and predictions. The applicability of Monte Carlo simulations is very wide, as they can form predictions that are often very difficult to formulate due to the presence of randomness.
# Dart simulation: With 100 iterations, my final values ranged anywhere from 2.8 to 3.4. However, as I increased the number of iterations, the outcomes grew more accurate, producing almost always a 3.13 to 3.15 value at 100000 iterations.

import random

insidecircle = 0

num = 100000

for x in range(num):

	xpos = random.random()*random.choice([-1,1])

	ypos = random.random()*random.choice([-1,1])

	xpos = abs(xpos)

	ypos = abs(ypos)

	dist = ((xpos**2) + (ypos**2))**0.5

	if dist <= 1:

		insidecircle = insidecircle + 1

insidecircle = 4*insidecircle/num

print(insidecircle)