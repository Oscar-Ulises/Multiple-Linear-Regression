import numpy as np
from sklearn.linear_model import LinearRegression
from math import ceil

F,N = list(map(int,input().split()))
features = []
target = []
for n in range(N):
    value = list(map(float,input().split()))
    target.append(value[-1])
    feature = []
    for f in range(F):
        feature.append(value[f])
    features.append(feature)

features = np.array(features)
target = np.array(target)
    
regression = LinearRegression()
model = regression.fit(features,target)

T = int(input())
for _ in range(T):
    new_value = list(map(float,input().split()))
    number = model.predict([new_value])[0]
    print( ceil(number * 100) / 100.0 )
