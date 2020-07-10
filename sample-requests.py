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
XAPITOKEN = "PUTYOURAPITOKENHERE"

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
survey_id = surveys['result']['elements'][0]['id']
surveyDefinitionUrl = "/survey-definitions/"+survey_id
surveysDefinitionResponse = requests.get(baseUrl+surveyDefinitionUrl, headers=headers)
surveyDefinition = surveysDefinitionResponse.json()

print_dict("survey", surveyDefinition)

