from setuptools import setup, find_packages, Extension

with open("README.md","r", encoding = 'utf-8') as fp:
	readme = fp.read()

setup(
	name="gmimtools",
	version="0.1.0",
	description="A suite of ground motion intensity measure tools.",
	author="A. Renmin Pretell Ductram",
	author_email='rpretell@unr.edu',
	url="https://github.com/RPretellD/gmimtools",
    long_description=readme,
    
    packages=find_packages(),
	include_package_data=True,
	
    install_requires=["numpy","Cython"],

	license='MIT',
	keywords='gmim',
	classifiers=[
        "Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
	]
)