#!/bin/bash
pyinstaller --onefile \
    --add-data="./config.json":. \
    pac_man.py