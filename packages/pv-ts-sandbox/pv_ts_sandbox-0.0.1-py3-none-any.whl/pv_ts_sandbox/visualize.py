import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MaxNLocator
import matplotlib.dates as mdates
import seaborn as sns
import missingno as msno
import joypy
import calendar
from .preprocess import add_month, add_year

# Produce a plot based on user selected variable
def plot_var_vs_time(df, col, title=""):
    if col in df.columns:
        xlabel='TIMESTAMP'
        ylabel=col
        x = df['TIMESTAMP']
        y = df[col]
        plt.plot(x, y, color='tab:red')
        plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
        hfmt = mdates.DateFormatter('%Y-%m-%d %H:%M:%S')
        plt.gca().xaxis.set_major_formatter(hfmt)
        plt.gcf().autofmt_xdate()
        plt.show()

# Produce a ridgeline plot based on user selected variable
def plot_var_month_ridgeline(df, col):
    if 'Month' not in df.columns:
        add_month(df)

    if col in df.columns:
        fig, axes = joypy.joyplot(data=df, column=col, by='Month', xlabels=col, ylabels= 'Month of Year')
        plt.show()

# Produce a Year / Month heatmap for user selected variable
def plot_var_heatmap(df, col):
    if 'Year' not in df.columns:
         add_year(df)
    if 'Month' not in df.columns:
        add_month(df)

    if col in df.columns:
        all_month_year_df = pd.pivot_table(df, values=col,
                                    index=["Month"],
                                    columns=["Year"],
                                    fill_value=0,
                                    margins=True)
        named_index = [[calendar.month_abbr[i] if isinstance(i, int) else i for i in list(all_month_year_df.index)]] # name months
        all_month_year_df = all_month_year_df.set_index(named_index)
        print(all_month_year_df.head())
        ax = sns.heatmap(all_month_year_df, cmap='RdYlGn_r',
                    robust=True,
                    fmt='.2f',
                    annot=True,
                    linewidths=.5,
                    annot_kws={'size':11},
                    cbar_kws={'shrink':.8,
                            'label':col})                       
        
        ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=10)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=0, fontsize=10)
        plt.title('Average '+col, fontdict={'fontsize':18})
        plt.show()


# Produce bar graph with count of values present per columns, ignoring missing values
def plot_missing_bar(df):
    msno.bar(df=df)
    plt.show()