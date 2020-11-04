#!/usr/bin/env python

import io, sys

from google.protobuf.compiler import plugin_pb2 as plugin


def generate_code(request, response):
    for proto_file in request.proto_file:
        output = []

        f = response.file.add()
        f.name = proto_file.name + '.debug'
        f.content = request.proto_file.__str__()

        # f = response.file.add()
        # f.name = proto_file.message_type[0].name + '_pb2.py'
        # f.insertion_point = 'imports'
        # f.content = 'import numpy as np'

        # f = response.file.add()
        # f.name = proto_file.message_type[0].name + '_pb2.py'
        # f.insertion_point = 'imports'
        # f.content = '\ndef __assign__( self, x ):\n\tprint(f\'assigned {x}\')'

        # f = response.file.add()
        # f.name = proto_file.message_type[0].name + '_pb2.py'
        # f.insertion_point = 'class_scope:ndarray'
        # f.content = ', \'assign\' : __assign__'


if __name__ == '__main__':
    # Read request message from stdin
    data = io.open(sys.stdin.fileno(), "rb").read()

    # Parse request
    request = plugin.CodeGeneratorRequest()
    request.ParseFromString(data)

    # Create response
    response = plugin.CodeGeneratorResponse()

    # Generate code
    generate_code(request, response)

    # Serialise response message
    output = response.SerializeToString()

    # Write to stdout
    io.open(sys.stdout.fileno(), "wb").write(response.SerializeToString())