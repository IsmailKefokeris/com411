

def gang():
    print ("Loading Gang...")
    friends = []
    friends.append("Scooby Doo")
    friends.append("Shaggy Rogers")
    friends.append("Fred Jones")
    friends.append("Daphne Blake")
    friends.append("Velma Dinkley")
    
    print (friends)
    print ("...Done!")
    return friends

def phrases(list):
    quotes = {}
    
    for friend in list:
        print (f"What does {friend} say?")
        quote = input()
        quotes[friend] = quote
    
    return quotes

def save(quotes):
    
    with open("data/files/miniassessment2quotes.txt", "w") as file:
        
        for key, value in quotes.items():
            file.write(f"{key}: {value} \n")

friends = gang()
quotes = phrases(friends)
print(f"\nPhrases: {quotes}\n") 

save(quotes) 
print("The file contains...")
file = open("quotes.txt")
print(file.read())
file.close()
            