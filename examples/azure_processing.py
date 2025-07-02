"""
Example of processing parquet files from Azure Blob Storage with XenTokenizer.
"""

import os
import logging
from pathlib import Path
from xen_tokenizer import AzureParquetProcessor, TokenizerConfig, AzureConfig

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """Main function to demonstrate Azure processing."""
    # Configuration
    tokenizer_config = TokenizerConfig(
        max_length=2048,
        pad_token="[PAD]",
        eos_token="</s>",
        unk_token="[UNK]"
    )
    
    # Azure configuration - you can also set these as environment variables
    azure_config = AzureConfig(
        connection_string=os.getenv("AZURE_STORAGE_CONNECTION_STRING"),
        container_name=os.getenv("AZURE_CONTAINER_NAME", "your-container"),
        input_prefix="raw_data/",
        output_prefix="processed_data/",
        max_workers=4
    )
    
    try:
        # Initialize the processor
        processor = AzureParquetProcessor(
            tokenizer_config=tokenizer_config,
            azure_config=azure_config
        )
        
        # Process all files
        logger.info("Starting to process files...")
        processor.process_all()
        logger.info("Processing completed successfully!")
        
    except Exception as e:
        logger.error(f"Error during processing: {e}", exc_info=True)
        raise

if __name__ == "__main__":
    main()
