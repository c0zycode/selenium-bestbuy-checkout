from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#PATH is the path to where the chromedriver is
PATH = "path-to-chrom-driver"
driver = webdriver.Chrome(PATH)
driver.implicitly_wait(5)
#driver.get is the URL of the item that you wish to purchase
driver.get("https://www.bestbuy.com/site/turtle-beach-recon-200-amplified-gaming-headset-for-xbox-one-xbox-series-xs-playstation4-playstation5-and-nintendo-switch-black/6260915.p?skuId=6260915")

driver.implicitly_wait(5)

add_to_cart = driver.find_element_by_xpath("//*[contains(@id, 'fulfillment-add-to-cart-button')]")
ad

modalContainer = driver.find_element_by_xpath("//*[contains(@class, 'modal-window')]")

driver.implicitly_wait(5)

go_to_cart = modalContainer.find_element_by_xpath("//*[contains(@class, 'go-to-cart')]")
go_to_cart.element_to_be_clickable().click()

checkout = driver.find_element_by_xpath("//*[contains(@class, 'checkout-buttons__checkout')]")
checkout.element_to_be_clickable().click()

email = driver.find_element_by_id("fld-e")
#send_keys allows you to add your email address login for Best Buy
email.send_keys("your-email-here")

password = driver.find_element_by_id("fld-p1")
#add your password here
password.send_keys("password", Keys.RETURN)

driver.implicitly_wait(9)

#security code on back of your card on file to confirm purchase
securitycode = driver.find_element_by_id("credit-card-cvv")
securitycode.send_keys("000")

placeorder = driver.find_element_by_xpath("//*[contains(@class, 'order-button')]")
placeorder.element_to_be_clickable().click()