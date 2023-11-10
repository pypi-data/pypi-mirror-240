import logging
logging.basicConfig(level=logging.INFO)
from sonarcloudx1.abstract import AbstractSonar
from sonarcloudx1	import factories

# Represents a software Project Pull Requests
class ProjectPullRequests(AbstractSonar):

	def __init__(self,personal_access_token, organization):
		super(ProjectPullRequests,self).__init__(personal_access_token=personal_access_token,organization=organization)
	
	def get_projectpullrequests(self, project_key):
		return self.sonar.project_pull_requests.search_project_pull_requests(project=project_key)

	def get_all(self, today=False): 
		try:
			logging.info("Start function: get_projectpulltrequests")
			
			project_service = factories.Project(personal_access_token=self.personal_access_token,organization=self.organization)
			projects = project_service.get_all()
			projectpullrequests = []
			
			for project in projects:
				projectpullrequests_return = self.get_projectpullrequests(project['key'])
				projectpullrequests_return['project'] = project
				projectpullrequests.append(projectpullrequests_return)

			return projectpullrequests

		except Exception as e: 
			logging.error("OS error: {0}".format(e))
			logging.error(e.__dict__) 

		logging.info("Retrieve All Project Pull Requests")
		
