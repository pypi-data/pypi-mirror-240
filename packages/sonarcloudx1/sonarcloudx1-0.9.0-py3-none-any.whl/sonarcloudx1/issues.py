import logging
logging.basicConfig(level=logging.INFO)
from sonarcloudx1.abstract import AbstractSonar
from sonarcloudx1	import factories
import json

# Represents a software Components
class Issues(AbstractSonar):

	def __init__(self,personal_access_token, organization):
		super(Issues,self).__init__(personal_access_token=personal_access_token, organization=organization)
	
	def get_qnt_paginas(self, project):
		try:
			logging.info("Start function: get_issues_qnt_paginas")
			result = self.sonar.issues.search_issues(projects=project['key'])
			quant = result['paging']['total']/100 #100 é o atributo ps DEFAULT. ps = número de elementos por página.
			quant = int(quant) + 1
			return quant

		except Exception as e: 
			logging.error("OS error: {0}".format(e))
			logging.error(e.__dict__)

	logging.info("Retrieve issues quant paginas")	


	def get_all(self, today=False): 
		try:
			logging.info("Start function: get_issues")
			
			project_service = factories.ProjectFactory(personal_access_token=self.personal_access_token, organization=self.organization)
			projects = project_service.get_all()

			list_dict_issues = []


			for project in projects:
				
				for pagina in range(0, self.get_qnt_paginas(project=project)): #Resolvendo o problema de paginação
					issues = self.sonar.issues.search_issues(projects=project['key'], p=pagina)
					issues['project'] = project
					list_dict_issues.append(issues)
					
							

			return list_dict_issues

		except Exception as e: 
			logging.error("OS error: {0}".format(e))
			logging.error(e.__dict__) 

		logging.info("Retrieve All Issues")
		
