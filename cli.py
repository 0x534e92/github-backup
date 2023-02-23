from GithubBackup import GithubBackup
import sys
import argparse

def repos(args):
    github_token = args[0]

    try:
        backup_dir = args[1]
    except IndexError:
        backup_dir = None

    gh = GithubBackup(github_token=args[0])
    gh.backup_all_repos(backup_directory=backup_dir)

def main():
    parser = argparse.ArgumentParser(description = "A CLI for backing up your public and private github repos")

    parser.add_argument("-r", "--repos", type=str, nargs='*',
                        metavar=("github_token", "backup_directory"), default=None,
                        help="Clone all repos and create a zip file of them")

    args = parser.parse_args()

    """
    This is probably over-kill, but all this is doing is routing the command to the correct method within this file. Probably a more better way to do this, but it'll be useful
    when this is possibly extended...if I have the time :P
    """
    command = next(iter((args.__dict__.items())))
    globals()[command[0]](command[1])

if __name__ == "__main__":
    main()