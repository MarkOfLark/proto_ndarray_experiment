#!/usr/bin/env python
from TestMessage_pb2 import TestMessage
import numpy as np
import io

if __name__ == '__main__':
    x = np.random.normal( 0.0, 1.0, (3, 4, 2) );

    message_to_write = TestMessage();
    message_to_write.array.assign( x );

    f = io.BytesIO();
    f.write( message_to_write.SerializeToString() )

