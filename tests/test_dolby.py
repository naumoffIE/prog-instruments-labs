from enable_dolby_vision_hdmi import enable_dolby_vision_hdmi, hex_to_int, int_to_hex


def run_tests():
    """Run test cases to validate the enable_dolby_vision_hdmi function."""
    samples = (
        ('480376825e6d95', '480377825e6d95'),
        ('4403609248458f', '4403619248458f'),
        ('4d4e4a725a7776', '4d4e4b725a7776'),
        ('480a7e86607694', '480a7f86607694'),
        ('48039e5898aa5c', '48039f5898aa5c'),
    )
    for hex_input, expected_hex_output in samples:
        hex_output = enable_dolby_vision_hdmi(hex_input)
        assert hex_output == expected_hex_output, (
            f"Test failed: {hex_input} -> {hex_output} (expected {expected_hex_output})"
        )
    print("All tests passed.")

    def test_hex_to_int():
        assert hex_to_int('0a') == 10
        assert hex_to_int('ff') == 255
        assert hex_to_int('A1') == 161

    def test_int_to_hex():
        assert int_to_hex(10) == '0a'
        assert int_to_hex(255) == 'ff'
        assert int_to_hex(0) == '00'
