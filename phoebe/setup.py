#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	**setup.py**
	installer, uninstaller, tarball preparer and test runner for phoebe

	Copyright 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl

	for more details regarding setup and setuptools let's have a look at:
		https://setuptools.readthedocs.io/en/latest/setuptools.html
"""
# pylint: disable=no-name-in-module, import-error, bad-continuation
import errno
import os
import sys
from subprocess import call, PIPE
from distutils.command.build_py import build_py
from setuptools import setup
from setuptools.command.test import test as TestCommand
from src.inf import Inf


class PyTest(TestCommand):
	"""
	PyTest class to run my unit tests
	"""
	# pylint: disable=attribute-defined-outside-init
	# user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

	def initialize_options(self):
		TestCommand.initialize_options(self)
		self.pytest_args = ['--verbose']

	def run(self):
		# import shlex
		import pytest
		# err = pytest.main(shlex.split(self.pytest_args))
		err = pytest.main(self.pytest_args)
		sys.exit(err)


class Uninstall(build_py):
	"""
	Uninstall class to uninstall the package

	it can be done by:
		python setup.py install --record files.txt
		cat files.txt | xargs rm -rf
	"""
	# pylint: disable=missing-docstring, too-few-public-methods, no-self-use

	def run(self):
		tmp_file = '/tmp/phoebe_install_list'
		call(['python', 'setup.py', 'install', '--record', tmp_file], stdout=PIPE)

		if os.path.exists(tmp_file):
			with open(tmp_file, 'r') as open_file:
				record_list = open_file.read()

			record_list = record_list.split('\n')
			for recorded_line in record_list:
				# if len(recorded_line) > 0:
				if recorded_line:
					print 'removing: %s' % recorded_line
					try:
						os.unlink(recorded_line)
					except OSError as error:
						if error.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
							raise
			os.unlink(tmp_file)
		else:
			print >> sys.stderr, 'error: nothing to uninstall?'


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
		url=Inf.URL,
		license=Inf.LICENSE,
		description=Inf.DESC,
		# long_description
		# platforms
		classifiers=[
			# look at https://pypi.python.org/pypi?%3Aaction=list_classifiers
			'Development Status :: 3 - Alpha',
			'Environment :: Console'
		],
		# keywords
		# provides
		requires=[
			'docopt',  # >=0.6.2
		],
		install_requires=[
			'docopt>=0.6.2',
		],
		packages=['phoebe'],
		scripts=['bin/phoebe'],
		# entry_points={'console_scripts': ['vcf_parser=vcm.command_line:main'], },
		# dependency_links=['http://github.com/user/repo/tarball/master#egg=package-1.0'],
		setup_requires=['pytest-runner'],
		tests_require=['pytest'],
		cmdclass=dict(
			test=PyTest,
			uninstall=Uninstall,
		),
		zip_safe=True
	)


if __name__ == '__main__':
	run_setup()

# eof.
