ga.py
=====

A minimal genetic algorithm in Python.


Installation
------------

Requires Numpy. Try `easy_install numpy`.


Usage
-----

Run the program as follows: `$ ./ga.py`. If you want to set the seed
to 17, use `$ ./ga.py 17`.


Parameters
----------

The fitness function is called `FITNESS`. It's set to just sum the
ones in the genome, ie OneMax. It's easy to change. At the same time
also change `FITNESS_THRESHOLD` to the appropriate maximum value.

The parameters `LEN` (genome length), `POPSIZE` (population size),
`GENERATIONS` (number of generations to run for), `CROSSOVER_PROB`
(probability of using crossover as opposed to reproduction) and `PMUT`
(probability of mutating an individual created by crossover or
reproduction) are available. 

Bonus: `SELECTION` (selection method, either `tournament` or
`roulette` (fitness-proportionate)) is also available. Tournament
performs much much better on large OneMax problems.


Minimal?
--------

The number of lines of code (non-comment, non-blank) can be found
using this command, which reports 71 lines:

`$ cat ga.py | grep -v "^#" | grep -v "^[[:space:]]*$" | wc`


Performance
-----------

Genomes are stored as Numpy boolean arrays to save space and make
copying fast.

You can time it using this command:

`$ time ./ga.py`

which gives 1.2s for 100 generations, 100 popsize, 100 genome length
on my iMac.

You can profile it using this command:

`$ python -m cProfile ga.py`

which prints out a long list of function names and the total time
spent in each. Interesting: change `FITNESS` to `sum` (instead of
`numpy.sum`), and `sum` now dominates running time.

Code
----

```python
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
```