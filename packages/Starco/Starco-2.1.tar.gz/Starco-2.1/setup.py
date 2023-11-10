from setuptools import setup
requires = [
    'cffi==1.15.1',
    'cryptography==41.0.3',
    'pycparser==2.21',
    'beautifulsoup4==4.12.2',
    'lxml==4.9.3',
    'requests==2.31.0',
    'easy-db==0.9.15',
    'hcloud==1.26.0',
    'cloudflare==2.11.6'


]
setup(
    name = 'Starco',
    version='2.1',
    author='Mojtaba Tahmasbi',
    packages=[
        'starco/debug',
        'starco/pkl',
        'starco/scraper',
        'starco/utils',
        'starco/db',
        'starco/hetzner',
        'starco/xray_connctor',
        'starco/cloudflare',
        ],
    install_requires=requires,
)