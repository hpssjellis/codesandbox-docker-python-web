# codesandbox-docker-python-web

1. Login to [codesandbox](https://codesandbox.io/dashboard/recent)  and possibly click the left most box and choose the dashboard
2. Create a devbox and search for "docker"
3. In the ```.devcontainer``` find the ```Dockerfile``` and replace ```FROM Ubuntu``` with ```FROM python:3.12``` save ```ctrl-S```and let that install
4. Open a new terminal near the bottom of the page.
7. test if python is installed '''python3 --version``` and test if pip is installed ```pip3 --version```
5. test if ```python -V``` and ```pip -V``` work, note it is a captial V, most other Ubuntu versions checks use a small v
8. install flask   ```pip3 install Flask```  Note: many installations on Ubuntu use ```apt install ????``` but this time we use pip.
9. Check if flask was installed ```flask --version```
10. Copy the 2 files ```tz07-flask.py``` and ```tz07-web.py``` near the README.md file, or just creatte the files and copy the code
11. Don't forget to save the files with ```ctrl-s```
12. In the terminal activate the flask code which calls the pure python code ```python3 tz07-flask.py```
13. copy the generated URL to your ```index.html``` page
