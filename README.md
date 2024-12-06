# E-commerce Intelligence Tool

## Overview
Automated tool for extracting and analyzing e-commerce website data, including Amazon marketplace presence and contact verification.

## Features
- BuiltWith data extraction
- Amazon marketplace presence validation
- Email contact verification
- Detailed CSV reporting
- Rich CLI experience

## Prerequisites
- Python 3.8+
- Chrome Browser
- API Keys:
  - BuiltWith
  - Hunter.io

## Installation
```bash
# Clone repository
git clone https://github.com/yourusername/ecommerce-intelligence-tool.git

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -e .

# Configure environment
cp .env.example .env
# Edit .env with your API keys
```

## Usage
```bash
# Basic usage
ecommerce-tool

# Specify output file
ecommerce-tool --output custom_report.csv

# Limit websites
ecommerce-tool --limit 50
```

## Configuration
Edit `.env` file to set:
- BuiltWith API Key
- Hunter.io API Key
- Log level
- Processing limits

## Contributing
1. Fork repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create pull request
