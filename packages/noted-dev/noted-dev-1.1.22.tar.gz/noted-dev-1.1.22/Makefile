# © Copyright 2022 CERN. This software is distributed under the terms of
# the GNU General Public Licence version 3 (GPL Version 3), copied verbatim
# in the file "LICENCE.txt". In applying this licence, CERN does not waive
# the privileges and immunities granted to it by virtue of its status as an
# Intergovernmental Organization or submit itself to any jurisdiction.

# Steps to install NOTED using a virtual environment:
# ubuntu@pr1:~$ sudo apt-get update
# ubuntu@pr1:~$ sudo apt-get upgrade
# ubuntu@pr1:~$ sudo apt-get install python3-pip
# ubuntu@pr1:~$ pip3 install virtualenv 
# ubuntu@pr1:~$ python3 -m venv venv-noted
# ubuntu@pr1:~$ . venv-noted/bin/activate
# (venv-noted) ubuntu@pr1:~$ python3 -m pip install noted-dev
# (venv-noted) ubuntu@pr1:~$ find . -name Makefile
# Result: ./venv-noted/lib/python3.8/site-packages/noted/Makefile
# (venv-noted) ubuntu@pr1:~$ make -C ./venv-noted/lib/python3.8/site-packages/noted/ build_linux
# Enter your authentication token
# (venv-noted) ubuntu@pr1:~$ nano noted/config/config.yaml
# Write your config file
# (venv-noted) ubuntu@pr1:~$ noted noted/config/config.yaml

build_linux:
	sudo apt-get update
	sudo apt-get upgrade
	sudo apt-get install python3-pip
	make install_noted

build_darwin:
	brew update
	brew upgrade
	brew install python3
	make install_noted

build_centos:
	yum update
	yum upgrade
	yum install python3-pip
	make install_noted

CONFIG_FILE := $(shell find . -name config-example.yaml)
PARAMS_FILE := $(shell find . -name params.ini)
SENSE1_FILE := $(shell find . -name sense-provision.sh)
SENSE2_FILE := $(shell find . -name sense-cancel.sh)

install_noted:
	pip3 install --upgrade pip
	pip3 install pyyaml
	pip3 install pandas
	pip3 install sense-o-api
	sudo apt-get install sendmail
	@echo "Creating folder structure for NOTED:"
	mkdir $(HOME)/noted
	mkdir $(HOME)/noted/logs
	mkdir $(HOME)/noted/config
	mkdir $(HOME)/noted/query
	mkdir $(HOME)/noted/transfers
	mkdir $(HOME)/noted/sense-o
	mkdir $(HOME)/noted/params
	cp $(CONFIG_FILE) $(HOME)/noted/config
	cp $(SENSE1_FILE) $(HOME)/noted/sense-o
	cp $(SENSE2_FILE) $(HOME)/noted/sense-o
	@echo "" >> $(PARAMS_FILE)
	@echo "[AUTH TOKEN]" >> $(PARAMS_FILE)
	@echo "; Authorization token to access CERN Grafana Proxy [TO BE COMPLETED BY THE USER]" >> $(PARAMS_FILE)
	@read -p "Enter your authentication token:" auth; \
	echo "auth_token = $${auth}" >> $(PARAMS_FILE)
	@echo "" >> $(PARAMS_FILE)
	@echo "[CMD]" >> $(PARAMS_FILE)
	@echo "; Curl command to query in elastic search" >> $(PARAMS_FILE)
	@echo "cmd = curl -s -X POST \"\$${FTS PARAMETERS:url_fts_raw_queue}\" -H \"Authorization: Bearer \$${AUTH TOKEN:auth_token}\" -H 'Content-Type: application/json' --data-binary \"@\$${QUERY PARAMETERS:filename_src_query}\"" >> $(PARAMS_FILE)
	@echo "" >> $(PARAMS_FILE)
	@echo ""
	cp $(PARAMS_FILE) $(HOME)/noted/params
	noted -h
	@echo ""
	@echo "Finished the installation of NOTED: a framework to optimise network traffic via the analysis of data from File Transfer Services.\n"

# Create venv to build package:
# python3 -m venv venv-noted
# . venv-noted/bin/activate
# ./venv-noted/bin/python3 -m pip install --upgrade pip
build_package_linux:
	python3 -m pip install --upgrade pip
	python3 -m pip install wheel
	python3 -m pip install build
	cp Makefile src/noted/
	sudo python3 -m build --sdist --wheel
	rm -rf src/noted/Makefile

# Create venv to build package:
# python3 -m venv venv-noted
# . venv-noted/bin/activate
# ./venv-noted/bin/python3 -m pip install --upgrade pip
build_package_centos:
	python3 -m pip install --upgrade pip
	python3 -m pip install build
	sudo python setup.py bdist_rpm

check_package:
	python3 -m twine check dist/*

upload_package_testpypi:
	python3 -m twine upload --repository testpypi dist/*

upload_package_pypi:
	python3 -m twine upload dist/*

# python3 -m venv venv-noted
# . venv-noted/bin/activate
# ./venv-noted/bin/python3 -m pip install --upgrade pip
install_dev_mode:
	sudo python3 setup.py install

# python3 -m venv venv-noted
# . venv-noted/bin/activate
# ./venv-noted/bin/python3 -m pip install --upgrade pip
clean:
	sudo rm -rf build/
	sudo rm -rf dist/
