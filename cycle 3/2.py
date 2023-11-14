import matplotlib.pyplot as plt
import numpy as np

day = ["Mon", "Tue", "Wed", "Thurs", "Fri"]
drinks = np.array([300, 450, 150, 400, 650])
food = np.array([400, 500, 350, 300, 500])
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

#plot1
ax1.plot(day, drinks, linestyle='--', color='cyan', marker='h', markersize=10, markeredgecolor='black')
ax1.set_title("sales data1", loc='right')
ax1.set_xlabel("days of week")
ax1.set_ylabel("sale of drinks")

#plot2
ax2.plot(day, food, linestyle='--', color='yellow', marker='d', markersize=10, markeredgecolor='red')
ax2.set_title("sales data2", loc='center')
ax2.set_xlabel("days of week")
ax2.set_ylabel("sale of food")

plt.show()

