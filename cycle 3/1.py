import matplotlib.pyplot as plt
import numpy as np
# Data for x and y axis
year = np.array([2001, 2002, 2003, 2004, 2005, 2006, 2007])
value = np.array([24000, 22500, 19700, 17500, 14500, 10000, 5800])

#define graph characteristics
plt.plot(year, value, marker = "*", linestyle='-.', color='red',  markersize=20, markerfacecolor='green')


#name axis
plt.title("Value Depreciation", loc='left')
plt.xlabel("year")
plt.ylabel("value")

#show graph
plt.show()
