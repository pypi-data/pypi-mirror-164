from .methods import (Methods,)


class BaleClient(object,):
	def __init__(self, token,):
		self.token = token
		self.request = Methods(token,)

	def sendMessage(self, chat_id, text, reply_to_message_id = None,):
		return self.request.methodMaking('sendMessage',{
			'chat_id': int(chat_id),
			'text': text,
			'reply_to_message_id': reply_to_message_id,
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
		result = self.request.methodMaking('sendPhoto', {
		'photo': photo,
		'chat_id': chat_id,
		'caption': caption,
		'reply_to_message_id': reply_to_message_id,
		},)
		if result.get('ok'):
			return result.get('result')
		return None

	def sendAudio(self, chat_id, audio, caption = None, duration = None, title = None, reply_to_message_id = None,):
		result = self.request.methodMaking('sendAudio', {
		'audio': audio,
		'chat_id': chat_id,
		'caption': caption,
		'reply_to_message_id': reply_to_message_id,
		'duration': duration,
		'title': title,
		},)
		if result.get('ok'):
			return result.get('result')
		return None

	def sendDocument(self, chat_id, document, caption = None, reply_to_message_id = None):
		result = self.request.methodMaking('sendDocument', {
		'docuement': document,
		'chat_id': chat_id,
		'caption': caption,
		'reply_to_message_id': reply_to_message_id,
		},)
		if result.get('ok'):
			return result.get('result')
		return None

	def sendVideo(self, chat_id, video, duration = None, width = None, height = None, caption = None, reply_to_message_id = None,):
		result = self.request.methodMaking('sendVideo', {
		'video': video,
		'chat_id': chat_id,
		'caption': caption,
		'reply_to_message_id': reply_to_message_id,
		'duration': duration,
		'width': width,
		'height': height,
		},)
		if result.get('ok'):
			return result.get('result')
		return None

	def sendVoice(self, chat_id, voice, caption = None, duration = None, reply_to_message_id = None):
		result = self.request.methodMaking('sendVoice', {
		'voice': voice,
		'chat_id': chat_id,
		'caption': caption,
		'reply_to_message_id': reply_to_message_id,
		'duration': duration,
		},)
		if result.get('ok'):
			return result.get('result')
		return None

	def sendLocation(self, chat_id, latitude, longitude, reply_to_message_id = None,):
		result = self.request.methodMaking('sendLocation', {
		'chat_id': chat_id,
		'latitude': latitude,
		'longitude': longitude,
		'reply_to_message_id': reply_to_message_id,
		},)
		if result.get('ok'):
			return result.get('result')
		return None

	def sendContact(self, chat_id, phone_number, first_name, last_name = None, reply_to_message_id = None,):
		result = self.request.methodMaking('sendContact', {
		'chat_id': chat_id,
		'phone_number': phone_number,
		'first_name': first_name,
		'last_name': last_name,
		'reply_to_message_id': reply_to_message_id,
		},)
		if result.get('ok'):
			return result.get('result')
		return None

	def getFile(self, file_id,):
		result = self.request.methodMaking('getFile', {
		'file_id': file_id,
		},)
		if result.get('ok'):
			return result.get('result')
		return None

	def getChats(self, chat_id,):
		result = self.request.methodMaking('getChats', {
		'chat_id': chat_id,
		},)
		if result.get('ok'):
			return result.get('result')
		return None

	def getChatAdministrators(self, chat_id,):
		result = self.request.methodMaking('getChatAdministrators', {
		'chat_id': chat_id,
		},)
		if result.get('ok'):
			return result.get('result')
		return None

	def getChatMembersCount(self, chat_id,):
		result = self.request.methodMaking('getChatMembersCount', {
		'chat_id': chat_id,
		},)
		if result.get('ok'):
			return result.get('result')
		return None

	def getChatMember(self, chat_id, user_id,):
		result = self.request.methodMaking('getChatMember', {
		'chat_id': chat_id,
		'user_id': user_id,
		},)
		if result.get('ok'):
			return result.get('result')
		return None