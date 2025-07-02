"""
XenTokeniser - Advanced Colab Usage

This example demonstrates advanced usage of XenTokeniser in Google Colab,
including parallel processing and resource management.
"""

# 1. First, run these commands in Colab:
"""
# Install required packages
!pip install torch transformers tqdm datasets
!git clone https://github.com/yourusername/XenTokeniser.git
%cd XenTokeniser
!pip install -e .
"""

import os
import torch
from datasets import load_dataset
from tqdm.auto import tqdm
from xen_tokenizer import XenTokenizerFast, TokenizerConfig

# 2. Setup device (automatically uses GPU if available)
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Using device: {device}")

# 3. Initialize tokenizer with custom config
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
).to(device)

# 4. Load a sample dataset (or use your own)
print("Loading dataset...")
try:
    # Try to load a small dataset from Hugging Face
    dataset = load_dataset("imdb", split='train[:1%]')
    texts = dataset['text']
    print(f"Loaded {len(texts)} samples from IMDB dataset")
except:
    # Fallback to sample data
    texts = ["This is a test sentence."] * 1000
    print("Using sample data")

# 5. Tokenization function with progress tracking
def tokenize_batch(batch):
    return tokenizer.batch_encode_plus(
        batch,
        padding='max_length',
        truncation=True,
        max_length=config.max_length,
        return_tensors='pt',
        return_attention_mask=True
    )

# 6. Process dataset in batches
batch_size = 32 if device == 'cuda' else 8
results = []

print(f"Tokenizing {len(texts)} samples with batch size {batch_size}")
for i in tqdm(range(0, len(texts), batch_size)):
    batch = texts[i:i + batch_size]
    batch_encoded = tokenize_batch(batch)
    
    # Move tensors to device
    batch_encoded = {k: v.to(device) for k, v in batch_encoded.items()}
    
    # Process your batch here (e.g., model inference)
    # model_output = model(**batch_encoded)
    
    results.append(batch_encoded)

# 7. Show statistics
input_ids = torch.cat([r['input_ids'] for r in results], dim=0)
print("\nTokenization complete!")
print(f"Total samples processed: {len(input_ids)}")
print(f"Sequence length: {input_ids.shape[1]}")
print(f"Vocabulary size: {tokenizer.vocab_size}")

# 8. Example of decoding
example = results[0]
print("\nExample input:", texts[0][:100] + "...")
print("\nTokenized output (first 20 tokens):")
print(example['input_ids'][0][:20].cpu().numpy())
print("\nDecoded back:")
print(tokenizer.decode(example['input_ids'][0][:20]))
