import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
import tkinter
import random
import operator
import matplotlib.pyplot
import matplotlib.animation
import agentframeworkfinal
import csv
import sys
import requests
import bs4

def read_environment():
    """
    This function reads the environment from our "in.txt" file, which should 
    have the same amount of rows as columns.

    Returns
    -------
    envir : list
        A 2D list where each (y,x) entry represents the amount of resources 
        in that coordinate.

    """
    envir = []
    #note that "in.txt" needs to be a square matrix (same number of rows as cols)
    f = open('in.txt', newline='')
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader: # A list of rows
        rowlist = []
        for value in row: # A list of value
            rowlist.append(value)
        envir.append(rowlist)
    f.close() # Don't close until you are done with the reader;
            # the data is read on request.
    print("Loading environment...")
    return envir

def initialise_agents(num_of_agents, environment):
    """
    Fishes initial starting positions of our agents by scarping web data.
    Initialises our agents model.

    Parameters
    ----------
    num_of_agents : int
        Number of agents in our simulation.
    environment : list
        2D list representing amount of resources in our environment.

    Returns
    -------
    agents : list of Agent()
        List of our initialised agents with their starting positions.

    """
    r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
    content = r.text
    soup = bs4.BeautifulSoup(content, 'html.parser')
    td_ys = soup.find_all(attrs={"class" : "y"})
    td_xs = soup.find_all(attrs={"class" : "x"})

    agents = []
    # Make the agents.
    for i in range(num_of_agents):
        #note here that we multiply the scraped values by 3 since they are 
        #limited to a 100 by 100 grid, whereas we have a 300 by 300 grid.
        y = int(td_ys[i].text) * 3 
        x = int(td_xs[i].text) * 3
        agents.append(agentframeworkfinal.Agent(environment, agents, x, y))
    print("Initialising Agents...")
    return agents


def interaction(agents, neighbourhood):
    """
    Agents are shuffled to remove regularity error.
    They then nteract with the environment and each other (move, eat and share
    resources).

    Parameters
    ----------
    agents : list of Agent()

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

def gen_function(b = [0]):
    """
    Generator function to be used with Funcanimation.

    Parameters
    ----------
    b : TYPE, optional
        DESCRIPTION. The default is [0].

    Yields
    ------
    TYPE
        DESCRIPTION.

    """
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on): #stopping condition AND limited number of iterations (a gives limited number of iter)
        yield a			# Returns control and waits next call.
        a = a + 1

def update(frame_number):   
    """
    Function to be used with Funcanimation. Updates each frame.

    Parameters
    ----------
    frame_number : int
        Frame number, goes up to however many iterations we allow.

    Returns
    -------
    None.

    """
    global carry_on
    fig.clear()
    matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.ylim(0, len(environment))
    matplotlib.pyplot.xlim(0, len(environment))
    
    #make our agents interact with each other and evironment
    interaction(agents, neighbourhood)   
   
    #stopping condition
    if average_2D(environment) < 100: #if average level of grass falls below 100
        carry_on = False
        print("Stopping condition")
    else:
        pass
    
    for agent in agents:
        # print(agent)
        matplotlib.pyplot.scatter(agent.x, agent.y, c = 'red')
        
def print_agent():
    """
    Print state of agents.

    Returns
    -------
    None.

    """
    for agent in agents:
        print(agent)

def run():
    """
    Animates our agents' moving in the environment, which is also visually 
    represented.

    Returns
    -------
    None.

    """
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()
      
def exit_gui():
    """
    Closes GUI window and quits mainloop().

    Returns
    -------
    None.

    """
    root.quit()
    root.destroy()


def is_integer(n):
    """
    Find whether a string is an integer.

    Parameters
    ----------
    n : string
        Any string.

    Returns
    -------
    Bool
        Returns True if string is an integer.
        Returns False otherwise.

    """
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


if __name__ == "__main__":

    #define global parameters
    carry_on = True
    #default initial parameters
    NUM_OF_AGENTS = 10
    NUM_OF_ITERATIONS = 100
    NEIGHBOURHOOD = 20
    
    
    #read in the parameters from the command line
    #check that the user has inputted the right number of arguments to cmd line
    if len(sys.argv) == 4:
        arg1 = is_integer(sys.argv[1])
        arg2 = is_integer(sys.argv[2])
        arg3 = is_integer(sys.argv[3])

        if arg1:
            num_of_agents = int(sys.argv[1])
        else:
            print("Number of agents must be an integer. Using default values.")
            num_of_agents = NUM_OF_AGENTS
    
        if arg2:
            num_of_iterations = int(sys.argv[2])
        else:
            print("Number of iterations must be an integer. Using default values.")
            num_of_iterations = NUM_OF_ITERATIONS
    
        if arg3:
            neighbourhood = int(sys.argv[3])
        else:
                print("Neighbourhood must be an integer. Using default values.")
                neighbourhood = NEIGHBOURHOOD

    else:
        print("Incorrect number of arguments inputted. Using default values.")
        num_of_agents = NUM_OF_AGENTS
        num_of_iterations = NUM_OF_ITERATIONS
        neighbourhood = NEIGHBOURHOOD


    print("Loading initial parameters...")
    print("Number of agents =", num_of_agents)
    print("Number of iterations =", num_of_iterations)
    print("Neighbourhood =", neighbourhood)
    
    #initialise our model
    environment = read_environment()
    agents = initialise_agents(num_of_agents, environment)

    #gui part of the program
    #fig = Figure(figsize=(7,7))
    fig = matplotlib.pyplot.figure(figsize=(7, 7))
    # ax = fig.add_axes([0, 0, 1, 1])
    root = tkinter.Tk()
    root.wm_title("Model")
    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
    canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    menu_bar = tkinter.Menu(root)
    root.config(menu=menu_bar)
    model_menu = tkinter.Menu(menu_bar)
    menu_bar.add_cascade(label="Model", menu=model_menu)
    model_menu.add_command(label="Run model", command=run)
    model_menu.add_command(label="Print agents", command=print_agent)
    model_menu.add_command(label="Save environment data", command=save_data(environment))
    model_menu.add_separator()
    model_menu.add_command(label="Exit", command=exit_gui)

    #Note: need to keep empty fig window open for animation to work. Not sure how to fix this yet
    root.mainloop() # Wait for interactions.