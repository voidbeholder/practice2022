import numpy as np
data = np.genfromtxt('sample.csv', delimiter = ',', skip_header = 1)

std = data.std(axis = 1, keepdims=True)
means = data.mean(axis = 1, keepdims=True)

inds = []
stds = []
mns = []

for num, j in enumerate(std):
    if int(j) < 250:
        inds.append(num)
        stds.append(j.tolist())
        # print(num, np.round(j, 2))

for ind, k in enumerate(means):
    if ind in inds:
        mns.append(k.tolist())    
        # print(ind, np.round(k, 2))

#решейпнули индексы, чтобы обмануть vstack
inds_arr = np.array(inds)
newinds = np.reshape(inds_arr, (-1, 1))

final = np.hstack([newinds, mns, stds])

np.savetxt('output.txt', final, fmt = '%.2f', delimiter=', ')
