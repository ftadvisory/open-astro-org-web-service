# OpenAstroWebService
 
Webservice to generate Astrological charts using a trimmed down version of OpenAstro.org (https://github.com/pascallemazurier/openastro-dev) and the full version of Pyswisseph which is a python implementation of swiss ephemeris (https://github.com/astrorigin/pyswisseph).

The source applications were re-engineered to be deployed as a web service with Docker deployment.  All source and configurations for the deployment are included in this repository. 

Consistent with the OpenAstro and Pysswisseph projects, this is published under the GNU Affero General Public License version 3.  See the LICENSE.txt file.

Note that the original swisseph library is distributed under a dual licensing system: GNU Affero General Public License, or Swiss Ephemeris Professional License. For more information, see file libswe/LICENSE (https://github.com/astrorigin/swisseph/blob/696bda432298d482d27e67a0cf1238920301a7dd/LICENSE).

Instructions to setup (assuming use of VS Code)

- uses ZSH scripts to build (will require changing the permission of these scripts to enable execution)
- Requires Python 3.9 or higher and a docker environment 
- A valid project is required to run on gcp 
- Setup a virtual Python environment (https://code.visualstudio.com/docs/python/environments) in the project's root directory
	- python3 -m venv .venv
	- source ./.venv/bin/activate

- Confirm that Python is installed
	- which python (should point to the virtual environment setup above) 
	- python --version (should be Python 3.9+)

- Change the permissions for the shell scripts
	- chmod 744 *.zsh

- Setup the development environment (loads required packages)
	- ./setDevEnv.zsh

- To build the python packages run:
	- ./package-build.zsh

- To deploy to docker and run (on port 5050)
	- ./docker-build.zsh

- To test the docker deployment
	- http://localhost:5050 
	- will return: "Web Service for OpenAstro v1.1.57"

	- python ./invokeService.py 
	- will return the chart for Joanne Woodward

	- ./test-webservice-and-cleanup.zsh 
	- will install needed packages, test the docker deployment and remove the packages.  Note that this completely removes the relevant packages.  To reinstall them use "setDevEnv.zsh"

- To deploy to GCP - after editing gcloud-build.zsh to point to the GCP project
	- ./gloud-build.zsh

- To test the GCP installation
	- http://your-gcp-url 
	- will return: "Web Service for OpenAstro v1.1.57"
		
	- And after editing invokeService.py to point to the GCP deployment

	- ./test/invokeService.py 
	- will return the chart for Joanne Woodward
