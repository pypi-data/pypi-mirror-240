
import io
from setuptools import setup, find_packages

setup(
    name='automate3chapter24',
    version='2023.11.7',
    url='https://github.com/asweigart/automateboringstuff3',
    author='Al Sweigart',
    author_email='al@inventwithpython.com',
    description=('This package installs the latest compatible version of the packages covered in Chapter 24 of Automate the Boring Stuff with Python, 3rd Edition.'),
    long_description='This package installs the latest compatible version of the packages covered in Chapter 24 of Automate the Boring Stuff with Python, 3rd Edition.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'opencv-python==4.8.1.78',
        'numpy==1.26.1',
        'wavio==0.0.8',
        'sounddevice==0.4.6',
        'pygame==2.5.2',
        'playsound==1.3.0',
        'python-vlc==3.0.20123',
    ],
    keywords="automate boring stuff python",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
