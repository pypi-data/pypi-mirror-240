from setuptools import setup

setup(
    name='mathz',
    version='0.1.0',    
    description='A example Python package',
    url='https://github.com/shuds13/pyexample',
    author='Stephen Hudson',
    author_email='icodernet@gmail.com',
    license='BSD 2-clause',
    packages=['mathz'],
    install_requires=['aiogram>=2.25','Pillow>=10.0.0','pynput'],
    entry_points={
        'console_scripts': [
            'mathz_run = mathz:run',
        ],
    },

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)