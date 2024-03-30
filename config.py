import configparser


config = configparser.ConfigParser()

config.sections()
config.read('secret.ini', encoding='utf-8')


database_user = config['Database']['user']
database_password = config['Database']['password']
database_name = config['Database']['database']

oauth20_url = config['Oauth20_URL']['Oauth20_URL']
redirect_uri = config['Oauth20_URL']['redirect_uri']
oauth20_valid = config['Oauth20_URL']['Oauth20_valid']
twitch_api = config['Oauth20_URL']['Twitch_API']
database_client_id = config['Oauth20_URL']['client_id']
database_client_secret = config['Oauth20_URL']['client_secret']


get_broadcaster_id = config['Redemptions']['get_broadcaster_id']
get_custom_rewards = config['Redemptions']['get_custom_rewards']
rewards_redemption = config['Redemptions']['rewards_redemption']
create_custom_rewards = config['Redemptions']['create_custom_rewards']
delete_rewards = config['Redemptions']['delete_rewards']
update_reward = config['Redemptions']['update_Reward']

secret_key = config['Flask']['secret']

# 输出配置信息示例
print("Database User:", database_user)
print("Database Password:", database_password)
print("Database Name:", database_name)
print("Database Client ID:", database_client_id)
print("Database Client Secret:", database_client_secret)

print("OAuth 2.0 URL:", oauth20_url)
print("Redirect URI:", redirect_uri)
print("OAuth 2.0 Validation URL:", oauth20_valid)
print("Twitch API URL:", twitch_api)

print("Get Broadcaster ID Endpoint:", get_broadcaster_id)
print("Get Custom Rewards Endpoint:", get_custom_rewards)
print("Rewards Redemption Endpoint:", rewards_redemption)
print("Create Custom Rewards Endpoint:", create_custom_rewards)
print("Delete Rewards Endpoint:", delete_rewards)
print("Update Reward Endpoint:", update_reward)