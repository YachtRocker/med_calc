from setuptools import find_packages, setup

setup(
    name='medcalclib',
    packages=find_packages(include=['medcalclib']),
    version='0.1.5',
    description='Medical formula calculations',
    author='D Kohn',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)