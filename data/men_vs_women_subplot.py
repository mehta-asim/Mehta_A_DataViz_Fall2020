import matplotlib.pyplot as plt


years = ['Bronze','Silver','Gold']
men_medals = [66,128,192]
# bronze_medals = [0,0,5,0,2,1,18,1,1,18,1,1,1,4,3,5,7,15,11,8,5]
# silver_medals = [0,0,1,13,0,0,2,17]

women_medals = [41,75,123]
labels = ['Total','Bronze','Silver','Gold']

plt.subplot(1,2,1)
plt.plot(years, men_medals, linewidth=3.0, color=(51/255, 255/255, 255/255), marker='X', ms= 10, mfc = '#ffff33', mec = 'b')
plt.title("Men", fontsize = 18, pad = "20")
plt.ylabel("Total Medals won in Number", fontsize=15)
plt.xlabel("Type of Medal", fontsize=15)
plt.subplot(1,2,2)
plt.plot(years,women_medals, linewidth=3.0, color=(255/255, 255/255, 51/255), marker='X', ms= 10, mfc = '#ffff33', mec = 'b')
plt.title("Women", fontsize = 18, pad = "20")
plt.suptitle("Canadian Men vs Women in Winter Olympics \n from 1924-2014", fontsize = 18)
plt.show()