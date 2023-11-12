import setuptools

setuptools.setup(
    name="ConsoleMasterPy",
    version="1.0.5",
    author="Ronchetti Ezequiel Nicolás",
    author_email="RonchettiEzequielNicolas@hotmail.com",
    description="Console/Terminal functionality",
    long_description="Console/Terminal functionality",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        'cursor>=1.3.5',
        'sty>=1.0.4',
    ],
)
