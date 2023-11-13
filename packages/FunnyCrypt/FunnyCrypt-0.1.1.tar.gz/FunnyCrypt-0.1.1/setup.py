from setuptools import setup

setup(
    name='FunnyCrypt',
    version='0.1.1',
    packages=['FunnyCrypt'],
    entry_points={
        'console_scripts': [
            'FunnyCrypt=FunnyCrypt.__main__:main',
        ],
    },
    install_requires=[
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
