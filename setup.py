#!/usr/bin/env python
# -*- mode: python; -*-

import os
import sys
from subprocess import call

from pysollib.settings import PACKAGE, PACKAGE_URL, VERSION

from setuptools import find_packages, setup

if sys.platform == 'win32':
    import py2exe  # noqa: F401

if sys.platform in ['darwin', 'win32']:
    data_dir = 'data'
    locale_dir = 'locale'
else:
    data_dir = 'share/PySolFC'
    locale_dir = 'share/locale'

data_files = []


def add_data_files(source, destination):
    for path, _, files in os.walk(source):
        data_files.append((path.replace(source, destination, 1),
                           [os.path.join(path, f) for f in files]))


add_data_files('data', data_dir)
add_data_files('locale', locale_dir)

if sys.platform not in ['darwin', 'win32']:
    for size in os.listdir('data/images/icons'):
        data_files.append(('share/icons/hicolor/%s/apps' % size,
                           ['data/images/icons/%s/pysol.png' % size]))
    data_files.append(('share/applications', ['misc/pysol.desktop']))

# from pprint import pprint; pprint(data_files)
# import sys; sys.exit()

long_description = '''\
PySolFC is a collection of more than 1000 solitaire card games.
Its features include modern look and feel (uses Tile widget set), multiple
cardsets and tableau backgrounds, sound, unlimited undo, player statistics,
a hint system, demo games, a solitaire wizard, support for user written
plug-ins, an integrated HTML help browser, and lots of documentation.
'''

kw = {
    'name': 'PySolFC',
    'version': VERSION,
    'url': PACKAGE_URL,
    'author': 'Skomoroh',
    'author_email': 'skomoroh@gmail.com',
    'description': 'a Python solitaire game collection',
    'install_requires': [
        'attrs',
        'configobj',
        'pycotap',
        'pysol_cards',
        'random2',
        'six',
    ],
    'long_description': long_description,
    'license': 'GPL',
    'scripts': ['pysol.py'],
    'packages': find_packages(),
    'data_files': data_files,
    }

if sys.platform == 'win32':
    kw['windows'] = [{'script': 'pysol.py',
                      'icon_resources': [(1, 'misc/pysol.ico')], }]
    kw['packages'].remove('pysollib.pysolgtk')
elif sys.platform == 'darwin':
    # Use Freecell Solver if it is installed.
    # http://fc-solve.berlios.de/
    SOLVER_LIB_PATH = "/usr/local/lib/libfreecell-solver.0.dylib"
    SOLVER = ["/usr/local/bin/fc-solve"]
    if not os.path.exists(SOLVER_LIB_PATH):
        SOLVER_LIB_PATH = None
        SOLVER = []

    GETINFO_STRING = ("PySol Fan Club Edition %s %s, "
                      "(C) 1998-2003 Markus F.X.J. Oberhumer, "
                      "(C) 2006-2007 Skomoroh") % (PACKAGE, VERSION)
    PLIST = {
        'CFBundleDevelopmentRegion': 'en_US',
        'CFBundleExecutable': PACKAGE,
        'CFBundleDisplayName': PACKAGE,
        'CFBundleGetInfoString': GETINFO_STRING,
        'CFBundleIdentifier': 'net.sourceforge.pysolfc',
        'CFBundleName': PACKAGE,
        'CFBundleVersion': VERSION,
        'CFBundleShortVersionString': VERSION,
        'NSHumanReadableCopyright':
            "Copyright (C) 1998-2003 Markus F.X.J. Oberhumer",
        }
    FRAMEWORKS = [SOLVER_LIB_PATH] if SOLVER_LIB_PATH else []
    kw['app'] = ['pysol.py']
    kw['options'] = {'py2app': {
        'argv_emulation': True,
        'plist': PLIST,
        'iconfile': 'misc/PySol.icns',
        'frameworks': FRAMEWORKS,
        'excludes': ['pysollib.pysolgtk'],
        }}
    kw['setup_requires'] = ['py2app']
    kw['data_files'] += SOLVER

setup(**kw)

# Modify the fc-solve binary with install_name_tool to use the dependent
# libfreecell-solver dynamic library in the app bundle.
if sys.platform == 'darwin' and SOLVER:
    os.chdir('dist/%s.app/Contents/Resources' % PACKAGE)
    call("install_name_tool -change " +
         "/usr/local/lib/libfreecell-solver.0.dylib " +
         "@executable_path/../Frameworks/libfreecell-solver.0.dylib fc-solve",
         shell=True)
