import statistics
import random
import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
data  = df["temp"].tolist()

dataset = []
for i in range(0, 100):
    random_index = random.randint(0, len(data))
    value = data[random_index]
    dataset.append(value)

mean = statistics.mean(dataset)
std_dev = statistics.stdev(dataset)

print("Mean", mean)
print("Standard Deviation", std_dev)

def random_set_of_mean(counter):
    dataset = []
    for i in range(counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(mean_list)
    print("Mean of Sampling Distribution is", mean)
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()

def setup():
    mean_list = []
    for i in range(0, 1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print("Mean of Sampling Distribution is", mean)

setup()

population_mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print("Mean is", population_mean)
print("Standard deviation is", std_deviation)

fig = ff.create_distplot([data], ["temp"], show_hist=False)
fig.show()

def standard_deviation():
    mean_list = []
    for i in range(0, 1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    std_deviation = statistics.stdev(mean_list)
    print("Standard Deviation of Sampling Distribution is", std_deviation)

standard_deviation()