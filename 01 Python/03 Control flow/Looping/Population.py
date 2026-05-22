# The current population of a town is 10000. The population of the town is increasing at the rate of  10% per year.
# You have to write a program to find out the population of the town at the end of the last 10 years.

population = 10000
growth_rate = 0.10

for year in range(1, 11):
    population += population * growth_rate
    print("The population of the town at the end of", year, "years is:", population)