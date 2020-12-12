import matplotlib.pyplot as plt 

labels = ['USA','Canada','Norway','Finland','Soviet Union']
values = [653,625,457,434,434]
colors = ['red','green','blue','yellow','orange']
explode = [0,0.2,0,0,0]
fig, ax1 = plt.subplots(figsize = (24,12))

ax1.pie(values, startangle=-90, autopct=lambda p:f'{p:.2f}%({p*sum(values)/100 :.0f})', explode=explode, shadow=True, colors=colors)
plt.title("Canada vs Top 5 Countries", fontsize = 18)
ax1.legend(labels, loc ="upper right")
plt.show()