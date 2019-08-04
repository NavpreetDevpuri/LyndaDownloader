###### By Navpreet Devpuri
## On Linux
### First install 'requests' package by runing following command 
`pip insatll requests`

### Optional arguments with python script
***If you run script without this argumentst then It will ask this things on run time***<br/>

2. ***-url*** : **Url link** of Lynda course.
3. ***-savedir or -sd*** : Directory **location (Full path)** on your system where you want to save files (by default set to the same location as LyndaDownloader.py).
4. ***-quality or -q*** : **Video quality** (360p or 0, 540p or 1, 720p or 2).
5. ***-fromfolder or -ff*** : In case you want to download only few topics by entring **starting topic number** (by default set to 1 which means start download from 1st topic of course).
##### For example : 
```python 
python3 '/home/navpreetdevpuri/Downloads/LyndaDownloader.py' -url 'https://www.lynda.com/C-tutorials/C-Essential-Training/772322-2.html' -sd '/home/navpreetdevpuri/Downloads/' -q 720p 
```

## On Android
##### You can also run this script in android (How to run python script on android ?)
1. Download and install **Termux** app. (remember to give *storage permission* from phone's settings and *turn off battery optimization* for Termux app to make app run long)
2. Run following commads : 
   -  `apt-get update`
   -  `apt-get install python`
   -  `pip install requests`
3. Know you can run python script on android


##### For example : 
```python 
python '/storage/emulated/0/Download/LyndaDownloader.py' -url 'https://www.lynda.com/C-tutorials/C-Essential-Training/772322-2.html' -sd '/storage/emulated/0/Download/' -q 2 
```



