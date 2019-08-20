#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**setup.py**
installer, uninstaller, tarball preparer and test runner for phoebe

Copyright (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>

for more details regarding setup and setuptools let's have a look at:
	https://setuptools.readthedocs.io/en/latest/setuptools.html
"""
import errno
import os
import sys
from subprocess import call, PIPE
from distutils.command.build_py import build_py
from setuptools import setup
from setuptools.command.test import test as TestCommand
from phoebe.inf import Inf


class PyTest(TestCommand):
	"""
	PyTest class to run my unit tests
	"""
	def initialize_options(self):
		TestCommand.initialize_options(self)
		self.pytest_args = ['--verbose']

	def run(self):
		import pytest
		err = pytest.main(self.pytest_args)
		sys.exit(err)


class Uninstall(build_py):
	"""
	Uninstall class to uninstall the package

	it can be done by:
		python setup.py install --record files.txt
		cat files.txt | xargs rm -rf
	"""
	def run(self):
		tmp = '/tmp/phoebe_install_list'
		call(['python', 'setup.py', 'install', '--record', tmp], stdout=PIPE)

		if os.path.exists(tmp):
			with open(tmp, 'r') as open_file:
				record_list = open_file.read()

			record_list = record_list.split('\n')
			for recorded_line in record_list:
				if recorded_line:
					print('removing: %s' % recorded_line)
					try:
						os.unlink(recorded_line)
					except OSError as error:
						if error.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
							raise
			os.unlink(tmp)
		else:
			print('error: nothing to uninstall?', file=sys.stderr)


def run_setup():
	"""
	main setup function,
	for more details please have a look:
		'python setup.py --help'
	or
		'python setup.py --help-commands'
	"""
	setup(
		name=Inf.NAME,
		version=Inf.VERSION,
		author=Inf.AUTHOR,
		author_email=Inf.AUTHOR_EMAIL,
		# maintainer
		# maintainer-email
		contact=Inf.AUTHOR,
		contact_email=Inf.AUTHOR_EMAIL,
		description=Inf.DESC,
		# url=Inf.URL,
		license=Inf.LICENSE,
		# platforms
		# keywords
		# provides
		requires=['click', 'pyyaml'],
		install_requires=['click>=7.0', 'pyyaml>=5.1.2'],
		packages=['phoebe'],
		scripts=['bin/phoebe'],
		# entry_points={'console_scripts': ['vcf_parser=vcm.command_line:main'], },
		# dependency_links=['http://github.com/user/repo/tarball/master#egg=package-1.0'],
		setup_requires=['pytest-runner'],
		tests_require=['pytest'],
		cmdclass=dict(test=PyTest, uninstall=Uninstall)
		# zip_safe=True
	)


if __name__ == '__main__':
	run_setup()

# eof.
