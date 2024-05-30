import configparser


config = configparser.ConfigParser()

config.sections()
config.read('secret.ini', encoding='utf-8')


database_user = config['Database']['user']
database_password = config['Database']['password']
database_name = config['Database']['database']
database_host = config['Database']['host']

oauth20_url = config['Oauth20_URL']['Oauth20_url']
redirect_url = config['Oauth20_URL']['redirect_url']
oauth20_valid = config['Oauth20_URL']['Oauth20_valid']
twitch_api = config['Oauth20_URL']['Twitch_API']
client_id = config['Oauth20_URL']['client_id']
client_secret = config['Oauth20_URL']['client_secret']


get_broadcaster_id = config['Redemptions']['get_broadcaster_id']
get_custom_reward = config['Redemptions']['get_custom_rewards']
rewards_redemption = config['Redemptions']['rewards_redemption']
create_custom_reward = config['Redemptions']['create_custom_rewards']
delete_reward = config['Redemptions']['delete_rewards']
update_reward = config['Redemptions']['update_Reward']
get_VIPs = config['Redemptions']['get_VIPs']
get_MODs = config['Redemptions']['get_MODs']

secret_key = config['Flask']['secret']
