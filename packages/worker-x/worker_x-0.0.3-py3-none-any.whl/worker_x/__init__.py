
from threading import Thread,Lock
import time
import ctypes


class ThreadData(list):
    lock = Lock()
    _i = -1
    def next(self, loop=False):
        with self.lock:
            if loop:
                self._i = (self._i + 1) % self.__len__()
            else:
                self._i += 1
            __i = self._i
        if __i < self.__len__():
            return super().__getitem__(__i)
        
class Worker(Thread):
    def terminate(self):
        is_alive = False
        for _ in range(20):
            if self.is_alive():
                is_alive = True
                break
            time.sleep(0.1)
        if is_alive == False:
            return
        exc = ctypes.py_object(SystemExit)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
            ctypes.c_long(self.ident), exc)
        if res == 0:
            raise ValueError("nonexistent thread id")
        elif res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(self.ident, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")
        

class Pool():
    def __init__(self,thread:int,target,list_args:list,deamon=None) -> None:
        self.__inp = ThreadData(list_args)
        self.__thread_num = thread
        self.__thread = []
        self.target = target
        self.daemon = deamon

    
    def start(self):
        for _ in range(self.__thread_num):
            t = Worker(target=self.target,list_args=self.__inp,daemon=self.daemon)
            t.start()
            self.__thread.append(t)

    
    def terminate(self):
        for t in self.__thread:
            t.terminate()    
            

# def test(x,y):
#     return x*y

# X = [1,2,3,4,5,6,7,8,9,10]
# Y = [10,9,8,7,6,5,4,3,2,1]
# w = Pool(3,test,zip(X,Y),deamon=True)
# w.start()
# print(w.join())