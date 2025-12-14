import sys


def hex_to_int(hex: str) -> int:
    """Convert a hexadecimal string to an integer."""
    return int(hex, 16)


def int_to_hex(num: int) -> str:
    """Convert an integer to a 2-character hexadecimal string."""
    return f'{num:02x}'


def enable_dolby_vision_hdmi(hex: str) -> str:
    """
    Enable Dolby Vision HDMI by modifying the appropriate byte in a 14-character
    hexadecimal string.
    """
    if len(hex) != 14 or not all(c in '0123456789abcdefABCDEF' for c in hex):
        raise ValueError("Input must be a 14-character hexadecimal string.")

    hex_chunks_index = 2  # Index of the Dolby Vision value in the chunks

    # Split into chunks of 2 characters
    hex_chunks = [hex[i: i + 2] for i in range(0, len(hex), 2)]

    # Set the last bit to enable 'LLDV-HDMI'
    dolby_bits = hex_to_int(hex_chunks[hex_chunks_index])
    dolby_bits |= 1  # Enable the last bit
    hex_chunks[hex_chunks_index] = int_to_hex(dolby_bits)

    return ''.join(hex_chunks)


def main():
    """Main function to handle command-line input."""
    if len(sys.argv) != 2:
        print("Usage: python -m enable_dolby <14-character_hex_code>")
        sys.exit(1)

    video_hex = sys.argv[1].strip()
    try:
        new_video_hex = enable_dolby_vision_hdmi(video_hex)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    if new_video_hex == video_hex:
        print(f"Warning: `video_hex` of '{video_hex}' is already enabled with LLDV-HDMI")
    else:
        print(f"Update `video_hex` from '{video_hex}' to '{new_video_hex}' to enable LLDV-HDMI")


if __name__ == '__main__':
    main()
