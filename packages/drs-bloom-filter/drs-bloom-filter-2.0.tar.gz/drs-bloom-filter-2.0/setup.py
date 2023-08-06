
from setuptools import setup, find_packages
setup(
    name="drs-bloom-filter",
    version="2.00",
    packages=find_packages(),
    scripts=['bloom_filter_mod.py'],

    # metadata for upload to PyPI
    author="Daniel Richard Stromberg",
    author_email="strombrg@gmail.com",
    description='Pure Python Bloom Filter module',
    long_description='''
A pure python bloom filter (low storage requirement, probabilistic
set datastructure) is provided.

Includes mmap, in-memory and disk-seek backends.

The user specifies the desired maximum number of elements and the
desired maximum false positive probability, and the module
calculates the rest.
''',
    license = "MIT",
    keywords = "probabilistic set datastructure",
	 url='http://stromberg.dnsalias.org/~strombrg/drs-bloom-filter/',
	 platforms='Cross platform',
	 classifiers=[
		 "Development Status :: 5 - Production/Stable",
		 "Intended Audience :: Developers",
		 "Programming Language :: Python :: 3",
		 ],
)

