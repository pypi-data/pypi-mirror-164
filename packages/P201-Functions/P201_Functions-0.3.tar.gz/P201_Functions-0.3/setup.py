from setuptools import setup, find_packages

setup(name='P201_Functions',
	version='0.3',
	license='MIT',
	author_email='edward.brash@cnu.edu',
	url='https://github.com/brash99/PhysicsLabs/blob/main/PHYS201L/JupyterNotebooks/P201_Functions.py',
	description='Fitting and Weighted Average Functions for Physics 201/202',
	author='Edward Brash',
	packages=['P201_Functions'],
	install_requires=['numpy','matplotlib','scikit-learn','scipy'],
	zip_safe=False)
