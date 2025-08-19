from github_api_analytics_kit import GitHubAPI
from github_api_analytics_kit.utils import aggregate_commits_by_week, profile_repo_data

def main():
    owner = input("Enter repo owner: ")
    repo = input("Enter repo name: ")
    api = GitHubAPI()
    commits = api.get_repo_commits(owner, repo)
    profile = profile_repo_data(commits)
    weekly = aggregate_commits_by_week(commits)
    print("Profile:", profile)
    print("Weekly Summary:\n", weekly)

if __name__ == "__main__":
    main()
