import sys
from unittest.mock import patch
import pytest as pytest

from enable_dolby_vision_hdmi import enable_dolby_vision_hdmi, hex_to_int, int_to_hex, main


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


def test_enable_dolby_min_byte():
    """Проверка минимального значения байта (0x00 -> 0x01)."""
    result = enable_dolby_vision_hdmi('480300825e6d95')
    assert result == '480301825e6d95'


def test_enable_dolby_invalid_input():
    """Некорректная входная строка."""
    with pytest.raises(ValueError, match="14-character hexadecimal"):
        enable_dolby_vision_hdmi('short')


def test_enable_dolby_mocked_helpers():
    """Тест с моками, проверяем вызовы вспомогательных функций."""
    with patch('enable_dolby_vision_hdmi.hex_to_int') as mock_hex_to_int, \
            patch('enable_dolby_vision_hdmi.int_to_hex') as mock_int_to_hex:
        mock_hex_to_int.return_value = 0x82
        mock_int_to_hex.return_value = '83'

        result = enable_dolby_vision_hdmi('480382825e6d95')
        # hex_to_int был вызван 1 раз с аргументом '82' (3-й байт)
        mock_hex_to_int.assert_called_once_with('82')
        # int_to_hex был вызван 1 раз с аргументом 0x83 (0x82 | 1)
        mock_int_to_hex.assert_called_once_with(0x83)
        assert result == '480383825e6d95'


def test_main_valid_input():
    """Тестируем работу main() через командную строку."""
    test_hex = '480376825e6d95'
    expected_output = f"Update `video_hex` from '{test_hex}' to '480377825e6d95' to enable LLDV-HDMI"

    # мокаем sys.argv и print
    with patch.object(sys, 'argv', ['enable_dolby_vision_hdmi.py', test_hex]), \
            patch('builtins.print') as mock_print:
        main()
        mock_print.assert_called_once_with(expected_output)
