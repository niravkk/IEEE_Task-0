import numpy as np
scores = np.array([70, 91, 58, 87, 76])
hours = np.array([4.5, 10, 2, 6, 7.3])
preScores = np.array([70, 95, 83, 100, 67, 76])
attendance = np.array([85, 23, 44, 100, 78])

print(np.shape(scores))    
print("Mean score: ", np.mean(scores))
print("Max score: ", np.max(scores))
print("Min score: ", np.min(scores))
print("Standard deviation: ", np.std(scores))
np.add(scores, 5)
boolArray = scores>=75
print(boolArray)
print(scores[boolArray])