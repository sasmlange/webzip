from setuptools import setup, find_packages

setup(
    name='webzip',
    version='1.0',
    description='Install python packages from any source on the web',
    author='Maximilian Lange',
    author_email='maxhlange@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'webzip = webzip.installer:action',
        ],
    },
)