# Python example

This directory contains an example for running Python 3 in Gramine, including
the Makefile and a template for generating the manifest.

# Generating the manifest

## Installing prerequisites

For generating the manifest and running the test scripts, please run the following
command to install the required packages (Ubuntu-specific):

    sudo apt-get install libnss-mdns python3-numpy python3-scipy

## Building for Linux

Run `make` (non-debug) or `make DEBUG=1` (debug) in the directory.

## Building for SGX

Run `make SGX=1` (non-debug) or `make SGX=1 DEBUG=1` (debug) in the directory.

If you want to run the `scripts/sgx-quote.py` script, you must build the example
with SGX remote attestation enabled. By default, the example is built *without*
remote attestation.

If you want to build the example for DCAP attestation, first make sure you have
a working DCAP setup. Then build the example as follows:
```
make SGX=1 RA_TYPE=dcap
```

Otherwise, you will probably want to use EPID attestation. For this, you will
additionally need to provide an SPID and specify whether it is set up for
linkable quotes or not:

```
make SGX=1 RA_TYPE=epid RA_CLIENT_SPID=12345678901234567890123456789012 \
    RA_CLIENT_LINKABLE=0
```


# Run Server

```
gramine-sgx ./python scripts/server.py
```

Log file location: /tmp/log.txt
