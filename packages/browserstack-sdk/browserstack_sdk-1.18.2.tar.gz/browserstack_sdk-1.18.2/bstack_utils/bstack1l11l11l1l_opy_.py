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
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result
def _1l11l1111l_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack1l11l1ll11_opy_:
    def __init__(self, handler):
        self._1l11l1lll1_opy_ = {}
        self._1l11l1l1ll_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        self._1l11l1lll1_opy_[bstack111ll_opy_ (u"ࠪࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᄌ")] = Module._inject_setup_function_fixture
        self._1l11l1lll1_opy_[bstack111ll_opy_ (u"ࠫࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᄍ")] = Module._inject_setup_module_fixture
        self._1l11l1lll1_opy_[bstack111ll_opy_ (u"ࠬࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᄎ")] = Class._inject_setup_class_fixture
        self._1l11l1lll1_opy_[bstack111ll_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᄏ")] = Class._inject_setup_method_fixture
        Module._inject_setup_function_fixture = self.bstack1l11l111ll_opy_(bstack111ll_opy_ (u"ࠧࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᄐ"))
        Module._inject_setup_module_fixture = self.bstack1l11l111ll_opy_(bstack111ll_opy_ (u"ࠨ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᄑ"))
        Class._inject_setup_class_fixture = self.bstack1l11l111ll_opy_(bstack111ll_opy_ (u"ࠩࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᄒ"))
        Class._inject_setup_method_fixture = self.bstack1l11l111ll_opy_(bstack111ll_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᄓ"))
    def bstack1l11l111l1_opy_(self, bstack1l11l11111_opy_, hook_type):
        meth = getattr(bstack1l11l11111_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._1l11l1l1ll_opy_[hook_type] = meth
            setattr(bstack1l11l11111_opy_, hook_type, self.bstack1l11l1l1l1_opy_(hook_type))
    def bstack1l11l11lll_opy_(self, instance, bstack1l11l1l11l_opy_):
        if bstack1l11l1l11l_opy_ == bstack111ll_opy_ (u"ࠦ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠢᄔ"):
            self.bstack1l11l111l1_opy_(instance.obj, bstack111ll_opy_ (u"ࠧࡹࡥࡵࡷࡳࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠨᄕ"))
            self.bstack1l11l111l1_opy_(instance.obj, bstack111ll_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࠥᄖ"))
        if bstack1l11l1l11l_opy_ == bstack111ll_opy_ (u"ࠢ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣᄗ"):
            self.bstack1l11l111l1_opy_(instance.obj, bstack111ll_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠢᄘ"))
            self.bstack1l11l111l1_opy_(instance.obj, bstack111ll_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠦᄙ"))
        if bstack1l11l1l11l_opy_ == bstack111ll_opy_ (u"ࠥࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠥᄚ"):
            self.bstack1l11l111l1_opy_(instance.obj, bstack111ll_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠤᄛ"))
            self.bstack1l11l111l1_opy_(instance.obj, bstack111ll_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡤ࡮ࡤࡷࡸࠨᄜ"))
        if bstack1l11l1l11l_opy_ == bstack111ll_opy_ (u"ࠨ࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠢᄝ"):
            self.bstack1l11l111l1_opy_(instance.obj, bstack111ll_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩࠨᄞ"))
            self.bstack1l11l111l1_opy_(instance.obj, bstack111ll_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠥᄟ"))
    @staticmethod
    def bstack1l11l1l111_opy_(hook_type, func, args):
        if hook_type in [bstack111ll_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡨࡸ࡭ࡵࡤࠨᄠ"), bstack111ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳࡥࡵࡪࡲࡨࠬᄡ")]:
            _1l11l1111l_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack1l11l1l1l1_opy_(self, hook_type):
        def bstack1l11l1ll1l_opy_(arg=None):
            self.handler(hook_type, bstack111ll_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࠫᄢ"))
            result = None
            exception = None
            try:
                self.bstack1l11l1l111_opy_(hook_type, self._1l11l1l1ll_opy_[hook_type], (arg,))
                result = Result(result=bstack111ll_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᄣ"))
            except Exception as e:
                result = Result(result=bstack111ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᄤ"), exception=e)
                self.handler(hook_type, bstack111ll_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭ᄥ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack111ll_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧᄦ"), result)
        def bstack1l11l11l11_opy_(this, arg=None):
            self.handler(hook_type, bstack111ll_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࠩᄧ"))
            result = None
            exception = None
            try:
                self.bstack1l11l1l111_opy_(hook_type, self._1l11l1l1ll_opy_[hook_type], (this, arg))
                result = Result(result=bstack111ll_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᄨ"))
            except Exception as e:
                result = Result(result=bstack111ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᄩ"), exception=e)
                self.handler(hook_type, bstack111ll_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫᄪ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack111ll_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬᄫ"), result)
        if hook_type in [bstack111ll_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ᄬ"), bstack111ll_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠪᄭ")]:
            return bstack1l11l11l11_opy_
        return bstack1l11l1ll1l_opy_
    def bstack1l11l111ll_opy_(self, bstack1l11l1l11l_opy_):
        def bstack1l11l11ll1_opy_(this, *args, **kwargs):
            self.bstack1l11l11lll_opy_(this, bstack1l11l1l11l_opy_)
            self._1l11l1lll1_opy_[bstack1l11l1l11l_opy_](this, *args, **kwargs)
        return bstack1l11l11ll1_opy_