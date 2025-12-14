import pytest as pytest

from enable_dolby_vision_hdmi import enable_dolby_vision_hdmi, hex_to_int, int_to_hex


@pytest.mark.parametrize("input_hex, expected_hex", [
    ('480376825e6d95', '480377825e6d95'),
    ('4403609248458f', '4403619248458f'),
    ('4d4e4a725a7776', '4d4e4b725a7776'),
    ('480a7e86607694', '480a7f86607694'),
    ('48039e5898aa5c', '48039f5898aa5c'),
])
def test_enable_dolby_real_samples(input_hex, expected_hex):
    """ТЕСТ ИЗ run_tests(), теперь параметризованный."""
    result = enable_dolby_vision_hdmi(input_hex)
    assert result == expected_hex, f"Failed for {input_hex}"


def test_hex_to_int():
    assert hex_to_int('0a') == 10
    assert hex_to_int('ff') == 255
    assert hex_to_int('A1') == 161


def test_int_to_hex():
    assert int_to_hex(10) == '0a'
    assert int_to_hex(255) == 'ff'
    assert int_to_hex(0) == '00'


def test_enable_dolby_already_enabled():
    """Код, где последний бит уже установлен (3-й байт 0x77 -> 0x77)."""
    result = enable_dolby_vision_hdmi('480377825e6d95')
    assert result == '480377825e6d95'  # Не должен измениться
