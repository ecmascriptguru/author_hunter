import json

from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions

from flask import current_app

class WatsonMixin(object):
    """
    Watson library to collect authors by using **IBM Watson** service
    """
    def __init__(self):
        username = current_app.config['WATSON_USERNAME']
        password = current_app.config['WATSON_PASSWORD']
        if username and password:
            self.engine = NaturalLanguageUnderstandingV1(username=username, password=password, version='2017-02-27')
        else:
            print("WATSON API KEY missing in config.")
            return False

    def set_credentials(self, username, password):
        self.username = username
        self.password = password
        self.engine = NaturalLanguageUnderstandingV1(username=username, password=password, version='2017-02-27')

    def get_authors(self, url, **kwargs):
        if not self.validate:
            return []
            
        try:
            response = self.engine.analyze(
                url=url,
                features=Features(
                    entities=EntitiesOptions(
                    **kwargs,
                    limit=250)))
            
            authors = list()
            for entity in response.get('entities'):
                if entity.get('type') == 'Person':
                    authors.append(entity.get('text'))

            return authors
        except Exception as e:
            print(str(e))
            return []

    def validate(self):
        if not self.engine:
            print("Please reinitialize engine with watson api key.")
            return False
        else:
            return True

