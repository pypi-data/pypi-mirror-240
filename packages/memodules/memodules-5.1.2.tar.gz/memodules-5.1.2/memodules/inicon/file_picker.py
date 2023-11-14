# region	|=-=-=-=|Import  Section|=-=-=-=|
from collections import namedtuple
from tkinter import filedialog
from inicon import ini
import socket
import glob
import sys
import os
from os import (
    path as op,
    mkdir
)
import re
# endregion
# 			|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
__AlternativeCommandLine = None
__develop_var__ = ['-d', '--debug']
_dbg = True

# region	|=-=-=-=|Setup Section|=-=-=-=|
MODE = namedtuple('save_tg_mode', ['OverRide', 'Additional'])('w', 'a')
config_path = namedtuple('ConfigPath',
                         ['pathini', 'iniext', 'tgfile']
                         )('./path.ini', '*.ini', '*.tg')
path_ini = None
with ini(config_path.pathini, 'utf-8') as f:
    path_ini = f.read()
Constant = namedtuple('Constant',
                      ['DIRECTORY', 'FILE', 'FILES', 'TGFILE']
                      )('D', 'F', 'FS', 'TG')

if len(sys.argv) > 1 or __AlternativeCommandLine is not None:
    _dbg = all(item in __develop_var__ for item in sys.argv)
if _dbg:
    _mode = 'debug'
    # PC名取得(デバッグ用)
    _host = socket.gethostname().upper()
else:
    _host = None
    _mode = 'normal'


"""def cache():
    _path = None
    # 現在ディレクトリ/path.jsonある？
    if op.isfile("./path.ini"):
        # コンフィグ取得
        with ini("./path.ini", 'utf-8') as f:
            f.read()
            _path = f[_mode]

    # pathにhostがある、もしくはpathとhostがNoneじゃないなら
    if _host in _path or not (_path is None and _host is None):
        # pathのhostの項目取得
        return _path[_host]
    elif 'setting' in _path:
        uDoc = None
        if _path['setting'] is None:
            uDoc = op.join(op.expanduser("~/Documents"), '.ini_optimizer/.setting')
            if not op.isdir(uDoc):
                success = False
                dLetter = op.splitdrive(uDoc)[0]
                _mid = op.normpath(uDoc).split(os.path.sep)
                _tgt = op.join(dLetter, *_mid[:-1])
                del _mid
                while not success:
                    if not op.isdir(_tgt):
                        mkdir(_tgt)
                    elif not op.isdir(uDoc):
                        mkdir(uDoc)
                        success = True
                del _tgt, dLetter
        else:
            uDoc = _path['setting']

        return op.join(uDoc, 'env.json')"""


# __SETTING_FILE = cache()
# endregion
# 			|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|


class PickBaseAndTarget:
    def __init__(self, initial_dir: str, mode: str = Constant.TGFILE):
        self.__base_file = filedialog.askopenfilename(
            defaultextension='.ini',
            filetypes=[(u'構成設定', '.ini'),
                       (u'テキストファイル', '.txt'),
                       (u'全てのファイル', '.*')],
            initialdir=initial_dir,
            title=''
        )

        self.__target = namedtuple('TargetPath', ['directory', 'file'])
        self.__target = self.__target(None, None)

        if mode == Constant.DIRECTORY:  # directory選択モード
            self.__target.directory = \
                filedialog.askdirectory(initialdir=initial_dir,)
            self.__target.file = []
            for f in glob.glob(f'{op.join(self.__target.directory, "*.ini")}',
                               recursive=True):
                self.__target.file.append(f)
        elif mode == Constant.FILE:  # file単体選択モード
            self.__target.directory = 'ディレクトリは選択されていません。'
            self.__target.file = \
                filedialog.askopenfilename(filetypes=[(u'構成設定', '.ini'),
                                                      (u'テキストファイル', '.txt'),
                                                      (u'全てのファイル', '.*')],
                                           initialdir=initial_dir,
                                           title='最適化ファイルの選択(単体)',)
        elif mode == Constant.FILES:  # file複数選択モード (フォルダ越え選択できるのか要確認)
            self.__target.directory = 'ディレクトリは選択されていません。'
            self.__target.file = \
                filedialog.askopenfilenames(filetypes=[(u'構成設定', '.ini'),
                                                       (u'テキストファイル', '.txt'),
                                                       (u'全てのファイル', '.*')],
                                            initialdir=initial_dir,
                                            title='最適化ファイルの選択(複数)',)
        # オリジナル拡張子ファイル.tgに記録されてるパスを使うモード (RFC起動で自動最適化の時はこれを採用予定)
        elif mode == Constant.TGFILE:
            if op.isfile(config_path.tgfile):
                self.__target.directory = self.__target.file = []
                with open(config_path.tgfile, 'r', encoding='utf-8') as f:
                    _mid = f.read()

                if '\n' in _mid:
                    _mid = re.sub('\n', ';', _mid).split(';')

                for _path in _mid:
                    if op.isdir(_path):
                        self.__target.directory.append(_path)
                    elif op.isfile(_path):
                        self.__target.file.append(_path)

                if len(self.__target.directory) == 0:
                    self.__target.directory = '指定パスにディレクトリは含まれていません。'
                elif len(self.__target.file) == 0:
                    self.__target.file = '指定パスにファイルは含まれていません。'

    @property
    def Base(self):
        return self.__base_file

    @property
    def Target(self):
        return self.__target.directory

    @property
    def Targets(self):
        return self.__target.file


def store_file(initial_dir, mode=MODE.Additional):
    files: list[str] = []
    for f in filedialog.askopenfilenames(filetypes=[(u'構成設定', '.ini'),
                                                    (u'テキストファイル', '.txt'),
                                                    (u'全てのファイル', '.*')],
                                         initialdir=initial_dir,
                                         title='最適化ファイルの選択(複数)'):
        files.append(f)
    files = ';'.join(files)
    with open(path_ini['CONFIG']['TGFILE'], mode, encoding='utf-8') as f:
        f.write(files)


def store_folder(initial_dir, mode=MODE.Additional):
    files: list[str] = []
    direct = filedialog.askdirectory(initialdir=initial_dir,
                                     title='プロジェクトフォルダの選択')
    direct = op.join(direct, '**', config_path.iniext)
    for f in glob.glob(pathname=direct, recursive=True):
        files.append(f)
    files = ';'.join(files)
    with open(path_ini['CONFIG']['TGFILE'], mode, encoding='utf-8') as f:
        f.write(files)


def put_files() -> list | None:
    if int(path_ini['CONFIG']['FIRSTRUN']) == 1:
        return None
    else:
        files = []
        with open(path_ini['CONFIG']['TGFILE'], 'r', encoding='utf-8') as f:
            files = f.read().split(';')

        return files


if __name__ == '__main__':
    store_folder(path_ini['CONFIG']['PROJECTDIR'])
elif __name__ == '____':
    picker = PickBaseAndTarget(
        r'E:\DevelopmentEnvironment\python\RFCevo_addin')
    print(f'{picker.Base}, {picker.Target}\n{picker.Targets}')
