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
import sys
class bstack1l1ll11ll1_opy_:
    def __init__(self, handler):
        self._1l1ll111ll_opy_ = sys.stdout.write
        self._1l1ll11l1l_opy_ = sys.stderr.write
        self.handler = handler
        self._started = False
    def start(self):
        if self._started:
            return
        self._started = True
        sys.stdout.write = self.bstack1l1ll11l11_opy_
        sys.stdout.error = self.bstack1l1ll111l1_opy_
    def bstack1l1ll11l11_opy_(self, _str):
        self._1l1ll111ll_opy_(_str)
        if self.handler:
            self.handler({bstack111ll_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨൌ"): bstack111ll_opy_ (u"ࠪࡍࡓࡌࡏࠨ്"), bstack111ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬൎ"): _str})
    def bstack1l1ll111l1_opy_(self, _str):
        self._1l1ll11l1l_opy_(_str)
        if self.handler:
            self.handler({bstack111ll_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ൏"): bstack111ll_opy_ (u"࠭ࡅࡓࡔࡒࡖࠬ൐"), bstack111ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ൑"): _str})
    def reset(self):
        if not self._started:
            return
        self._started = False
        sys.stdout.write = self._1l1ll111ll_opy_
        sys.stderr.write = self._1l1ll11l1l_opy_