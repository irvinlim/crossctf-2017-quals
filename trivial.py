# 2017.05.13 01:27:12 +08
# Embedded file name: trivial.py
import json
import sys

def check(flag):
    processed = flag[::-1]
    # processed = processed.decode('base64')
    final = json.loads(processed)
    if final['check_code'] != 'AK4782':
        return False
    if final['flag_content']['numbers'] * 2 != 18529313:
        return False
    if final['flag_content']['change'] != 'standardisation'[::2]:
        return False
    if final['flag_content']['settled'] != 'CrossCTF{%s_%d_%s}':
        return False
    temp = final['flag_content']
    return temp['settled'] % (temp['change'], temp['numbers'], final['check_code'])


def main():
    print 'CrossCTF{%s_%d_%s}' % ("sadriain", 9264656, 'AK4782')
    # if len(sys.argv) != 2:
    #     print 'No'
    #     sys.exit()
    # result = check(sys.argv[1])
    # if result:
    #     print result
    # else:
    #     print 'No'


if __name__ == '__main__':
    main()
# okay decompyling trivial.pyc_08771156e6a4ca18de03f186d68bc499 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.13 01:27:12 +08
