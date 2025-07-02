"""
Configuration classes for XenTokenizer.
"""

import json
from dataclasses import dataclass, field, asdict
from typing import Optional, Dict, Any


@dataclass
class TokenizerConfig:
    """
    Configuration class for XenTokenizer.
    """
    # Tokenizer parameters
    max_length: int = 2048
    padding_side: str = "right"
    truncation: bool = True
    
    # Special tokens
    pad_token: str = "<pad>"
    eos_token: str = "</s>"
    unk_token: str = "<unk>"
    bos_token: str = "<s>"
    
    # Additional configuration
    add_prefix_space: bool = False
    clean_up_tokenization_spaces: bool = True
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the config to a dictionary."""
        return asdict(self)
    
    def to_json_string(self) -> str:
        """Serialize this instance to a JSON string."""
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=False)
    
    def to_json_file(self, json_file_path: str) -> None:
        """Save this instance to a JSON file."""
        with open(json_file_path, 'w', encoding='utf-8') as f:
            f.write(self.to_json_string())
    
    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> 'TokenizerConfig':
        """Construct a config from a dictionary."""
        return cls(**config_dict)
    
    @classmethod
    def from_json_file(cls, json_file: str) -> 'TokenizerConfig':
        """Construct a config from a JSON file."""
        with open(json_file, 'r', encoding='utf-8') as f:
            config_dict = json.load(f)
        return cls.from_dict(config_dict)


@dataclass
class AzureConfig:
    """
    Configuration for Azure Blob Storage integration.
    """
    connection_string: str = ""
    container_name: str = ""
    input_prefix: str = "raw_data/"
    output_prefix: str = "processed_data/"
    max_workers: int = 4
    
    @classmethod
    def from_env(cls) -> 'AzureConfig':
        """Load configuration from environment variables."""
        import os
        return cls(
            connection_string=os.getenv("AZURE_STORAGE_CONNECTION_STRING", ""),
            container_name=os.getenv("AZURE_CONTAINER_NAME", ""),
            input_prefix=os.getenv("AZURE_INPUT_PREFIX", "raw_data/"),
            output_prefix=os.getenv("AZURE_OUTPUT_PREFIX", "processed_data/"),
            max_workers=int(os.getenv("AZURE_MAX_WORKERS", "4"))
        )
