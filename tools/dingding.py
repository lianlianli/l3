import os
import requests


def send_dingding(message):
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=0eab762f24fd009918f9a40da93861af2c71f4d116da056c9f79827a4df5107c'
    proxies = {
        'http': os.getenv('HTTP_PROXY', 'http://proxy.i.brainpp.cn:3128'),
        'https': os.getenv('HTTPS_PROXY', 'http://proxy.i.brainpp.cn:3128'),
    }
    message='path:'+os.getcwd()+'\n'+'\n'.join(message)+'\n'
    data = {
        'msgtype': 'text',
        'text': {
            'content': message,
        },
        'at': {
            'isAtAll': True
         }
     }
    resp = requests.post(webhook, json=data, proxies=proxies)
    try:
        resp.raise_for_status()
    except Exception as e:
        print('Send dingding failed ({}): {}'.format(e, message))


if __name__ == '__main__':
    msg = ['result:%s'%('lalalalala'),'mood:great','where:beijing']
    send_dingding(msg)
