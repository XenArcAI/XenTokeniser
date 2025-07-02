"""
XenTokeniser - Colab Quickstart

A minimal example showing how to use XenTokeniser in Google Colab.
"""

# 1. Install required packages (run this in Colab first)
# !pip install torch transformers tqdm
# !git clone https://github.com/yourusername/XenTokeniser.git
# %cd XenTokeniser
# !pip install -e .

from xen_tokenizer import XenTokenizerFast, TokenizerConfig
from tqdm.auto import tqdm

# 2. Initialize tokenizer
tokenizer = XenTokenizerFast(
    tokenizer_file="tokenizer.json",  # Path to your tokenizer file
    config=TokenizerConfig(
        max_length=512,
        pad_token="[PAD]"
    )
)

# 3. Sample dataset
texts = [
    "This is a test sentence.",
    "XenTokeniser is fast and efficient.",
    "It handles parallel processing automatically.",
] * 1000  # Create more samples

# 4. Tokenize in batches
batch_size = 64
results = []

for i in tqdm(range(0, len(texts), batch_size)):
    batch = texts[i:i + batch_size]
    encoded = tokenizer.batch_encode_plus(
        batch,
        padding='max_length',
        truncation=True,
        return_tensors='pt',
        max_length=512
    )
    results.append(encoded)

print(f"Tokenized {len(texts)} samples in {len(results)} batches")
print("Sample output:", {k: v.shape for k, v in results[0].items()})
