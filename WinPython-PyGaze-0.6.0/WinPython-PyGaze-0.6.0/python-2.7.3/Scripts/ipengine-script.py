#!python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'ipython==0.13.1','console_scripts','ipengine'
__requires__ = 'ipython==0.13.1'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('ipython==0.13.1', 'console_scripts', 'ipengine')()
    )
