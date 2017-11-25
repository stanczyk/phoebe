#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**parser.py**
python implementation of vcf_parser

in the module:

* *class* **Parser**

	Copyright 2017 Jaroslaw Stanczyk, e-mail: jaroslaw.stanczyk@upwr.edu.pl
"""
# pylint: disable=missing-docstring, relative-import, bad-continuation

import sys
import docopt  # https://pypi.python.org/pypi/docopt/
import vcf  # http://pyvcf.rtfd.org/
from err import Err
from info import Info


class Parser(object):
	"""Parser class"""
	def __init__(self):
		self.args = None
		self.file_handler = None
		self.file_name = None
		self.reader = None
		self.prn = False

	def _prn(self):
		if not self.prn:
			self.prn = True
			print '---'

	def set_up_argv(self):
		# parse command line options
		self.args = docopt.docopt(Info.DOC, version=self.get_version())
		# print self.args

		if self.args['-v']:
			print self.get_version()
			exit(Err.NOOP)

		if self.args['-V'] or self.args['--verbose']:
			self._prn()
			print Info.VER

		if self.args['-s'] or self.args['--stdin']:
			self.file_name = 'stdin'
			self.file_handler = sys.stdin
		else:
			self.file_name = self.args['<vcf_file>']

	def set_up_file_handler(self):
		if not self.file_name:
			return Err.ERR_NO_INPUT_FILE
		if self.file_handler:  # it means you read from stdin
			return Err.NOOP
		# you read from ordinary file
		return self.get_file_handler()

	# def set_up_web(self, file_name, data):
	# 	# prepare file to read by vcf
	# 	self.file_name = '/tmp/' + file_name
	# 	ans = self.write_file(data)
	# 	if ans != Err.NOOP:
	# 		return ans, None
	# 	return self.get_file_handler()

	def parse(self):
		"""
		main function of vcf_parser.

		:return: tuple (status, error_line) where
			status 0 if everything was OK, != 0 otherwise, than
			error_line points line in VCF file where error appeared
		"""
		# try:
		self.reader = vcf.Reader(self.file_handler)
		try:
			self.reader.metadata['fileformat']
		except KeyError:
			return Err.ERR_VCF_READER
		return Err.NOOP

	# def write_file(self, data=None):
	# 	try:
	# 		f = open(self.file_name, 'w')
	# 	except (OSError, IOError):
	# 		return Err.ERR_NO_PERMISSION
	# 	try:
	# 		f.write(data)
	# 		f.close()
	# 	except (OSError, IOError):
	# 		os.remove(self.file_name)
	# 		return Err.ERR_IO
	# 	return Err.NOOP

	# def tear_down_web(self):
	# 	self.file_handler.close()
	# 	os.remove(self.file_name)

	# def main_web(self, file_name=None, data=None):
	# 	"""interface from web"""
	# 	err, self.file_handler = self.set_up_web(file_name, data)
	# 	if not err:
	# 		# parse file
	# 		err, self.line = self.parse()
	# 	# clean up
	# 	self.tear_down_web()
	# 	return err, self.line

	def main_cli(self):
		self.set_up_argv()
		err = self.set_up_file_handler()
		if not err:
			# parse file
			err = self.parse()

			if not err:
				if self.args['-i'] or self.args['--info']:
					self._prn()
					Info().show(self.get_info(), default_flow_style=False)

				if self.args['-m'] or self.args['--metadata']:
					self._prn()
					Info().show(self.get_metadata(), default_flow_style=False)

				if self.args['-b'] or self.args['--body']:
					self._prn()
					Info().show(self.get_body(), default_flow_style=False)

			# clean up
			self.tear_down_cli()
		return err

	def tear_down_cli(self):
		if self.file_name:
			if self.file_handler is not sys.stdin:
				self.file_handler.close()

	def get_body(self):
		for record in self.reader:
			print record.CHROM,
			print record.POS,
			print record.ID,
			print record.REF,
			print record.ALT,
			print record.QUAL,
			print record.FILTER,
			print record.INFO,
			print record.FORMAT
			# print record.samples,
			# print record.genotype

	@staticmethod
	def get_err_description(error_code):
		return Err().value_to_name(error_code)

	def get_file_handler(self):
		try:
			self.file_handler = open(self.file_name, 'r')
		except IOError as ioe:
			if ioe.errno == 2:
				return Err.ERR_NO_FILE
			if ioe.errno == 13:
				return Err.ERR_NO_PERMISSION
			return Err.ERR_IO
		return Err.NOOP

	def get_info(self):
		# zwraca nazwę wczytanego pliku, jego wersję, ilość osobników, ilośc snipów
		i = 0
		for _ in self.reader:
			i += 1
		return {
			'file_name': self.file_name,
			'file_format': self.reader.metadata['fileformat'],
			'samples': self.reader.samples,
			'rec_amount': i,
		}

	def get_metadata(self):
		print self.reader.metadata
		print self.reader.infos
		print self.reader.filters
		print self.reader.formats
		print self.reader.samples

	# 	for k in self.reader.infos:
	# 		print '\t', self.reader.infos[k]
	# 		print '\t', self.reader.infos[k].id, self.reader.infos[k].desc
	# 		return self.reader.infos

	# def show_metadata(self):
	# 	print 'meta-information:'
	# 	for k, v in self.reader.metadata.items():
	# 		print '\t%s=%s' % (str(k), str(v))

	# def show_infos(self):
	# 	print 'meta info:'
	# 	for k in self.reader.infos:
	# 		# print '\t', self.reader.infos[k]
	# 		print '\t', self.reader.infos[k].id, self.reader.infos[k].desc

	@staticmethod
	def get_version():
		return '---\n' + \
			Info().VER + '\n' + \
			'\n' + \
			Info().WRITTEN

	def epilog(self, err):
		if self.args['-V'] or self.args['--verbose']:
			desc = self.get_err_description(err)
			ans = {
				'parsing status': [
					err,
					desc,
				]
			}
			Info().show(ans, default_flow_style=False)

	def main(self):
		err = self.main_cli()
		self.epilog(err)
		sys.exit(err)


if __name__ == '__main__':
	PAR = Parser()
	PAR.main()

# eof.
