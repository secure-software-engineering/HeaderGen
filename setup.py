import setuptools

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setuptools.setup(
    name='headergen',
    version='0.1.0',    
    description='HeaderGen: Automated cell header generator',
    url='',
    author='',
    author_email='',
    packages=setuptools.find_packages(),
    install_requires=[requirements],
    entry_points = '''
        [console_scripts]
        headergen=cli:generate
    '''
)
