import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

def animate(i):
    df_trump = pd.read_csv('data_trump.csv')
    df_biden = pd.read_csv('data_biden.csv')
    positive_count_trump = len(df_trump[df_trump['trump_sentiment'] == 'positive'])
    negative_count_trump = len(df_trump[df_trump['trump_sentiment'] == 'negative'])
    neutral_count_trump = len(df_trump[df_trump['trump_sentiment'] == 'neutral'])

    positive_count_biden = len(df_biden[df_biden['biden_sentiment'] == 'positive'])
    negative_count_biden = len(df_biden[df_biden['biden_sentiment'] == 'negative'])
    neutral_count_biden = len(df_biden[df_biden['biden_sentiment'] == 'neutral'])
    y1 = positive_count_trump
    y2 = negative_count_trump
    y3 = neutral_count_trump
    y4 = positive_count_biden
    y5 = negative_count_biden
    y6 = neutral_count_biden
    plt.cla()

    # Use bar graph instead of plot
    plt.bar('positive_trump', y1, label='positive_trump')
    plt.bar('negative_trump', y2, label='negative_trump')
    plt.bar('neutral_trump', y3, label='neutral_trump')
    plt.bar('positive_biden', y4, label='positive_biden')
    plt.bar('negative_biden', y5, label='negative_biden')
    plt.bar('neutral_biden', y6, label='neutral_biden')


    plt.legend(loc='upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.show()
