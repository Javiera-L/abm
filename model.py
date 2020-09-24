import random
import operator
import matplotlib.pyplot
import agentframework
import csv
import sys

#setting parameters
# num_of_agents = 10
# num_of_iterations = 100
# neighbourhood = 20

num_of_agents = sys.argv[0]
num_of_iterations = sys.argv[1]
neighbourhood = sys.argv[2]


environment = []
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader: # A list of rows
    rowlist = [] 
    for value in row: # A list of value
        rowlist.append(value)
        #print(value) # Float
    #print(rowlist)
    environment.append(rowlist)
    
f.close() # Don't close until you are done with the reader;
        # the data is read on request.
size = len(environment)
print(size)
"""
environment = []
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader: # A list of rows
        rowlist = [] 
        for value in row: # A list of value
            rowlist.append(value)
            #print(value) # Float
        print(rowlist)
        environment.append(rowlist)
"""

matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()


# def distance_between(agents_row_a, agents_row_b):
#     return (((agents_row_a.x - agents_row_b.x)**2) + 
#     ((agents_row_a.y - agents_row_b.y)**2))**0.5


agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, size, agents))

# Move the agents.
for j in range(num_of_iterations):
    random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)


#matplotlib.pyplot.xlim(0, 99)
#matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

# for agents_row_a in agents:
#     for agents_row_b in agents:
#         distance = distance_between(agents_row_a, agents_row_b)

#choose arbitrarily any agent to find the updated environment
#we will choose agent[0]
#t
outfile = open('outfile.txt', 'w')
for line in environment:
    for value in line:
        outfile.write(str(value))
        outfile.write(', ')
outfile.close()


for agent in agents:
    print(agent)


