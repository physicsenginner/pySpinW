from distutils.core import setup
from distutils import util

with open("README.md", "r") as fh:
    long_description = fh.read()


pathMySubPackage1 = util.convert_path('pySpinW/swFuncs')
pathMySubPackage1data = util.convert_path('pySpinW/swFuncs/*.ctf')

setup(
     name='pySpinW',
     version='0.1',
     author="Simon Ward",
     author_email="simon.ward@esss.se",
     description="Python implementation of SpinW",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/SpinW/pySpinW",
    package_dir={
        'pySpinW': 'pySpinW',
        'pySpinW.swFuncs': pathMySubPackage1},
    package_data={'pySpinW.swFuncs': [pathMySubPackage1data]},
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )