# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyssandra']

package_data = \
{'': ['*']}

install_requires = \
['case-switcher>=1.3.13,<2.0.0',
 'cassandra-driver>=3.28.0,<4.0.0',
 'pydantic>=2.4.2,<3.0.0']

setup_kwargs = {
    'name': 'pyssandra',
    'version': '0.12.4',
    'description': 'Use pydantic models to create basic CQL queries.',
    'long_description': '# Pyssandra\n\nCassandra object mapper using Pydantic models.\n\n### Example\n\n```python\nimport uuid\n\nfrom cassandra.auth import PlainTextAuthProvider\nfrom cassandra.cluster import Cluster\nfrom pydantic import BaseModel, Field\n\nfrom pyssandra import Pyssandra\n\ncloud_config = {"secure_connect_bundle": "/path/to/secure-connect-dbname.zip"}\nauth_provider = PlainTextAuthProvider(username="user", password="pass")\ncluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)\nsession = cluster.connect()\n\nkeyspace = "test"\ndb = Pyssandra(session, keyspace)\n\n\n@db.table(partition_keys=["id"], index=["first"])\nclass User(BaseModel):\n    """Test user model."""\n\n    id: uuid.UUID = Field(default_factory=uuid.uuid4)\n    first: str\n    last: str\n\n\n# Create DB Table.\ndb[User].sync()\n\n# CRUD Methods.\nuser = User(first="Test", last="User")\nawait db[User].insert(user)\nawait db[User].find_one({"id": user.id})\npage1 = await db[User].find_many(where={"first": "Test"}, page_size=10)\npage2 = await db[User].find_many(where={"first": "Test"}, page_size=10, paging_state=page1.paging_state)\nawait db[User].update(user)\nawait db[User].delete({"id": user.id})\n```\n',
    'author': 'Matthew Burkard',
    'author_email': 'matthewjburkard@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/mburkard/pyssandra',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
