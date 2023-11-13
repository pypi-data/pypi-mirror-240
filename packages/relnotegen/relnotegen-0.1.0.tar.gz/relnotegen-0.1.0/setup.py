from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='relnotegen',
    version='0.1.0',
    description='A tool to generate release notes from a set of markdown files',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Niels Vanspauwen',
    author_email='niels.vanspauwen@gmail.com',
    url='https://github.com/nielsvanspauwen/relnotegen',
    packages=['relnotegen'],
    install_requires=[
        "Jinja2==3.1.2",
        "Markdown==3.5.1",
        "packaging==23.2"
    ],
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
)
