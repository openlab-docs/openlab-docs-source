# coding: utf-8
import glob
import os
import collections


def get_doc_list(base_path):
    """
    guide 목록 수집
    """
    doc_info = collections.OrderedDict()
    doc_path = []
    doc_path += glob.glob(os.path.join(base_path, '*', '*'))
    # doc_path += glob.glob(os.path.join(base_path, '*', '*_guide'))
    # doc_path += glob.glob(os.path.join(base_path, '*', '*_manual'))

    for path in sorted(doc_path):
        if os.path.isdir(path):
            _, guide_type, guide_name = path.rsplit(os.sep, 2)
            doc_info['%s.%s'%(guide_type,guide_name)] = path

    return doc_info


def _test():
    import sys
    base_path = sys.argv[1]
    print(get_doc_list(base_path))


if __name__ == '__main__':
    _test()
