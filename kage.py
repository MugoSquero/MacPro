#!/usr/bin/env python
# -*- coding: utf-8 -*-

MAIN="Kage"
AUTHOR="BeyazHacker.com"

import os

if (os.path.exists("/usr/share/set/modules/Kage") == True):
	os.system("cd /usr/share/set/modules/Kage/ && npm run dev")

elif (os.path.exists("/usr/share/set/modules/Kage") == False):
	os.system("apt install npm")
	os.system("apt install libgconf-2-4 -y")
	os.system("git clone https://github.com/WayzDev/Kage.git")
	os.system("cp -r Kage/ /usr/share/set/modules/")
	os.system("cd /usr/share/set/modules/Kage/ && npm install")
	os.system("clear")
	os.system("cd /usr/share/set/modules/Kage/ && npm run dev")



