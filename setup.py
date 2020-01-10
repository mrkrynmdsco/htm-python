
from setuptools import setup, find_packages


with open("RADME.md", 'r') as fh:
    long_description = fh.read()

setup(
    name="htm-python",
    version="0.0.1",
    author="Mark Dasco",
    author_email="mrkrynmdsco@gmail.com",
    description="Python Re-Implementation of HTM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mrkrynmdsco/htm-python",
    packages=find_packages(),
    license="GNU Affero General Public License v3 or later (AGPLv3+)",
    python_requires='>=3.7',
)
