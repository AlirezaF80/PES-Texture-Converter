import os

import Ftex

FTEX_TOOLS_PATH = '.\\Tools\\FtexTools.exe'


def convert_textures(file_paths):
    for file_path in file_paths:
        file_name, file_extension = os.path.splitext(file_path)
        print(file_extension)
        if file_extension.lower() == '.dds':
            convert_dds(file_path)
        elif file_extension.lower() == '.ftex':
            convert_ftex(file_path)
        else:
            return False
    return True


def convert_dds(dds_path, ftex_path=None):
    if not ftex_path or len(ftex_path) <= 2:
        os.system('"{} -f 0 {}"'.format(FTEX_TOOLS_PATH, dds_path))
    pass


def convert_ftex(ftex_path, dds_path=None):
    if not dds_path:
        dds_path = ftex_path[:-4] + "dds"
    try:
        Ftex.ftexToDds(ftex_path, dds_path)
    except:
        os.system('"{} {}"'.format(FTEX_TOOLS_PATH, ftex_path))
    pass
