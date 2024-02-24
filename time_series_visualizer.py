import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',parse_dates = ["date"],index_col = "date")


print(df.head())

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))]

# print("after:", df.shape)
# print(df.head())

def draw_line_plot():
    # Draw line plot

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df.index, df['value'], color='r')

    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['year'] = df.index.year
    df['month'] = df.index.month
    df_bar = df.groupby(['year','month'])['value'].mean().unstack()

    # Create bar plot using Seaborn
    fig = df_bar.plot.bar(legend= True,figsize=(10,5),ylabel = "Average Page Views",xlabel='Years').figure

    plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    df_box["month_num"] = df_box['date'].dt.month
    df_box = df_box.sort_values("month_num")

    fig, axes = plt.subplots(nrows=1,ncols = 2,figsize=(15,5))
    axes[0] = sns.boxplot(x=df_box['year'],y=df_box['value'],ax=axes[0])
    axes[1] = sns.boxplot(x=df_box['month'],y=df_box['value'],ax=axes[1])

    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
