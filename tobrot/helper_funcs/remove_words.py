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
       a = yo
       #b = ['KatmovieHD']
       b = REMOVE_WORD.split()
       for bya in b:
             if bya in a:
                 ko = a.replace(bya, "")
                 a = ko
       a=ko 
       a=a.split()
       a=" ".join(a)
       
       #print(a)
       return a;


      
