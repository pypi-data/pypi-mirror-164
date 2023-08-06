
import os
from os.path import basename
import re 	#regular expressions
import shutil
import zipfile

class ProjectBuilder:

	def __init__(self):

		self.WorkingDirectory		= os.getcwd()	# Root Folder where manage.py is located
		self.inputProjectName		= ""			# User inputs existing development project name
		self.inputNewProjectName	= ""			# User inputs new name of project to deploy	

		self.srcProjectFolder		= ""			# Location of development project folder.

		self.distProjectsFolder		= os.path.join( self.WorkingDirectory, "dist\\projects")
		self.distProjectFolderUpper	= ""
		self.distProjectFolderLower	= ""

		self.srcManagePy			= ""
		self.distManagePy			= ""			# Location in distributino folder

		self.srcGuardedJSON			= ""
		self.distGuardedJSON		= ""

		self.distSettingsPy			= ""
		self.distAsgiPy				= ""
		self.distWsgiPy				= ""

		self.ZipFileName			= ""			# takes on inputNewProjectName + '.zip'

		# Execute
		try:
			self.LaunchFolderTest()				# Program launching from Root Folder?
			self.GetInputs()					# Get user inputs at console.
			self.SetLocations()					# Figure out where the original stuff and the new stuff goes.
			self.CopyToDist()					# Copy new project to the \dist\ folder
			self.UpdateFiles()					# Update the new project files.
			self.WriteZipFile()
		except  Exception as Oops:
			print(Oops)
			print("Cannot Continue. Please resolve the error and run again.")
			exit()

		# Done executing.
		print("Note. Work complete.")

	# =================== METHODS

	def LaunchFolderTest(self):

		if not (os.path.isfile('manage.py')):
			print('Oops. This program must run in the same folder as where "manage.py" exists. Quitting.')
			exit()


	def GetInputs(self):

		self.inputProjectName = input("Input Existing Project Name: ")
		self.srcProjectFolder =  os.path.join(self.WorkingDirectory, self.inputProjectName)
		if not os.path.isdir(self.srcProjectFolder):
			print('Note. Oops. Folder named ' + self.inputProjectName + ' was not found. Have to quit.')
			exit()

		print("Note. Folder Found.")
		print("Note. Inspecting Folder.")

		# Passed Existing Project Validations.	
		self.inputNewProjectName = input("Input Name For New Django Project To Deploy: ")


	def SetLocations(self):

		print("Note. Setting locations for new project.")

		#self.relativeDistProjects 

		self.srcProjectFolder		= os.path.join(self.WorkingDirectory, self.inputProjectName)
		self.distProjectFolderUpper	= os.path.join(self.distProjectsFolder, self.inputNewProjectName)
		self.distProjectFolderLower	= os.path.join(self.distProjectFolderUpper, self.inputNewProjectName)

		self.srcManagePy			= os.path.join(self.WorkingDirectory, "manage.py")
		self.distManagePy			= os.path.join(self.distProjectFolderUpper, 'manage.py')

		self.srcGuardedJSON			= os.path.join(self.WorkingDirectory, "guardedsettings.json")
		self.distGuardedJSON		= os.path.join(self.distProjectFolderUpper, 'guardedsettings.json')

		self.distSettingsPy 		= os.path.join(self.distProjectFolderLower, "settings.py")
		self.distAsgiPy			= os.path.join(self.distProjectFolderLower, "asgi.py")
		self.distWsgiPy			= os.path.join(self.distProjectFolderLower, "wsgi.py")

		self.ZipFileName			= os.path.join(self.distProjectsFolder, self.inputNewProjectName + "_Project.zip")


	def CopyToDist(self):

		print("Note. Copying new project to \\dist\\ folder.")

		shutil.copytree(self.srcProjectFolder, self.distProjectFolderLower )
		shutil.copy(self.srcManagePy, self.distManagePy)
		shutil.copy(self.srcGuardedJSON, self.distGuardedJSON)


	def UpdateFiles(self):
		print("Note. Updating Project files with new project name.")

		# -----------Update manage.py
		with open(self.distManagePy, 'r') as manageReadFile:
			manageContent = manageReadFile.read()

		compiled = re.compile(re.escape(self.inputProjectName + ".settings"), re.IGNORECASE)
		resource = compiled.sub(self.inputNewProjectName + ".settings", manageContent)
		manageContentNew = str(resource)

		with open(self.distManagePy, 'w') as manageWriteFile:
			manageWriteFile.write(manageContentNew)


		# --------Update the new project settings.py
		with open(self.distSettingsPy, 'r') as settingsReadFile:
			settingsContent = settingsReadFile.read()

		compiled = re.compile(re.escape(self.inputProjectName + "."), re.IGNORECASE)
		resource = compiled.sub(self.inputNewProjectName + ".", settingsContent)
		settingsContentNew = str(resource)

		with open(self.distSettingsPy, 'w') as settingsWriteFile:
			settingsWriteFile.write(settingsContentNew)


		# -------Update the new project asgi.py
		with open(self.distAsgiPy, 'r') as asgiReadFile:
			asgiContent = asgiReadFile.read()

		compiled = re.compile(re.escape(self.inputProjectName + "."), re.IGNORECASE)
		resource = compiled.sub(self.inputNewProjectName + ".", asgiContent)
		asgiContentNew = str(resource)

		with open(self.distAsgiPy, 'w') as asgiWriteFile:
			asgiWriteFile.write(asgiContentNew)


		# -------Update the new project wsgi.py
		with open(self.distWsgiPy, 'r') as wsgiReadFile:
			wsgiContent = wsgiReadFile.read()

		compiled = re.compile(re.escape(self.inputProjectName + "."), re.IGNORECASE)
		resource = compiled.sub(self.inputNewProjectName + ".", wsgiContent)
		wsgiContentNew = str(resource)

		with open(self.distWsgiPy, 'w') as wsgiWriteFile:
			wsgiWriteFile.write(wsgiContentNew)


	def WriteZipFile(self):

		print("Note. Writing Zip File For New Project.")

		self.ProjectZip = zipfile.ZipFile(self.ZipFileName, 'w')
	
		self.ProjectZip.write(self.distManagePy, arcname = "manage.py")
		self.ProjectZip.write(self.distGuardedJSON, arcname = "guardedsettings.json")

		distInit		= os.path.join(self.distProjectFolderLower, "__init__.py")
		archiveInit	= os.path.join(self.inputNewProjectName,"__init__.py")
		self.ProjectZip.write(distInit, arcname = archiveInit)

		distAsgi		= os.path.join(self.distProjectFolderLower, "asgi.py")
		archiveAsgi	= os.path.join(self.inputNewProjectName,"asgi.py")
		self.ProjectZip.write(distAsgi, arcname = archiveAsgi)

		distSettings	= os.path.join(self.distProjectFolderLower, "settings.py")
		archiveSettings= os.path.join(self.inputNewProjectName,"settings.py")
		self.ProjectZip.write(distSettings, arcname = archiveSettings)

		distUrls		= os.path.join(self.distProjectFolderLower, "urls.py")
		archiveUrls	= os.path.join(self.inputNewProjectName,"urls.py")
		self.ProjectZip.write(distUrls, arcname = archiveUrls)

		distWsgi		= os.path.join(self.distProjectFolderLower, "wsgi.py")
		archiveWsgi	= os.path.join(self.inputNewProjectName,"wsgi.py")
		self.ProjectZip.write(distWsgi, arcname = archiveWsgi)

		
def main():
	builder = ProjectBuilder()	

if __name__ == "__main__":		
	main()

