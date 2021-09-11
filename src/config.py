from io import FileIO
from src.console import Console
import xmltodict
import json

class Config(dict):

    default_ext = 'xml'
    console = Console()

    """
    Get the configuration from .status.EXT

    :param ext: Extension of the configuration file
    :param type: Type of the config file (xml, yml, json)
    :type ext: str
    :type type: str
    """
    def __init__(self, ext: str = default_ext, type: str = default_ext):

        self._ext = ext
        self._type = type

        try:
            with open('.status.' + self._ext, 'r') as f:
                self._f_read = f.read()
        except FileNotFoundError:
            self.console.error("Coudn't find configuration file")

        if not self.parseContent():
            self.console.error("Coudn't parse configuration file")


    """
    Parse the configuration file depending on its type

    :return bool: True if parsing was complete
    """
    def parseContent(self):

        try:
            if self._type == 'xml':

                self.__dict__ = json.loads(json.dumps(xmltodict.parse(
                    self._f_read
                )['config']))

            return True

        except Exception as e:
            self.console.error(e, exit=False)
            return False

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __repr__(self):
        return repr(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, key):
        del self.__dict__[key]

    def clear(self):
        return self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def has_key(self, k):
        return k in self.__dict__

    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()

    def pop(self, *args):
        return self.__dict__.pop(*args)

    def __cmp__(self, dict_):
        return self.__cmp__(self.__dict__, dict_)

    def __contains__(self, item):
        return item in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)

    def __unicode__(self):
        return unicode(repr(self.__dict__))