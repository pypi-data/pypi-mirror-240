from setuptools import find_packages, setup

setup(
    name='primeclassify',
    packages=find_packages(include=['primeclassify']),
    version='0.1.3',
    description='Prime number classifications',
    author='Rich Holmes',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
