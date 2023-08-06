from setuptools import setup, find_packages


setup(
    name='pypi_publish_rockroll',
    version='0.1',
    license='Apache License 2.0',
    author="Author Name",
    author_email='email@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/beverly0005/pypi_publish',
    keywords='example pypi project',
    #install_requires=[],

)