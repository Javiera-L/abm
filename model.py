import random
import operator
import matplotlib.pyplot
import agentframework
 

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + 
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent())

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        agents[i].move()

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)






# def distance_between(agents_row_a, agents_row_b):
#     return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5


# num_of_agents = 10
# num_of_iterations = 100
# agents = []
# for i in range(num_of_agents):
#     agents.append([random.randint(0,100),random.randint(0,100)])
# # y0, x0
# print(agents)

# for j in range(num_of_iterations):
#     for i in range(num_of_agents):
#         if random.random() < 0.5:
#             agents[i][0] = (agents[i][0] + 1) % 100
#         else:
#             agents[i][0] = (agents[i][0] - 1) % 100
        
#         if random.random() < 0.5:
#             agents[i][1] = (agents[i][1] +1) % 100
#         else:
#             agents[i][1] = (agents[i][1] -1) % 100


# print(agents)
# #coord = max(agents, key=operator.itemgetter(1))

# matplotlib.pyplot.ylim(0, 99)
# matplotlib.pyplot.xlim(0, 99)

# for i in range(num_of_agents):
#     matplotlib.pyplot.scatter(agents[i][1],agents[i][0])

# #matplotlib.pyplot.scatter(coord[1],coord[0], color = 'red')

# matplotlib.pyplot.show()

# for agents_row_a in agents:
#     for agents_row_b in agents:
#         distance = distance_between(agents_row_a, agents_row_b)

