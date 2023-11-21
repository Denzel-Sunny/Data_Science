import matplotlib.pyplot as plt
import numpy as np

#data
Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
affordable_segment = [173, 153, 195, 147, 120, 144, 148, 109, 174, 130, 172, 131]
luxury_segment = [189, 189, 105, 112, 173, 109, 151, 197, 174, 145, 177, 161]
super_luxury_segment = [185, 185, 126, 134, 196, 153, 112, 133, 200, 145, 167, 110]

plt.title("Sales Data")
plt.xlabel("months of year", fontsize=18)
plt.ylabel("Sales of Segments")

#plots for different segments
plt.scatter(Months, luxury_segment, color='yellow', label='Luxury', s=100)
plt.scatter(Months, super_luxury_segment, color='blue', label='Super Luxury', s=100)
plt.scatter(Months, affordable_segment, color='pink', label='Affordable')

plt.legend()

plt.show()
