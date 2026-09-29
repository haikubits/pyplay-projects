import struct
from typing import Iterator

class MessageStreamParser:
    HEADER_SIZE = 4
    def __init__(self) -> None:
        self._buffer = bytearray()
    
    def process_chunk(self, chunk: bytes) -> Iterator[bytes]:
        
        self._buffer.extend(chunk)
        buffer_len = len(self._buffer)
        cursor = 0
        
        while True:
            # Check if the payload size info is present in the buffer
            if cursor + self.HEADER_SIZE > buffer_len:
                break
            
            payload_length = struct.unpack_from('>I', self._buffer, cursor)[0]
            message_end = cursor + self.HEADER_SIZE + payload_length
            
            # check if the complete payload is present in the buffer
            if message_end > buffer_len:
                break
            
            message_start = cursor + self.HEADER_SIZE
            payload = bytes(self._buffer[message_start:message_end])
            cursor = message_end
            yield payload
        
        # clear up the buffer space that has already been parsed
        if cursor > 0:
            del self._buffer[:cursor]

        
if __name__ == "__main__":
    parser = MessageStreamParser()

    # Create 3 distinct messages
    msg1 = b"ORDER_ACK:ID=101"
    msg2 = b"TRADE_FILL:ID=101:QTY=50:PX=450.25"
    msg3 = b"HEARTBEAT"

    # Wire format serialization: [4 bytes Length][Payload]
    wire_data = bytearray()
    for m in [msg1, msg2, msg3]:
        wire_data.extend(struct.pack(">I", len(m)) + m)

    # Simulate erratic network delivery with arbitrary chunk boundaries
    chunk_splits = [3, 10, 25, len(wire_data)]
    extracted_messages = []
    prev = 0

    print("Simulating fragmented TCP stream arrival:")
    for split_point in chunk_splits:
        packet = bytes(wire_data[prev:split_point])
        prev = split_point
        print(f"  Received raw packet ({len(packet)} bytes): {packet!r}")
        
        for complete_msg in parser.process_chunk(packet):
            extracted_messages.append(complete_msg)

    print(f"\nSuccessfully reconstructed {len(extracted_messages)} messages:")
    for msg in extracted_messages:
        print(f"  Decoded: {msg.decode()}")