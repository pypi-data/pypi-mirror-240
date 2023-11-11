from setuptools import setup, find_packages
from videoclipper.version import __version__

setup(
    name='videoclipper',
    version=__version__,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'videoclipper=videoclipper.videoclipper:main'
        ],
    },
    install_requires=[
        'argparse',
        # Add other dependencies as necessary
    ],
    python_requires='>=3.6',
)
