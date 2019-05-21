import os
import distutils.dir_util
import shutil
import logging


class Copier:
    def __init__(self, xcode_dir, visualstudio_dir):
        self.xcode_dir = xcode_dir
        self.visualstudio_dir = visualstudio_dir
        self.logger = logging.getLogger("copy_logger")


    def is_safe_adapt(self, adapt_type):
        try:
            copier_log_file = open("copier.log", "r")
            copier_log = copier_log_file.readlines()
            copier_log_file.close()

            last_logged_action = copier_log[-1].split()[-1:]
            if last_logged_action == adapt_type:
                return True
            return False
        except FileNotFoundError:
            return True


    def adapt(self, adapt_type):
        if not self.is_safe_adapt(adapt_type):
            user_input = input("Previous pull not copied. This adapt will overwrite it\n.Do you wish to proceed? [y/n]")
            if user_input not in ('Y', 'y'):
                return

        try:
            for item in os.listdir(self.xcode_dir):
                if item.startswith("."):
                    continue

                item_path = self.xcode_dir + "/" + item
                if os.path.isfile(item_path):
                    shutil.copy2(item_path, self.visualstudio_dir)
                elif os.path.isdir(item_path):
                    distutils.dir_util.copy_tree(item_path, self.visualstudio_dir)

            self.logger.info(adapt_type)
        except Exception as e:
            print(e)


#distutils.dir_util.copy_tree(SRC, DEST)
SRC = "/Users/ajayraj/Documents/Xcode-VS-Adapt/src"
DEST = "/Users/ajayraj/Documents/Xcode-VS-Adapt/dest"