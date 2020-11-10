import matplotlib.pyplot as plt


def load_temp_data():
    temps = [10, 20, 18, 19, 5]
    return temps

def load_moist_data():
    moist = [20,40,30,15,12]
    return moist

def display(data):
    plt.plot(data[0], "r")
    plt.step(data[1], "*--")
    plt.show()

def save(data):
    with open("visual/plots/output.txt", "w") as file:
        temps = data[0]
        moist = data[1]
        for temp in temps:
            file.write(f"{temp}, ")
        
        file.write("\n")

        for m in moist:
            file.write(f"{m}, ")

temp = load_temp_data()
moist = load_moist_data()


display([temp, moist])
save([temp, moist])