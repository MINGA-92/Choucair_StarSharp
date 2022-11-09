
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium import webdriver
from datetime import datetime as Date

import pyautogui
import unittest
import time
import sys
import os

#Variables Globales
global driver
global Url
global NameBusinessUnit
global NameMeeting
global MeetingNumber
global EndDate
Url= "https://serenity.is/demo/"
NameBusinessUnit= "Testing..."
NameMeeting= "Testing Automation"
MeetingNumber= "1111"
Date= "11/28/2022"


def AgendamientoReunion():
	try:
		#Organization
		try:
			#Selector con Xpath
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="nav_menu1_3"]/li[1]/a/span')))
			driver.find_element(By.XPATH, '//*[@id="nav_menu1_3"]/li[1]/a/span').click()
		except:
			#Selector con FullXpath
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/aside/div[2]/div[2]/div[1]/ul/li[3]/ul/li[1]/a/span')))
			driver.find_element(By.XPATH, '//html/body/aside/div[2]/div[2]/div[1]/ul/li[3]/ul/li[1]/a/span').click()
		time.sleep(2)


		#Business Units
		try:
			#Selector con Xpath
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="nav_menu1_3_1"]/li[1]/a/span')))
			driver.find_element(By.XPATH, '//*[@id="nav_menu1_3_1"]/li[1]/a/span').click()
		except:
			#Selector con FullXpath
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/aside/div[2]/div[2]/div[1]/ul/li[3]/ul/li[1]/ul/li[1]/a/span')))
			driver.find_element(By.XPATH, '//html/body/aside/div[2]/div[2]/div[1]/ul/li[3]/ul/li[1]/ul/li[1]/a/span').click()
		time.sleep(4)


		#New Business Units
		try:
			#Selector con Xpath
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="GridDiv"]/div[2]/div[2]/div/div/div[1]/div/span')))
			driver.find_element(By.XPATH, '//*[@id="GridDiv"]/div[2]/div[2]/div/div/div[1]/div/span').click()
			time.sleep(2)
		except:
			try:
				#Selector con FullXpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/main/section/div/div[2]/div[2]/div/div/div[1]/div/span')))
				driver.find_element(By.XPATH, '//html/body/main/section/div/div[2]/div[2]/div/div/div[1]/div/span').click()
			except:
				#Selector con ID
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'GridDiv')))
				driver.find_element(By.ID,'GridDiv').click()
			time.sleep(2)

		#Name
		try:
			#Selector con FullXpath
			WebDriverWait(driver, 28).until(EC.visibility_of_element_located((By.XPATH,'//html/body/div[4]/div[2]/div/div[2]/form/div/div[1]/div/div/div[1]/input')))
			driver.find_element(By.XPATH, '//html/body/div[4]/div[2]/div/div[2]/form/div/div[1]/div/div/div[1]/input').send_keys(NameBusinessUnit)
			time.sleep(2)
		except:
			try:
				#Selector con Xpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="Serenity_Pro_Organization_BusinessUnitDialog8_Name"]')))
				driver.find_element(By.XPATH, '//*[@id="Serenity_Pro_Organization_BusinessUnitDialog8_Name"]').send_keys(NameBusinessUnit)
			except:
				#Selector con ID
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'Serenity_Pro_Organization_BusinessUnitDialog8_Name')))
				driver.find_element(By.ID,'Serenity_Pro_Organization_BusinessUnitDialog8_Name').send_keys(NameBusinessUnit)
			time.sleep(2)


		#Parent Unit
		try:
			#Selector con FullXpath
			WebDriverWait(driver, 28).until(EC.visibility_of_element_located((By.XPATH,'//html/body/div[4]/div[2]/div/div[2]/form/div/div[1]/div/div/div[2]/div[1]/a/span[2]')))
			driver.find_element(By.XPATH, '//html/body/div[4]/div[2]/div/div[2]/form/div/div[1]/div/div/div[2]/div[1]/a/span[2]').click()
			time.sleep(2)
		except:
			try:
				#Selector con Xpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="s2id_Serenity_Pro_Organization_BusinessUnitDialog8_ParentUnitId"]/a/span[2]')))
				driver.find_element(By.XPATH, '//*[@id="s2id_Serenity_Pro_Organization_BusinessUnitDialog8_ParentUnitId"]/a/span[2]').click()
			except:
				#Selector con ID
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'s2id_Serenity_Pro_Organization_BusinessUnitDialog8_ParentUnitId')))
				driver.find_element(By.ID,'s2id_Serenity_Pro_Organization_BusinessUnitDialog8_ParentUnitId').click()
			time.sleep(2)
		#Option AcmeCorp
		try:
			#Selector con FullXpath
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/div[7]/ul/li[1]/div')))
			driver.find_element(By.XPATH, '//html/body/div[7]/ul/li[1]/div').click()
			time.sleep(2)
		except:
			try:
				#Selector con Xpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-result-label-20"]')))
				driver.find_element(By.XPATH, '//*[@id="select2-result-label-20"]').click()
			except:
				#Selector con ID
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'select2-result-label-20')))
				driver.find_element(By.ID,'select2-result-label-20').click()
			time.sleep(2)


		#Salvar Business Unit
		try:
			#Selector con FullXpath
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/span')))
			driver.find_element(By.XPATH, '//html/body/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/span').click()
			time.sleep(2)
		except:
			try:
				#Selector con Xpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="Serenity_Pro_Organization_BusinessUnitDialog3_Toolbar"]/div/div/div/div[1]/div/span')))
				driver.find_element(By.XPATH, '//*[@id="Serenity_Pro_Organization_BusinessUnitDialog3_Toolbar"]/div/div/div/div[1]/div/span').click()
			except:
				#Selector con ID
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'Serenity_Pro_Organization_BusinessUnitDialog3_Toolbar')))
				driver.find_element(By.ID,'Serenity_Pro_Organization_BusinessUnitDialog3_Toolbar').click()
			time.sleep(2)

		print("¡Business Unit Creado Con Exito!   😏")



		#Meeting
		try:
			try:
				#Selector con Xpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="nav_menu1_3"]/li[2]/a/span')))
				driver.find_element(By.XPATH, '//*[@id="nav_menu1_3"]/li[2]/a/span').click()
			except:
				#Selector con FullXpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/aside/div[2]/div[2]/div[1]/ul/li[3]/ul/li[2]/a/span')))
				driver.find_element(By.XPATH, '//html/body/aside/div[2]/div[2]/div[1]/ul/li[3]/ul/li[2]/a/span').click()
			time.sleep(2)

			#Reuniones
			try:
				#Selector con Xpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="nav_menu1_3_2"]/li[1]/a/span')))
				driver.find_element(By.XPATH, '//*[@id="nav_menu1_3_2"]/li[1]/a/span').click()
			except:
				#Selector con FullXpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/aside/div[2]/div[2]/div[1]/ul/li[3]/ul/li[2]/ul/li[1]/a/span')))
				driver.find_element(By.XPATH, '//html/body/aside/div[2]/div[2]/div[1]/ul/li[3]/ul/li[2]/ul/li[1]/a/span').click()
			time.sleep(2)

			#NewReunion
			try:
				#Selector con Xpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="GridDiv"]/div[2]/div[2]/div/div/div[1]/div/span')))
				driver.find_element(By.XPATH, '//*[@id="GridDiv"]/div[2]/div[2]/div/div/div[1]/div/span').click()
				time.sleep(2)
			except:
				try:
					#Selector con FullXpath
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/main/section/div/div[2]/div[2]/div/div/div[1]/div/span')))
					driver.find_element(By.XPATH, '//html/body/main/section/div/div[2]/div[2]/div/div/div[1]/div/span').click()
				except:
					#Selector con ID
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'GridDiv')))
					driver.find_element(By.ID,'GridDiv').click()
				time.sleep(2)

			
			#NameMeeting
			try:
				#Selector con Xpath
				WebDriverWait(driver, 28).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="Serenity_Pro_Meeting_MeetingDialog10_MeetingName"]')))
				driver.find_element(By.XPATH, '//*[@id="Serenity_Pro_Meeting_MeetingDialog10_MeetingName"]').send_keys(NameMeeting)
				time.sleep(2)
			except:
				try:
					#Selector con FullXpath
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[1]/input')))
					driver.find_element(By.XPATH, '//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[1]/input').send_keys(NameMeeting)
				except:
					#Selector con ID
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'Serenity_Pro_Meeting_MeetingDialog10_MeetingName')))
					driver.find_element(By.ID,'Serenity_Pro_Meeting_MeetingDialog10_MeetingName').send_keys(NameMeeting)
				time.sleep(2)


			#Meeting Number
			try:
				#Selector con Xpath
				WebDriverWait(driver, 28).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="Serenity_Pro_Meeting_MeetingDialog10_MeetingNumber"]')))
				driver.find_element(By.XPATH, '//*[@id="Serenity_Pro_Meeting_MeetingDialog10_MeetingNumber"]').send_keys(MeetingNumber)
				time.sleep(2)
			except:
				try:
					#Selector con FullXpath
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[3]/input')))
					driver.find_element(By.XPATH, '//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[3]/input').send_keys(MeetingNumber)
				except:
					#Selector con ID
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'Serenity_Pro_Meeting_MeetingDialog10_MeetingNumber')))
					driver.find_element(By.ID,'Serenity_Pro_Meeting_MeetingDialog10_MeetingNumber').send_keys(MeetingNumber)
				time.sleep(2)


			#Meeting Type
			try:
				#Selector con Xpath
				WebDriverWait(driver, 28).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="s2id_Serenity_Pro_Meeting_MeetingDialog10_MeetingTypeId"]/a/span[2]')))
				driver.find_element(By.XPATH, '//*[@id="s2id_Serenity_Pro_Meeting_MeetingDialog10_MeetingTypeId"]/a/span[2]').click()
				time.sleep(2)
			except:
				try:
					#Selector con FullXpath
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[2]/div[1]/a/span[2]')))
					driver.find_element(By.XPATH, '//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[2]/div[1]/a/span[2]').click()
				except:
					#Selector con ID
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'s2id_Serenity_Pro_Meeting_MeetingDialog10_MeetingTypeId')))
					driver.find_element(By.ID,'s2id_Serenity_Pro_Meeting_MeetingDialog10_MeetingTypeId').click()
				time.sleep(2)


			#Option Strategy
			try:
				#Selector con FullXpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/div[6]/ul/li[5]/div')))
				driver.find_element(By.XPATH, '//html/body/div[6]/ul/li[5]/div').click()
				time.sleep(2)
			except:
				try:
					#Selector con Xpath
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-result-label-23"]')))
					driver.find_element(By.XPATH, '//*[@id="select2-result-label-23"]').click()
				except:
					#Selector con ID
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'select2-result-label-23')))
					driver.find_element(By.ID,'select2-result-label-23').click()
				time.sleep(2)


			#Start Date
			try:
				#Selector con Xpath
				WebDriverWait(driver, 28).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="Serenity_Pro_Meeting_MeetingDialog10_StartDate"]')))
				driver.find_element(By.XPATH, '//*[@id="Serenity_Pro_Meeting_MeetingDialog10_StartDate"]').click()
				Selector= "Xpath"
				time.sleep(4)
			except:
				try:
					#Selector con FullXpath
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[4]/input')))
					driver.find_element(By.XPATH, '//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[4]/input').click()
					Selector= "FullXpath"
				except:
					#Selector con ID
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'Serenity_Pro_Meeting_MeetingDialog10_StartDate')))
					driver.find_element(By.ID,'Serenity_Pro_Meeting_MeetingDialog10_StartDate').click()
					Selector= "ID"
				time.sleep(4)

			pyautogui.press('backspace')
			pyautogui.press('backspace')
			pyautogui.press('backspace')
			pyautogui.press('backspace')
			pyautogui.press('backspace')
			pyautogui.press('backspace')
			pyautogui.press('backspace')
			pyautogui.press('backspace')
			pyautogui.press('backspace')
			pyautogui.press('backspace')
			time.sleep(2)

			print("Selector: ", Selector)
			if Selector == "Xpath":
				driver.find_element(By.XPATH, '//*[@id="Serenity_Pro_Meeting_MeetingDialog10_StartDate"]').send_keys(Date)
			elif Selector == "FullXpath":
				driver.find_element(By.XPATH, '//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[4]/input').send_keys(Date)
			else:
				driver.find_element(By.ID,'Serenity_Pro_Meeting_MeetingDialog10_StartDate').send_keys(Date)
			time.sleep(2)


			#End Date
			try:
				#SelectorEnd con Xpath
				WebDriverWait(driver, 28).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="Serenity_Pro_Meeting_MeetingDialog10_EndDate"]')))
				driver.find_element(By.XPATH, '//*[@id="Serenity_Pro_Meeting_MeetingDialog10_EndDate"]').click()
				SelectorEnd= "Xpath"
				time.sleep(4)
			except:
				try:
					#SelectorEnd con FullXpath
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[5]/input')))
					driver.find_element(By.XPATH, '//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[5]/input').click()
					SelectorEnd= "FullXpath"
				except:
					#SelectorEnd con ID
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'Serenity_Pro_Meeting_MeetingDialog10_EndDate')))
					driver.find_element(By.ID,'Serenity_Pro_Meeting_MeetingDialog10_EndDate').click()
					SelectorEnd= "ID"
				time.sleep(4)

			pyautogui.press('backspace')
			pyautogui.press('backspace')
			pyautogui.press('backspace')
			pyautogui.press('backspace')
			pyautogui.press('backspace')
			pyautogui.press('backspace')
			pyautogui.press('backspace')
			pyautogui.press('backspace')
			pyautogui.press('backspace')
			pyautogui.press('backspace')
			time.sleep(2)

			print("SelectorEnd: ", SelectorEnd)
			if SelectorEnd == "Xpath":
				driver.find_element(By.XPATH, '//*[@id="Serenity_Pro_Meeting_MeetingDialog10_EndDate"]').send_keys(Date)
			elif SelectorEnd == "FullXpath":
				driver.find_element(By.XPATH, '//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[5]/input').send_keys(Date)
			else:
				driver.find_element(By.ID,'Serenity_Pro_Meeting_MeetingDialog10_EndDate').send_keys(Date)
			time.sleep(2)

			#HoraInicio
			try:
				#Selector con Xpath
				WebDriverWait(driver, 28).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="Serenity_Pro_Meeting_MeetingDialog10_PropertyGrid"]/div/div/div[4]/select')))
				driver.find_element(By.XPATH, '//*[@id="Serenity_Pro_Meeting_MeetingDialog10_PropertyGrid"]/div/div/div[4]/select').click()
				time.sleep(2)
			except:
				try:
					#Selector con FullXpath
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[4]/select')))
					driver.find_element(By.XPATH, '//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[4]/select').click()
				except:
					#Selector con ID
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'Serenity_Pro_Meeting_MeetingDialog10_PropertyGrid')))
					driver.find_element(By.ID,'Serenity_Pro_Meeting_MeetingDialog10_PropertyGrid').click()
				time.sleep(2)
			#Option HoraInicio
			try:
				#Selector con FullXpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[4]/select/option[173]')))
				driver.find_element(By.XPATH, '//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[4]/select/option[173]').click()
				time.sleep(2)
			except:
				try:
					#Selector con Xpath
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="Serenity_Pro_Meeting_MeetingDialog10_PropertyGrid"]/div/div/div[4]/select/option[173]')))
					driver.find_element(By.XPATH, '//*[@id="Serenity_Pro_Meeting_MeetingDialog10_PropertyGrid"]/div/div/div[4]/select/option[173]').click()
				except:
					#Selector con ID
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'Serenity_Pro_Meeting_MeetingDialog10_PropertyGrid')))
					driver.find_element(By.ID,'Serenity_Pro_Meeting_MeetingDialog10_PropertyGrid').click()
				time.sleep(2)


			#HoraFinal
			try:
				#Selector con Xpath
				WebDriverWait(driver, 28).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="Serenity_Pro_Meeting_MeetingDialog10_PropertyGrid"]/div/div/div[5]/select')))
				driver.find_element(By.XPATH, '//*[@id="Serenity_Pro_Meeting_MeetingDialog10_PropertyGrid"]/div/div/div[5]/select').click()
				time.sleep(2)
			except:
				try:
					#Selector con FullXpath
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[5]/select')))
					driver.find_element(By.XPATH, '//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[5]/select').click()
				except:
					#Selector con ID
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'Serenity_Pro_Meeting_MeetingDialog10_PropertyGrid')))
					driver.find_element(By.ID,'Serenity_Pro_Meeting_MeetingDialog10_PropertyGrid').click()
				time.sleep(2)
			#Option HoraFinal
			try:
				#Selector con FullXpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[5]/select/option[181]')))
				driver.find_element(By.XPATH, '//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[5]/select/option[181]').click()
				time.sleep(2)
			except:
				try:
					#Selector con Xpath
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="Serenity_Pro_Meeting_MeetingDialog10_PropertyGrid"]/div/div/div[5]/select/option[37]')))
					driver.find_element(By.XPATH, '//*[@id="Serenity_Pro_Meeting_MeetingDialog10_PropertyGrid"]/div/div/div[5]/select/option[37]').click()
				except:
					#Selector con ID
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'Serenity_Pro_Meeting_MeetingDialog10_PropertyGrid')))
					driver.find_element(By.ID,'Serenity_Pro_Meeting_MeetingDialog10_PropertyGrid').click()
				time.sleep(2)

			
			#Location
			try:
				#Selector con Xpath
				WebDriverWait(driver, 28).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="s2id_Serenity_Pro_Meeting_MeetingDialog10_LocationId"]/a/span[2]')))
				driver.find_element(By.XPATH, '//*[@id="s2id_Serenity_Pro_Meeting_MeetingDialog10_LocationId"]/a/span[2]').click()
				time.sleep(2)
			except:
				try:
					#Selector con FullXpath
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[6]/div[1]/a/span[2]')))
					driver.find_element(By.XPATH, '//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[6]/div[1]/a/span[2]').click()
				except:
					#Selector con ID
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'s2id_Serenity_Pro_Meeting_MeetingDialog10_LocationId')))
					driver.find_element(By.ID,'s2id_Serenity_Pro_Meeting_MeetingDialog10_LocationId').click()
				time.sleep(2)
			#Option Location
			try:
				#Selector con FullXpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/div[7]/ul/li[4]/div/span')))
				driver.find_element(By.XPATH, '//html/body/div[7]/ul/li[4]/div/span').click()
				time.sleep(2)
			except:
				try:
					#Selector con Xpath
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-result-label-11"]/span')))
					driver.find_element(By.XPATH, '//*[@id="select2-result-label-11"]/span').click()
				except:
					pyautogui.press('enter')
				time.sleep(4)
			
			#Unit
			try:
				#Selector con FullXpath
				WebDriverWait(driver, 28).until(EC.visibility_of_element_located((By.XPATH,'//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[7]/div[1]/a/span[2]')))
				driver.find_element(By.XPATH, '//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[7]/div[1]/a/span[2]').click()
				time.sleep(2)
			except:
				try:
					#Selector con Xpath
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="s2id_Serenity_Pro_Meeting_MeetingDialog10_UnitId"]/a/span[2]')))
					driver.find_element(By.XPATH, '//*[@id="s2id_Serenity_Pro_Meeting_MeetingDialog10_UnitId"]/a/span[2]').click()
				except:
					#Selector con ID
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'s2id_Serenity_Pro_Meeting_MeetingDialog10_UnitId')))
					driver.find_element(By.ID,'s2id_Serenity_Pro_Meeting_MeetingDialog10_UnitId').click()
				time.sleep(2)
			#Option Unit
			try:
				#Selector con Xpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-result-label-399"]')))
				driver.find_element(By.XPATH, '//*[@id="select2-result-label-399"]').click()
				time.sleep(2)
			except:
				try:
					#Selector con FullXpath
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/div[8]/ul/li[4]/div')))
					driver.find_element(By.XPATH, '//html/body/div[8]/ul/li[4]/div').click()
				except:
					#Selector con ID
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'select2-result-label-399')))
					driver.find_element(By.ID,'select2-result-label-399').click()
				time.sleep(2)

			
			#Organized By
			try:
				#Selector con FullXpath
				WebDriverWait(driver, 28).until(EC.visibility_of_element_located((By.XPATH,'//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[8]/div[1]/a/span[2]')))
				driver.find_element(By.XPATH, '//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[8]/div[1]/a/span[2]').click()
				time.sleep(2)
			except:
				try:
					#Selector con Xpath
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="s2id_Serenity_Pro_Meeting_MeetingDialog10_OrganizerContactId"]/a/span[2]')))
					driver.find_element(By.XPATH, '//*[@id="s2id_Serenity_Pro_Meeting_MeetingDialog10_OrganizerContactId"]/a/span[2]').click()
				except:
					#Selector con ID
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'s2id_Serenity_Pro_Meeting_MeetingDialog10_OrganizerContactId')))
					driver.find_element(By.ID,'s2id_Serenity_Pro_Meeting_MeetingDialog10_OrganizerContactId').click()
				time.sleep(2)
			#Option Organized By
			try:
				#Selector con Xpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-result-label-57"]')))
				driver.find_element(By.XPATH, '//*[@id="select2-result-label-57"]').click()
				time.sleep(2)
			except:
				try:
					#Selector con FullXpath
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/div[7]/ul/li[20]/div')))
					driver.find_element(By.XPATH, '//html/body/div[7]/ul/li[20]/div').click()
				except:
					#Selector con ID
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'select2-result-label-57')))
					driver.find_element(By.ID,'select2-result-label-57').click()
				time.sleep(2)


			#Reporter
			try:
				#Selector con FullXpath
				WebDriverWait(driver, 28).until(EC.visibility_of_element_located((By.XPATH,'//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[9]/div[1]/a/span[2]')))
				driver.find_element(By.XPATH, '//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[9]/div[1]/a/span[2]').click()
				time.sleep(2)
			except:
				try:
					#Selector con Xpath
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="s2id_Serenity_Pro_Meeting_MeetingDialog10_ReporterContactId"]/a/span[2]')))
					driver.find_element(By.XPATH, '//*[@id="s2id_Serenity_Pro_Meeting_MeetingDialog10_ReporterContactId"]/a/span[2]').click()
				except:
					#Selector con ID
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'s2id_Serenity_Pro_Meeting_MeetingDialog10_ReporterContactId')))
					driver.find_element(By.ID,'s2id_Serenity_Pro_Meeting_MeetingDialog10_ReporterContactId').click()
				time.sleep(2)
			#Option Reporter
			try:
				#Selector con Xpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-result-label-164"]')))
				driver.find_element(By.XPATH, '//*[@id="select2-result-label-164"]').click()
				time.sleep(2)
			except:
				try:
					#Selector con FullXpath
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/div[8]/ul/li[27]/div')))
					driver.find_element(By.XPATH, '//html/body/div[8]/ul/li[27]/div').click()
				except:
					#Selector con ID
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'select2-result-label-164')))
					driver.find_element(By.ID,'select2-result-label-164').click()
				time.sleep(2)


			#Attendee List
			try:
				#Selector con FullXpath
				WebDriverWait(driver, 28).until(EC.visibility_of_element_located((By.XPATH,'//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[10]/div[1]/div[1]/div[2]/a/span[2]')))
				driver.find_element(By.XPATH, '//html/body/main/section/div[2]/div[2]/div[1]/div[2]/form/div/div/div/div/div[10]/div[1]/div[1]/div[2]/a/span[2]').click()
				time.sleep(2)
			except:
				try:
					#Selector con Xpath
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="s2id_autogen11"]/a/span[2]')))
					driver.find_element(By.XPATH, '//*[@id="s2id_autogen11"]/a/span[2]').click()
				except:
					#Selector con ID
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'s2id_autogen11')))
					driver.find_element(By.ID,'s2id_autogen11').click()
				time.sleep(2)
			#Option Attendee List
			try:
				#Selector con Xpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select2-result-label-304"]')))
				driver.find_element(By.XPATH, '//*[@id="select2-result-label-304"]').click()
				time.sleep(2)
			except:
				try:
					#Selector con FullXpath
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/div[9]/ul/li[67]/div')))
					driver.find_element(By.XPATH, '//html/body/div[9]/ul/li[67]/div').click()
				except:
					#Selector con ID
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'select2-result-label-304')))
					driver.find_element(By.ID,'select2-result-label-304').click()
				time.sleep(2)


			#Salvar Reunion
			try:
				#Selector con FullXpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/main/section/div[2]/div[2]/div[1]/div[1]/div/div/div/div[1]/div')))
				driver.find_element(By.XPATH, '//html/body/main/section/div[2]/div[2]/div[1]/div[1]/div/div/div/div[1]/div').click()
				time.sleep(2)
			except:
				try:
					#Selector con Xpath
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="Serenity_Pro_Meeting_MeetingDialog10_Toolbar"]/div/div/div/div[1]/div')))
					driver.find_element(By.XPATH, '//*[@id="Serenity_Pro_Meeting_MeetingDialog10_Toolbar"]/div/div/div/div[1]/div').click()
				except:
					#Selector con ID
					WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.ID,'Serenity_Pro_Meeting_MeetingDialog10_Toolbar')))
					driver.find_element(By.ID,'Serenity_Pro_Meeting_MeetingDialog10_Toolbar').click()
				time.sleep(2)

			print("¡Proceso Complwto Finalizado Con Exito!   😏")
			print(" - 😏😏😏 - ")

		except Exception as e:
			print("☠ eRrOr Meeting:", e)
			raise e	

	except Exception as e:
		print("☠ eRrOr Agendamiento Reunion:", e)
		raise e

def Logueo():
	try:
		try:
			#BtnIngresar
			WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="LoginPanel0_LoginButton"]')))
			driver.find_element(By.XPATH, '//*[@id="LoginPanel0_LoginButton"]').click()
			time.sleep(4)
		except:
			try:
				#Selector con JSpath
				driver.execute_script('document.querySelector("#LoginPanel0_LoginButton").click()')
				print("Ingreso Con JSpath...")
			except:
				#Selector con FullXpath
				WebDriverWait(driver, 11).until(EC.visibility_of_element_located((By.XPATH,'//html/body/div[1]/div[1]/div[1]/form/div[3]/button')))
				driver.find_element(By.XPATH, '//html/body/div[1]/div[1]/div[1]/form/div[3]/button').click()
			time.sleep(4)
		ComprobarLogin= True

	except Exception as e:
		ComprobarLogin= False
		print("☠ eRrOr Logueo:", e)
		raise e

	if ComprobarLogin == True:
		print("Logueo Correcto  😏")
		driver.maximize_window()
		time.sleep(2)
		AgendamientoReunion()
	else:
		driver.close()
		print("Logueo Incorrecto  ☠")
		time.sleep(4)
		ChromeDriverInicial()


def ChromeDriverInicial():

	global driver
	os.system("TASKKILL /F /IM chromedriver.exe")
	RutaEjecutablePrograma = os.path.dirname(sys.argv[0]) + "\\"
	ComprobarDriver= " "
	
	try:
		RutaChromeDriver= RutaEjecutablePrograma + 'chromedriver.exe'
		ChromeOption= webdriver.ChromeOptions()
		driver = webdriver.Chrome(executable_path=RutaChromeDriver, options=ChromeOption)
		driver.set_window_rect(x=392, y=11, width=1128, height=911)
		driver.get(Url)
		time.sleep(2)
		print("Ingresando A= " +(driver.current_url)+ " ...")
		ComprobarDriver= "OK"
	except Exception as e:
		#raise e
		print("☠ Error / En El Driver De Chrome  😪")
		ComprobarDriver= "False"

	print("ComprobarDriver: "+ ComprobarDriver)
	if ComprobarDriver == "OK":
		time.sleep(2)
		Logueo()
	else: 	
		try:
			print("Instalando Chrome...")
			time.sleep(2)
			driver = webdriver.Chrome(ChromeDriverManager().install())
			driver.set_window_rect(x=392, y=11, width=1128, height=911)
			driver.get(Url)
			print("Ingresando A= " +(driver.current_url)+ " ...")
			ComprobarDriver= "OK"
			time.sleep(2)
		except Exception as e:
			print("☠ eRrOr Instalando Chrome... ☠" + str(e))
			ComprobarDriver = False
			time.sleep(2)
			try:
				#Capturar De Pantalla.
				Pantallazo= pyautogui.screenshot()
				Pantallazo.save("Reportes/Capturas/eRrOr_InstalandoChrome.png")
				time.sleep(2)
			except:
				print("eRrOr=>  !No Se Guardo La Imagen!    🤔")
				pass

		print("ComprobarDriver: "+ ComprobarDriver)
		if ComprobarDriver == "OK":
			time.sleep(2)
			Logueo()
		else:
			time.sleep(2)
			ChromeDriverInicial()

ChromeDriverInicial()
