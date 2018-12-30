import numpy as np
import matplotlib.pyplot as plt


N = 9
menMeans = (20, 35, 30, 35, 27, 56, 34, 66, 21)
womenMeans = (25, 32, 34, 20, 25, 56, 32, 11, 78)

ind = np.arange(N)
width = 0.30

p1 = plt.bar(ind, menMeans, width, color ='red' )
p2 = plt.bar(ind, womenMeans, width,
             bottom=menMeans, color = 'blue' )

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9'))
plt.yticks(np.arange(0, 200,10))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()