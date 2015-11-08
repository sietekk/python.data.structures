from setuptools import setup, find_packages

setup(name='python.data.structures',
    version='0.0.1',
    description=('Data structures examples from Problem Solving with '
                 'Algorithms and Data Structures using Python, Second Edition')
    long_description = open('README.rst', 'r').read(),
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
    ],
    keywords='python data structures algorithms',
    url='https://github.com/sietekk/python.data.structures',
    author='Michael Conroy',
    author_email='sietekk@gmail.com',
    license='MIT',
    package_dir = {'': 'src'},
    packages = find_packages(
        where='src', exclude=["tests", "tests.*"]
    ),
    #install_requires=[],
    #test_suite=''
    #tests_require=[],
    #entry_points={},
    include_package_data=True,
    zip_safe=False)
