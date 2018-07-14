import logging
import logging.handlers
import asyncio
import os
from hbmqtt.broker import Broker

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

hlogger = logging.getLogger('logh')
hlogger.setLevel(level=logging.INFO)
handler1 = logging.handlers.SysLogHandler(address =('172.27.20.2',9876))
handler1.setFormatter(logging.Formatter("%(message)s"))
hlogger.addHandler(handler1) 




handler = logging.StreamHandler()
formatter = "[%(asctime)s] :: %(levelname)s :: %(name)s :: %(message)s"
handler.setFormatter(logging.Formatter(formatter))
logger.addHandler(handler)
#logger = logging.getLogger('my_log')


#handler=logging.handlers.SysLogHandler(address=('172.27.20.2','6789'))
#logger.addHandler(handler)
#logger.debug('hello')
#logger.critical('this is critical')

config = {
    'listeners': {
        'default': {
            'type': 'tcp',
            'bind': '0.0.0.0:1883',
        },
        'ws-mqtt': {
            'bind': '0.0.0.0:8080',
            'type': 'ws',
            'max_connections': 10,
        },
	#'tcp-ssl':{
	#    'bind': '0.0.0.0:8883',
	#    'ssl' : 'on',
	#    'certfile' : '/home/p2p/Music/server.crt',
	#    'keyfile'  : '/home/p2p/Music/server.key',
        #    'cafile' : '/home/p2p/Music/ca.crt'
	#}
    },
    'sys_interval': 10,
    'auth': {
        'allow-anonymous': True,
        'password-file': os.path.join(os.path.dirname(os.path.realpath(__file__)), "passwd"),
        'plugins': [
            'auth_file', 'auth_anonymous'
	     #'auth_file'
        ]

    }
}

broker = Broker(config)


@asyncio.coroutine
def test_coro():
    yield from broker.start()
    #yield from asyncio.sleep(5)
    #yield from broker.shutdown()


if __name__ == '__main__':        
    #formatter ="[%(asctime)s] :: %(levelname)s :: %(name)s :: %(message)s"   
    
    
    asyncio.get_event_loop().run_until_complete(test_coro())
    asyncio.get_event_loop().run_forever()

