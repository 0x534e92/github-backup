from github import Github
import os
from datetime import datetime
import subprocess

class GithubBackup:
    def __init__(self, github_token):
        self.github_token = github_token

    def backup_all_repos(self, backup_directory=""):
        """
        This method will currently clone all the repos and then generate a zip file of all the repos
        :param backup_directory: target directory is where the backups should live, otherwise we'll default to a custom directory
        within the user's home directory
        :return:
        """

        # The whole purpose of this script is to get all the repos in one folder zipped up
        # Sure, we'll re-clone them, but I think this is much cleaner than overwriting an existing folder
        if not backup_directory:
            backup_directory = self._create_backup_directory()


        # Here's the basic algorithm:
        # 1.) Go through all the user's repos
        # 2.) Clone each repo fresh
        # 3.) Go back to the root of `backup_directory` and create a zip of the newly created directory
        subprocess.run(["cd", backup_directory])
        cwd = os.getcwd()

        print("Starting the cloning process...this may take a few minutes.")

        commands = [f'cd {backup_directory}']
        for repo in self.client.get_user().get_repos():
            commands.append(f'git clone {repo.html_url}')

        command_str = ";".join(commands)

        subprocess.run(command_str, shell=True, capture_output=True)

        print(f"Cloned all {len(commands) - 1 } repos to the following directory: {backup_directory}")

    # Set a default directory of $HOME/github_backups/current_time/
    def _create_backup_directory(self):
        current_time = datetime.now().strftime('%Y-%m-%d-%H_%M_%S')
        path = os.path.expanduser("~") + os.sep + "github_backups" + os.sep + current_time

        os.makedirs(path, exist_ok=False)

        return path

    @property
    def client(self):
        return Github(self.github_token)

