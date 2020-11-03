import os

def search(Fname):
    print ("Searching....")
    sections = []
    books = []
    parts = None

    with open(Fname, "r") as file:
        for line in file:
            if line.startswith("Section:"):
                parts = line.split(":")
                sections.append(parts[1][:-1])
            else:
                books.append(line[:-1])
    
    both = (sections, books)
    print("Done!...")

    return both


def save(Fname, data):
    print("Saving....")

    with open(Fname, "w") as file:
        file.write("Sections: ")
        for sections in data[0]:
            file.write(str(sections) + ",")
        
        file.write("\nBooks: ")
        for books in data[1]:
            file.write(str(books) + ",")

    
    print("Done!")



def run():

    data = search("data/files/books.txt")
    save("data/files/section-books.txt", data)


run()
