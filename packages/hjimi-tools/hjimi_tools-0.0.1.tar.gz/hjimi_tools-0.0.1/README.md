# hjimi_tools

# Python Package Setup Script

This script is a utility for automatically setting up a new Python package structure. It creates a directory structure for the package, as well as several important files such as \`pyproject.toml\`, \`README.md\`, \`LICENSE\`, and \`requirements.txt\`.

## Usage

To use this script, you simply need to run it with Python and pass the name of the package you want to create as a command line argument. For example:

\```bash
python setup_package.py --package_name hjimi_tools
\```

This will create a new directory called \`hjimi_tools\` with the following structure:

\```
hjimi_tools/
├── src/
│   └── hjimi_tools/
│       └── __init__.py
├── test/
├── pyproject.toml
├── README.md
├── LICENSE
└── requirements.txt
\```

## Command Line Arguments

The script accepts several command line arguments for customizing the package:

- \`package_name\`: The name of the package to set up. This is a required argument.
- \`--version\`: The version of the package. Defaults to '0.0.1'.
- \`--description\`: The description of the package. Defaults to 'A small example package'.
- \`--author\`: The author of the package. Defaults to 'Example Author'.
- \`--author_email\`: The email of the author. Defaults to 'author@example.com'.
- \`--homepage\`: The homepage URL of the package. Defaults to 'https://github.com/YOUR_USERNAME/YOUR_REPOSITORY'.
- \`--bug_tracker\`: The bug tracker URL of the package. Defaults to 'https://github.com/YOUR_USERNAME/YOUR_REPOSITORY/issues'.

## Requirements

This script requires Python 3.8 or higher.
