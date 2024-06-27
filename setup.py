from setuptools import setup, find_packages

setup(
    name='sorter',
    version='0.1.0',
    packages=find_packages(),
    scripts=['src/sorter.py'],
    install_requires=[
        'watchdog',
    ],
    entry_points={
        'console_scripts': [
            'sorter=sorter:main',
        ],
    },
    author='VulcanX',
    author_email='N/A',
    description='Automatically sort downloaded files into OS-specific directories.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/VulcanX-2003/DownloadSorter',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
