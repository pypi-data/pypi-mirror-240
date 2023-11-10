from setuptools import setup

setup(
    name='manoj-server',
    version='1.0.1',
    author='Manoj',
    author_email='mmanoj20037@gmail.com',
    description='This is personal server',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'start-server = manoj_server.manoj_server:print_banner',
        ],
    },
    classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
)
