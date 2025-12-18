from remove_duplicates import remove_duplicates
import pytest

TEST_SCENARIOS = [
    pytest.param([1, 2, 3, 2, 4, 1, 5], [1, 2, 3, 4, 5], id="out of order duplicates"),
    pytest.param([1, 1, 1], [1], id="all same value"),
    pytest.param([], [], id="empty input"),
]


class TestRemoveDuplicates:

    @pytest.mark.parametrize("test_value,expected_result", TEST_SCENARIOS)
    def test_remove_duplicates(self, test_value, expected_result):
        """
        test that validates the remove duplicates function in a variety of scenarios
        """
        assert remove_duplicates(test_value) == expected_result
