import pandas as pd
import numpy as np

S = pd.Series([11, 28, 72, 3, 5, 8])
print(S)

print(S.index)
print(S.values)



X = np.array([11, 28, 72, 3, 5, 8])
print(X)
print(S.values)
# both are the same type:
print(type(S.values), type(X))

fruits = ['apples', 'oranges', 'cherries', 'pears']
quantities = [20, 33, 52, 10]
S = pd.Series(quantities, index=fruits)
print(S)

fruits = ['apples', 'oranges', 'cherries', 'pears']
S = pd.Series([20, 33, 52, 10], index=fruits)
S2 = pd.Series([17, 13, 31, 32], index=fruits)
print(S + S2)
print("Summe aus S: ", sum(S))


fruits = ['peaches', 'oranges', 'cherries', 'pears']
fruits2 = ['raspberries', 'oranges', 'cherries', 'pears']
S = pd.Series([20, 33, 52, 10], index=fruits)
S2 = pd.Series([17, 13, 31, 32], index=fruits2)
print(S + S2)


#print(S['apples'])


#print(S[['apples', 'oranges', 'cherries']])

print(S > 30)

print(S[S > 30])

print(zip(S.tolist(), S.index))

print(np.sin(S))

def foo(x):
  if x > 50:
    return x
  else:
    return x+10
  
print(S.apply(foo))

S.apply(lambda x: x if x > 50 else x * 10)

