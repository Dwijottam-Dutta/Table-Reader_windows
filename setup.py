import sys
from cx_Freeze import setup, Executable
setup( name = "Table Reader", version = "1.3.4",
       description = "Table Reader",
       executables = [Executable("table_reader.py",
                                 base = "Win32GUI",
                                 icon="assets/table_reader.ico")])
