# nerdlerxml

Converts XML to a dictionary. Can take inputs from URL, a file and binary data. To convert XML to a dictionary is more than 80% faster than xmltodict module

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install nerdlerxml.

```bash
pip install nerdlerxml
```

## Usage
Example 1:
```python
from nerdlerxml import nerdlerxml

url = "https://example.org/example.xml"

# returns the dictionary of url
result = nerdlerxml(url=url).to_dict()
```

Example 2:
```python
from nerdlerxml import nerdlerxml

filepath = "example.xml"

# returns the dictionary of url
result = nerdlerxml(filepath=filepath).to_dict()
```

Example 3:
```python
from nerdlerxml import nerdlerxml

filepath = "example.xml"

with open(filepath, "rb") as f:
    data = f.read()

# returns the dictionary of url
result = nerdlerxml(fileobject=data).to_dict()
```

## License
[MIT](https://choosealicense.com/licenses/mit/)