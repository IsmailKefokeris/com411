#operators

print ("Enter the number of lives.")
lives = int(input())

print ("Enter the energy level.")
energy = int(input())

print ("Enter the shield level.")
shield = int(input())


print ("Health set: Lives {}, Energy {}, Shield {}".format(lives,energy,shield))

print ("Lives: "," ❤ " * lives)
print ("Energy: "," ✺ " * energy)
print ("Shields: "," ❂ " * shield)