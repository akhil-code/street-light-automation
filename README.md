# Street Light Automation
Developed an Image processing model that detects the presence of Humans and automatically adjusts the brightness of that street lights proximate to them. The model basically detects and localizes the presence of humans by characterstics of their motion, dimensions etc. This information is then used to find nearby street lights and control their brightness.

## Setup instructions
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

#### Prerequisites
+ [Python](https://www.python.org/downloads/)
+ [OpenCV](https://opencv.org/releases.html) (Image processing library)
+ Camera Application for Android - [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en) (optional)

#### Deployment
+ Clone the Repository `git clone https://github.com/akhil-code/street-light-automation`
+ Change current directory to this repository
+ Run python script using command `python videoAnalysis.py`

#### Application Settings
+ video resolution: 480x360,
+ quality: 90
---
### Future plans
+ Will use deep learning inorder to identify the person rather than only detecting him/her.

### Learn more
+ [OpenCV documentation](https://docs.opencv.org/2.4/doc/tutorials/tutorials.html)

### Authors
+ Akhil Guttula
+ Amit Kaushal
+ Deepak
+ Lipsoo
