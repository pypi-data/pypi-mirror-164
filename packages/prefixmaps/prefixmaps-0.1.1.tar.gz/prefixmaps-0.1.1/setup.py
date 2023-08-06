# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['prefixmaps',
 'prefixmaps.data',
 'prefixmaps.datamodel',
 'prefixmaps.ingest',
 'prefixmaps.io']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0']

entry_points = \
{'console_scripts': ['slurp-prefixmaps = prefixmaps.ingest.etl_runner:cli']}

setup_kwargs = {
    'name': 'prefixmaps',
    'version': '0.1.1',
    'description': '',
    'long_description': '# prefixmaps\n\nA python library for retrieving semantic prefix maps\n\nA semantic prefix map will map a a prefix (e.g. `skos`) to a namespace (e.g `http://www.w3.org/2004/02/skos/core#`)\n\nThis library is designed to satisfy the following requirements\n\n- coverage of prefixes from multiple different domains\n- multiple authorities\n- preferred semantic namespace is prioritized over web URLs\n- authority preferred prefix is prioritized\n- lightweight\n- network-independence\n- versioned prefix maps\n- ability to retrieve latest from external authority on network\n\n## Installation\n\n```\npip install prefixmaps\n```\n\n## Usage\n\nto use in combination with [curies](https://github.com/cthoyt/curies) library:\n\n```python\nfrom prefixmaps.io.parser import load_context, load_multi_context\nfrom curies import Converter\n\nctxt = load_multi_context(["obo", "bioregistry.upper", "linked_data", "prefixcc"])\nconverter = Converter.from_prefix_map(ctxt.as_dict())\n\n>>> converter.expand("CHEBI:1")\n\'http://purl.obolibrary.org/obo/CHEBI_1\'\n>>> converter.expand("GEO:1")\n\'http://purl.obolibrary.org/obo/GEO_1\'\n>>> converter.expand("owl:Class")\n\'http://www.w3.org/2002/07/owl#Class\'\n>>> converter.expand("FlyBase:FBgn123")\n\'http://identifiers.org/fb/FBgn123\'\n```\n\n### Refresh\n\nBy default this will make use of metadata distributed alongside the package. This has certain advantages in terms\nof reproducibility, but it means if a new ontology or prefix is added to an upstream source you won\'t see this.\n\nTo refresh and use the latest upstream:\n\n```python\nctxt = load_context("obo", refresh=True)\n```\n\n### Order\n\norder is significant - sources listed first will take priority. The as_dict method ensures that the map is bijective\n\n## Contexts\n\nSee [contexts.curated.yaml](src/prefixmaps/data/contexts.curated.yaml)\n\nSee the description fields\n',
    'author': 'cmungall',
    'author_email': 'cjm@berkeleybop.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
