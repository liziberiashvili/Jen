from pathlib import Path

import pytest

from managers.DriverManager import DriverManager
from utils.ParserUtils import ParserUtils


@pytest.fixture(autouse=True, scope="function")
def setUp():
    path = Path("resources/config.json")
    config_data = ParserUtils.parse_json(path.absolute())
    driver = DriverManager.get_driver()
    driver.get(config_data["url"])
    driver.maximize_window()
    yield
    DriverManager.close_driver()
