from setuptools import setup, find_packages

setup(
    name = 'PyOpenGraph',
    version = '0.2',
    description = 'PyOpenGraph is a library written in Python for parsing Open Graph protocol information from web sites.',
    author = 'Gerson Minichiello',
    author_email = 'gerson.minichiello@gmail.com',
    url='http://github.com/minichiello/PyOpenGraph',
    download_url = 'http://pypi.python.org/pypi/PyOpenGraph',
    platforms = 'Any',
    license = 'MIT License',
    packages = find_packages(),
    long_description=open("README.md").read(),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
