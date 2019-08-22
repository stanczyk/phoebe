# -*- coding: utf-8 -*-
"""
yml_data

Copyright (c) 2017-2019 Jarosław Stańczyk <j.stanczyk@hotmail.com>
"""
# pylint: disable=bad-continuation

#
#            -------     -------     -------
# u_1 >--->--| M_1 |-->--| M_2 |-->--| M_3 |-->-- y_1
#            -------     -------     -------
#

DANE = {
	# input definition
	'input':
		[
			{
				# input u_1
				'u_1':
					{
						'op-time': 'd_0',
						# the time after which the item is delivered to the input, default: 0 (available immediately)
						# there is no need to define this value if it is equal to the default
						'connect': 'M_1',
						# to which system item (processing unit or output) the input is connected
						'tr-time': 't_{0,1}'
						# transport time from input to system item
					}
			}
		],
	# prod-unit definition
	'prod-unit':
		[
			{
				# production unit M_1
				'M_1':
					{
						'op-time': 'd_1',
						# operation time on M_1
						'connect': 'M_2',
						# to which system item (processing unit or output) this processing unit is connected
						'tr-time': 't_{1,2}'
						# transport time from input to system item
					}
			},
			{'M_2': {'op-time': 'd_2', 'connect': 'M_3', 'tr-time': 't_{2,3}'}},
			{'M_3': {'op-time': 'd_3', 'connect': 'y_1', 'tr-time': 't_{3,4}'}}
		],
	# output definition
	'output': [{'y_1': {}}],
	# times def.
	'values': {'d_0': 1, 'd_1': 3, 'd_2': 2, 'd_3': 6, 't_{0,1}': 1, 't_{1,2}': 2, 't_{2,3}': 0, 't_{3,4}': 1}
}

# end.
