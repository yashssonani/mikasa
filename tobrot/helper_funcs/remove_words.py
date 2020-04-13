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
      return_name = "hello.mkv"
      #uj = "hell" "mojo"
      a = yo #"@GTMovise Orange.is.the.New.Black.S01E04.720p.BrRip.Hin-Eng.x265.HEVC-KatmovieHD.nl [Telly].mkv"
      r_word = REMOVE_WORD
      #print(AUTH_USERS)
      r_word = r_word.split()
      #print(AUTH_USERS)
      #yy = chr(5)
      #print(yy)
      cars = []
      cars = cars + r_word
      #print(cars)
      #TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

      for b in cars:
            if b in a:
                  c = a.replace(b, "")
                  a=c
      c = a


      if c is none:
         return_name = return_name 
      else:
         return_name = c

            #yoki = ' '.join(c.split())
  return return_name
