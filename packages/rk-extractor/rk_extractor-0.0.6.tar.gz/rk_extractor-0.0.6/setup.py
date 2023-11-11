from setuptools import setup, find_packages

import glob

setup(
    name              = 'rk_extractor',
    version           = '0.0.6',
    description       = 'Used to extract RK from simultaneous fits',
    scripts           = glob.glob('scripts/jobs/*'),
    long_description  = '',
    package_dir       = {'' : 'src'},
    packages          = [''],
    install_requires  = open('requirements.txt').read().splitlines()
)

