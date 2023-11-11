# Pyssandra

Cassandra object mapper using Pydantic models.

### Example

```python
import uuid

from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
from pydantic import BaseModel, Field

from pyssandra import Pyssandra

cloud_config = {"secure_connect_bundle": "/path/to/secure-connect-dbname.zip"}
auth_provider = PlainTextAuthProvider(username="user", password="pass")
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

keyspace = "test"
db = Pyssandra(session, keyspace)


@db.table(partition_keys=["id"], index=["first"])
class User(BaseModel):
    """Test user model."""

    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    first: str
    last: str


# Create DB Table.
db[User].sync()

# CRUD Methods.
user = User(first="Test", last="User")
await db[User].insert(user)
await db[User].find_one({"id": user.id})
page1 = await db[User].find_many(where={"first": "Test"}, page_size=10)
page2 = await db[User].find_many(where={"first": "Test"}, page_size=10, paging_state=page1.paging_state)
await db[User].update(user)
await db[User].delete({"id": user.id})
```
