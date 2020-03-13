


class IndexRstGenerator():
    def __init__(self, doc_name):
        self._doc_name = doc_name
        self._doc_path = []

    def add_doc_path_list(self, doc_path_list):
        for path in doc_path_list:
            if path not in self._doc_path:
                self._doc_path.append(path)


    def write(self, write_path):
        body = [
            "{} Documentation".format(self._doc_name), 
            "="*100, 
            "", 
            ".. toctree::", 
            "    :maxdepth: 1", 
            "",
        ]

        for path in self._doc_path:
            body.append("    {}/index.rst".format(path))

        with open(write_path, 'w') as fd:
            fd.write('\n'.join(body))

