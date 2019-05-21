import git
import setup
import click
import copier
import logging

try:
    setup_tasks = setup.Setup()
    setup_tasks.set_dictConfig()
    xcode_dir, visualstudio_dir, git_dir = setup_tasks.get_directories()
    logger = logging.getLogger("copy_logger")
    repository = git.Repo(git_dir)
except Exception as e:
    print("Setup failed", e)
    exit(0)


@click.group()
def adapt():
    pass


@adapt.command("x-vs")
def xcode_visualstudio():
    adapt_copier = copier.Copier(xcode_dir, visualstudio_dir)
    adapt_copier.adapt("Xcode-VisualStudio")


@adapt.command("vs-x")
def visualstudio_xcode():
    adapt_copier = copier.Copier(visualstudio_dir, xcode_dir)
    adapt_copier.adapt("VisualStudio-Xcode")


@adapt.command("push")
@click.argument("commit_message")
def git_push(commit_message):
    try:
        repository.git.add(u=True)
        logger.info("GIT ADD")
        repository.git.commit(m=commit_message)
        repository.commit()
        logger.info("GIT COMMIT")
        repository.remotes.origin.push(refspec="master:master")
        logger.info("GIT PUSH")
    except Exception as e:
        print(e)


@adapt.command("pull")
def git_pull():
    try:
        repository.remotes.origin.pull(refspec="master:master")
        logger.info("GIT PULL")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    adapt()