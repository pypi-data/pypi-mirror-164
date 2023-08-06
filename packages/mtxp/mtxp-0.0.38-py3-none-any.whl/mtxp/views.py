from . import mtxp_blue

@mtxp_blue.route('/')
def home():
    return 'mtxphome'

@mtxp_blue.route('/deluser')
def deluser():
    return 'deluser'