from django.shortcuts import render
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from time import sleep
import requests

#сгенерированные значения для VKapi
token = 'e0d5603ae0d5603ae0d5603a19e0a69bfeee0d5e0d5603abfb1d05071d7f639945289e0'
ver = '5.124'

def test(request):
	friends = []
	if request.user.is_authenticated:
		username = request.user.username
		response = requests.get('https://api.vk.com/method/users.get',
		params={
		'access_token': token,
		'v': ver,
		'user_ids': username
		})
		#получаем ID пользователя
		user_id = response.json()['response'][0]['id']

		response = requests.get('https://api.vk.com/method/friends.get',
		params={
		'access_token': token,
		'v': ver,
		'user_id': user_id,
		'fields': 'photo_100,first_name,last_name',
		'count': 5,
		}
		)
		data = response.json()
		#получаем друзей пользователя
		for friend in data['response']['items']:
			frined = {'first_name': friend['first_name'], 'last_name': friend['last_name'],'photo':friend['photo_100']}
			friends.append(friend)
	return render(request, 'auth/index.html', context={'friends':friends})
