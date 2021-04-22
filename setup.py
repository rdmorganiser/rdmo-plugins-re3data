import re

from setuptools import find_packages, setup

# get metadata from mudule using a regexp
with open('rdmo_re3data/__init__.py') as f:
    metadata = dict(re.findall(r'__(.*)__ = [\']([^\']*)[\']', f.read()))

setup(
    name=metadata['title'],
    version=metadata['version'],
    author=metadata['author'],
    author_email=metadata['email'],
    maintainer=metadata['author'],
    maintainer_email=metadata['email'],
    license=metadata['license'],
    url='https://github.com/rdmorganiser/rdmo-plugins',
    description=u'The dynamic re3data optionset will query re3data.org for repositories that match the research field of the project.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5'
    ],
    packages=find_packages(),
    include_package_data=True
)
