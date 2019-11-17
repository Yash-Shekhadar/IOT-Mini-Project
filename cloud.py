from google.cloud import storage
import os
from datetime import date
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/Downloads/iotcamera-d59a7-firebase-adminsdk-wgdcl-c576e6fbad.json"

directory = "./violation/"
def cloud_upload():
	
	try:
		files = []
		
		for r,d,f in os.walk(directory):
			for img in f:
				files.append((os.path.join(r,img),img))		
		#for i in files:
			#print(i)
		client = storage.Client()
		bucket = client.get_bucket('iotcamera-d59a7.appspot.com')
		
		today = date.today()
		cloud_dir = str(today.strftime("%d-%m-%Y")) +"/"
		
		for path,name in files:
		
			blob = bucket.blob(cloud_dir + name)	
			blob.upload_from_filename(filename = path)
			os.remove(path)
			
		return 1
	except:
		return 0
		

#cloud_upload() 		

	
