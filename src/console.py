from termcolor import cprint
import sys
import os

class Console():

    ERROR_PREFIX = '[ERROR]: '
    WARING_PREFIX = '[WARNING]: '
    INFO_PREFIX = '[INFO]: '

    """
    Eror with red text in the terminal

    :param text: String to be displayed
    :param exit: Exit the program
    :type text: str
    :type exit: bool
    """
    def error(self, text: str, exit: bool = True):
        cprint(self.ERROR_PREFIX + text, 'red')

        if exit:
            sys.exit(1)

    """
    Print a info message with orange text in the terminal

    :param text: String to be displayed
    :type text: str
    """
    def info(self, text: str):
        print(self.INFO_PREFIX + text)

    """
    Warn with yello text in the terminal

    :param text: String to be displayed
    :type text: str
    """
    def waring(self, text: str):
        cprint(self.WARING_PREFIX + text, 'yellow')

    """
    create a new folder with log

    :param folder: the name of the folder
    :param replace: replace folder if exists
    :type folder: str
    :type replace: bool
    :default replace: True
    """
    def mkdir(self, folder: str, replace = True):

        if replace and os.path.isdir(folder):
            filelist = [ f for f in os.listdir(folder) ]
            for f in filelist:
                os.remove(os.path.join(folder, f))

            self.waring(f'deleting folder {folder}')
            os.rmdir(folder)

        self.info(f"creating folder {folder}...")
        os.mkdir(folder)