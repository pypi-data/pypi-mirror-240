from setuptools import setup

from DataHub import __version__

setup(
    name='digivis-datahub',
    version=__version__,

    url='https://github.com/anton04/Datahub',
    author='Anton Gustafsson',
    author_email='anton.gustafsson@ri.se',
    description='A package for handeling multiple MQTT connections',

    py_modules=['DataHub'],
)
