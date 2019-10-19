import dialogflow
import json
import os
import google.protobuf  as pf

project_id = os.getenv("DIALOGFLOW_PROJECT_ID")
session_id = os.getenv("DIALOGFLOW_SESSION_ID")
language_code = 'en'

def detect_intent_texts(text):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)

    return response.query_result.intent.display_name

#print(detect_intent_texts("วน"))