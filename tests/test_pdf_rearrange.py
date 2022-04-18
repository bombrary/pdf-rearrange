import pytest
from pdf_rearrange import full_page_indicies

test_cases_full_page_indices = [
    ([4,1,2,3], 4, [3, 0, 1, 2]),
    ([4,1,2,3], 5, [3, 0, 1, 2, 7, 4, 5, 6]),
    ([1], 5, [0, 1, 2, 3, 4]),
]

@pytest.mark.parametrize('chunk, num_pages, expect', test_cases_full_page_indices)
def test_full_page_indicies(chunk, num_pages, expect):
    assert full_page_indicies(chunk, num_pages) == expect
