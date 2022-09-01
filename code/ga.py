#!/usr/bin/env python

import sys, time, numpy, random

# Individual has a genome and fitness and knows how to print itself
class Individual:
    def __init__(self, genome):
        if genome is None:
            self.genome = numpy.array(numpy.random.random_integers(0, 1, LEN), dtype='bool')
        else:
            self.genome = genome
        self.fitness = FITNESS(self.genome)
    def __str__(self):
        return "".join(str(int(i)) for i in self.genome)
        
# Uniform crossover
def xover(a, b):
    g, h = a.genome.copy(), b.genome.copy()
    for pt in range(len(g)):
        if numpy.random.random() < 0.5:
            g[pt], h[pt] = h[pt], g[pt]
    return (Individual(g), Individual(h))

# Per-gene bit-flip mutation
def mutate(a):
    g = a.genome.copy()
    for pt in range(len(g)):
        if numpy.random.random() < PMUT:
            g[pt] = not g[pt]
    return Individual(g)

# Print statistics, and return True if we have succeeded already.
def stats(pop, gen):
    best = max(pop, key=lambda x: x.fitness)
    print("{0} {1:.2f} {2} {3}".format(gen, numpy.mean([i.fitness for i in pop]), best.fitness, str(best)))
    return (best.fitness >= SUCCESS_THRESHOLD)

# Roulette-wheel (fitness-proportionate) selection. Tricky but fast.
# http://stackoverflow.com/questions/2140787/select-random-k-elements-from-a-list-whose-elements-have-weights
def roulette(items, n):
    total = float(sum(w.fitness for w in items))
    i = 0
    w, v = items[0].fitness, items[0]
    while n:
        x = total * (1 - numpy.random.random() ** (1.0 / n))
        total -= x
        while x > w:
            x -= w
            i += 1
            w, v = items[i].fitness, items[i]
        w -= x
        yield v
        n -= 1

# Use many tournaments to get parents
def tournament(items, n, tsize=5):
    for i in range(n):
        candidates = random.sample(items, tsize)
        yield max(candidates, key=lambda x: x.fitness)

# Run one generation
def step(pop):
    newpop = []
    parents = SELECTION(pop, len(pop) + 1) # one extra for final xover    
    while len(newpop) < len(pop):
        if numpy.random.random() < CROSSOVER_PROB:
            # crossover and mutate to get two new individuals
            newpop.extend(map(mutate, xover(parents.next(), parents.next())))
        else:
            # clone and mutate to get one new individual
            newpop.append(mutate(parents.next()))
    return newpop
    
def main():
    if len(sys.argv) > 1:
        numpy.random.seed(int(sys.argv[1]))
    print("GENERATIONS {0}, POPSIZE {1}, LEN {2}, CROSSOVER_PROB {3}, PMUT {4}".format(GENERATIONS, POPSIZE, LEN, CROSSOVER_PROB, PMUT))
    pop = [Individual(None) for i in range(POPSIZE)]
    stats(pop, 0)
    for gen in range(1, GENERATIONS):
        pop = step(pop)
        if stats(pop, gen):
            print("Success")
            sys.exit()
    print("Failure")

# parameters
GENERATIONS, POPSIZE, LEN, CROSSOVER_PROB, PMUT = (100, 100, 100, 0.5, 0.1)
FITNESS, SUCCESS_THRESHOLD = (numpy.sum, LEN)
SELECTION = roulette # roulette sucks: tournament is better

main()