from setuptools import setup, find_packages

VERSION = '0.0.3' 
DESCRIPTION = 'Google_Sheets API Wrapper Class'
LONG_DESCRIPTION = 'Google Sheets API Wrapper Class built of gspreads module'
# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="smack_gsheets", 
        version=VERSION,
        author="Mathew Mammen Jacob",
        author_email="<mathew.mammenjacob@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['gspread','gspread_dataframe'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)