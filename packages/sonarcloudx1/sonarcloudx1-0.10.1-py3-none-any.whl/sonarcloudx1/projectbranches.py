import logging
logging.basicConfig(level=logging.INFO)
from sonarcloudx1.abstract import AbstractSonar
from sonarcloudx1	import factories

# Represents a software Project Branches
class ProjectBranches(AbstractSonar):

	def __init__(self,personal_access_token, organization):
		super(ProjectBranches,self).__init__(personal_access_token=personal_access_token,organization=organization)
	
	def get_projectbranches(self, project_key):
		return self.sonar.project_branches.search_project_branches(project=project_key)

	def get_all(self, today=False): 
		try:
			logging.info("Start function: get_projectbranches")
			
			project_service = factories.Project(personal_access_token=self.personal_access_token, organization=self.organization)
			projects = project_service.get_all()
			projectbranches = []
			
			for project in projects:
				projectbranches_return = self.get_projectbranches(project['key'])
				projectbranches_return['project'] = project
				projectbranches.append(projectbranches_return)

			return projectbranches

		except Exception as e: 
			logging.error("OS error: {0}".format(e))
			logging.error(e.__dict__) 

		logging.info("Retrieve All Project Branches")
		
		
