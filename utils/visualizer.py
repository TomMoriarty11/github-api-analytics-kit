import matplotlib.pyplot as plt

def plot_weekly_commits(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df['week'], df['commit_count'], marker='o')
    plt.title("Weekly Commit Activity")
    plt.xlabel("Week")
    plt.ylabel("Commits")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
