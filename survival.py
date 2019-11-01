
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("train.csv")

df1=df[(df["Sex"]=='male') & (df["Age"]<10) & (df["Survived"]==1)]
df2=df[(df["Sex"]=='female') & (df["Age"]<10) & (df["Survived"]==1)]

df3=df[(df["Sex"]=='male') & (df["Age"]>=10) & (df["Age"]<20) & (df["Survived"]==1)]
df4=df[(df["Sex"]=='female') & (df["Age"]>=10) & (df["Age"]<20) & (df["Survived"]==1)]

df5=df[(df["Sex"]=='male') & (df["Age"]>=20) & (df["Age"]<30) & (df["Survived"]==1)]
df6=df[(df["Sex"]=='female') & (df["Age"]>=20) & (df["Age"]<30) & (df["Survived"]==1)]

df7=df[(df["Sex"]=='male') & (df["Age"]>=30) & (df["Age"]<40) & (df["Survived"]==1)]
df8=df[(df["Sex"]=='female') & (df["Age"]>=30) & (df["Age"]<40) & (df["Survived"]==1)]

df9=df[(df["Sex"]=='male') & (df["Age"]>=40) & (df["Age"]<50) & (df["Survived"]==1)]
df10=df[(df["Sex"]=='female') & (df["Age"]>=40) & (df["Age"]<50) & (df["Survived"]==1)]

df11=df[(df["Sex"]=='male') & (df["Age"]>=50) & (df["Age"]<60) & (df["Survived"]==1)]
df12=df[(df["Sex"]=='female') & (df["Age"]>=50) & (df["Age"]<60) & (df["Survived"]==1)]

df13=df[(df["Sex"]=='male') & (df["Age"]>=60) & (df["Age"]<70) & (df["Survived"]==1)]
df14=df[(df["Sex"]=='female') & (df["Age"]>=60) & (df["Age"]<70) & (df["Survived"]==1)]

df15=df[(df["Sex"]=='male') & (df["Age"]>=70) & (df["Age"]<80) & (df["Survived"]==1)]
df16=df[(df["Sex"]=='female') & (df["Age"]>=70) & (df["Age"]<80) & (df["Survived"]==1)]

df17=df[(df["Sex"]=='male') & (df["Age"]>=80) & (df["Age"]<90) & (df["Survived"]==1)]
df18=df[(df["Sex"]=='female') & (df["Age"]>=80) & (df["Age"]<90) & (df["Survived"]==1)]

df19=df[(df["Sex"]=='male') & (df["Age"]>=90) & (df["Age"]<100) & (df["Survived"]==1)]
df20=df[(df["Sex"]=='female') & (df["Age"]>=90) & (df["Age"]<100) & (df["Survived"]==1)]

x=[10,20,30,40,50,60,70,80,90,100]

Male=[len(df1["Survived"]),len(df3["Survived"]),len(df5["Survived"]),len(df7["Survived"]),
      len(df9["Survived"]),len(df11["Survived"]),len(df13["Survived"]),len(df15["Survived"]),
      len(df17["Survived"]),len(df19["Survived"])]

Female=[len(df2["Survived"]),len(df4["Survived"]),len(df6["Survived"]),len(df8["Survived"]),
      len(df10["Survived"]),len(df12["Survived"]),len(df14["Survived"]),len(df16["Survived"]),
      len(df18["Survived"]),len(df20["Survived"])]
width = 2

plt.bar([elem - width/2 for elem in x],Male,width,label="Male")

plt.bar([elem + width/2 for elem in x],Female, width, label="Female")
plt.title("Survival by Age and Gender")
plt.xlabel("Age")
plt.ylabel("Count")
plt.xticks([10,20,30,40,50,60,70,80,90,100])
plt.legend(loc='best')
plt.show()