#!/bin/zsh
python -m pip install ./package.deployment/openastro-1.1.57.tar.gz
python -m pip install prettytable
python -m pip install requests
./test/invokeService.py
python -m pip uninstall -y openastro
python -m pip uninstall -y prettytable
python -m pip uninstall -y requests
python -m pip uninstall -y pyswisseph
