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
