import random
import statistics

def gaussian_distribution():
    random_nums = []
    mu = 100
    sigma = 10
    for x in range(0, 1000):
        random_nums.append(random.gauss(mu, sigma))
    return random_nums   

nums = gaussian_distribution()
print("Mean:", statistics.mean(nums))
print("Standard Deviation:", statistics.stdev(nums))