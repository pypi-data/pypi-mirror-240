from setuptools import setup, find_packages


setup(
    name='subprocess_executor',
    version='1.0.1',
    author='Dušan Mitrović',
    author_email='dusanmitrovic@elfak.rs',
    url='https://github.com/dusanmitrovic98/python_subprocess_executor.git',
    packages=['subprocess_executor'],
    install_requires=find_packages(),
    description='Python Subprocess Executor Package',
    long_description="""
    This Python package provides a convenient way to execute subprocess commands either 
    consecutively or in parallel, along with logging the output. It includes features 
    for handling concurrent subprocess execution using multiprocessing.

    Features:
    - Execute subprocess commands and capture their output.
    - Log the execution of each command, including any errors.
    - Run multiple subprocess commands consecutively.
    - Run multiple subprocess commands in parallel with adjustable pool size.

    Usage:
    You can use this package to streamline the execution of subprocess commands and 
    efficiently manage their output. It's particularly useful for tasks that involve 
    running multiple external commands in a Python script.

    For usage instructions and more details, please refer to the project's documentation 
    and README.

    GitHub Repository: https://github.com/dusanmitrovic98/python_subprocess_executor.git
    """,
    classifiers=[
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Operating System :: OS Independent',
    'Environment :: Console',
    'Topic :: System :: Shells',
    'Topic :: Utilities'],
)