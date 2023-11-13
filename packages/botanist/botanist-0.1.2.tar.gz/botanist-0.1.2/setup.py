
#
#	https://setuptools.pypa.io/en/latest/userguide/quickstart.html
#

from setuptools import setup, find_packages

name = 'botanist'

description = ''
try:
	with open ('botanist.html') as f:
		description = f.read ()

except Exception as E:
	pass;

setup (
    name = name,
    version = '0.1.2',
    install_requires = [],	
	package_dir = { name: 'fields/gardens/' + name },
	
	license = "pscl",
	long_description = description,
	long_description_content_type = "text/plain"
	
	
	#package_data = {
	#	NAME: [ 'DATA/**/*' ]
	#}
)