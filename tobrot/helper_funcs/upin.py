import asyncio

import aiohttp

upload_url = "http://195.154.232.19:7000/upload_request"      #   Inspect the upload page and grab it (may change in future).
auth_mail = ""                                                #   Email with which you signed up.
auth_password = ""                                              #   Inspect the upload page and grab it.

async def url_up(file):
  async with aiohttp.ClientSession() as session:
    file_to_upload = file                                       #   Path to the file.
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
    #asyncio.run(url_up(file))
    upload_response = await r.json(content_type=None)
    if 'success' in upload_response['type']:
            info = upload_response['info']
            file_id = info['file_id']
            file_code = info['file_code']
            kola = "http://upindia.mobi" + f"/{file_id}/{file_code}"
            #print(kola)
            #return "http://upindia.mobi" + f"/{file_id}/{file_code}"
    #else:
            #return "none"
    #r = await session.post("https://api.shorte.st/s/d3c901a7e36354d8fc57ec1e6b4a3cab/"+kola)
    r = await session.get("https://shrinkearn.com/api?api=7564baef25bedf110f660c06a05fc2f42491f563&url="+kola)
   # print(await r.text())  
    #   Response will be a html page with json formated data.
    #asyncio.run(url_up(file))
    upload_response = await r.json(content_type=None)
    if 'success' in upload_response['status']:
            shortenedUrl = upload_response['shortenedUrl']
            #file_id = info['file_id']
            #file_code = info['file_code']
            #kola = "http://upindia.mobi" + f"/{file_id}/{file_code}"
            #print(kola)
            return shortenedUrl
    else:
            return "none"        
    
