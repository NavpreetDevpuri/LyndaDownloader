### First install 'requests' package by runing following command 
`pip insatll requests`

### Optional arguments with python script
***If you run script without this argumentst then It will ask this thigs on run time***<br/>

2. **Url link** of Lynda course.
3. Directory **location (Full path)** on your system where you want to save files (by default set to the same location as LyndaDownloader.py).
4. **Video quality** (0 for 360p, 1 for 540p, 2 for 720p).
5. In case you want to download only few topics by entring **starting topic number** (by default set to 1 which means start download from 1st topic of course).
##### For example : 
```python 
python3 '/home/navpreetdevpuri/Downloads/LyndaDownloader.py' 'https://www.lynda.com/C-tutorials/C-Essential-Training/772322-2.html' '/home/navpreetdevpuri/Downloads/' 2 
```


##### You can also run this script in android (How to run python script on android ?)
1. Download and install **Termux** app. (remember to give storage permission from phone's settings)
2. Run following commads : 
   -  `apt-get update`
   -  `apt-get install python`
   -  `pip install requests`
3. Know you can run python script on android


##### For example : 
```python 
python '/storage/emulated/0/Download/LyndaDownloader.py' 'https://www.lynda.com/C-tutorials/C-Essential-Training/772322-2.html' '/storage/emulated/0/Download/' 2 
```



