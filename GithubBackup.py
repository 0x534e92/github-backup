from github import Github

class GithubBackup:
    def __init__(self, github_token):
        self.github_token = github_token

    def backup_all_repos(self, backup_directory=""):
        for repo in self.client.get_user().get_repos():
            print(repo.name)

    @property
    def client(self):
        return Github(self.github_token)

