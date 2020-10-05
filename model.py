import random
import operator
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv
import sys

 
# num_of_agents = sys.argv[0]
# num_of_iterations = sys.argv[1]
# neighbourhood = sys.argv[2]


def read_environment():
    #need to modify to make filename an argument
    #Read in file with environment data
    envir = []
    f = open('in.txt', newline='')
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader: # A list of rows
        rowlist = []
        for value in row: # A list of value
            rowlist.append(value)
        envir.append(rowlist)
    f.close() # Don't close until you are done with the reader;
            # the data is read on request.
    return envir


def initialise_agents(num_of_agents, environment):
    """
    Create our agents.

    Parameters
    ----------
    environment : 2D list
        Represents the environment of our agents. Number of rows must equal 
        the number of columns (square matrix).
    size : int
        Size/dimension of 2D list.

    Returns
    -------
    agents : list of Agent()
        List of Agent() class.

    """
    agents = []
    # Make the agents.
    for i in range(num_of_agents):
        agents.append(agentframework.Agent(environment, agents))
    return agents


def interaction(agents, neighbourhood):
    """
    Agents are shuffled to remove regularity error.
    They then nteract with the environment and each other (move, eat and share
    resources).

    Parameters
    ----------
    agents : list of Agent()
        DESCRIPTION.

    Returns
    -------
    None.

    """
    random.shuffle(agents)
    for agent in agents:
        agent.move()
        agent.eat()
        agent.share_with_neighbours(neighbourhood)


def average_2D(list):
    """
    Find the average of a 2D list.

    Parameters
    ----------
    list : list of lists (2D)
        Equivalent to a square array.

    Returns
    -------
    average : int
        Average value in list of lists.

    """
    av_rows = 0
    for row in list:
        av_rows += sum(row)/len(row)
    average = av_rows/len(list)
    return average
     
   
def animate_func(agents, environment, num_of_iterations, neighbourhood):
    fig = matplotlib.pyplot.figure(figsize=(7, 7))
    #ax = fig.add_axes([0, 0, 1, 1])
    
    def gen_function(b = [0]):
        a = 0
        global carry_on #Not actually needed as we're not assigning, but clearer
        while (a < num_of_iterations) & (carry_on): #stopping condition AND limited number of iterations (a gives limited number of iter)
            yield a			# Returns control and waits next call.
            a = a + 1
    
    def update(frame_number):    
        global carry_on    
        fig.clear()
        matplotlib.pyplot.imshow(environment)
        matplotlib.pyplot.ylim(0, len(environment))
        matplotlib.pyplot.xlim(0, len(environment))
        #matplotlib.pyplot.axis(xlim = (0,300), ylim = (0, 300))
        
        interaction(agents, neighbourhood)   
        
        # if average_2D(environment) < 100: #if average level of grass falls below 100
        #     carry_on = False
        #     print("stopping condition")
        # else:
        #     pass
        
        for agent in agents:
            #print(agent)
            matplotlib.pyplot.scatter(agent.y, agent.x, c = 'red')

    animation = matplotlib.animation.FuncAnimation(fig, update, frames=num_of_iterations, repeat=False)
    #matplotlib.pyplot.show()
    return animation
    
    
def save_data(env_list):
    """
    Save environment data to a .txt file after our simulation.

    Parameters
    ----------
    env_list : 2D list
        Environment data after our agents have interacted with it.

    Returns
    -------
    None.

    """
    outfile = open('outfile.txt', 'w')
    for line in env_list:
        for value in line:
            outfile.write(str(value))
            outfile.write(', ')
    outfile.close()


if __name__ == '__main__':
    #setting parameters
    carry_on = True
    num_of_agents = 10
    num_of_iterations = 100
    neighbourhood = 20
    
    
    #initialising our model
    environment = read_environment()
    agents = initialise_agents(num_of_agents, environment)
    
    #print(environment)
    for agent in agents:
        print(agent)
    

    print('\n')
    #interaction(agents, neighbourhood)    
    ani = animate_func(agents, environment, num_of_iterations, neighbourhood)
    matplotlib.pyplot.show(block = False)
    print('\n')

    for agent in agents:
        print(agent)
