from setuptools import setup
from discdb.__init__ import __version__


setup(
    name="discdb",
    version=__version__,
    author="Hunter",
    description="A simple module to store data in JSON format in discord messages",
    long_description_content_type="text/markdown",
    url="https://github.com/Hunter2807/discdb",
    classifiers=[
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=[
        "discord.py",
    ],
    packages=["discdb"],
    python_requires='>3.6'
)
