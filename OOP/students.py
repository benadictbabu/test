import matplotlib.pyplot as plt
import numpy as np
students = ["John", "Jane", "Doe", "Smith","bob"]
marks = [75,85, 90,78,95]
plt.plot(students, marks)
plt.show()
plt.bar(students, marks)
plt.show()
plt.pie(marks, labels=students)
plt.show()