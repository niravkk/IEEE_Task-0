import pandas as pd
data = pd.read_csv("student_performance.csv", encoding = "utf-8")
print(data.head(6))
print("Rows: ",data.shape[0])
print("Columns: ", data.shape[1])
#.isna() replaces any missing data(NaN) with True
#.any() returns whether any element is True
print(data.isna().any())
#no missing data
print("Mean final score: ", data["Final_Score"].mean())
print("Maximum score: ", data["Final_Score"].max())

improvement = data["Final_Score"] - data["Previous_Score"]
data["Improvement"] = improvement

boolArray = data["Attendance"]>80
filtered = data[boolArray]
print(filtered)

data = data.sort_values(by=["Final_Score"], ascending = False)

data.to_csv("processed_student_performance.csv")