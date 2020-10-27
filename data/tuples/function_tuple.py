
def likelihood_min():
    likelihoods = (50, 38, 27, 99, 4)
    return (min(likelihoods))

def likelihood_max():
    likelihoods = (50, 38, 27, 99, 4)
    return (max(likelihoods))

def run():
    select = input("Max or Min: ")

    if ("max" in select):
        likely = likelihood_max()
        print ("Maximum Likelihood of falling: {}%".format(likely))
    elif ("min" in select):
        likely = likelihood_min()
        print ("Minimum Likelihood of falling: {}%".format(likely))
    elif ("both" in select):
        likelymin = likelihood_min()
        likelymax = likelihood_max()
        print ("Maximum Likelihood of falling: {}%".format(likelymax))
        print ("Minimum Likelihood of falling: {}%".format(likelymin))
    else:
        print("ERROR....Only enter the words Min or Max")
