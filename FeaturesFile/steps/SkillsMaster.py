"""
    Step definition SkillsMaster.py
    -----------------
    Contains the given, when, then step definitions for the endpoints /Skills and /Skills/<id>
"""
import json

import pandas as pd
import requests as requests
from behave import *
from utilFiles.CONSTANTS import *
from utilFiles.Fetch_data_from_sql import get_data_from_DB, get_deleted_data_from_DB
from utilFiles.JSON_schema_validation import validate_json
from utilFiles.fetch_data_from_property_file import readProperties

use_step_matcher("re")

"""
    "Given" Step definition SkillsMaster.py
    -----------------
    This step is where the configuration details of the API /Skills are fetched
"""

@given("Skills User is on Endpoint: url/Skills with valid username and password")
def step_impl(context):
    read_file = readProperties(CONFIG_PROPERTIES_FILE)
    context.base_url = read_file.get(URL).data
    context.username = read_file.get(Username).data
    context.password = read_file[Pwd].data

@given('Skills User with  username & password from "(?P<sheetName>.+)" and (?P<rowNumber>.+) is on Endpoint: url/Skills')
def step_impl(context, sheetName, rowNumber):
    skillsread_file = readProperties(SKILLS_PROPERTIES_FILE)
    context.ExcelFilePath = skillsread_file.get(ExcelPath).data
    data = pd.read_excel(context.ExcelFilePath, sheetName)
    context.base_url = skillsread_file.get(URL).data
    context.UserName = data[CONST_USER_NAME][int(rowNumber)]
    context.Password = data[CONST_PASSWORD][int(rowNumber)]
    context.StatusCode = data[CONST_STATUS_CODE][int(rowNumber)]
    print("Authorization details:", type(context.UserName), context.Password)

"""
    "When" Step definition SkillsMaster.py
    -----------------
    This step sends requests to the /Skills API
"""
@when("skills User sends GET request")
def step_impl(context):
    context.response = requests.get(context.base_url+SKILLS_ENDPOINT, auth=(context.username, context.password))
    print(context.response.text)


@when('User sends GET request on skill id from "(?P<SheetName>.+)" and (?P<RowNumber>.+)')
def step_impl(context, SheetName, RowNumber):
    skillsread_file = readProperties(SKILLS_PROPERTIES_FILE)
    context.ExcelFilePath = skillsread_file.get(ExcelPath).data
    data = pd.read_excel(context.ExcelFilePath, SheetName)
    context.Skill_ID = data[CONST_SKILL_ID][int(RowNumber)]
    context.StatusCode = data[CONST_STATUS_CODE][int(RowNumber)]
    context.StatusMsg = data[CONST_STATUS_MESSAGE][int(RowNumber)]
    context.response = requests.get(context.base_url + SKILLS_ENDPOINT+"/"+str(context.Skill_ID), auth=(context.username, context.password))
    print(context.response.text)


@when("skills User sends  a request on GET")
def step_impl(context):
    context.response = requests.get(context.base_url + SKILLS_ENDPOINT, auth=(context.UserName, context.Password))
    print(context.response.text)


@when('skills User sends POST request body in skills from "(?P<SheetName>.+)" and (?P<RowNumber>.+) with valid JSON Schema')
def step_impl(context, SheetName, RowNumber):
    skillsread_file = readProperties(SKILLS_PROPERTIES_FILE)
    context.ExcelFilePath = skillsread_file.get(ExcelPath).data
    data = pd.read_excel(context.ExcelFilePath, SheetName)
    context.Skill_name = data[CONST_SKILL_NAME][int(RowNumber)]
    if context.Skill_name == 'true' or context.Skill_name == 'false':
        context.Skill_name = bool(context.Skill_name)

    context.body = {CONST_SKILL_NAME: context.Skill_name}
    context.StatusCode = data[CONST_STATUS_CODE][int(RowNumber)]
    context.StatusMsg = data[CONST_STATUS_MESSAGE][int(RowNumber)]
    context.response = requests.post(context.base_url + SKILLS_ENDPOINT, json=context.body,
                                     auth=(context.username, context.password))

    print(context.response.text)



@when('skills User sends PUT request on id and request body in skills from "(?P<SheetName>.+)" and (?P<RowNumber>.+) with valid JSON Schema')
def step_impl(context, SheetName, RowNumber):
    skillsread_file = readProperties(SKILLS_PROPERTIES_FILE)
    context.ExcelFilePath = skillsread_file.get(ExcelPath).data
    data = pd.read_excel(context.ExcelFilePath, SheetName)
    context.Skill_ID = int(data[CONST_SKILL_ID][int(RowNumber)])
    context.Skill_name = data[CONST_SKILL_NAME][int(RowNumber)]
    print(context.Skill_name)
    if context.Skill_name == 'true' or context.Skill_name == 'false':
        context.Skill_name = bool(context.Skill_name)
    context.body = {CONST_SKILL_NAME: context.Skill_name}
    context.StatusCode = data[CONST_STATUS_CODE][int(RowNumber)]
    context.StatusMsg = data[CONST_STATUS_MESSAGE][int(RowNumber)]
    context.response = requests.put(context.base_url + SKILLS_ENDPOINT + "/" + str(context.Skill_ID),
                                    json=context.body, auth=(context.username, context.password))
    print(context.response.text)


@when('skills User sends DELETE skill id ON DELETE Method from "(?P<SheetName>.+)" and (?P<RowNumber>.+)')
def step_impl(context, SheetName, RowNumber):
    skillsread_file = readProperties(SKILLS_PROPERTIES_FILE)
    context.ExcelFilePath = skillsread_file.get(ExcelPath).data
    data = pd.read_excel(context.ExcelFilePath, SheetName)
    context.Skill_ID = data[CONST_SKILL_ID][int(RowNumber)]
    context.StatusCode = data[CONST_STATUS_CODE][int(RowNumber)]
    context.StatusMsg = data[CONST_STATUS_MESSAGE][int(RowNumber)]
    context.response = requests.delete(context.base_url + SKILLS_ENDPOINT + "/" + str(context.Skill_ID),
                                       auth=(context.username, context.password))
    print(context.response.text)

"""
    Then Step definition SkillsMaster.py
    -----------------
    This step verifies the StatusCode and StatusMessage of /Skills API
"""

@then("skills User validates StatusCode")
def step_impl(context):
    assert context.response.status_code == 200

@then('skills User validates the StatusCode from "(?P<SheetName>.+)" sheet and (?P<RowNumber>.+) row')
def step_impl(context, SheetName, RowNumber):
    assert context.response.status_code == context.StatusCode


@then('skills User validates the StatusCode and StatusMessage from "(?P<SheetName>.+)" sheet and (?P<RowNumber>.+) row')
def step_impl(context, SheetName, RowNumber):
    assert context.response.status_code == context.StatusCode
    json_object = json.loads(context.response.text)
    if not (context.StatusCode == CONST_GET_SUCCESS_STATUS_CODE) :
       assert context.StatusMsg == json_object["message"]

@then('skills User validates the StatusCode and the StatusMessage from "(?P<SheetName>.+)" sheet and (?P<RowNumber>.+) row')
def step_impl(context, SheetName, RowNumber):
    assert context.response.status_code == context.StatusCode
    json_object = json.loads(context.response.text)
    if (context.StatusCode == CONST_GET_SUCCESS_STATUS_CODE) or (
            context.StatusCode == CONST_POST_SUCCESS_STATUS_CODE):
       assert context.StatusMsg == json_object["message"]

"""
    The Following Steps are to validate the JSON schema response of GET/GET ID/POST/PUT methods
"""

@step("skills JSON schema is valid")
def step_impl(context):
    # Convert json to python object.
    jsonData = json.loads(context.response.text)
    Newread_file = readProperties(SKILLS_PROPERTIES_FILE)
    context.jsonFilePath=Newread_file.get(Skills_GET_Filepath).data
    # validate it
    is_valid, msg = validate_json(jsonData,context.jsonFilePath)
    print(msg)


@step('JSON schema is valid for GET with id in Skills')
def step_impl(context):
    if (context.StatusCode == CONST_GET_SUCCESS_STATUS_CODE) or (context.StatusCode == CONST_POST_SUCCESS_STATUS_CODE):
        jsonData = json.loads(context.response.text)
        Newread_file = readProperties(SKILLS_PROPERTIES_FILE)
        context.jsonFilePath = Newread_file.get(Skills_GET_id_Filepath).data

        # validate it
        is_valid, msg = validate_json(jsonData, context.jsonFilePath)
        print(msg)

@step("JSON schema is valid for POST/PUT METHOD in Skills")
def step_impl(context):
    if (context.StatusCode == CONST_GET_SUCCESS_STATUS_CODE) or (context.StatusCode == CONST_POST_SUCCESS_STATUS_CODE):
        jsonData = json.loads(context.response.text)
        print("jsonData:",jsonData)
        Newread_file = readProperties(SKILLS_PROPERTIES_FILE)
        context.jsonFilePath = Newread_file.get(Skills_POST_Filepath).data

        # validate it
        is_valid, msg = validate_json(jsonData, context.jsonFilePath)
        print(msg)


@step('skills User should receive the skill in JSON body from "(?P<SheetName>.+)" and (?P<RowNumber>.+)')
def step_impl(context, SheetName, RowNumber):
    if (context.StatusCode == CONST_GET_SUCCESS_STATUS_CODE) or (context.StatusCode == CONST_POST_SUCCESS_STATUS_CODE):
         print("Response:", context.response.text)
         Newread_file = readProperties(SKILLS_PROPERTIES_FILE)
         context.ExcelFilePath = Newread_file.get(ExcelPath).data
         data = pd.read_excel(context.ExcelFilePath, SheetName)
         context.Skill_name = data[CONST_SKILL_NAME][int(RowNumber)]
         jsonData = json.loads(context.response.text)

         assert jsonData[CONST_SKILL_NAME] == context.Skill_name

"""
    The Following Steps are to validate DB for GET ID/POST/PUT/DELETE methods
"""



@step('skills check the Database with Skill id from "(?P<SheetName>.+)" and (?P<RowNumber>.+)')
def step_impl(context, SheetName, RowNumber):
    if (context.StatusCode == CONST_GET_SUCCESS_STATUS_CODE) or (context.StatusCode == CONST_POST_SUCCESS_STATUS_CODE):
        read_file = readProperties(CONFIG_PROPERTIES_FILE)
        context.dbHostname = read_file.get(dbHostname).data
        context.dbName = read_file.get(dbName).data
        context.dbUsername = read_file.get(dbUsername).data
        context.dbPassword = read_file.get(dbPassword).data
        context.Query="select skill_id,skill_name from tbl_lms_skill_master where skill_id='" + str(context.Skill_ID)+"'"
        dbdf=get_data_from_DB(context.dbHostname, context.dbName, context.dbUsername, context.dbPassword, context.Query)
        json_dic = json.loads(context.response.text)


        for key in dbdf.keys() & json_dic.keys():
            if key in json_dic and dbdf:
                assert json_dic[key] == dbdf[key]


@step('skills User checks the Database to validate deletion from "(?P<SheetName>.+)" sheet and (?P<RowNumber>.+) row')
def step_impl(context, SheetName, RowNumber):
    if (context.StatusCode == CONST_GET_SUCCESS_STATUS_CODE) or (context.StatusCode == CONST_POST_SUCCESS_STATUS_CODE):
        read_file = readProperties(CONFIG_PROPERTIES_FILE)
        context.dbHostname = read_file.get(dbHostname).data
        context.dbName = read_file.get(dbName).data
        context.dbUsername = read_file.get(dbUsername).data
        context.dbPassword = read_file.get(dbPassword).data
        context.Query = "SELECT EXISTS(SELECT * FROM tbl_lms_skill_master WHERE skill_id='" + str(context.Skill_ID)+"'" + ")"

        dbdf = get_deleted_data_from_DB(context.dbHostname, context.dbName, context.dbUsername, context.dbPassword,
                            context.Query)

        if dbdf['exists']:
           print("Deletion incomplete")

        else:
           print("Successfully deleted")

