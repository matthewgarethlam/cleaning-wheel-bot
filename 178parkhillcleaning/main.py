import pywhatkit
import numpy as np
import pandas as pd
from datetime import date

#get date
# today = date.today()
# print(today)

# read logging csv
log = pd.read_csv('/Users/matthewlam/Desktop/178parkhillcleaning/logging.csv')
# print(log[log.filepath.max() == log['filepath']].filepath)

#last 4 characters of string
prevfilepath=log[log.filepath.max() == log['filepath']].filepath
print(prevfilepath)
# prevwheel= prevfilepath[-10:]
# print(prevwheel)



#definitions

# imagepath = "/Users/matthewlam/Desktop/178parkhillcleaning/wheel1.jpg"
# caption= "no timestamp"
# group_id = "EgntfnQHwRYASbeQAzhpwL"




#sending
# syntax: phone number with country code, message, hour and minutes
# pywhatkit.sendwhats_image(group_id, imagepath, caption)


#logging


