from flask import Blueprint

register_blue = Blueprint("register_blue",
                          __name__,
                          static_folder=None,  # 子应用如有单独静态文件夹，则使用。
                          static_url_path=None,
                          template_folder='templates',
                          url_prefix="/register",
                          subdomain=None,
                          url_defaults=None,
                          root_path=None
                          )

# 关联views中的视图， 处于Blueprint解决循环导入问题
from .views import *
