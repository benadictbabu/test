import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("marks.csv")

print(df)
plt.pie(  df["total marks"],labels=df["name"], autopct='%1.1f%%')
plt.title("Student Marks Pie Chart")
plt.show()
plt.bar(df["name"], df["total marks"],df["average marks"])
plt.show()