"""
Core tokenizer implementation for XenTokenizer.
"""

import os
import json
from typing import Dict, List, Optional, Union
from transformers import PreTrainedTokenizerFast
from .config import TokenizerConfig


class XenTokenizerFast(PreTrainedTokenizerFast):
    """
    A fast tokenizer for Xen, based on PreTrainedTokenizerFast.
    """
    
    def __init__(
        self,
        tokenizer_file: str,
        config: Optional[TokenizerConfig] = None,
        **kwargs
    ):
        """
        Initialize the tokenizer.
        
        Args:
            tokenizer_file: Path to the tokenizer.json file
            config: Optional TokenizerConfig instance
            **kwargs: Additional arguments for PreTrainedTokenizerFast
        """
        # Set default config if not provided
        self.config = config or TokenizerConfig()
        
        # Initialize the parent class
        super().__init__(
            tokenizer_file=tokenizer_file,
            model_max_length=self.config.max_length,
            **kwargs
        )
        
        # Add special tokens if not already present
        self._add_special_tokens()
    
    def _add_special_tokens(self) -> None:
        """Add special tokens to the tokenizer."""
        # Add default special tokens if not already present
        special_tokens_dict = {}
        
        if self.pad_token is None:
            special_tokens_dict["pad_token"] = self.config.pad_token
        if self.eos_token is None:
            special_tokens_dict["eos_token"] = self.config.eos_token
        if self.unk_token is None:
            special_tokens_dict["unk_token"] = self.config.unk_token
        if self.bos_token is None:
            special_tokens_dict["bos_token"] = self.config.bos_token
        
        # Add task-specific special tokens
        for token in ["<tool_call>", "<tool_response>", "<vision>"]:
            if token not in self.get_vocab():
                special_tokens_dict["additional_special_tokens"] = special_tokens_dict.get("additional_special_tokens", []) + [token]
        
        # Update the tokenizer with special tokens
        if special_tokens_dict:
            self.add_special_tokens(special_tokens_dict)
    
    def save_pretrained(self, save_directory: str, **kwargs) -> None:
        """Save the tokenizer to the specified directory."""
        os.makedirs(save_directory, exist_ok=True)
        
        # Save the tokenizer files
        self.backend_tokenizer.save(os.path.join(save_directory, "tokenizer.json"))
        
        # Save the config
        if hasattr(self, 'config'):
            with open(os.path.join(save_directory, "config.json"), 'w', encoding='utf-8') as f:
                json.dump(self.config.to_dict(), f, indent=2, ensure_ascii=False)
        
        # Save the tokenizer configuration
        tokenizer_config = {
            "tokenizer_class": self.__class__.__name__,
            "model_max_length": self.model_max_length,
        }
        with open(os.path.join(save_directory, "tokenizer_config.json"), 'w', encoding='utf-8') as f:
            json.dump(tokenizer_config, f, indent=2, ensure_ascii=False)
    
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path: str, **kwargs) -> 'XenTokenizerFast':
        """Load a tokenizer from a pretrained model or path."""
        # Check if the path exists
        if not os.path.exists(pretrained_model_name_or_path):
            raise ValueError(f"Directory {pretrained_model_name_or_path} does not exist.")
        
        # Load the tokenizer
        tokenizer_file = os.path.join(pretrained_model_name_or_path, "tokenizer.json")
        if not os.path.exists(tokenizer_file):
            raise ValueError(f"tokenizer.json not found in {pretrained_model_name_or_path}")
        
        # Load the config if it exists
        config_file = os.path.join(pretrained_model_name_or_path, "config.json")
        config = None
        if os.path.exists(config_file):
            config = TokenizerConfig.from_json_file(config_file)
        
        return cls(tokenizer_file=tokenizer_file, config=config, **kwargs)
