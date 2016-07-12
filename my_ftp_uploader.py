#!/usr/bin/env python
import time

# needs to return a list of (Name, Value, Bool)
def generate_ftp_download_dir(trans = None):
    if trans:
       username = trans.user.username
       unix_timestamp = str(int(time.time()))
       upload_path = "galaxy_" + username + "_" + unix_timestamp
       return_obj = []
       return_obj.append( (upload_path, upload_path, True) )
       return return_obj
    return []
