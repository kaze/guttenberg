from setuptools import setup, find_packages


setup(
    name='guttenberg-search',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'pluggy',
        'pygments',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        guttenberg=guttenberg_search.main:cli
    ''',
)
