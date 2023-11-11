# GPT PDF Reader

GPT PDF Reader is a Python package that utilizes GPT-4V and other tools to extract and process information from PDF files.

## Features

- Extracts figures from PDF files using the `pdffigures2` Scala library.
- Converts PDF pages to images and uploads them to Google Cloud Bucket.
- Utilizes GPT-4V Vision to generate Markdown content from pdf an than inserts image urls into markdown.

## Installation

The installation process requires Java and Scala. The following instructions are for macOS users:

```bash
brew tap AdoptOpenJDK/openjdk
brew install --cask adoptopenjdk11
brew install jenv
echo 'export PATH="$HOME/.jenv/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(jenv init -)"' >> ~/.zshrc
```

After updating your shell configuration, close and reopen your terminal, then set Java 11 as the global version using jenv:

```bash
jenv add /Library/Java/JavaVirtualMachines/adoptopenjdk-11.jdk/Contents/Home/
jenv global 11.0.11
```

Install GPT PDF Reader via pip:

```bash
pip install gptpdfreader
```

Configure the required environment variables in your .env file without spaces or unnecessary quotes:

```env
OPENAI_API_KEY=open_ai_key
GOOGLE_ID=google_project_id
GOOGLE_BUCKET=google_bucket_name
```

## Usage

To process a PDF and generate Markdown content:

```python
from gptpdfreader.reader import main

main('path_to_your_pdf.pdf')
```

This will process the specified PDF and output a Markdown file with the extracted information in the same directory.

## Limitations 

some limitations

## Contributing

We welcome contributions! Please open an issue or submit a pull request on our GitHub repository.

## Support

For questions and support, please open an issue in the GitHub issue tracker.

## License




