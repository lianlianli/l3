import urllib.parse
def get_path_type(path):
    info=urllib.parse.urlsplit(path)
    if info.scheme:
        return info.scheme
    else:
        return 'It is maybe a local path.'

if __name__ == '__main__':
    path='http://zhidao.baidu.com/question/1495707102172314019.html'
    result=get_path_type(path)
    print(result)
