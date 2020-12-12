import matplotlib.pyplot as plt
import numpy as np

years = [1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1994,1998,2002,2006,2010,2014]

city = ['Albertville','Calgary','Chamonix','Cortina d Ampezzo','Garmisch Partenkirchen','Grenoble','Innsbruck','Lake PLacid','Lillehammer','Nagano','Oslo','Salt Lake City','Sapporo','Sarajevo','Sochi','Squaw Valley','St. Moritz','Turin','Vancouver']

medals = [37,6,9,20,13,20,10,22,40,49,17,75,1,4,90,21,32,68,91]

explode = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.2,0,0,0,0.4]

colors = ["#E74C3C","#2ECC71","#2E86C1","#F4D03F","#F39C12","#5B2C6F","#17202A","#884EA0","#2980B9","#2980B9","#48C9B0","#F9E79F","#EDBB99","#D7BDE2","#F2D7D5","#808B96","#D4EFDF","#C39BD3","#B2BABB"]



fig, ax1 = plt.subplots(figsize = (24,12))

ax1.pie(medals, startangle=0, shadow=True, colors = colors, explode=explode)
ax1.legend(city, loc ="upper right")


plt.title("Medals earned by different Cities \n in Canada", fontsize = 18, pad = "20")
plt.show()