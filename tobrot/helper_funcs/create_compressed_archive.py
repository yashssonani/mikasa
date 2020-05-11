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
import tarfile

async def create_archive(input_directory):
    return_name = None
    
    if os.path.exists(input_directory):
        base_dir_name = os.path.basename(input_directory)
        compressed_file_name = f"{base_dir_name}.tar.gz"
        # #BlameTelegram
        suffix_extention_length = 1 + 3 + 1 + 2
        if len(base_dir_name) > (64 - suffix_extention_length):
            compressed_file_name = base_dir_name[0:(64 - suffix_extention_length)]
            compressed_file_name += ".tar.gz"
        # fix for https://t.me/c/1434259219/13344
        file_genertor_command = [
            "tar",
            "-zcvf",
            compressed_file_name,
            f"{input_directory}"
        ]
        process = await asyncio.create_subprocess_exec(
            *file_genertor_command,
            # stdout must a pipe to be accessible as process.stdout
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        # Wait for the subprocess to finish
        stdout, stderr = await process.communicate()
        e_response = stderr.decode().strip()
        t_response = stdout.decode().strip()
        if os.path.exists(compressed_file_name):
            try:
                shutil.rmtree(input_directory)
            except:
                pass
            return_name = compressed_file_name
    return return_name

async def create_unzip(input_directory):
    #return_name = None
    working_directory = os.path.dirname(os.path.abspath(input_directory))
    new_working_directory = os.path.join(
        working_directory,
        str(time.time())
    )
    if not os.path.isdir(new_working_directory):
        os.makedirs(new_working_directory)
    #if os.path.exists(input_directory):
        #base_dir_name = os.path.basename(input_directory)
        #compressed_file_name = f"{base_dir_name}.tar.gz"
        # #BlameTelegram
        #suffix_extention_length = 1 + 3 + 1 + 2
        #if len(base_dir_name) > (64 - suffix_extention_length):
            #compressed_file_name = base_dir_name[0:(64 - suffix_extention_length)]
            #compressed_file_name += ".tar.gz"
        # fix for https://t.me/c/1434259219/13344
        """'file_genertor_command = [
            "tar",
            "-zcvf",
            compressed_file_name,
            f"{input_directory}"
        ]
        """
        if ".tar" in input_directory:
           my_tar = tarfile.open(input_directory)

           extract_file = my_tar.extractall(new_working_directory) 

           my_tar.close() 
        if ".zip" in input_directory:
           target = input_directory
           handle = zipfile.ZipFile(target)
        
           extract_file = handle.extractall(new_working_directory)
           handle.close
        """
        process = await asyncio.create_subprocess_exec(
            *extract_file,
            # stdout must a pipe to be accessible as process.stdout
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        # Wait for the subprocess to finish
        stdout, stderr = await process.communicate()
        e_response = stderr.decode().strip()
        t_response = stdout.decode().strip()
        """
     
        if os.path.exists(new_working_directory):
            try:
                shutil.rmtree(input_directory)
            except:
                pass
            return_name = new_working_directory
    return return_name

