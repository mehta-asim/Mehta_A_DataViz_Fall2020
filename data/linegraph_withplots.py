import matplotlib.pyplot as plt


years = [1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1994,1998,2002,2006,2010,2014]
total_medals = [9,12,20,13,20,17,20,21,7,20,1,3,2,4,6,37,40,49,75,68,91,90]


bronze_medals = [0,0,5,0,2,1,18,1,1,18,0,1,1,1,4,3,5,7,15,11,8,5]
silver_medals = [0,0,1,13,0,0,2,17,2,1,1,1,1,1,2,29,32,28,7,28,15,22]
gold_medals = [9,12,14,0,18,16,0,3,4,1,0,1,0,2,0,5,3,14,53,29,68,63]
labels = ['Total','Bronze','Silver','Gold']
fig, ax1 = plt.subplots(figsize = (24,12))


ax1.plot(years, total_medals, linewidth=3.0, color=(255/255, 51/255, 51/255), marker='o', ms= 10, mfc = 'w', mec = 'r')
ax1.plot(years,bronze_medals, linewidth=2.0, color=(255/255, 178/255, 102/255), marker='o', ms= 10, mfc = 'w', mec = '#cc6600')
ax1.plot(years,silver_medals, linewidth=2.0, color=(160/255, 160/255, 160/255), marker='o', ms= 10, mfc = 'w', mec = '#a0a0a0')
ax1.plot(years,gold_medals, linewidth=2.0, color=(249/255, 213/255, 71/255), marker='o', ms= 10, mfc = 'w', mec = '#F9D547')
ax1.legend(labels, loc ="upper left", prop={'size': 20})
plt.title("Canada's Performance in Winter Olympics \n from 1924-2014", fontsize = 18, pad = "20")
plt.ylabel("Total Medals won in Number", fontsize=15)
plt.xlabel("Perfomance by Year", fontsize=15)
plt.show()