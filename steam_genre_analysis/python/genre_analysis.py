import pandas as pd
import matplotlib.pyplot as plt
import os


os.makedirs("figures", exist_ok=True)


df = pd.read_csv("data/genre_analysis.csv")
df

os.makedirs("figures", exist_ok=True)

plt.figure(figsize=(10, 6))
scatter = plt.scatter(
    df['avg_rating'],
    df['avg_players'],
    s=df['number_of_games'] * 100,
    alpha=0.7,
    c='skyblue',
    edgecolors='black'
)

for i, row in df.iterrows():
    plt.text(row['avg_rating'] + 0.02, row['avg_players'], row['genre'], fontsize=9)

plt.title("Game Genres: Rating vs Daily Players")
plt.xlabel("Average Rating")
plt.ylabel("Average Daily Players")
plt.grid(True)
plt.tight_layout()
plt.savefig("figures/genre_rating_vs_players.png")
plt.show()





plt.figure(figsize=(10, 6))
plt.bar(df['genre'], df['avg_players'], color='mediumslateblue')
plt.xticks(rotation=45, ha='right')
plt.title("Average Daily Players of Game Genres")
plt.xlabel("Genre")
plt.ylabel("Average Daily Players")
plt.tight_layout()
plt.savefig("figures/genre_avg_players_bar.png")
plt.show()