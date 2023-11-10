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
class bstack11ll11111l_opy_:
    def __init__(self, handler):
        self._11ll1111ll_opy_ = None
        self.handler = handler
        self._11ll1111l1_opy_ = self.bstack11l1lllll1_opy_()
        self.patch()
    def patch(self):
        self._11ll1111ll_opy_ = self._11ll1111l1_opy_.execute
        self._11ll1111l1_opy_.execute = self.bstack11l1llllll_opy_()
    def bstack11l1llllll_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            response = self._11ll1111ll_opy_(this, driver_command, *args, **kwargs)
            self.handler(driver_command, response)
            return response
        return execute
    def reset(self):
        self._11ll1111l1_opy_.execute = self._11ll1111ll_opy_
    @staticmethod
    def bstack11l1lllll1_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver