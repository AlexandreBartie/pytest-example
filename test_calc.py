import pytest
import logging

import calc

logger = logging.getLogger(__name__)

@pytest.mark.parametrize("test, id, result, numbers", 
    [
    ('01. Sum two numbers',           'C12345',    6,       [2,4]),
    ('02. Sum three numbers',         'C12346',   14,     [2,5,7]),
    ('03. Sum unique number',         'C12347',    2,         [2]),
    ('04. Sum null numbers',          'C12347',    0,          []),
    ('05. Sum two numbers decimals',  'C12345',  6.6,   [2.2,4.4]),
    ('06. Sum two numbers negatives', 'C12345',   -6,     [-2,-4]),
    ])
def test_sum(test, id, result, numbers):  
    logger.info(f'<<<BARTIE>>> [{id}] {test}')
    assert calc.sum(*numbers) == result
