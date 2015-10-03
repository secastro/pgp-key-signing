## Installation

By running

```
    pip install -r requirements.txt
```

you will get the modules needed for this code.

## Selection the GPG version that work better for you

It's encouraged to use GPG version 2.1
If you are using OSX with brew, then you could use this:

```
    brew install homebrew/versions/gnupg21
```

## Running

1. Put the PGP/GPG exported keys received by email into the keys/ directory
1. Run make
1. Open the printout.html in a browser
1. Generate a printable version

Explicitly avoided using a HTML2PDF converter to reduce the number of
requirements.

