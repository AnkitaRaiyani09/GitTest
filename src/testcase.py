from pathlib import Path
from src.driver import Driver
import softest
import logging

logger = logging.getLogger(__name__)


class TestCase(softest.TestCase):

    def test_github(self):
        driver = Driver.create_driver()
        try:
            element = driver.find_element_by_xpath("//a[@href='/login']")
            self.soft_assert(self.assertIsNotNone, element, msg="Not able to find sign in element")
            element.click()
            self.soft_assert(self.assertIsNotNone, driver.find_element_by_id("login"), msg="Not able to find login page"
                                                                                           " element")
            self.assert_all()
            driver.get_screenshot_as_file(str(Path.home()) + "/Documents/GitTest/image/testcase_1.png")
        except Exception as ex:
            logger.warning("Failed to verify test case 1 : Verify that by clicking on Sign in button user is redirected"
                           " to login page", exc_info=ex)

        try:
            driver.find_element_by_name("commit").click()
            self.soft_assert(self.assertIsNotNone, driver.find_element_by_id("js-flash-container"),
                             msg="Error message is not present.")
            self.assert_all()
            driver.get_screenshot_as_file(str(Path.home()) + "/Documents/GitTest/image/testcase_2.png")
        except Exception as ex:
            logger.warning("Failed to verify test case 2 : Verify that username and password fields are mandatory"
                           " in login page", exc_info=ex)

        try:
            driver.find_element_by_class_name("label-link").click()
            driver.find_element_by_id("email_field").send_keys("xz@xz.com")
            driver.find_element_by_name("commit").click()
            self.soft_assert(self.assertIsNotNone, driver.find_element_by_id("js-flash-container"),
                             msg="Error message is not present.")
            self.assert_all()
            driver.get_screenshot_as_file(str(Path.home()) + "/Documents/GitTest/image/testcase_3.png")
        except Exception as ex:
            logger.warning("Failed to verify test case 3 : Verify that inserting m.ie into email field in "
                           "reset_password page displays message Can't find that email, sorry.", exc_info=ex)

        try:
            driver.find_element_by_id("email_field").send_keys("")
            driver.find_element_by_name("commit").click()
            # print(driver.find_element_by_xpath("//div[@id='js-flash-container']/div").__getattribute__("text"))
            self.soft_assert(self.assertIsNotNone, driver.find_element_by_id("js-flash-container"),
                             msg="Error message is not present.")
            self.assert_all()
            driver.get_screenshot_as_file(str(Path.home()) + "/Documents/GitTest/image/testcase_4.png")
        except Exception as ex:
            logger.warning("Failed to verify test case 4 : Verify that inserting empty value into email field in "
                           "reset_password page displays message Can't find that email, sorry.", exc_info=ex)

        try:
            driver.find_element_by_id("email_field").send_keys("")
            driver.find_element_by_name("commit").click()
            message = driver.find_element_by_xpath("//div[@id='js-flash-container']/div").__getattribute__("text")
            self.soft_assert(self.assertTrue, True if "address is not a verified" in message else False,
                             msg="Error message is not verified.")
            self.assert_all()
            driver.get_screenshot_as_file(str(Path.home()) + "/Documents/GitTest/image/testcase_5.png")
        except Exception as ex:
            logger.warning("Failed to verify test case 5 :  Verify that the first word in error message in "
                           "reset_password page is 'address is not a verified'", exc_info=ex)

        try:
            driver.get("https://github.com/")
            driver.find_element_by_xpath("//a[@href='/login']/../div/../a[2]").click()
            self.soft_assert(self.assertIsNotNone, driver.find_element_by_xpath("//div[text()='Join GitHub']"),
                             msg="Jojn Github page is not opened.")
            self.assert_all()
            driver.get_screenshot_as_file(str(Path.home()) + "/Documents/GitTest/image/testcase_6.png")
        except Exception as ex:
            logger.warning("Failed to verify test case 6 : Verify that clicking on Sign up button will redirect user "
                           "into join github page", exc_info=ex)

        try:
            self.soft_assert(self.assertIsNotNone, driver.find_element_by_xpath("//h1[text()='Create your account']"),
                             msg="Create your account text is not present.")
            self.assert_all()
            driver.get_screenshot_as_file(str(Path.home()) + "/Documents/GitTest/image/testcase_7.png")
        except Exception as ex:
            logger.warning("Failed to verify test case 7 : Verify that join github page contains text "
                           "Create your personal account", exc_info=ex)

        try:
            driver.find_element_by_id("user_email").send_keys("xyz")
            self.soft_assert(self.assertTrue, driver.find_element_by_id("signup_button").get_attribute("disabled"),
                             msg="Create account button is not disabled.")
            self.assert_all()
            driver.get_screenshot_as_file(str(Path.home()) + "/Documents/GitTest/image/testcase_8.png")
        except Exception as ex:
            logger.warning("Failed to verify test case 8 : Verify that Create an account button is greyed when an "
                           "existing email address is inserted in join github page.", exc_info=ex)


if __name__ == '__main__':
    softest.main()
