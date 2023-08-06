import setuptools

with open("README.md") as file:
    description = file.read()

setuptools.setup(
    name="packagechecker",
    version="2.0",
    author="OneEyedDancer",
    description="Проверка необходимых пакетов, и их установка",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://codeberg.org/OneEyedDancer/python-package-checker.git",
    packages=['packagechecker'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
