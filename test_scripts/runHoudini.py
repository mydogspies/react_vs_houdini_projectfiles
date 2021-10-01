import os
import subprocess

houdini_install_path = 'path://to//Houdini 18.5.596/'
local_project_path = 'path://to/projects/'

houdini_app = houdini_install_path + "bin/houdini.exe"
houdini_default_file = local_project_path + "houdini/exampleProjects/projectOne/remote_sphere.hipnc"
houdini_default_script = local_project_path + "houdini/exampleProjects/projectOne/scripts/run_some_python.py"
os.environ['JOB'] = local_project_path + "houdini/exampleProjects/projectOne"
houdini_cmd = '{} {} {}'.format(houdini_app, houdini_default_file, houdini_default_script)
subprocess.Popen(houdini_cmd)