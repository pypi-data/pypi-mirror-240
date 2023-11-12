# Manuscriptify
# Compile google docs into a manuscript
# Copyright (c) 2022 Manuscriptify
# Business Source Licence: https://mariadb.com/bsl11
"""
invoke the package

"""
import sys, subprocess

def manuscriptify():
    """package the command for setup.py"""
    shell_command = ['python', '-m', 'manuscriptify'] + sys.argv[1:]
    subprocess.run(shell_command)
