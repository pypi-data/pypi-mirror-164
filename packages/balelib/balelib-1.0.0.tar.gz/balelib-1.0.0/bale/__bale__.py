from .methods import (Methods,)


class BaleClient(object,):
	def __init__(self, token,):
		self.token = token
		self.request = Methods(token,)

	def sendMessage(self, chat_id, text,):
		return self.request.methodMaking('sendMessage',{
			'chat_id': int(chat_id),
			'text': text,
		},)

	def getUpdates(self,):
		return self.request.methodMaking('getUpdates', {'offset': 0, 'limit': 0},)

	def getMe(self,):
		result = self.request.methodMaking('getMe', {})
		if result.get('ok'):
			return result.get('result')
		else:
			return None

	def editMessage(self, chat_id, new_text, message_id,):
		return self.request.methodMaking('editMessageText', {
			'chat_id': chat_id,
			'text': new_text,
			'message_id': int(message_id)
		,},)

	def deleteMessage(self, chat_id, message_id,):
		return self.request.methodMaking('deleteMessage', {'chat_id': chat_id, 'message_id': str(message_id,),},)

	def sendPhoto(self, chat_id, photo, caption = None, reply_to_message_id = None,):
		result = self.request.methodMaking('sendPhoto',
		{"photo": photo, "chat_id": chat_id, "caption": caption},)
		if result.get('ok'):
			return result.get('result')
		return None