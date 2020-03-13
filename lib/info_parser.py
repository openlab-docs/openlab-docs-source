from .error import DocInfoError

INDEX_RST = """
.. toctree::
    :maxdepth: %(maxdepth)s
    :caption: %(caption)s
    :name: %(caption)s
    :numbered:

%(document_list)s


"""


class DocInfoParser():
    section_type_list = [
        'info'
    ]
    info_key_list = [
        'title', 'project', 'copyright', 'author', 'version', 'release'
    ]

    def __init__(self, conf_file_path):
        self._conf_file_path = conf_file_path

        self.title = None
        self.project = None
        self.copyright = None
        self.author = None
        self.version = None
        self.relase = None

        self.index_list = []

    def parse_info(self, line):
        key, value = map(lambda c: c.strip(), line.split('=', 1))

        if key not in DocInfoParser.info_key_list:
            raise DocInfoError("not match info, %s" % key)

        setattr(self, key, value)

    def parse(self):
        section_type = None

        for line in open(self._conf_file_path):
            line = line.strip()
            if line == '' or line.startswith('#'):
                continue

            if line.startswith('[') and line.endswith(']'):
                section_type = line[1:-1].strip()
                continue

            if section_type is None:
                continue
            elif section_type not in DocInfoParser.section_type_list:
                raise DocInfoError("not match section, %s" % section_type)

            if section_type == 'info':
                self.parse_info(line)
            elif section_type == 'index':
                self.parse_index(line)

    def get_info(self):
        result_dic = {}
        for key in DocInfoParser.info_key_list:
            try:
                result_dic[key] = getattr(self, key)
            except AttributeError as err:
                raise DocInfoError('no search infomation at info.conf, %s' % key)

        return result_dic

    def write_info(self, file_path, static_path_list):
        with open(file_path, 'w') as fd:
            for k, v in self.get_info().items():
                fd.write("%s = '%s'\n" % (k, v))

            if static_path_list is None:
                static_path_list = [
                    '/'.join(['t_source', 'static']),
                    '/'.join(['templates', 'web', 'theme.css'])]

            fd.write("html_static_path = ['%s']" % "','".join(static_path_list))


def test():
    import sys
    doc_info = DocInfoParser(sys.argv[1])

    print(doc_info.get_info())


if __name__ == '__main__':
    test()
