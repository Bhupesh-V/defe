# the following script generates defe CLI distribution
cp -R core defe/core
rm -rf build/
rm -rf dist/
rm -rf defe.egg-info/
python3 setup.py sdist bdist_wheel
rm -rf defe/core/
rm -rf build/
rm -rf defe.egg-info/
twine upload dist/*