from setuptools import setup, find_packages


setup(
    name="decisions_tree",
    version="0.1.0",
    author="Juan D. Velasquez",
    author_email="jdvelasq@unal.edu.co",
    license="MIT",
    url="http://github.com/jdvelasq/decisions-tree",
    description="Decision Analysis in Python",
    long_description="Decisoion Tree Analysis in Python",
    keywords="analytics",
    platforms="any",
    provides=["decisions_tree"],
    install_requires=[
        "numpy",
        "matplotlib",
    ],
    packages=find_packages(),
    package_dir={"decisions_tree": "decisions_tree"},
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
