# StringShorten

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue)](https://www.python.org/downloads/)

## Description

StringShorten is a Python package that provides a simple utility for shortening strings. It includes functions to truncate or abbreviate strings, making it useful for tasks like displaying shortened text in UIs, logging, or generating concise summaries.

## Features

- Shorten long strings to a specified length.
- Abbreviate text while preserving essential information.
- Easy-to-use API for text manipulation.

## Installation

You can install StringShorten using pip:

```bash
pip install stringShorten
```
## Usage
```python
from shorten_text.shorten import shorten_text

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
shortened_text = shorten_text(text, max_length=20)
print(shortened_text)
```
## Contributing
Contributions are welcome! Please check the contribution guidelines before submitting pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.