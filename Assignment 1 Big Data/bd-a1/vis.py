import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------
data = pd.read_csv("res_dpre.csv")
#------------------------------------

plt.figure(figsize=(8, 6))
plt.scatter(data['x'], data['y'])
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")

plt.savefig("vis.png")
plt.close()