from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="xen-tokenizer",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="High-performance multilingual tokenizer based on Qwen architecture",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/xen-tokenizer",
    packages=find_packages(),
    package_data={
        'xen_tokenizer': ['tokenizer.json'],
    },
    install_requires=[
        'torch>=1.8.0',
        'transformers>=4.18.0',
        'tqdm>=4.62.0',
        'pyyaml>=5.4.1',
        'sentencepiece>=0.1.96',
    ],
    extras_require={
        'azure': [
            'azure-storage-blob>=12.8.1',
            'pyarrow>=6.0.0',
            'pandas>=1.3.0',
        ],
        'dev': [
            'pytest>=6.0.0',
            'black>=21.7b0',
            'isort>=5.9.0',
            'mypy>=0.910',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    python_requires='>=3.7',
)
