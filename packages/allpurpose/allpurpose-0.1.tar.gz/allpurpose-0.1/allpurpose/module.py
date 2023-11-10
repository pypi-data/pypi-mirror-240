import importlib.util
import sys
import os

class Module:
	m = None
	@staticmethod
	def imp(path):
		module_name = os.path.splitext(path)[0].split('/')[-1]
		spec = importlib.util.spec_from_file_location(module_name, path)
		module = importlib.util.module_from_spec(spec)
		sys.modules[module_name] = module
		spec.loader.exec_module(module)
		Module.m = module
		return Module.m

	@staticmethod
	def imp_object(path, object_name):
		return getattr(Module.imp(path), object_name)

	@staticmethod
	def imp_class(path):
		module_name = path.split('/')[-1].split('.')[0]
		if not path.endswith('.py'):
			path += '.py'
		class_name = ''.join(x.capitalize() for x in module_name.lower().split('_'))
		return Module.imp_object(path, class_name)
