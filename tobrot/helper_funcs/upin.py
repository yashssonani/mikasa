import asyncio

import aiohttp

upload_url = "http://195.154.232.19:7000/upload_request"      #   Inspect the upload page and grab it (may change in future).
auth_mail = ""                                                #   Email with which you signed up.
auth_password = ""                                              #   Inspect the upload page and grab it.

async def url_up(file):
  async with aiohttp.ClientSession() as session:
    file_to_upload = ''                                       #   Path to the file.
    data = {'file' : open(file_to_upload, 'rb'),
      'folder_id': '0',                                       #   Folder to which uploads go.
      'auth_mail': "nwkdqt@hi2.in",
      'auth_password': "df9ee1b7d413bd5610a926136dc09563",
      'domain': 'upindia.mobi',
      'ajax': 'yes'
    }
    r = await session.post(upload_url, data=data)
    print(await r.text())  
    #   Response will be a html page with json formated data.
    asyncio.run(url_up(file))
    upload_response = await r.json(content_type=None)
        if 'success' in upload_response['type']:
            info = upload_response['info']
            file_id = info['file_id']
            file_code = info['file_code']
            
            return "http://upindia.mobi" + f"/{file_id}/{file_code}"
        else
            return "none"
