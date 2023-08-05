from setuptools import setup

from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="htcollector",
    version="0.1.10",
    description="Tools to log updates from Shelly HT devices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://varkenvarken.github.io/shellyhtcollector2/",
    author="varkenvarken",
    author_email="test@example.com",
    license="GPLv3",
    packages=["htcollector"],
    python_requires=">=3.8",
    install_requires=["mariadb==1.1.4", "python-dateutil==2.8.2"],
    extras_require={"graph": ["numpy==1.23.1", "matplotlib==3.5.3"]},
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
