import os
from glob import glob
from os.path import basename, splitext

from setuptools import find_packages, setup

setup(
    name="ml_pkg_housing",
    version="0.0.1",
    license="MIT",
    description="An example package for ml project learning",
    author="Vikash Kumar",
    author_email="vikash.kumar@tigeranalytics.com",
    url="http://pypi.python.org/pypi/ml_pkg_housing/",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=[
        "keyword1",
        "keyword2",
        "keyword3",
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    install_requires=[
        "numpy==1.23.2",
        "pandas==1.4.3",
        "scikit-learn==1.1.2",
        "scipy==1.9.0",
    ],
    extras_require={
        ':python_version=="3.8"': ["argparse"],
        "interactive": ["matplotlib>=2.2.0", "jupyter"],
    },
    setup_requires=["flake8"],
    tests_require=["unittest"],
    entry_points={
        "console_scripts": [
            "ml_pkg_housing= ml_pkg_example.ingest_data:data_preprocessing",
        ]
    },
)
