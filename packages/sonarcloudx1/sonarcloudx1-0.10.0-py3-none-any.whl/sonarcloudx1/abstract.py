from abc import ABC
from sonarqube import SonarQubeClient
import sonarqube

class AbstractSonar(ABC):

    def __init__(self, personal_access_token, organization):

        self.personal_access_token = personal_access_token
        self.sonar_url = 'https://sonarcloud.io/'
        self.organization = organization
        self.sonar = SonarQubeClient(sonarqube_url=self.sonar_url, token=personal_access_token)

    