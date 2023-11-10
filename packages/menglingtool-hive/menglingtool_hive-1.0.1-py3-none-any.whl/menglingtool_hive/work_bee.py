from threading import Thread
import time
import traceback
import requests


def _retryFunc_args(name='', ci=3, sleeptime=5, sleepfunc=time.sleep, iftz=True):
    def retryFunc(func):
        def temp(*values, **kwargs):
            e = None
            for i in range(1, ci + 1):
                try:
                    return func(*values, **kwargs)
                except:
                    e = traceback.format_exc()
                    if iftz:
                        print(e)
                        print(name, '失败，正在重试...第', i, '次，休息', sleeptime, '秒')
                    if sleeptime > 0: sleepfunc(sleeptime)
            print('错误参数组：', values)
            raise ValueError(f'{e}\n重试全部失败，抛出错误')

        return temp

    return retryFunc


class Bee:
    def __init__(self, fc_ip: str, fc_port: int):
        # 生成随机名称
        self.gf_name = f'{time.time()}'.replace('.', '')
        self.fc_url0 = f'http://{fc_ip}:{fc_port}'
        self.makefunc = None
        # 记录任务
        self.datas = []
        self.fh_config = {}
        self.sleep_time = 5

    # 登记
    def register(self):
        try:
            r = requests.get(self.fc_url0 + f'/gf/register?gf_name={self.gf_name}')
            dt = r.json()
            if len(dt) == 0:
                return None
            else:
                return dt['makefunc_txt'], dt.get('datas', []), dt.get('fh_config', {})
        except:
            traceback.print_exc()
            assert False, f'错误返回  {r.text}'

    # 提交完成
    def complete(self):
        # 提交完成
        requests.get(self.fc_url0 + f'/gf/complete?gf_name={self.gf_name}')

    # 监听链接
    def linsten(self):
        while True:
            # 请求
            try:
                result = self.register()
            except:
                traceback.print_exc()
                print('监听出错!')
                result = None
            if result is not None:
                func, self.datas, self.fh_config = result
                exec(func + '\nself.makefunc=makefunc')
            time.sleep(self.sleep_time)

    @_retryFunc_args()
    def cellRun(self):
        print(f'开始任务...数量:{len(self.datas)}')
        try:
            self.makefunc(self.datas, **self.fh_config)
            self.datas = list()
        except:
            traceback.print_exc()
            print('[失败]')

    def run(self):
        # 开始监听
        print('开始监听:', self.fc_url0)
        Thread(target=self.linsten).start()
        while True:
            if len(self.datas) > 0:
                self.cellRun()
                self.complete()
            time.sleep(self.sleep_time)

# if __name__ == '__main__':
#     import config
#
#     gbee = Bee(config.FC_CONNECT['fc_ip'], config.FC_CONNECT['fc_port'])
#     gbee.run()
