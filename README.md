# XenTokenizer

A high-performance, multilingual tokenizer based on the Qwen architecture, optimized for handling diverse languages including Indian languages and Greek.

## Features

- 🚀 **High Performance**: Processes over 900k tokens/second on CPU
- 🌍 **Multilingual**: Supports 10+ Indian languages, English, and Greek
- 🔧 **Easy Integration**: Built on top of Hugging Face's `PreTrainedTokenizerFast`
- 🛠️ **Special Tokens**: Built-in support for chat, vision, and task-specific tokens

## Installation

```bash
# Basic installation
pip install xen-tokenizer

# With Azure support for processing parquet files
pip install xen-tokenizer[azure]

# For development
pip install xen-tokenizer[dev]
```

## Quick Start

```python
from xen_tokenizer import XenTokenizerFast

# Initialize the tokenizer
tokenizer = XenTokenizerFast(tokenizer_file="tokenizer.json")

# Tokenize text
text = "Hello, world! Γειά σας! नमस्ते!"
tokens = tokenizer.encode(text)
print(tokens)

# Decode back to text
decoded = tokenizer.decode(tokens)
print(decoded)
```

## Azure Integration

Process parquet files directly from Azure Blob Storage:

```python
from xen_tokenizer.processor import AzureParquetProcessor

processor = AzureParquetProcessor(
    connection_string="your_connection_string",
    container_name="your_container",
    input_prefix="raw_data/",
    output_prefix="processed_data/"
)

# Process all parquet files
processor.process_all()
```

## Development

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/xen-tokenizer.git
   cd xen-tokenizer
   ```

2. Install in development mode:
   ```bash
   pip install -e .[dev]
   ```

3. Run tests:
   ```bash
   pytest
   ```

## License

MIT
# XenTokeniser

> **IMPORTANT**: This is a private project for XenArcAI internal use only. Unauthorized use, distribution, or modification is strictly prohibited.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

XenTokeniser is a high-performance, multilingual tokenizer developed exclusively for XenArcAI's internal NLP workflows. It provides fast tokenization with support for parallel processing and automatic resource management.

**Confidential**: This project and its contents are proprietary and confidential information of XenArcAI.

## Features

- 🚀 **Blazing Fast**: Optimized for performance with parallel processing
- 🌍 **Multilingual**: Supports multiple languages out of the box
- ⚡ **Efficient**: Low memory footprint with smart batching
- 🔄 **Hugging Face Compatible**: Seamless integration with the Transformers library
- 🛠️ **Configurable**: Customize tokenization parameters to fit your needs
- 📊 **Progress Tracking**: Built-in progress bars for long-running tasks

## Installation

```bash
pip install xen-tokenizer
```

Or install from source:

```bash
git clone https://github.com/XenArcAI/XenTokeniser.git
cd XenTokeniser
pip install -e .
```

## Quick Start

```python
from xen_tokenizer import XenTokenizerFast, TokenizerConfig

# Initialize with default config
tokenizer = XenTokenizerFast(tokenizer_file="tokenizer.json")

# Tokenize text
text = "XenTokeniser is fast and efficient!"
encoded = tokenizer.encode(text)
decoded = tokenizer.decode(encoded)

print(f"Encoded: {encoded}")
print(f"Decoded: {decoded}")
```

## Advanced Usage

### Custom Configuration

```python
config = TokenizerConfig(
    max_length=512,
    pad_token="[PAD]",
    eos_token="</s>",
    bos_token="<s>",
    unk_token="[UNK]"
)

tokenizer = XenTokenizerFast(
    tokenizer_file="tokenizer.json",
    config=config
)
```

### Batch Processing

```python
texts = ["First text", "Second text", "..."] * 1000

# Process in batches
batch_size = 32
for i in range(0, len(texts), batch_size):
    batch = texts[i:i + batch_size]
    encoded = tokenizer.batch_encode_plus(
        batch,
        padding='max_length',
        truncation=True,
        max_length=512,
        return_tensors='pt'
    )
    # Process your batch...
```

## Google Colab Examples

We provide ready-to-run Colab notebooks:

1. [Quick Start](examples/colab_quickstart.py) - Basic usage
2. [Advanced Usage](examples/colab_advanced_usage.py) - With parallel processing and dataset handling

## Development

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/XenArcAI/XenTokeniser.git
   cd XenTokeniser
   ```

2. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

### Running Tests

```bash
pytest tests/
```

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on how to submit pull requests.

## License

This is proprietary software owned by XenArcAI. All rights reserved. Unauthorized copying, distribution, modification, public display, or public performance of this software is strictly prohibited.

## Contact

For any questions regarding this project, please contact the XenArcAI development team.
