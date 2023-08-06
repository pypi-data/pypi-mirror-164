"""Tests for tradingtools.util.helpers."""

from tradingtools.util.helpers import to_nearest


class TestUtilHelpers:

    def test_to_nearest_without_round_down(self):
        assert to_nearest(354.3647338242, 100) == 400.0
        assert to_nearest(747.7471243511, 100) == 700.0

    def test_to_nearest_without_round_down(self):
        assert to_nearest(354.3647338242, 100, round_down=True) == 300.0
        assert to_nearest(747.7471243511, 100, round_down=True) == 700.0
        assert to_nearest(799.9999999999, 100, round_down=True) == 700.0
        assert to_nearest(399.9999999999, 100, round_down=True) == 300.0
        assert to_nearest(700, 100, round_down=True) == 700.0
        assert to_nearest(300, 100, round_down=True) == 300.0
