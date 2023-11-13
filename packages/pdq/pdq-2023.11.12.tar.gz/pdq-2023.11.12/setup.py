from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='pdq',  # required
    version='2023.11.12',
    description='pdq',
    long_description=long_description,
    author='Feng Zhu',
    author_email='infnorm@outlook.com',
    url='https://github.com/fzhu2e/pdq',
    packages=find_packages(),
    include_package_data=True,
    license='BSD-3',
    zip_safe=False,
    keywords='pdq',
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
    ],
)
