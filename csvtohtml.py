import pandas as pd

b=input("Enter csvfile")
a=pd.read_csv(b)
a.tohtml(b)
htmlfile=a.tohtml()
print(htmlfile)
