import os
import sys
import subprocess


project_name = None

if len(sys.argv) < 2:
    sys.exit("EXITING: Must give project name as arg")
else:
    project_name = sys.argv[1]

project_path = os.path.join(os.path.dirname(__file__), '../{}'.format(project_name))

print("project_name is: {}".format(project_path))
os.mkdir(project_path)
os.chdir(project_path)

subprocess.call(["npx", "create-react-app", project_name])
os.chdir(project_name)
subprocess.call(["npm", "start"])
