from selenium import webdriver

def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="C:/labs/chromedriver.exe")
    driver.maximize_window()

def test_form_entry():
    driver.get("http://localhost/selenium/form.php")
    driver.find_element_by_name("nip").send_keys("234")
    driver.find_element_by_name("nama").send_keys("Redha")
    driver.find_element_by_name("nik").send_keys("14")
    driver.find_element_by_name("alamat").send_keys("Tangerang")
    driver.find_element_by_name("perusahaan").send_keys("PT ")
    driver.find_element_by_name("tanggal").send_keys("12/12/2026")
    driver.find_element_by_name("divisi").send_keys("IT")
    driver.find_element_by_name("posisi").send_keys("Staff")
    driver.find_element_by_name("gaji").send_keys("1000")
    driver.find_element_by_name("atasan").send_keys("Ada")
    driver.find_element_by_name("submit").click()

def test_cleanup():
    driver.close()
    driver.quit()
