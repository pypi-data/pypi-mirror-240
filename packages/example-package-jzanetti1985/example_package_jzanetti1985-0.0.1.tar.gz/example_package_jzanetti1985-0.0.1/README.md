step 1: python setup.py sdist bdist_wheel
step 2: pip install .
step 3: pip install twine
step 4: twine upload dist/*


1: python3 -m pip install --upgrade build
2. python3 -m build