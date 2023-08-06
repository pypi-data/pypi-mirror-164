from .base import BackendBase
from .bk_qiniu import Qiniu
from .bk_wy import WYSF

backend_factory = {
    'qiniu': Qiniu,
    'wysf': WYSF
}