'''
Created on 2012/02/27

@author: harendra
'''
from BaseHandler import BaseHandler
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import logging
from google.appengine.api import files
from google.appengine.api import images
import json
class FileuploadHandler(BaseHandler):
    def get(self):
        blobstore.create_upload_url('/downloader')
        context={}
        self.render_response("listdetailsnew.html",**context)

class FileDownloadHandler(blobstore_handlers.BlobstoreUploadHandler,BaseHandler):
    def post(self):
        upload_files=self.request.POST
        #image=upload_files['file']
        logging.error(upload_files)
        keys=upload_files.keys()
        imageurls=[]
        for key in keys:
            if key.find("uploadimage")!=-1:
                image=upload_files[key]
                file_name=files.blobstore.create(mime_type='image/jpg')
                with files.open(file_name,'a') as f:
                    f.write(image.value)
                files.finalize(file_name)
                blob_key=files.blobstore.get_blob_key(file_name)
                imageurls.append(images.get_serving_url(blob_key))
        context={}
        context['imagelinks']=imageurls
        logging.error(context);
        self.response.write(json.dumps(context))
                
        '''
        #logging.error(image.filename) filename
        #logging.error(image.value) data
        file_name=files.blobstore.create(mime_type='image/jpg')
        with files.open(file_name,'a') as f:
            f.write(image.value)
        files.finalize(file_name)
        blob_key=files.blobstore.get_blob_key(file_name)
        logging.error(blob_key)
        context={'imageurl':images.get_serving_url(blob_key)}
        #self.render_response("showimage.html",**context)
        '''
           
             
    
        