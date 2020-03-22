#!/bin/bash

# the following script generates defe package


cp -R core defe/core

# remove already exising distribtuions
rm -rf build/
rm -rf dist/
rm -rf defe.egg-info/

# generate new distribution
python3 setup.py sdist bdist_wheel

# clean up
rm -rf defe/core/
rm -rf build/
rm -rf defe.egg-info/

# upload to pypi
twine upload dist/*