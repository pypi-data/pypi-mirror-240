from setuptools import setup
requires = [
    'cffi==1.15.1',
    'cryptography==41.0.3',
    'pycparser==2.21',
    'beautifulsoup4==4.12.2',
    'lxml==4.9.3',
    'requests==2.31.0',
]
setup(
    name = 'PyStarco',
    version='1',
    author='Mojtaba Tahmasbi',
    packages=[
        'pystarco/debug',
        'pystarco/pkl',
        'pystarco/scraper',
        'pystarco/utils',
        ],
    install_requires=requires,
)