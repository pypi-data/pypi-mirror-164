from requests import (request,)
from json import (dumps,)


class Methods(object,):
	def __init__(self, token,):
		self.token = token

	def methodMaking(self, method_name, method_data,):
		url = self.url(method_name,)
		return request(
				'POST',
				url = url,
				json = method_data,
			).json()

	def url(self, method_name,):
		return 'https://tapi.bale.ai/bot{}/{}/'.format(self.token, method_name,)