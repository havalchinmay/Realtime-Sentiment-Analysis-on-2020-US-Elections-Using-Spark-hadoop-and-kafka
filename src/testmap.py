import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from matplotlib.animation import FuncAnimation
import matplotlib.colors as mcolors

# Load initial data
data_trump = pd.read_csv('data_trump.csv')
data_biden = pd.read_csv('data_biden.csv')
data_trump = data_trump.drop(columns=['batch', 'trump_tweet'])
data_biden = data_biden.drop(columns=['batch', 'biden_tweet'])

pd.set_option('future.no_silent_downcasting', True)
data_trump = data_trump[data_trump['state'] != 'Puerto Rico']
data_biden = data_biden[data_biden['state'] != 'Puerto Rico']
data_trump['trump_sentiment'] = data_trump['trump_sentiment'].replace({'positive': 1, 'negative': -1, 'neutral': 0})
data_biden['biden_sentiment'] = data_biden['biden_sentiment'].replace({'positive': -1, 'negative': 1, 'neutral': 0})

data_trump = data_trump.groupby('state').sum()
data_biden = data_biden.groupby('state').sum()

merged_df = data_trump.merge(data_biden, on='state', how='inner')
merged_df['total_sentiment'] = merged_df['trump_sentiment'] + merged_df['biden_sentiment']
merged_df = merged_df.drop(columns=['biden_sentiment', 'trump_sentiment'])

us_map = gpd.read_file('US 50 States Boundaries Shapefile_20240421.zip')
us_map = us_map.drop(columns=['drawseq', 'state_fips', 'sub_region', 'state_abbr'])
merge_df = us_map.join(merged_df, on='state_name', how='right')

def custom_color_map(value):
    if value >= 0:
        color = mcolors.to_hex(plt.cm.Reds(value / 2))
    else:
        color = mcolors.to_hex(plt.cm.Blues(-value / 2))
    return color

merge_df['color'] = merge_df['total_sentiment'].apply(custom_color_map)

# Setup the initial plot
fig, ax = plt.subplots()
ax.set_axis_off()
plt.tight_layout()

# Function to update the plot
def update(frame):
    ax.clear()
    ax.set_axis_off()

    # Update data
    data_trump = pd.read_csv('data_trump.csv')
    data_biden = pd.read_csv('data_biden.csv')
    data_trump = data_trump.drop(columns=['batch', 'trump_tweet'])
    data_biden = data_biden.drop(columns=['batch', 'biden_tweet'])

    pd.set_option('future.no_silent_downcasting', True)
    data_trump = data_trump[data_trump['state'] != 'Puerto Rico']
    data_biden = data_biden[data_biden['state'] != 'Puerto Rico']
    data_trump['trump_sentiment'] = data_trump['trump_sentiment'].replace({'positive': 1, 'negative': -1, 'neutral': 0})
    data_biden['biden_sentiment'] = data_biden['biden_sentiment'].replace({'positive': -1, 'negative': 1, 'neutral': 0})

    data_trump = data_trump.groupby('state').sum()
    data_biden = data_biden.groupby('state').sum()

    merged_df = data_trump.merge(data_biden, on='state', how='inner')
    merged_df['total_sentiment'] = merged_df['trump_sentiment'] + merged_df['biden_sentiment']
    merged_df = merged_df.drop(columns=['biden_sentiment', 'trump_sentiment'])

    merge_df = us_map.join(merged_df, on='state_name', how='right')

    merge_df['color'] = merge_df['total_sentiment'].apply(custom_color_map)

    # Plot the updated map
    merge_df.plot(
        ax=ax,
        legend=True,
        cmap='RdBu_r',
        color=merge_df['color'],
        edgecolor='black',
        linewidth=0.4
    )
    ax.set_title('Live US Election Map', fontdict={'fontsize': 20}, pad=15)

# Create animation
ani = FuncAnimation(fig, update, frames=1000, interval=2000)

# Show the plot
plt.show()
