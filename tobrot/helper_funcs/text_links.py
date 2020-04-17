import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import asyncio
import os
import time
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from PIL import Image
from tobrot.helper_funcs.display_progress import progress_for_pyrogram, humanbytes
from tobrot.helper_funcs.help_Nekmo_ffmpeg import take_screen_shot
from tobrot.helper_funcs.split_large_files import split_large_files
from tobrot.helper_funcs.copy_similar_file import copy_file
from tobrot.helper_funcs.remove_words import remove_w
from tobrot import (
    TG_MAX_FILE_SIZE,
    EDIT_SLEEP_TIME_OUT,
    DOWNLOAD_LOCATION,
    REMOVE_WORD
)


async def multi_links(reply_message):
    after_download_file_name = download_media(
            message=reply_message,
            file_name=download_location,
            progress=progress_for_pyrogram,
            progress_args=("trying to download")
        )
    with open(after_download_file_name) as kola:
        for rec in kola:
            
