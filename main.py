import os
import setup
import click
import copier
import logging

logger = logging.getLogger("copy_logger")
try:
    setup_tasks = setup.Setup()
    setup_tasks.set_dictConfig()
    xcode_dir, visualstudio_dir, git_dir = setup_tasks.get_directories()
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
@click.argument("message")
def git_push(message):
    cwd = os.getcwd()
    try:
        os.chdir(git_dir)
        os.system('git commit -m "%s"' % (message))
        logger.info("GIT COMMIT")
        os.system("git push origin master")
        logger.info("GIT PUSH")
        print("Commit and Push Successful")
    except Exception as e:
        print(e)
    finally:
        os.chdir(cwd)


if __name__ == "__main__":
    adapt()