#!python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pylint==0.26.0','console_scripts','epylint'
__requires__ = 'pylint==0.26.0'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pylint==0.26.0', 'console_scripts', 'epylint')()
    )
