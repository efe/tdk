from setuptools import setup


setup(
    name='tdk',
    description='A command line tool to query meaning of Turkish word from official dictionary.',
    version='0.1',
    py_modules=['tdk'],
    url='https://github.com/efe/tdk-cli',
    author='Efe Öge',
    license='GPL3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Natural Language :: Turkish',
    ],
    install_requires=[
        'Click',
        'bs4',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'tdk=tdk:cli',
        ],
    },
)