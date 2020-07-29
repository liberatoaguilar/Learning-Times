import random

popsize = 200
TargetString = "LIBERATO AGUILAR"
genes = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP
QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

class Organism(object):

    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()

    def cal_fitness(self):
        global TargetString
        fitness = 0
        for tgt, gnome in zip(TargetString,self.chromosome):
            if gnome != tgt:
                fitness += 1
        return fitness

    @classmethod
    def create_genome(self):
        newchrome = ""
        global genes
        for x in range(len(TargetString)):
            newchrome += random.choice(genes)
        return newchrome

    @classmethod
    def mutate(self):
        global genes
        return random.choice(genes)

    def offspring(self,parent2):
        newchrome = ""
        for p1, p2 in zip(self.chromosome,parent2.chromosome):
            whichparent = random.random()
            if whichparent < 0.45:
                newchrome += p1
            elif whichparent < 0.90:
                newchrome += p2
            else:
                newchrome += self.mutate()
        return Organism(newchrome)

def main():
    done = False
    population = []
    generation = 0
    for x in range(popsize):
        neworg = Organism(Organism.create_genome())
        population.append(neworg)
    while not done:

        population.sort(key= lambda a: a.fitness)

        for x in population[:1]:
            print("Chromosome: "+x.chromosome+" fitness: "+str(x.fitness)+" Generation: "+str(generation))
        #print('\n')

        if population[0].fitness <= 0:
            done = True
            break

        newpopulation = []
        poptopten = popsize*0.1
        poprest = popsize*0.9
        newpopulation.extend(population[:int(poptopten)])

        for x in range(int(poprest)):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = Organism.offspring(parent1,parent2)
            newpopulation.append(child)

        population = newpopulation
        generation += 1
    print("Done!\nGenerations: " + str(generation) +"\nChromosome: "+population[0].chromosome+"\nFitness: "+str(population[0].fitness))

main()
