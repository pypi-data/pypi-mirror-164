from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name='P201_Functions',
	version='0.5',
	license='MIT',
	author_email='edward.brash@cnu.edu',
	url='https://github.com/brash99/PhysicsLabs/blob/main/PHYS201L/JupyterNotebooks/P201_Functions.py',
	description='Fitting and Weighted Average Functions for Physics 201/202',
	author='Edward Brash',
	packages=['P201_Functions'],
	long_description=long_description,
	long_description_content_type='text/markdown',
	install_requires=['numpy','matplotlib','scikit-learn','scipy'],
	zip_safe=False)
