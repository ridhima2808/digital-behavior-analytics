import pandas as pd
import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt
import os

# Create folder if it doesn't exist
os.makedirs('charts', exist_ok=True)

# Read CSV
df = pd.read_csv('digital_behaviour.csv')

# Calculate total social-media screen time
df['Total_Screen_Time'] = (
    df['Instagram_Minutes']
    + df['YouTube_Minutes']
    + df['LinkedIn_Minutes']
    + df['WhatsApp_Minutes']
)

# Create Day 1, Day 2, Day 3...
df['day_label'] = [f"Day {i+1}" for i in range(len(df))]


# -------------------------
# 1. Screen time per day
# -------------------------

plt.figure(figsize=(12, 6))

plt.bar(
    df['day_label'],
    df['Total_Screen_Time'],
    color='blue'
)

plt.title('Screen Time per Day')
plt.xlabel('Days')
plt.ylabel('Total Screen Time (minutes)')

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('charts/total_screen_time.png')

plt.close()


# -------------------------
# 2. Total usage per app
# -------------------------

apps = ['Instagram', 'WhatsApp', 'YouTube', 'LinkedIn']

totals = [
    df['Instagram_Minutes'].sum(),
    df['WhatsApp_Minutes'].sum(),
    df['YouTube_Minutes'].sum(),
    df['LinkedIn_Minutes'].sum()
]

plt.figure(figsize=(12, 6))

plt.bar(
    apps,
    totals,
    color=["#E1306C", "#25D366", "#FF0000", "#0A66C2"]
)

plt.title('Total Screen Time by App')
plt.ylabel('Minutes')

plt.tight_layout()

plt.savefig('charts/app_screen_time.png')

plt.close()


# -------------------------
# 3. Study vs Screen Time
# -------------------------

plt.figure(figsize=(12, 5))

plt.plot(
    df['day_label'],
    df['Study_Minutes'],
    marker='o',
    label='Study',
    color='pink'
)

plt.plot(
    df['day_label'],
    df['Total_Screen_Time'],
    marker='s',
    label='Screen Time',
    color='blue'
)

plt.title('Study Time vs Screen Time')
plt.xlabel('Days')
plt.ylabel('Minutes')

plt.xticks(rotation=45)

plt.legend()
plt.tight_layout()

plt.savefig('charts/study_vs_screen_time.png')

plt.close()


# -------------------------
# 4. Pie chart
# -------------------------

plt.figure(figsize=(5, 5))

plt.pie(
    totals,
    labels=apps,
    autopct='%1.1f%%',
    colors=["#E1306C", "#25D366", "#FF0000", "#0A66C2"]
)

plt.title('App Screen Time Distribution')

plt.tight_layout()

plt.savefig('charts/total_screen_time_pie.png')

plt.close()