import discord
import requests
import json
import asyncio
#create Client class Object
client = discord.Client()

def get_question():
	question = ''
	id = 1
	correct_answer = 0
	response = requests.get("https://127.0.0.1/api/random")
	json_data = json.loads(response.text)
	question += "Question: \n"
	question += json_data[0]['title'] + "\n"
	for answer in json_data[0]['answer']:
		question += str(id)+ ". " + answer['answer']+ "\n"
		if answer['is_correct']:
			correct_answer = id

		id += 1

	return(question,correct_answer)
			



@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('$hello'):
		await message.channel.send('Hello, I am a quiz-bot')

	if message.content.startswith('$question'):
		qs,answer = get_question()
		await message.channel.send(qs)

		def check(m):
			return m.author == message.author and m.content.isdigit()

		try:
			guess = await client.wait_for('message',check=check,timeout=5.0)
		except asyncio.TimeoutError:
			return await message.channel.send('Sorry, you took too long')
		if int(guess.content) == answer:
			return await message.channel.send("Correct")
		else:
			return await message.channel.send("Incorrect")

client.run('discord-bot-token')
