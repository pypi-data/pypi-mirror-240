import pandas as pd
import seaborn as sns


def plot_null_values(df):
    total = len(df)
    null_values = df.isnull().mean() * 100
    null_values = null_values.sort_values(ascending=False)
    null_values = null_values[null_values > 0]
    if not null_values.empty:
        print(null_values.values)
        ax = sns.barplot(y=null_values.index, x=null_values.values)
        for i in ax.containers:
            ax.bar_label(i, labels=null_values.values*total/100, label_type='center', fmt='%d')
    else:
        print("No null values")