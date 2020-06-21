from distutils.core import setup

setup(
    name='terrariaServerUpdater',
    version='0.1dev',
    packages=['terrariaServerUpdater', ],
    license='MIT Licence',
    author='Alex Cummins',
    install_requires=[
        "requests",
        'beautifulsoup4',
    ],
    long_description=open('README.md').read(),
)
