from setuptools import setup,find_packages
import os

# reading long description from file 
with open('Description.txt') as file: 
	long_description = file.read() 


# specify requirements of your package here 
REQUIREMENTS = ['requests'] 

# some more details 
CLASSIFIERS = [ 
	'Development Status :: 4 - Beta', 
	'Intended Audience :: Developers', 
	'Topic :: Internet', 
	'License :: OSI Approved :: MIT License', 
	'Programming Language :: Python :: 3', 
	] 

# calling the setup function 
setup(name='Ascento', 
	version='1.0.0', 
	description='This Package helps to create unique key (foriegn key) and droping the different type of null values, encoding and decoding', 
	long_description=long_description, 
	url='https://github.com/TejaAi/Ascento', 
	author='TejaSwaroop', 
	author_email='teja136@hotmail.com', 
	license='MIT', 
	packages=['TS'], 
	classifiers=CLASSIFIERS, 
	install_requires=REQUIREMENTS, 
	keywords=['Ascento','Unique_Key_Generator','NullValueDropper']
	) 
