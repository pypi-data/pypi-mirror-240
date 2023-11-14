from setuptools import setup 

setup( 
	name='mjrpc', 
	version='0.0.0', 
	description='A MuJoCo gRPC implementation for fast simulations and communication.',
	long_description='A MuJoCo gRPC implementation for fast simulations and communication.',
	author='Lucas Maggi', 
	author_email='lucas.maggi@usp.br', 
	packages=['mjrpc'], 
	install_requires=[
        'grpcio',
	], 
) 
