#!python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'rst2pdf==0.92','console_scripts','rst2pdf'
__requires__ = 'rst2pdf==0.92'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('rst2pdf==0.92', 'console_scripts', 'rst2pdf')()
    )
