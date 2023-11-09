# arc-vector-python
Python library and client for arc-vector database

## Installation

```
// remote install
pip install arc-vector-python

// local install by package
pip install arc_vector_python-1.6.2.tar.gz
```
## Features
1. Type hints for all API methods
2. Local mode - use same API without running server
3. REST and gRPC support
4. Minimal dependencies

## Connect to ArcVector Server
To connect to Qdrant server, simply specify host and port:

```
from arc_vector_client import ArcVectorClient
from arc_vector_client.models import Distance, VectorParams
# REST
client = ArcVectorClient(url="http://localhost:8333")
# gRPC
client = ArcVectorClient(host="localhost", grpc_port=8334, prefer_grpc=True)
```

## Async client

Starting from version 1.6.2, all python client methods are available in async version.

To use it, just import `AsyncArcVectorClient` instead of `ArcVectorClient`:

```Python
from arc_vector_client import AsyncArcVectorClient, models
import numpy as np
import asyncio

async def main():
    # Your async code using ArcVectorClient might be put here
    client = AsyncArcVectorClient(url="http://localhost:8333")
    # client = AsyncArcVectorClient(host="localhost", grpc_port=8334, prefer_grpc=True)
    await client.create_collection(
        collection_name="my_collection",
        vectors_config=models.VectorParams(size=10, distance=models.Distance.COSINE),
    )

    await client.upsert(
        collection_name="my_collection",
        points=[
            models.PointStruct(
                id=i,
                vector=np.random.rand(10).tolist(),
            )
            for i in range(100)
        ],
    )

    res = await client.search(
        collection_name="my_collection",
        query_vector=np.random.rand(10).tolist(),  # type: ignore
        limit=10,
    )

    print(res)

asyncio.run(main())
```

Both, gRPC and REST API are supported in async mode.
More examples can be found [here](./tests/test_async_arc_vector_client.py).
