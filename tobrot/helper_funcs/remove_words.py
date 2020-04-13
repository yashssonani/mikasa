#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
LOGGER = logging.getLogger(__name__)

import asyncio
import os
import shutil
import zipfile
import time
import re
from tobrot import (
    REMOVE_WORD

)
async def remove_w(yo):
      #uj = "hell" "mojo"
      a = yo #"@GTMovise Orange.is.the.New.Black.S01E04.720p.BrRip.Hin-Eng.x265.HEVC-KatmovieHD.nl [Telly].mkv"
      AUTH_USERS = REMOVE_WORD
      #print(AUTH_USERS)
      AUTH_USERS = AUTH_USERS.split()
      #print(AUTH_USERS)
      #yy = chr(5)
      #print(yy)
      cars = []
      cars = cars + AUTH_USERS
      #print(cars)
      #TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

      for b in cars:
            if b in a:
                  c = a.replace(b, "")
                  a=c
      c = a
"""
yas = ["  ","   ","    "]
print(yas)
for coni in yas:
      if coni in c:
            c = c.replace(coni, " ")
            c=c
c = print(c)

"""

      #yoki = ' '.join(c.split())
      return c
