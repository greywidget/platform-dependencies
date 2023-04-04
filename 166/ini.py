import configparser


class ToxIniParser:
    config = None

    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        self.config = configparser.ConfigParser()
        self.config.read_file(open(ini_file))

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
        New to properties? -> https://pybit.es/property-decorator.html
        """
        return len(self.config.sections())

    @property
    def environments(self):
        """Return a list of environments
        (= "envlist" attribute of [tox] section)"""
        envs = self.config.get("tox", option="envlist")
        sep = "," if "," in envs else None
        return [
            item.strip()
            for item in self.config.get("tox", option="envlist").split(sep=sep)
            if item
        ]

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        base_py = set()
        for section in self.config.sections():
            if self.config.has_option(section, "basepython"):
                base_py.add(self.config.get(section, "basepython"))
        return list(base_py)
