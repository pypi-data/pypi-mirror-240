from setuptools import setup

import os
if os.path.isfile('./http_magic/readme.md'):
	with open('./http_magic/readme.md') as f:
		long_description = f.read()
else:
	long_description = ''
setup(name='http_magic',author='German Espinosa',author_email='germanespinosa@gmail.com',long_description=long_description,long_description_content_type='text/markdown',packages=['http_magic'],install_requires=['json-cpp'],license='MIT',package_data={'http_magic':['files/*', 'files/html/*']},version='0.0.8',zip_safe=False)
