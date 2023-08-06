# graphenum

Introspect a GraphQL endpoint and generate his specification schema with path enumeration.

## Getting Started

It takes only two simple steps to fingerprint an endpoint using GraphDNA.

```bash
pip install graphenum
graphenum -u https://example.com/graphql -o schema.json
```

## Options

GraphEnum supports the following options:

```bash
graphenum \
# url of the GraphQL endpoint
-u/--url https://example.com/graphql \
# input schema file (raw GraphQL schema)
-s/--schema-path schema.json \
# output file name
-o/--output-schema schema.json \
# verbose output
-v/--verbose
```

## Environment Variables

**Logger** - *No effect if you pass your own logger*
| Name | Values  | Default| Behavior|
|------|--------|--------|--------|
| `LOG_FORMAT` | `console`, `json` | `console` | Change the log format accordingly |
| `DEBUG` | `True`, `False` | `False` | Enable debug logging |

## Integration

```python
import logging

from typing import Callable, Dict, Optional, List, Tuple
from graphenum import IntrospectionSchema
from graphenum.entities.internal import Callbacks

async def async_introspect(
    url: str,
    logger: Optional[logging.Logger] = None,
    headers: Optional[Dict[str, str]] = None,
    verbose_mode: bool = False,
    schema_path: Optional[str] = None,
    callbacks: Optional[Dict[Callbacks, List[Callable]]] = None,
) -> Tuple[IntrospectionSchema, aiohttp.ClientResponse]:
    ...

def introspect(
    url: str,
    logger: Optional[logging.Logger] = None,
    headers: Optional[Dict[str, str]] = None,
    verbose_mode: bool = False,
    schema_path: Optional[str] = None,
    callbacks: Optional[Dict[Callbacks, List[Callable]]] = None,
) -> Tuple[IntrospectionSchema, aiohttp.ClientResponse]:
    ...
```

## Local installation

```bash
git clone git@github.com:Escape-Technologies/graphenum.git
cd graphenum
chmod +x ./install-dev.sh
./install-dev.sh
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License ![PyPI - License](https://img.shields.io/pypi/l/GraphDNA)

[MIT](https://choosealicense.com/licenses/mit/)