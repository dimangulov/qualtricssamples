import requests

def print_dict(label, obj):
    print(label, " - ", obj)
    for x in obj:
        next_label = label + " - " + x
        next_obj = obj[x]
        if isinstance(next_obj, dict):
            print_dict(next_label, next_obj)
        else:
            print(next_label, " - ", next_obj)


#TODO your token is here https://experience.kpmgatlas.de/Q/QualtricsIdsSection/IdsSection
XAPITOKEN = "PUTYOURTOKENHERE"

headers = {"X-API-TOKEN": XAPITOKEN}

baseUrl = "https://fra1.qualtrics.com/API/v3"
surveyUrl = "/surveys"

surveysResponse = requests.get(baseUrl+surveyUrl, headers=headers)
surveys = surveysResponse.json()

print(surveys)

for survey in surveys['result']['elements']:
    print(survey['id'], "\t", survey['name'])

# print("Choose one of them, print id")
# survey_id = input()
survey_id = "SV_a2xyo21UcwnW657"
# surveys['result']['elements'][0]['id']
surveyDefinitionUrl = "/survey-definitions/"+survey_id

# surveysDefinitionResponse = requests.get(baseUrl+surveyDefinitionUrl, headers=headers)
#surveyDefinition = surveysDefinitionResponse.json()

# print(surveyDefinition)

copyHeaders = {
    "X-API-TOKEN": XAPITOKEN,
    "X-COPY-SOURCE": survey_id,
    "X-COPY-DESTINATION-OWNER": "UR_dgLbPfSCQScCFX7",
    "Content-Type": "application/json"}

surveyResponse = requests.get(baseUrl+"/surveys/"+survey_id, headers=headers)
surveyR = surveyResponse.json()["result"]
print(surveyR)
print(surveyR["name"])
surveyR["name"] = "some new name - 1"
print(surveyR["name"])

newName = input("Type name")
body = {"name": newName}
print(body)
postDefinitionResult = requests.post(baseUrl+"/surveys", json=body,  headers=copyHeaders)
print(postDefinitionResult)
print(postDefinitionResult.json())
newSurveyId = postDefinitionResult.json()["result"]["id"]

updateHeaders = {
    "X-API-TOKEN": XAPITOKEN,
    "Content-Type": "application/json"}
updateResult = requests.put(baseUrl+"/surveys/"+newSurveyId, json=body,  headers=updateHeaders)
print(updateResult)
# print_dict("survey", surveyDefinition)

