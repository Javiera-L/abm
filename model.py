import random
import operator
import matplotlib.pyplot 

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5


num_of_agents = 10
num_of_iterations = 100
agents = []
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])
# y0, x0
print(agents)

for j in range(num_of_iterations):
    for i in range(num_of_agents):
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
        
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] +1) % 100
        else:
            agents[i][1] = (agents[i][1] -1) % 100


# Random walk one step.
# if random.random() < 0.5:
#     agents[0][0] += 1
# else:
#     agents[0][0] -= 1

# if random.random() < 0.5:
#     agents[0][1] += 1
# else:
#     agents[0][1] -= 1

# #agents.append([agents[0][0],agents[0][1]])

# agents.append([random.randint(0,99),random.randint(0,99)])


# # Random walk one step.
# if random.random() < 0.5:
#     agents[1][0] += 1
# else:
#     agents[1][0] -= 1

# if random.random() < 0.5:
#     agents[1][1] += 1
# else:
#     agents[1][1] -= 1

#agents.append([agents[1][0],agents[1][1]])

print(agents)
#coord = max(agents, key=operator.itemgetter(1))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)

for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])

#matplotlib.pyplot.scatter(coord[1],coord[0], color = 'red')

matplotlib.pyplot.show()

distance = distance_between(agents[0], agents[1])
print(distance)
# answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
# print(answer)