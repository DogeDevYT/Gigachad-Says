from discord_webhook import DiscordWebhook, DiscordEmbed

webhook_url = 'https://discord.com/api/webhooks/1023004338571972638/NJGGCGIOksxmDVEWWk5Z5LqTGhwOXnZ9izdNjtTncq3sm_4dz0BJIZq2XrszbeY9gXct'

webhook = DiscordWebhook(url=webhook_url)

# create embed object for webhook
embed = DiscordEmbed(title='Gigachad Says', description='What do he say doe?', color='03b2f8')

# set author
embed.set_author(name='Raghav', url='https://github.com/DogeDevYT', icon_url='https://avatars.githubusercontent.com/u/52612977?v=4')

# set image
embed.set_image(url='https://melmagazine.com/wp-content/uploads/2021/01/66f-1.jpg')

# set thumbnail
embed.set_thumbnail(url='https://melmagazine.com/wp-content/uploads/2021/01/66f-1.jpg')

# set footer
embed.set_footer(text='So true Gigachad', icon_url='https://melmagazine.com/wp-content/uploads/2021/01/66f-1.jpg')

# set timestamp (default is now)
embed.set_timestamp()

# add fields to embed
embed.add_embed_field(name='Header', value='Swagulous 2')
embed.add_embed_field(name='Header again', value='Rungatunga')

# add embed object to webhook
webhook.add_embed(embed)

response = webhook.execute()

