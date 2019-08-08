from setuptools import setup


version = '1.0.0'
author = 'jieggii'
description = ''  # todo

with open('README.md', 'r') as file:
    long_description = file.read()

setup(
    name='mc',
    license='MIT',
    python_requires='>=3',
    version=version,
    author=author,
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jieggii/mc',
    author_email='jieggii@protonmail.com',
    packages=['mc'],
    project_urls={
        'Documentation': 'https://github.com/jieggii/mc/blob/master/docs/README.md',
        'Source': 'https://github.com/jieggii/mc',
        'Tracker': 'https://github.com/jieggii/mc/issues',
    },
)
