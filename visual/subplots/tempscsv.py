import matplotlib.pyplot as plt
import csv

def read_data():
    
    dic = {}
    with open("visual/subplots/temps.csv") as csvfile:

        csv_reader = csv.reader(csvfile, delimiter=',')
        header = next(csv_reader)

        dic = {
            header[0].strip():[]
            header[1].strip():[]
        }

        for row in csv_reader:
            dic[header[0]].append(row[0].strip())
            dic[header[1]].append(row[1].strip())
            

    dic["week1"] = week1
    dic["week2"] = week2

    return dic


def run():
    data = read_data()

    fig, axs = plt.subplots(2, 1, sharex="all")

    for index in range(len(data)):
        axs[index].plot