import logging
logging.basicConfig(level=logging.INFO)
from sonarcloudx1.abstract import AbstractSonar

# Represents a software Project
class SupportedProgramingLanguages(AbstractSonar):

	def __init__(self,personal_access_token, organization):
		super(SupportedProgramingLanguages,self).__init__(personal_access_token=personal_access_token, organization=organization)						


	def get_all(self, today=False): 


		try:			
			logging.info("Start function: get_projects")			
			            
			supported_programming_languages = self.sonar.languages.get_supported_programming_languages()

			if today == False:
				fazer_nada = 2
			
		except Exception as e: 
			logging.error("OS error: {0}".format(e))
			logging.error(e.__dict__) 

		logging.info("Retrieve All Projects")
		
		return supported_programming_languages['languages']

