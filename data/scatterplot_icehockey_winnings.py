import matplotlib.pyplot as plt
import numpy as np

years = [1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1994,1998,2002,2006,2010,2014]

medals = [9,12,14,13,17,16,17,17,0,18,0,0,0,0,0,23,23,20,43,19,44,46]

colors = np.random.randint(100, size=(22))
sizes = 10 * np.random.randint(100, size=(22))

plt.scatter(years,medals, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
plt.colorbar()
plt.title("Medals earned in Ice Hockey \n by Canada", fontsize = 18, pad = "20")
plt.ylabel("Number of Medals Won", fontsize=15)
plt.xlabel("Years Participated", fontsize=15)
plt.show()