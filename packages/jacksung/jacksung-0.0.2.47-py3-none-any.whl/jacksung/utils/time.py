import time
from datetime import datetime
import pytz
from jacksung.utils.log import oprint


class RemainTime:
    def __init__(self, epoch):
        self.start_time = time.time()
        self.epoch = epoch
        self.now_epoch = 0

    def update(self, log_temp='Rem Epochs:{}, Fin in {}', print_log=True, update_step=1):
        self.now_epoch += update_step
        epoch_time = time.time() - self.start_time
        epoch_remaining = self.epoch - self.now_epoch
        time_remaining = epoch_time * epoch_remaining
        pytz.timezone('Asia/Shanghai')  # 东八区
        t = datetime.fromtimestamp(int(time.time()) + time_remaining,
                                   pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
        log = log_temp.format(epoch_remaining, t)
        if print_log:
            oprint(log)
        self.start_time = time.time()
        return epoch_remaining, t
