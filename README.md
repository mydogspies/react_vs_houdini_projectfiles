# REACT vs HOUDINI - project files

### A tiny case study of one way to use React as the web front to manipulate parameters in Houdini.

This repo is the Houdini project directory with the specific scrip needed for all to work plus two example scripts.

The goal is to try out one of many ways to use a web front end to directly manipulate parameters in SideFX Houdini. It is by no means the only way and the necessarily correct way. In this case I used vanilla react for the front end, Flask running on Houdini's own Hython (in this case we stick to the built-in Python 2.7.15 in Houdini version 18.5.596) and using the Hrpyc library within Houdini's python distro to make the connection.

** I will not maintain this particular repo so no point in filing code issues but feel free to comment on better ways of doing this particular hurdle. **

Here are some specifics regarding the project files;
* In the **scripts** folder is the tiny Python script that runs on startup. It starts the Hrpyc server from within Houdini. The whole thing will not work without this step.
* In the **test_scripts folder** you can find an example of making a change to an EXISTING geometry using Hrpyc. Check out the Houdini docs on all things you can do with the Hou module (and in extension with Hrpyc). https://www.sidefx.com/docs/houdini/hom/hou/index.html
* Also, you will find the script that actually starts up Houdini remotely. In it I pass three parameters (path to executable, path to projects, path to start-up script). I also set the $JOB env var to make things slick from start. You can pass any env var within the start script.


HOW TO INSTALL AND RUN

See the other repos; 
* https://github.com/mydogspies/react_vs_houdini_backend or 
* https://github.com/mydogspies/react_vs_houdini_frontend

FINAL DISCLAIMER

This project is just a simple proof of concept I wrote in one evening and not meant to be production code. There are for sure much better ways to establish a React to Houdini pipeline and I would love to hear from anyone about your solution. Just drop a message in the issues in any of the three repos. 
