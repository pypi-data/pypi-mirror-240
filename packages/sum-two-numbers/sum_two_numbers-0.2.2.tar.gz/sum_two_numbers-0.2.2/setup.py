from setuptools import setup, find_packages

setup(
    name='sum_two_numbers',
    version='0.2.2',
    packages=find_packages(),
    install_requires=[
        # Any dependencies your package might have
    ],
    entry_points={
        'console_scripts': [
            'sum_two_numbers = sum_two_numbers.calculator:main',
        ],
    },
)
