import pandas as pd
import matplotlib.pyplot as plt
import os


df = pd.read_csv("data/steam_free_vs_paid.csv")
df

os.makedirs("figures", exist_ok=True)

plt.figure(figsize=(8, 5))
plt.bar(df['game_type'], df['avg_players'], color=['skyblue', 'orange'])
plt.title("Average Daily Players of Free and Paid Games")
plt.ylabel("Average Daily Players")
plt.tight_layout()
plt.savefig("figures/free_vs_paid_players.png")
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(df['game_type'], df['avg_rating'], color=['lightgreen', 'salmon'])
plt.title("Average Ratings of Free and Paid Games")
plt.ylabel("Average Rating")
plt.ylim(0, 10)  # Rating 10 üzerinden olduğu için
plt.tight_layout()
plt.savefig("figures/free_vs_paid_rating.png")
plt.show()