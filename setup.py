try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

def getPackages():

    p = []

    with open('requirements.txt', 'r') as f:

        for l in f.read().split('\n'):

            p.append(l)

    return p

setup(
    name='status-fetch',
    version='1.0.0',
    description='Fetch the status of your website',
    author='Status',
    url='https://github.com/status-hub/fetch/',
    packages=[
        'src'
    ],
    entry_points={
        "console_scripts": ["status-fetch=src.cli:cli"],
    },
    install_requires=getPackages(),
    license="GNU",
    zip_safe=False,
    keywords=['status', 'status CLI', 'status-fetch', 'fetch'],
    long_description=readme,
    long_description_content_type="text/markdown",
)