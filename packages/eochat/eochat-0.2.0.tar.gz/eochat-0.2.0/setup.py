from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="eochat",
    version="0.2.0",
    license='GPLv3',
    author="First Last, Script Filly",
    author_email="proto_anon_eo@protonmail.com, anonymous.indefinitely@gmail.com",
    description="A CLI chat client for Everfree Outpost",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/EO_utilities/eo-cli-chat",
    project_urls={ "Bug Tracker": "https://gitlab.com/EO_utilities/eo-cli-chat/-/issues", },
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        "Operating System :: OS Independent",
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires=">=3.6",
    py_modules=[],
    install_requires=['tornado', 'aioconsole','toml'],
    scripts=[],
    entry_points={
        'console_scripts': [
            'eochat = eochat.wrapper:main',
        ],
    },
    test_suite='tests',
)
