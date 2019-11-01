import matplotlib.pyplot as plt
import pandas as pd

fig, ax = plt.subplots(ncols=2,nrows=2,figsize=(8,8))
df=pd.read_csv("train.csv")

df1=df[(df["Sex"] == "male")]
x=df1["Age"]
y=df1["SibSp"]
ax[0,0].plot(x,y,"o")
ax[0,0].set_title("Male SibSp")
ax[0,0].set_xlabel("Age")
ax[0,0].set_ylabel("Number of Sibling/Spouse")
ax[0,0].set_xlim(-5,100)


df2=df[(df["Sex"] == "female")]
x=df2["Age"]
y=df2["SibSp"]
ax[0,1].plot(x,y,"o")
ax[0,1].set_title("Female SibSp")
ax[0,1].set_xlabel("Age")
ax[0,1].set_ylabel("Number of Sibling/Spouse")
ax[0,1].set_xlim(-5,100)

df3=df[(df["Sex"] == "male")]
x=df3["Age"]
y=df3["Parch"]
ax[1,0].plot(x,y,"o")
ax[1,0].set_title("Male Parch")
ax[1,0].set_xlabel("Age")
ax[1,0].set_ylabel("Number of Parents/Children")
ax[1,0].set_xlim(-5,100)
ax[1,0].set_ylim(-0.5,6.5)

df4=df[(df["Sex"] == "female")]
x=df4["Age"]
y=df4["Parch"]
ax[1,1].plot(x,y,"o")
ax[1,1].set_title("Female Parch")
ax[1,1].set_xlabel("Age")
ax[1,1].set_ylabel("Number of Parents/Children")
ax[1,1].set_xlim(-5,100)
ax[1,1].set_ylim(-0.5,6.5)

plt.subplots_adjust(hspace=0.5)
plt.subplots_adjust(wspace=0.5)
plt.show()