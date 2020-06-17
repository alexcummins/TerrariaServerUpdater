from distutils.core import setup

setup(
    name='terrariaServerUpdater',
    version='0.1dev',
    packages=['terrariaServerUpdater', ],
    license='MIT Licence',
    install_requires=[
        "requests",
        "bcrypt",
    ],
    long_description=open('README.md').read(),
)
