from setuptools import setup

setup(
    name='carcano_foolist',
    version='0.0.1',


    author='Marco Antonio Carcano',
    author_email='mc@carcano.ch',
    description='An example list object tha exploit Pyhon iteratable facilities',
    license= 'GNU Lesser General Public License v3 or later',
    keywords = 'iteratable list',
    url= 'https://github.com/mac-grimoire/python-spells.git',
    project_urls={
        'Bug Tracker': 'https://github.com/mac-grimoire/python-spells.git',
        'Documentation': 'https://github.com/mac-grimoire/python-spells.git',
        'Source Code': 'https://github.com/mac-grimoire/python-spells.git',
    },
    classifiers=[
        'OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)'
    ],

    packages=['carcano.foolist'],
    scripts=['bin/fooapp.py'],
    test_suite='nose.collector',
    tests_require=['nose'],
    data_files=[
        ('bin',['bin/logging.conf']),
        ('bin',['bin/fooapp.rsyslog'])
    ]
)

