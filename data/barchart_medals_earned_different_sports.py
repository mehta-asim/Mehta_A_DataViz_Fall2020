import matplotlib.pyplot as plt

sport = ['Biathlon','Bobsleigh','Curling','Ice Hockey','Skating','Skiing']

medals = [3,22,50,351,159,40]
colors = ['red','green','blue','yellow','orange','purple']



plt.barh(sport,medals,color=colors)
plt.title("Medals earned in Different Sports \n by Canada", fontsize = 18, pad = "20")
plt.ylabel("Sports participated in Olympics", fontsize=15)
plt.xlabel("Number of Medals Won", fontsize=15)
plt.show()