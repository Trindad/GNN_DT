import networkx as nx
import matplotlib.pyplot as plt
import datanetAPI
reader = datanetAPI.DatanetAPI('/home/silvana/GNN_challenge/datanetAPI-challenge2021/dataset/gnnet-ch21-dataset-train',
            [], [])
it = iter(reader)
# for sample in it:
#   <process sample code>
n = 2
for i in range(n):
    sample = next(it)
    # print(sample.maxAvgLambda)
    G = sample.topology_object
    nx.draw(G, with_labels=True)
    plt.show()