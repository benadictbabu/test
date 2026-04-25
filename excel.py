import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
print(df)

plt.bar(df["Name"],df["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Graph")
plt.show()  
# plt.pie(df["Marks"], labels=df["Name"])

plt.scatter(df["Name"], df["Marks"])

plt.show()