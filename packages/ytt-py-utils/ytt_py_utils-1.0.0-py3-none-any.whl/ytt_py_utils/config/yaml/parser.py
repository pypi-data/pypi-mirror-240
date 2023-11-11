import os
from pyaml_env import parse_config
from config import abstract

class YamlParser(abstract.Parser):
    """ YamlParser  """
    def __init__(self, fpath):
        """

        :param fpath:
        """

        self.fpath = fpath
        if self.config_file_exists() is True:
            self.data = self.load()
        else:
            print('Config file is not valid/does not exist')

    def load(self):
        """

        :return:
        """
        data = parse_config(self.fpath, tag='!TAG')
        return data

    def save(self):
        """

        :return:
        """
        with open(self.fpath, 'w') as f:
            f.close()

    def config_file_exists(self):
        if os.path.exists(self.fpath):
            return True
        else:
            return False