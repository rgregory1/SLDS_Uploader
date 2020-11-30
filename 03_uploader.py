from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pathlib
import psutil

import credentials
import sys

# from PS_Enroll_processor import fix_entry_codes

# import web_pdb


cur_dir = pathlib.Path.cwd()
one_up = pathlib.Path(__file__).resolve().parents[1]

blanks = pathlib.Path.cwd() / "blank_files"

if platform.system() == 'Darwin'
    print('maccado')

if psutil.MACOS:
    print("mac")
    browser = webdriver.Chrome("/Users/rgregory/Desktop/SLDS_Uploader/chromedriver_86")
else:
    print("pi")
    browser = webdriver.Chrome("/Users/rgregory/Desktop/SLDS_Uploader/chromedriver_84")


browser.implicitly_wait(100)
browser.get("https://slds.education.vermont.gov/edFusion/Web/Login.aspx")
time.sleep(1)


# log in
username = browser.find_element_by_id("txtUserName")
username.send_keys(credentials.my_username)
password = browser.find_element_by_id("txtAcceptId")
password.send_keys(credentials.my_password)

signin_btn = browser.find_element_by_id("login1")
signin_btn.click()

# hover and click on menu item below
action = ActionChains(browser)
time.sleep(3)
firstLevelMenu = browser.find_element_by_link_text("Integrate")
time.sleep(3)
action.move_to_element(firstLevelMenu).perform()
secondLevelMenu = browser.find_element_by_link_text("Submission Upload")
action.move_to_element(secondLevelMenu).perform()

secondLevelMenu.click()

time.sleep(1)


def slds_file_upload(cycles, file_list, dir_info):

    # #fill in empty entry codes (not needed as of March 2020)
    # if dir_info == one_up:
    #     fix_entry_codes(dir_info)

    # web_pdb.set_trace()
    for index in range(cycles):

        # drop down box to choose submission type
        domain_dropdown = browser.find_element_by_id("ctl00_MainContent_ddlFileType")
        domain_dropdown.click()
        time.sleep(2)
        browser.find_element_by_css_selector(".rddlItem[title='Submission']").click()
        time.sleep(3)

        # upload set of blank student files

        file_upload_string = ""
        for file in file_list:
            file_path = str(dir_info / file)
            file_upload_string = file_upload_string + file_path + " \n "

        print(file_upload_string)
        # trim final new line character from string
        file_upload_string = file_upload_string[:-3]

        # send files to choose file button
        browser.find_element_by_id("ctl00_MainContent_rdFileUploadfile0").send_keys(
            file_upload_string
        )
        time.sleep(3)

        # click upload button
        browser.find_element_by_id("ctl00_MainContent_imgbtnUpload").click()
        time.sleep(3)

        # choose collection
        collection_choice = browser.find_element_by_id(
            "ctl00_MainContent_ddlCollections"
        ).click()

        time.sleep(2)
        browser.find_element_by_css_selector(
            ".rddlItem[title='2021 - DC#03_NightlyCollection_Unofficial']"
        ).click()
        time.sleep(3)

        # click upload button AGAIN
        browser.find_element_by_id("ctl00_MainContent_imgbtnUpload").click()
        time.sleep(10)

        # click schedule now button
        browser.find_element_by_id("ctl00_MainContent_rbScheduleNow_input").click()
        time.sleep(10)


# old_student_file_list = ["03_0_Student_Identity.csv","03_4_PS_Enroll.csv","03_5_PS_GradeProg.csv"]

student_file_list = [
    "03_18_CIRS_Actions.csv",
    "03_6_PS_ADM.csv",
    "03_16_CIRS_Incidents.csv",
    "03_17_CIRS_Offenders.csv",
    "03_0_Student_Identity.csv",
    "03_12_Course.csv",
    "03_8_OrgProfile.csv",
    "03_15_StudentSecResults.csv",
    "03_5_PS_GradeProg.csv",
    "03_13_CourseSection.csv",
    "03_19_CIRS_Victims.csv",
    "03_11a_POS_RoleTable.csv",
    "03_11_POS.csv",
    "03_4_PS_Enroll.csv",
    "03_14a_StuSectionEnrollment.csv",
    "03_8a_OrgProfile_Holidays.csv",
    "03_14b_StaffSectionAssignment.csv",
    "03_0_Staff_Identity.csv",
    "03_7_PS_Att.csv",
    "03_10_EmpOrg.csv",
]

slds_file_upload(3, student_file_list, blanks)

# slds_file_upload(1, student_file_list, one_up)

print("done")
