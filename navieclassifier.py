import pandas as pd
df = pd.read_csv("data.csv")
attributes = ["Age", "Income", "Student", "Credit_Rating"]
target = "Buys_Computer"
test = {}
for attribute in attributes:
    test[attribute] = input(f"Enter {attribute}: ")
classes = df[target].unique()
probabilities = {}
for c in classes:
    subset = df[df[target] == c]
    prob = len(subset) / len(df)
    for attribute in attributes:
        count = len(subset[subset[attribute] == test[attribute]])
        unique = df[attribute].nunique()
        prob *= (count + 1) / (len(subset) + unique)
    probabilities[c] = prob
print("\nClass Probabilities:")
for cls in probabilities:
    print(cls, ":", probabilities[cls])
prediction = max(probabilities, key=probabilities.get)
print("\nPredicted Class:", prediction)