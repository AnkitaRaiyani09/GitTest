import logging
from pathlib import Path
from selenium import webdriver
logger = logging.getLogger(__name__)


class Driver:

    @staticmethod
    def create_driver() -> webdriver:
        driver = None
        try:
            logger.debug('Creating new [BrowserDriver]')
            path = f"--log-path=device.log"
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-notifications")
            options.add_argument("--kiosk")  # for linux or mac
            options.add_argument("--start-maximized")  # for windows
            driver = webdriver.Chrome(options=options, executable_path=str(Path.home()) + "Downloads/chromedriver",
                                      service_args=["--verbose", path])
            #driver.implicitly_wait(10)
            driver.get("https://github.com/")
        except Exception as ex:
            logger.warning("Failed to create driver.", exc_info=ex)
        return driver
