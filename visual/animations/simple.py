import matplotlib.pyplot as plt
import matplotlib.animation as animation
data = None
fig, ax = plt.subplots()

def init():
    data = {
        "x":[3,3, 4,4,3], 
        "y":[3,4, 4,3,3]
    }

def animate(frame):
    ax.cla() # clears axis
    ax.set_xlim(0,10)
    ax.set_ylim(0,10)
    ax.plot(frame, frame, "ro")

def run():
    simp_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 1000, init_func=init)

    plt.show()

run()