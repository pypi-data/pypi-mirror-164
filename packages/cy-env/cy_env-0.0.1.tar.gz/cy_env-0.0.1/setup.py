import setuptools
from pathlib import Path

setuptools.setup(
    name='cy_env',
    version='0.0.1',
    description="A OpenAI Gym Env for cy",
    long_description=Path("README.md").read_text(),
    long_description_conent_type="text/markdown",
    packages=setuptools.find_packages(include="cy_env"),
    install_require=['gym']
)