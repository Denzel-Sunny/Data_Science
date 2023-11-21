import matplotlib.pyplot as plt

#data
modes_of_transport = ["Walking", "Cycling", "Car", "Bus", "Train"]
frequency = [29, 15, 35, 18, 3]

plt.xlabel('Mode of Transport')
plt.ylabel('Frequency')
plt.title('Primary Mode of Transport to School')

plt.bar(modes_of_transport, frequency, width=0.1, color='green')

plt.show()
