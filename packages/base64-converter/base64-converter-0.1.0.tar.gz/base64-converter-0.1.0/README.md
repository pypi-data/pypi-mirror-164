# Base64 Converter

`base64-converter` is a CLI tool to quickly Base64 encode and decode strings.

## Installation - TBD

```bash
pip install --user <TBD>
```

## Usage

```bash
Usage: base64-converter [OPTIONS] COMMAND [ARGS]...

Base64 Converter

Options:
    --install-completion          Install completion for the current shell.
    --show-completion             Show completion for the current shell, to copy it or customize the installation.
    --help                        Show this message and exit.

Commands:
    d                             Base64 decode
    e                             Base64 encode
```

## Examples

### Base64 Encode

```bash
$ base64-converter e test

Output: dGVzdA==
```

### Base64 Decode

```bash
$ base64-converter e dGVzdA==

Output: test
```

## Tips & Tricks

I recommend shorthanding the CLI tool command. Be the lazy programmer.

```bash
# Linux/MacOS
$ alias b=base64-converter

# Windows
$ add alias base64-converter b

# Run Base64 Encode
$ b e test

Output: dGVzdA==

# Run Base64 Decode
$ b d dGVzdA==

Output: test
```

## Contributing

To make a contribution, fork the repo, make your changes and then submit a pull request. Please try to adhere to the existing style. If you've discovered a bug or have a feature request, create an issue.

Pending Features:

- Support iterations to allow multiple encoding/decoding in a single line.

## How it Works

Base64 Converter is written in Python and built on Typer. Typer is a library for building CLI applications.
