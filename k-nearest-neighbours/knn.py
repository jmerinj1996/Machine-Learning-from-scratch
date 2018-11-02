# K nearest neighbours
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from math import sqrt

#Counter is to get the most popular votes
from collections import Counter

style.use('fivethirtyeight')

#Define a dataset
dataset = {'c':[[1,5],[3,4],[2,1]], 'b':[[8,5],[8,7],[7,6]]}

def k_nearest_neighbors(data, predict, k = 3):
    distances = []
    sorted_distances = []
    for label in data:
        for feature in data[label]:
            euclidean_distance = np.sqrt(np.sum((np.array(feature)-np.array(predict))**2))
            distances.append([euclidean_distance,label])
    for i in sorted(distances)[:k]:
        sorted_distances.append(i[1])
    result = Counter(sorted_distances).most_common(1)[0][0]
    return result
predict = [5,7]
prediction = k_nearest_neighbors(dataset, predict)
print('Predict:', predict)
print('Class:', prediction)

#Visualization
[[plt.scatter(j[0],j[1],s = 100, color = i) for j in dataset[i]] for i in dataset]
plt.scatter(predict[0],predict[1],s=200, marker = '*', color = prediction)
plt.show()
