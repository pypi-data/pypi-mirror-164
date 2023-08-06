from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="eochat-qt",
    version="0.2.0",
    license='GPLv3',
    author="Script Filly",
    author_email="anonymous.indefinitely@gmail.com",
    description="Featureful GUI client for Everfree Outpost",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/script-anon/eo-qt6-chat",
    project_urls={ "Bug Tracker": "https://gitlab.com/script-anon/eo-qt6-chat/-/issues", },
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        "Operating System :: OS Independent",
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires=">=3.6",
    py_modules=['eochat_qt.config', 'eochat_qt.eo_defs', 'eochat_qt.helpers', 'eochat_qt.mainwindow', 'eochat_qt.main'],
    install_requires=['eochat', 'tornado', 'pyside6','toml'],
    scripts=[],
    entry_points={
        'console_scripts': [
            'eochat-qt = eochat_qt.main:main',
        ],
    },
    test_suite='tests',
)
