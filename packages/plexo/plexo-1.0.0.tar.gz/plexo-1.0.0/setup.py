# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['plexo',
 'plexo.codec',
 'plexo.ganglion',
 'plexo.namespace',
 'plexo.neuron',
 'plexo.schema',
 'plexo.schema.plexo_multicast',
 'plexo.synapse',
 'plexo.typing']

package_data = \
{'': ['*']}

install_requires = \
['capnpy>=0.10.0,<0.11.0',
 'pyrsistent>=0.20.0,<0.21.0',
 'python-jsonschema-objects>=0.5.0,<0.6.0',
 'pyzmq>=25.0.0,<26.0.0',
 'returns>=0.22.0,<0.23.0',
 'typing_extensions>=4.0,<5.0']

setup_kwargs = {
    'name': 'plexo',
    'version': '1.0.0',
    'description': 'Opinionated, reactive, schema-driven, distributed, and strongly-typed message passing',
    'long_description': '# pyplexo\n\n*pyplexo* is the Python implementation of *plexo*. It aims to be an opinionated, reactive, schema-driven, distributed,\nand\nstrongly-typed message passing framework with messages as types. Any type of data interchange format is supported and\ncan be transmitted both to in-process and inter-process listeners.\n\n## plexo\n\n*plexo* is an architecture in which data is transmitted across the network in a way where the receiver is able to\nunderstand the correct type to decode the data into. It does so by assigning type names to a predefined namespace to\ncreate a topic for receivers to subscribe to.\n\nWhile *plexo* is relatively stable and in production use between Python and Rust (\nsee [podping.cloud](https://github.com/Podcastindex-org/podping.cloud)\nand [podping-hivewriter](https://github.com/Podcastindex-org/podping-hivewriter)), the paradigm remains experimental.\nContributions and suggestions are encouraged.\n\n## Why does this exist?\n\nThe goal of the project is to allow data structures to be shared across the network by their type instead of server\nendpoints.  *plexo* implementations receive data structures and sends them to any interested parties subscribed to the\ndata structure\'s type.\n\nIt was originally created and developed for a tiny sake brewing operation. The development of this project enabled us to\nplug in new hardware sensors and data logging devices without the need to reconfigure multiple projects across a variety\nof hardware.\n\nThis was born out of a frustration of spending too much time writing data transformation and validation layers with\nunstructured and/or weakly typed data (JSON without schemas) across multiple languages.  *plexo* tries to solve this\nproblem without controlling the entire stack while avoiding protocol implementation details such as HTTP "REST" APIs.\n\n## Examples\n\nCheck the [examples](examples) for how to use the library -- particularly [axon/inprocess](examples/axon/inprocess) for\nmultiple examples of codec options and [axon/tcp_pair](examples/axon/tcp_pair) for an example of how to send a python\nclass between two networked python processes with pickle or JSON. Note that, while supplying the pickle codec is\nrequired, the *plexus* is smart enough to avoid the expensive process of encoding/decoding for in-process receivers;\ncodecs are only used for external transmission where serialization is required.\n\n[ganglion/plexo_multicast](examples/ganglion/plexo_multicast) provides a basic example of sending a python class\nacross the network over multicast. Each type in is assigned a dedicated multicast address within the `239.255.0.0/16`\nCIDR block as a means to provide generalized, zero configuration network communication without saturating a single\nsocket with unnecessary traffic. An adaptation of the Paxos consensus algorithm is used for the network to agree on\nwhich type is assign to which multicast group.\n',
    'author': 'Alecks Gates',
    'author_email': 'agates@mail.agates.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/plexo/pyplexo/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9.0,<3.12',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
