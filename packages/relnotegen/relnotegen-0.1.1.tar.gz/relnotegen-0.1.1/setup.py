from setuptools import setup, find_packages

with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='relnotegen',
    version='0.1.1',
    description='A tool to generate release notes from a set of markdown files',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Niels Vanspauwen',
    author_email='niels.vanspauwen@gmail.com',
    url='https://github.com/nielsvanspauwen/relnotegen',
    data_files=[('', ['LICENSE'])],
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    project_urls={
        'Source': 'https://github.com/nielsvanspauwen/relnotegen',
        'Tracker': 'https://github.com/nielsvanspauwen/relnotegen/issues',
    },
    keywords='release notes markdown',
    license='MIT',
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'relnotegen = relnotegen.relnotegen:main'
        ]
    },
)
