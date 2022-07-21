# TG机器人的令牌，tg找@BotFather创建机器人即可获取
from os import getenv

TOKEN = getenv('TOKEN', '')
# pikpak账号，可以为手机号、邮箱，支持任意多账号
USER = [getenv('USER', '')]
# 账号对应的密码，注意与账号顺序对应！！！
PASSWORD = [getenv('PASSWORD', '')]
# 以下分别为aria2 RPC的协议（http/https）、host、端口、密钥
ARIA2_HTTPS = getenv('ARIA2_HTTPS', False)
ARIA2_HOST = getenv('ARIA2_HOST', 'localhost')
ARIA2_PORT = getenv('ARIA2_PORT', 6800)
ARIA2_SECRET = getenv('ARIA2_SECRET', '')
# aria2下载根目录
ARIA2_DOWNLOAD_PATH = getenv('ARIA2_DOWNLOAD_PATH', '/tmp/aria2')
# 可以自定义TG API，也可以保持默认
TG_API_URL = getenv('TG_API_URL', 'https://api.telegram.org/')
