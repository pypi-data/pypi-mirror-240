# coding: UTF-8
import sys
bstack11111_opy_ = sys.version_info [0] == 2
bstack1lllll1l_opy_ = 2048
bstack1ll_opy_ = 7
def bstack111ll_opy_ (bstack111ll1l_opy_):
    global bstack1l1l11l_opy_
    bstack11ll1l_opy_ = ord (bstack111ll1l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack111ll1l_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack1ll11l1_opy_)
    bstack1l1l1ll_opy_ = bstack1ll11l1_opy_ [:bstack1lllll1_opy_] + bstack1ll11l1_opy_ [bstack1lllll1_opy_:]
    if bstack11111_opy_:
        bstack11llll_opy_ = unicode () .join ([unichr (ord (char) - bstack1lllll1l_opy_ - (bstack111llll_opy_ + bstack11ll1l_opy_) % bstack1ll_opy_) for bstack111llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack11llll_opy_ = str () .join ([chr (ord (char) - bstack1lllll1l_opy_ - (bstack111llll_opy_ + bstack11ll1l_opy_) % bstack1ll_opy_) for bstack111llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack11llll_opy_)
import threading
bstack11ll11l1ll_opy_ = 1000
bstack11ll11ll11_opy_ = 5
bstack11ll11l1l1_opy_ = 30
bstack11ll11lll1_opy_ = 2
class bstack11ll111ll1_opy_:
    def __init__(self, handler, bstack11ll11ll1l_opy_=bstack11ll11l1ll_opy_, bstack11ll11l11l_opy_=bstack11ll11ll11_opy_):
        self.queue = []
        self.handler = handler
        self.bstack11ll11ll1l_opy_ = bstack11ll11ll1l_opy_
        self.bstack11ll11l11l_opy_ = bstack11ll11l11l_opy_
        self.lock = threading.Lock()
        self.timer = None
    def start(self):
        if not self.timer:
            self.bstack11ll111l1l_opy_()
    def bstack11ll111l1l_opy_(self):
        self.timer = threading.Timer(self.bstack11ll11l11l_opy_, self.bstack11ll11llll_opy_)
        self.timer.start()
    def bstack11ll111l11_opy_(self):
        self.timer.cancel()
    def bstack11ll11l111_opy_(self):
        self.bstack11ll111l11_opy_()
        self.bstack11ll111l1l_opy_()
    def add(self, event):
        with self.lock:
            self.queue.append(event)
            if len(self.queue) >= self.bstack11ll11ll1l_opy_:
                t = threading.Thread(target=self.bstack11ll11llll_opy_)
                t.start()
                self.bstack11ll11l111_opy_()
    def bstack11ll11llll_opy_(self):
        if len(self.queue) <= 0:
            return
        data = self.queue[:self.bstack11ll11ll1l_opy_]
        del self.queue[:self.bstack11ll11ll1l_opy_]
        self.handler(data)
    def shutdown(self):
        self.bstack11ll111l11_opy_()
        while len(self.queue) > 0:
            self.bstack11ll11llll_opy_()