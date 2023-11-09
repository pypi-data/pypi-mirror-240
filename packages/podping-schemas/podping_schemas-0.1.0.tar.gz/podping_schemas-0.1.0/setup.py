# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['podping_schemas']

package_data = \
{'': ['*'],
 'podping_schemas': ['org/podcastindex/podping/hivewriter/podping_hive_transaction.capnp',
                     'org/podcastindex/podping/hivewriter/podping_hive_transaction.capnp',
                     'org/podcastindex/podping/hivewriter/podping_hive_write.capnp',
                     'org/podcastindex/podping/hivewriter/podping_hive_write.capnp',
                     'org/podcastindex/podping/podping.capnp',
                     'org/podcastindex/podping/podping.capnp',
                     'org/podcastindex/podping/podping.capnp',
                     'org/podcastindex/podping/podping.capnp',
                     'org/podcastindex/podping/podping.capnp',
                     'org/podcastindex/podping/podping_medium.capnp',
                     'org/podcastindex/podping/podping_medium.capnp',
                     'org/podcastindex/podping/podping_medium.capnp',
                     'org/podcastindex/podping/podping_medium.capnp',
                     'org/podcastindex/podping/podping_medium.capnp',
                     'org/podcastindex/podping/podping_reason.capnp',
                     'org/podcastindex/podping/podping_reason.capnp',
                     'org/podcastindex/podping/podping_reason.capnp',
                     'org/podcastindex/podping/podping_reason.capnp',
                     'org/podcastindex/podping/podping_reason.capnp',
                     'org/podcastindex/podping/podping_write.capnp',
                     'org/podcastindex/podping/podping_write.capnp',
                     'org/podcastindex/podping/podping_write.capnp',
                     'org/podcastindex/podping/podping_write.capnp',
                     'org/podcastindex/podping/podping_write.capnp',
                     'org/podcastindex/podping/podping_write_error.capnp',
                     'org/podcastindex/podping/podping_write_error.capnp',
                     'org/podcastindex/podping/podping_write_error.capnp',
                     'org/podcastindex/podping/podping_write_error.capnp',
                     'org/podcastindex/podping/podping_write_error.capnp']}

install_requires = \
['capnpy>=0.10.0,<0.11.0']

setup_kwargs = {
    'name': 'podping-schemas',
    'version': '0.1.0',
    'description': '',
    'long_description': '# podping-schemas-python\n\nPython schema files for Podping',
    'author': 'Alecks Gates',
    'author_email': 'agates@mail.agates.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
