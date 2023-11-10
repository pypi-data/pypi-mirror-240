from setuptools import setup, find_packages

setup(
    name='masklmm',
    version='0.1.0',    
    description='Python Library for MaSk-LMM',
    url='https://github.com/IBM/mask-lmm.git',
    author='Myson Burch, Aritra Bose',
    author_email='myson.burch@ibm.com, a.bose@ibm.com',
    packages=find_packages(),
    install_requires=['numpy',
                      'pandas',
                      'scipy',
                      'pysnptools',                     
                      ],

    classifiers=[
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
    ],
)