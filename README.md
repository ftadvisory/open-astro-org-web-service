# OpenAstroWebService
 
Webservice to generate Astrological charts using a trimmed down version of OpenAstro.org (https://github.com/pascallemazurier/openastro-dev) and the full version of Pyswisseph which is a python implementation of swiss ephemeris (https://github.com/astrorigin/pyswisseph).

The source applications were re-engineered to be deployed as a web service with Docker deployment.  All source and configurations for the deployment are included in this repository. 

Consistent with the OpenAstro and Pysswisseph projects, this is published under the GNU Affero General Public License version 3.  See the LICENSE.txt file.

Note that the original swisseph library is distributed under a dual licensing system: GNU Affero General Public License, or Swiss Ephemeris Professional License. For more information, see file libswe/LICENSE.

Instructions to setup (assuming use of VS Code)

- uses ZSH scripts to build (may require changing the permission of these scripts to enable execution)
- Requires python3.9 or higher and a docker environment 
- A valid project is required to run on gcp 
- Setup a virtual Python environment (https://code.visualstudio.com/docs/python/environments)
	python3 -m venv .venv
	source ./.venv/bin/activate

- Confirm that python is installed
	which python
	python --version 

- Setup the development environment
	./setDevEnv.zsh

- To build the python packages run:
	./package-build.zsh

- To deploy to docker and run (on port 5000)
	./docker-build.zsh

	To test 
		http://localhost:5000 
			should return: "Web Service for OpenAstro v1.1.57"

		./test/invokeService.py 
			will return the chart for Joanne Woodward

- To deploy to GCP
	Edit  gcloud-build.zsh to point to the GCP project
	./gloud-build.zsh

	To test 
		http://your-gcp-url 
			should return: "Web Service for OpenAstro v1.1.57"
		
		And after editing invokeService.py to point at the GCP project

		./test/invokeService.py 
			will return the chart for Joanne Woodward