import matplotlib.pyplot as plt





def read_data(path):

    funlist = []

    with open(path) as file:

        temp = file.readlines()

        for line in temp:
            funlist.append(int(line.strip())) # using the .strip() function to remove unwanted space (which also created the \n shit...)
    
    return funlist


def run():
    #runs the previous function and stores the data inside a (local) variable called data...
    data = read_data("visual/subplots/temps.txt")
    print(data)
    # Creates a 2D list (axs) which is 2 rows and 2 columns big... we target each individual plotby "axs[0,0]" where the 0 is the position
    fig, axs = plt.subplots(1, 2, sharex='all') #Shareex = "all" allows for all the subplots to use the same axis...


    fig.set_size_inches(20,20)
    x = range(0, 7, 1)

    axs[0].plot(x, data)

    axs[1].bar(x, data)

    plt.show()

run()



