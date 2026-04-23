import pandas as pd
data = {
    "students" : ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"],
 "marks" : [85, 92, 78, 90, 88, 95, 80, 91, 89, 94]
}
df = pd.DataFrame(data)
print(df)
print(df.loc[[2,4]])