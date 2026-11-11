import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('rand\coding\students.csv')
ex = df[df["Score"] > 80]["Course"].value_counts()

ex.plot(kind="bar")
plt.show()

print(ex)

__quit__ = True

while __quit__:
    ans = input("Choose Column > ")

    # asks if answer is a column
    if ans in df.columns:
        # if the list of unique values in a column is over the length of 5 then it will be sorted and only show the first and last five values
        if len(df[ans].unique()) > 5:
            output = df[ans].sort_values(ascending=False)
        else:
            output = df[ans].value_counts()
            
    # if columns is the answer then the columns will be shown
    elif ans == "Columns":
        output = df.columns

    else:
        __quit__ = False

    print(output)