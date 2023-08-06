from pathlib import Path
import setuptools


setuptools.setup(
    name='shipdf',
    long_description=Path('README.md').read_text(),
    version=1.2,
    packages=setuptools.find_packages(exclude=['test', 'data'])
)
