from src.console import Console
import io
import yaml
import string

class History:

    console = Console()
    default_folder = '.history'

    """
    create history data from sites info

    :param sites: Information recievend from all sites
    :type sites: dict
    """
    def __init__(self, sites: dict, folder: str = default_folder):
        self._sites = sites
        self.folder = folder

    def execute(self):

        self.console.mkdir(self.folder)

        for s in self._sites:

            site = self._sites[s]

            with io.open(self.folder + '/' + self.format_name(s) + '.yml', 'w', encoding='utf8') as outfile:
                yaml.dump(site, outfile, default_flow_style=False, allow_unicode=True)


    """
    get formated name of a site

    e.x.
    >> format_name('hello w*rld')
        hello-wrld

    :param name: The name of site
    :type name: str

    :return: (str) formated name
    """
    def format_name(self, name: str):

        name = name.strip()
        name = name.lower()
        name = name.replace(" ", "-")
        name = "".join(filter(lambda char: char in string.ascii_lowercase, name))

        return name