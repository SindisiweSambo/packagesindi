from setuptools import setup, find_packages

setup(
    name='packagesindi',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<SindisiweSambo>/<packagesindi>',
    author='<Sindisiwe Sambo>',
    author_email='<prommy95@gmail.com>'
)
