#!/usr/bin/env python

import os
import logging
import shutil

###############################################################################
    
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

class GeneratePyproject(object):
    """Generate needed pyproject files to use with setuptools"""

    def __init__(self, project_dir,
                 project_prefix="ops-py",
                 toml_filename="pyproject.toml",
                 default_license_file="LICENSE"):
        self.project_dir = project_dir
        self.project_prefix = project_prefix
        self.toml_filename = toml_filename
        self.default_license_file = default_license_file

        self.project_name = ""
        self.src_dir = ""
        self.project_items = []
        self.code_dir_name = ""
        self.init_file = ""
        self.license_file = ""
        self.readme_file = ""
        self.requirements_file = "" 
        self.description = ""


    def verify_project(self):
        if not os.path.isdir(self.project_dir):
            logging.error(f"'{self.project_dir}' directory does not exists.")
            return
        
        src_dir = os.path.join(self.project_dir, "src")
        if not os.path.isdir(src_dir):
            logging.error(f"'src' dir does not exists in '{self.project_dir}' directory.")
            return
        
        self.src_items = os.listdir(src_dir)
        self.src_dir = src_dir
        self.project_items = os.listdir(self.project_dir)
       
        self.set_requirements_file()
        self.set_readme_file() 
        self.set_license_file()
        self.set_version()
        self.set_project_name()
        self.set_description()


    def set_requirements_file(self):
        if "requirements.txt" in self.src_items: 
            self.requirements_file = "requirements.txt"
            return
            
        logging.warning(f"'src' dir in project dir does not contain a 'requirements.txt' file. It should be present in '{self.src_dir}' directory")

    
    def set_readme_file(self):
        for item in self.src_items:
            if item.lower().startswith("readme"):
                self.readme_file = item
                return

        logging.warning(f"'src' dir in project dir does not contain a readme file. It should be present in '{self.src_dir}' directory")
    

    def set_license_file(self):
        for item in self.src_items:
            if item.lower().startswith("license"):
                self.license_file = item
                return

        if os.path.isfile(self.default_license_file):
            self.license_file = "license.txt"
            license_file = os.path.join(self.src_dir, self.license_file)
            shutil.copyfile(self.default_license_file, license_file)

        logging.warning(f"'src' dir in project dir does not contain a license file. Default licence file (MIT) used instead.")


    def set_version(self):
        for item in self.src_items:
            item_path = os.path.join(self.src_dir, item)
            if os.path.isdir(item_path):
                code_files = os.listdir(item_path)
                if "__init__.py" in code_files:
                    self.init_file = os.path.join(item_path, "__init__.py")
                    self.code_dir_name = item
                    break
        
        if not self.code_dir_name:
            logging.error(f"No code directory found in the '{self.src_dir}' directory.")
            return
        
        if not self.init_file:
            logging.error(f"Code directory must include a __init__.py file")
            return
    

    def set_project_name(self):
        project_name = self.project_dir.split("/")[-1]
        if project_name:  
            self.project_name = f"{self.project_prefix}-{project_name}" 


    def set_description(self):
        with open(self.init_file) as f:
            for line in f.readlines():
                if line.startswith("__description__"):
                    self.description = line.split("=")[-1].replace('"','').strip()
                    return

        logging.warning(f"__init__.py file should include a description")
                    

    def write_config_files(self):
        self.verify_project()
        
        setup_data = """#!/usr/bin/env python3

from setuptools import setup

setup()
"""
        setup_file = os.path.join(self.src_dir, "setup.py")
        with open(setup_file, 'w') as f:
            f.write(setup_data)
        
        toml_data = f"""[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[project]
name = "{self.project_name}"
description = "{self.description}"
license = {{file = "{self.license_file}"}}
dynamic = ["version", "readme", "dependencies"]

[tool.setuptools.dynamic]
version = {{attr = "{self.code_dir_name}.__version__"}}
readme = {{file = "{self.readme_file}", content-type = "text/markdown"}}
dependencies = {{file = ["{self.requirements_file}"]}}
"""
        pyproject_file = os.path.join(self.src_dir, self.toml_filename) 
        with open(pyproject_file, 'w') as f:
            f.write(toml_data)
    
    
###############################################################################


if __name__ == '__main__':
    PROJECT_DIR = os.getenv("PROJECT_DIR")
    if not PROJECT_DIR:
        logging.error("PROJECT_DIR not set")
        exit(2) 

    if not os.path.isdir(PROJECT_DIR):
        logging.error("PROJECT_DIR does not exists")
        exit(2) 
    
    gp = GeneratePyproject(PROJECT_DIR)
    gp.write_config_files()
    