import os
import shutil

import Ftex

FTEX_TOOLS_PATH = '.\\Tools\\FtexTools.exe'


def convert_textures(file_paths):
    for file_path in file_paths:
        file_name, file_extension = os.path.splitext(file_path)
        if file_extension.lower() == '.dds':
            convert_dds(file_path)
        elif file_extension.lower() == '.ftex':
            convert_ftex(file_path)
        else:
            return False
    return True


def convert_dds(dds_path, ftex_path=None):
    if not ftex_path:
        ftex_path = dds_path[:-3] + "ftex"
    if os.path.exists(ftex_path):
        ftex_path = dds_path[:-4] + " (1).ftex"
        shutil.copy2(dds_path, dds_path[:-4] + " (1).dds")
        dds_path = dds_path[:-4] + " (1).dds"
    try:
        Ftex.ddsToFtex(dds_path, ftex_path, 'NORMAL')
    except:
        os.system('"{} -f 0 {}"'.format(FTEX_TOOLS_PATH, dds_path))
    if str(dds_path).endswith(" (1).dds"):
        os.remove(dds_path)

    # TODO: remove this method and see if the index is usable or not
    # this way you may delete a file that was there at first. e.g:
    # the "... (1).dds" file exists and you replace it with yours.


def convert_ftex(ftex_path, dds_path=None):
    if not dds_path:
        dds_path = ftex_path[:-4] + "dds"
    if os.path.exists(dds_path):
        dds_path = ftex_path[:-5] + " (1).dds"
        shutil.copy2(ftex_path, ftex_path[:-5] + " (1).ftex")
        ftex_path = ftex_path[:-5] + " (1).ftex"
    try:
        Ftex.ftexToDds(ftex_path, dds_path)
    except:
        os.system('{} "{}"'.format(FTEX_TOOLS_PATH, ftex_path))
    if str(ftex_path).endswith(" (1).ftex"):
        os.remove(ftex_path)

    # TODO: remove this method and see if the index is usable or not
    # this way you may delete a file that was there at first. e.g:
    # the "... (1).ftex" file exists and you replace it with yours.
