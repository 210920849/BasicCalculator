
from selenium.webdriver.common.by import By

First_number=(By.XPATH,'//input[@id="number1Field"]') #XPATH示例
Second_number=(By.XPATH,'//input[@id="number2Field"]') #XPATH示例
Operation=(By.ID, "selectOperationDropdown")
Calculator=(By.ID, "calculateButton")
Answer=(By.ID,"numberAnswerField")
Intergersonly=(By.ID,"integerSelect")
promot_message=(By.ID, "errorMsgField")