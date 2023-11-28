# codesandbox-docker-python-web

1. Login to [codesandbox](https://codesandbox.io/dashboard/recent)  and possibly click the left most box and choose the dashboard
2. Create a devbox and search for "docker"
3. In the ```.devcontainer``` find the ```Dockerfile``` and replace ```FROM ubuntu``` with ```FROM python:3.12``` save ```ctrl-S```and let that install
4. Open a new terminal near the bottom of the page.
7. test if python is installed ```python3 --version``` and test if pip is installed ```pip3 --version```
5. test if ```python -V``` and ```pip -V``` work, note it is a captial V, most other Ubuntu versions checks use a small v
8. install flask   ```pip3 install Flask```  Note: many installations on Ubuntu use ```apt install ????``` but this time we use pip.
9. Check if flask was installed ```flask --version```
10. Copy the 2 files ```tz07-flask.py``` and ```tz07-web.py``` near the README.md file, or just creatte the files and copy the code
11. Don't forget to save the files with ```ctrl-s```
12. In the terminal activate the flask code which calls the pure python code ```python3 tz07-flask.py```
13. copy the generated URL to your ```index.html``` page




#alternate methods:

1. Choose the default codesandbox ubuntu docker
2. ```Ctrl ` ``` to open a new terminal
3. ```uname -a``` then ```apt update``` then ```aptupgrade``` then ```apt update``` then ```uname -a```
4. ```apt install python3``` then ```python3 -V ```
5. ```apt install python3-pip``` then ```pip -V```
6. ```pip install flask```
7. Copy the 2 files ```tz07-flask.py``` and ```tz07-web.py``` near the README.md file, or just creatte the files and copy the code
8. Don't forget to save the files with ```ctrl-s```
9. In the terminal activate the flask code which calls the pure python code ```python3 tz07-flask.py```
10. copy the generated URL to your ```index.html``` page



# node 

I just setup nodejs with npm and tried a new file  called ```myNode.js``` which works in the same way

codesandbox to fork
https://codesandbox.io/p/devbox/jovial-dan-pq7mxy  


web page
https://pq7mxy-5000.csb.app/upload




