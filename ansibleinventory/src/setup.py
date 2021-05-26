from setuptools import setup

setup(
    name='carcano_ansibleinventory',
    version='0.0.1',
    install_requires=['PyYAML>=3.12'],

    author='Marco Antonio Carcano',
    author_email='mc@carcano.ch',
    description='Ansible Inventory script and packages',
    license= 'GNU Lesser General Public License v3 or later',
    keywords = 'ansible dynamic inventory',
    url= 'https://github.com/comolago/grymoire-python-spells.git',
    project_urls={
        'Bug Tracker': 'https://github.com/comolago/grymoire-python-spells.git',
        'Documentation': 'https://github.com/comolago/grymoire-python-spells.git',
        'Source Code': 'https://github.com/comolago/grymoire-python-spells.git',
    },
    classifiers=[
        'OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)'
    ],

    packages=['carcano.ansibleinventory'],
    scripts=['bin/ansible_inventory.py'],
    test_suite='nose.collector',
    tests_require=['nose'],
    data_files=[('bin',['bin/ansible_inventory_logging.conf'])]
)
