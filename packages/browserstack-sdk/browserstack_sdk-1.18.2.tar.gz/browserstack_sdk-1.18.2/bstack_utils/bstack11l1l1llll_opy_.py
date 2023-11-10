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
import os
from uuid import uuid4
from bstack_utils.helper import bstack1lll1111l1_opy_, bstack1l11llllll_opy_
from bstack_utils.bstack1lll11ll1l_opy_ import bstack11ll1l1l1l_opy_
class bstack11l1l11l11_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, bstack11l1l1l1l1_opy_=None, framework=None, tags=[], scope=[], bstack11l1l11ll1_opy_=None, bstack11l1l1l11l_opy_=True, bstack11l1ll1l11_opy_=None, bstack1lll111ll_opy_=None, result=None, duration=None, meta={}):
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack11l1l1l11l_opy_:
            self.uuid = uuid4().__str__()
        self.bstack11l1l1l1l1_opy_ = bstack11l1l1l1l1_opy_
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack11l1l11ll1_opy_ = bstack11l1l11ll1_opy_
        self.bstack11l1ll1l11_opy_ = bstack11l1ll1l11_opy_
        self.bstack1lll111ll_opy_ = bstack1lll111ll_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
    def bstack11l1l1l111_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11l1lll111_opy_(self):
        bstack11l1l1ll11_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack111ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪቒ"): bstack11l1l1ll11_opy_,
            bstack111ll_opy_ (u"ࠨ࡮ࡲࡧࡦࡺࡩࡰࡰࠪቓ"): bstack11l1l1ll11_opy_,
            bstack111ll_opy_ (u"ࠩࡹࡧࡤ࡬ࡩ࡭ࡧࡳࡥࡹ࡮ࠧቔ"): bstack11l1l1ll11_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack111ll_opy_ (u"࡙ࠥࡳ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡢࡴࡪࡹࡲ࡫࡮ࡵ࠼ࠣࠦቕ") + key)
            setattr(self, key, val)
    def bstack11l1l1l1ll_opy_(self):
        return {
            bstack111ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩቖ"): self.name,
            bstack111ll_opy_ (u"ࠬࡨ࡯ࡥࡻࠪ቗"): {
                bstack111ll_opy_ (u"࠭࡬ࡢࡰࡪࠫቘ"): bstack111ll_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ቙"),
                bstack111ll_opy_ (u"ࠨࡥࡲࡨࡪ࠭ቚ"): self.code
            },
            bstack111ll_opy_ (u"ࠩࡶࡧࡴࡶࡥࡴࠩቛ"): self.scope,
            bstack111ll_opy_ (u"ࠪࡸࡦ࡭ࡳࠨቜ"): self.tags,
            bstack111ll_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧቝ"): self.framework,
            bstack111ll_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩ቞"): self.bstack11l1l1l1l1_opy_
        }
    def bstack11l1l1ll1l_opy_(self):
        return {
         bstack111ll_opy_ (u"࠭࡭ࡦࡶࡤࠫ቟"): self.meta
        }
    def bstack11l1ll1lll_opy_(self):
        return {
            bstack111ll_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡒࡦࡴࡸࡲࡕࡧࡲࡢ࡯ࠪበ"): {
                bstack111ll_opy_ (u"ࠨࡴࡨࡶࡺࡴ࡟࡯ࡣࡰࡩࠬቡ"): self.bstack11l1l11ll1_opy_
            }
        }
    def bstack11l1ll11ll_opy_(self, bstack11l1ll111l_opy_, details):
        step = next(filter(lambda st: st[bstack111ll_opy_ (u"ࠩ࡬ࡨࠬቢ")] == bstack11l1ll111l_opy_, self.meta[bstack111ll_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩባ")]), None)
        step.update(details)
    def bstack11l1ll11l1_opy_(self, bstack11l1ll111l_opy_):
        step = next(filter(lambda st: st[bstack111ll_opy_ (u"ࠫ࡮ࡪࠧቤ")] == bstack11l1ll111l_opy_, self.meta[bstack111ll_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫብ")]), None)
        step.update({
            bstack111ll_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪቦ"): bstack1lll1111l1_opy_()
        })
    def bstack11l1l111ll_opy_(self, bstack11l1ll111l_opy_, result):
        bstack11l1ll1l11_opy_ = bstack1lll1111l1_opy_()
        step = next(filter(lambda st: st[bstack111ll_opy_ (u"ࠧࡪࡦࠪቧ")] == bstack11l1ll111l_opy_, self.meta[bstack111ll_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧቨ")]), None)
        step.update({
            bstack111ll_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧቩ"): bstack11l1ll1l11_opy_,
            bstack111ll_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬቪ"): bstack1l11llllll_opy_(step[bstack111ll_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨቫ")], bstack11l1ll1l11_opy_),
            bstack111ll_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬቬ"): result.result,
            bstack111ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧቭ"): str(result.exception) if result.exception else None
        })
    def bstack11l1ll1l1l_opy_(self):
        return {
            bstack111ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬቮ"): self.bstack11l1l1l111_opy_(),
            **self.bstack11l1l1l1ll_opy_(),
            **self.bstack11l1lll111_opy_(),
            **self.bstack11l1l1ll1l_opy_()
        }
    def bstack11l1l111l1_opy_(self):
        data = {
            bstack111ll_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ቯ"): self.bstack11l1ll1l11_opy_,
            bstack111ll_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪተ"): self.duration,
            bstack111ll_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪቱ"): self.result.result
        }
        if data[bstack111ll_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫቲ")] == bstack111ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬታ"):
            data[bstack111ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠬቴ")] = self.result.bstack1l1l11l111_opy_()
            data[bstack111ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨት")] = [{bstack111ll_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫቶ"): self.result.bstack1l11lll1ll_opy_()}]
        return data
    def bstack11l1l11lll_opy_(self):
        return {
            bstack111ll_opy_ (u"ࠩࡸࡹ࡮ࡪࠧቷ"): self.bstack11l1l1l111_opy_(),
            **self.bstack11l1l1l1ll_opy_(),
            **self.bstack11l1lll111_opy_(),
            **self.bstack11l1l111l1_opy_(),
            **self.bstack11l1l1ll1l_opy_()
        }
    def bstack11l1l1111l_opy_(self, event, result=None):
        if result:
            self.result = result
        if event == bstack111ll_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫቸ"):
            return self.bstack11l1ll1l1l_opy_()
        elif event == bstack111ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ቹ"):
            return self.bstack11l1l11lll_opy_()
    def bstack11l1ll1111_opy_(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack11l1ll1l11_opy_ = time if time else bstack1lll1111l1_opy_()
        self.duration = duration if duration else bstack1l11llllll_opy_(self.bstack11l1l1l1l1_opy_, self.bstack11l1ll1l11_opy_)
        if result:
            self.result = result
class bstack11l1l11l1l_opy_(bstack11l1l11l11_opy_):
    def __init__(self, *args, hooks=[], **kwargs):
        self.hooks = hooks
        super().__init__(*args, **kwargs, bstack1lll111ll_opy_=bstack111ll_opy_ (u"ࠬࡺࡥࡴࡶࠪቺ"))
    @classmethod
    def bstack11l1l1lll1_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack111ll_opy_ (u"࠭ࡩࡥࠩቻ"): id(step),
                bstack111ll_opy_ (u"ࠧࡵࡧࡻࡸࠬቼ"): step.name,
                bstack111ll_opy_ (u"ࠨ࡭ࡨࡽࡼࡵࡲࡥࠩች"): step.keyword,
            })
        return bstack11l1l11l1l_opy_(
            **kwargs,
            meta={
                bstack111ll_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࠪቾ"): {
                    bstack111ll_opy_ (u"ࠪࡲࡦࡳࡥࠨቿ"): feature.name,
                    bstack111ll_opy_ (u"ࠫࡵࡧࡴࡩࠩኀ"): feature.filename,
                    bstack111ll_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪኁ"): feature.description
                },
                bstack111ll_opy_ (u"࠭ࡳࡤࡧࡱࡥࡷ࡯࡯ࠨኂ"): {
                    bstack111ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬኃ"): scenario.name
                },
                bstack111ll_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧኄ"): steps,
                bstack111ll_opy_ (u"ࠩࡨࡼࡦࡳࡰ࡭ࡧࡶࠫኅ"): bstack11ll1l1l1l_opy_(test)
            }
        )
    def bstack11l1ll1ll1_opy_(self):
        return {
            bstack111ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩኆ"): self.hooks
        }
    def bstack11l1l11lll_opy_(self):
        return {
            **super().bstack11l1l11lll_opy_(),
            **self.bstack11l1ll1ll1_opy_()
        }
    def bstack11l1ll1111_opy_(self):
        return bstack111ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭ኇ")