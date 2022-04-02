# Barcode-scanner-with-Python-GUI
This is a project to be able to scan QR-Codes with the camera of the Raspberry Pi. Informations will be displayed on a GUI

# Hardware
All you need is is listed below:<br>
-Raspberry Pi Model 3 (or newer)<br>
-Raspberry Pi Camera V<br>
I recommend to build a camera tripod for the Pi-Cam (For example with a 3D printer). This way you don't have to hold the camera during the recording. This prevents the captured image from becoming blurred. This prevents a faulty readout.<br>
When you connect the camera to the Pi, make sure the cable is facing the right direction. Otherwise you will not get a picture.

# Software
First, you have to enable the camera port on the Raspberry Pi. There are a lot of tutorials out there so i will not go into detail about this step. Next, we have to install the required tools and libaries for my code. You can simply copy paste and execture the folling lines of codes: <br>

sudo apt-get update<br>
sudo apt-get install python3 python3-pip libzbar0<br>
sudo pip3 install opencv-python pyzbar imutils<br>
sudo apt-get install libcblas-dev libhdf5-dev libhdf5-serial-dev libatlas-base-dev lib<br>
jasper-dev libqtgui4 libqt4-test<br>

If you are using an older version of Python, please delete it. These will cause problems later when displaying the image in the GUI if they are not deleted
