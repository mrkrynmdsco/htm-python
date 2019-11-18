
from setuptools import setup, find_packages


with open("RADME.md", 'r') as fh:
    long_description = fh.read()

setup(
    name="htm-python",
    version="0.0.1",
    author="Mark Dasco, Numenta, HTM-Community",
    author_email="mrkrynmdsco@gmail.com",
    description="Python Re-Implementation of HTM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mrkrynmdsco/htm-python",
    packages=find_packages(),
    license="GNU Affero General Public License v3 or later (AGPLv3+)",
    classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
      "Operating System :: Microsoft :: Windows",
      "Operating System :: MacOS :: MacOS X",
      "Operating System :: POSIX :: Linux",
      "Operating System :: POSIX :: BSD",
      "Operating System :: OS Independent",
      # It has to be "5 - Production/Stable" or else pypi rejects it!
      "Development Status :: 5 - Production/Stable",
      "Environment :: Console",
      "Intended Audience :: Science/Research",
      "Intended Audience :: Developers",
      "Intended Audience :: Education",
      "Topic :: Scientific/Engineering :: Artificial Intelligence",
      "Natural Language :: English",
      "Programming Language :: Python"
    ],
    python_requires='>=3.7',
)
