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
import multiprocessing
import os
from browserstack_sdk.bstack1ll1l11l1_opy_ import *
from bstack_utils.helper import bstack1ll1l1l1l_opy_
from bstack_utils.messages import bstack1ll11l1ll1_opy_
from bstack_utils.constants import bstack11lll1l11_opy_
class bstack1ll111111_opy_:
    def __init__(self, args, logger, bstack1ll1111ll1_opy_, bstack1ll1111lll_opy_):
        self.args = args
        self.logger = logger
        self.bstack1ll1111ll1_opy_ = bstack1ll1111ll1_opy_
        self.bstack1ll1111lll_opy_ = bstack1ll1111lll_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack1llll111l1_opy_ = []
        self.bstack1ll111ll1l_opy_ = None
        self.bstack1l111111l_opy_ = []
        self.bstack1ll111ll11_opy_ = self.bstack1l1l1111_opy_()
        self.bstack1111111l1_opy_ = -1
    def bstack1ll1l1ll11_opy_(self, bstack1ll111llll_opy_):
        self.parse_args()
        self.bstack1ll111l11l_opy_()
        self.bstack1ll1111l11_opy_(bstack1ll111llll_opy_)
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    def bstack1ll111l1l1_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1111111l1_opy_ = -1
        if bstack111ll_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭ಡ") in self.bstack1ll1111ll1_opy_:
            self.bstack1111111l1_opy_ = self.bstack1ll1111ll1_opy_[bstack111ll_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧಢ")]
        try:
            bstack1ll111l111_opy_ = [bstack111ll_opy_ (u"ࠨ࠯࠰ࡨࡷ࡯ࡶࡦࡴࠪಣ"), bstack111ll_opy_ (u"ࠩ࠰࠱ࡵࡲࡵࡨ࡫ࡱࡷࠬತ"), bstack111ll_opy_ (u"ࠪ࠱ࡵ࠭ಥ")]
            if self.bstack1111111l1_opy_ >= 0:
                bstack1ll111l111_opy_.extend([bstack111ll_opy_ (u"ࠫ࠲࠳࡮ࡶ࡯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬದ"), bstack111ll_opy_ (u"ࠬ࠳࡮ࠨಧ")])
            for arg in bstack1ll111l111_opy_:
                self.bstack1ll111l1l1_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack1ll111l11l_opy_(self):
        bstack1ll111ll1l_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack1ll111ll1l_opy_ = bstack1ll111ll1l_opy_
        return bstack1ll111ll1l_opy_
    def bstack1ll1l1ll1_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            import importlib
            bstack1ll1111l1l_opy_ = importlib.find_loader(bstack111ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠨನ"))
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack1ll11l1ll1_opy_)
    def bstack1ll1111l11_opy_(self, bstack1ll111llll_opy_):
        if bstack1ll111llll_opy_:
            self.bstack1ll111ll1l_opy_.append(bstack111ll_opy_ (u"ࠧ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ಩"))
            self.bstack1ll111ll1l_opy_.append(bstack111ll_opy_ (u"ࠨࡖࡵࡹࡪ࠭ಪ"))
        self.bstack1ll111ll1l_opy_.append(bstack111ll_opy_ (u"ࠩ࠰ࡴࠬಫ"))
        self.bstack1ll111ll1l_opy_.append(bstack111ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡲ࡯ࡹ࡬࡯࡮ࠨಬ"))
        self.bstack1ll111ll1l_opy_.append(bstack111ll_opy_ (u"ࠫ࠲࠳ࡤࡳ࡫ࡹࡩࡷ࠭ಭ"))
        self.bstack1ll111ll1l_opy_.append(bstack111ll_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬಮ"))
        if self.bstack1111111l1_opy_ > 1:
            self.bstack1ll111ll1l_opy_.append(bstack111ll_opy_ (u"࠭࠭࡯ࠩಯ"))
            self.bstack1ll111ll1l_opy_.append(str(self.bstack1111111l1_opy_))
    def bstack1ll111l1ll_opy_(self):
        bstack1l111111l_opy_ = []
        for spec in self.bstack1llll111l1_opy_:
            bstack1l1111lll_opy_ = [spec]
            bstack1l1111lll_opy_ += self.bstack1ll111ll1l_opy_
            bstack1l111111l_opy_.append(bstack1l1111lll_opy_)
        self.bstack1l111111l_opy_ = bstack1l111111l_opy_
        return bstack1l111111l_opy_
    def bstack1l1l1111_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack1ll111ll11_opy_ = True
            return True
        except Exception as e:
            self.bstack1ll111ll11_opy_ = False
        return self.bstack1ll111ll11_opy_
    def bstack1111l1111_opy_(self, bstack1ll111lll1_opy_, bstack1ll1l1ll11_opy_):
        bstack1ll1l1ll11_opy_[bstack111ll_opy_ (u"ࠧࡄࡑࡑࡊࡎࡍࠧರ")] = self.bstack1ll1111ll1_opy_
        if bstack111ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫಱ") in self.bstack1ll1111ll1_opy_:
            bstack111ll1l1_opy_ = []
            manager = multiprocessing.Manager()
            bstack1ll11ll1l_opy_ = manager.list()
            for index, platform in enumerate(self.bstack1ll1111ll1_opy_[bstack111ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬಲ")]):
                bstack111ll1l1_opy_.append(multiprocessing.Process(name=str(index),
                                                           target=bstack1ll111lll1_opy_,
                                                           args=(self.bstack1ll111ll1l_opy_, bstack1ll1l1ll11_opy_)))
            i = 0
            for t in bstack111ll1l1_opy_:
                os.environ[bstack111ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪಳ")] = str(i)
                i += 1
                t.start()
            for t in bstack111ll1l1_opy_:
                t.join()
            return bstack1ll11ll1l_opy_