import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("performance.csv")
df = pd.DataFrame(data, columns = ["ratings"])

df.plot(figsize=(15, 6))
plt.show()