import os
import sys
import subprocess
import requests
from private_config import GITHUB_API_TOKEN


project_name = None
config = {
    'react_project': False,
    'github_project': False
}

if len(sys.argv) < 2:
    sys.exit("EXITING: Must give project name as arg")
else:
    project_name = sys.argv[1]
    if(project_name[0] == '-'):
        sys.exit("Project Name: {} cannot start a dash".format(project_name))

    config['react_project'] = ('--react-project' in sys.argv)
    config['github_project'] = ('--github-project' in sys.argv)


confirmation = raw_input("Create Project: {}\nwith config: {}\n (y/n)? ".format(
    project_name, config
))

if (confirmation):
    print("Creating Project")
else:
    sys.exit('EXITING')


project_path = os.path.join(os.path.dirname(__file__), '../{}'.format(project_name))

print("Making project directory at: {}".format(project_path))
try:
    os.mkdir(project_path)
except Exception as e:
    print("Could not make directory {}".format(project_path))
    sys.exit("Error: {}".format(e))


# github section
if(config['github_project']):
    headers = {"authorization": "Bearer {}".format(GITHUB_API_TOKEN)}
    query = """
    {
      repository(owner: "kushalk25", name: "HT6-fashion-app") {
        createdAt
        owner {
          login
          url
        }
        url
      }
    }
    """

    request = requests.post(
        'https://api.github.com/graphql',
        json={'query': query},
        headers=headers
    )
    if request.status_code == 200:
        print(request.json())
    else:
        sys.exit("Query failed to run by returning code of {}. {}".format(request, query))


os.chdir(project_path)

if (config['react_project']):
    print("Creatng React App")
    subprocess.call(["npx", "create-react-app", project_name])
    os.chdir(project_name)

    print("Launching Reach App")
    subprocess.Popen(["npm", "start"])
