from GithubBackup import GithubBackup
import sys
import argparse

def repos(args):
    gh = GithubBackup(args[0])
    gh.backup_all_repos()


def main():
    parser = argparse.ArgumentParser(description = "A CLI for backing up your public and private github repos")

    parser.add_argument("-r", "--repos", type=str, nargs=1,
                        metavar="github_token", default=None,
                        help="Backups all your github repos")

    args = parser.parse_args()

    # breakpoint()
    print('args', args)

    # This is probably over-kill, but all this is doing is routing the command to the correct method
    command = next(iter((args.__dict__.items())))
    globals()[command[0]](command[1])

if __name__ == "__main__":
    main()