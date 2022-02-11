from setuptools import find_packages, setup

setup(
    name='medcalclib',
    packages=find_packages(include=['medcalclib']),
    version='0.1.1',
    description='Medical formula calculations',
    author='Douglas Kohn',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.0.0'],
    test_suite='tests',
)