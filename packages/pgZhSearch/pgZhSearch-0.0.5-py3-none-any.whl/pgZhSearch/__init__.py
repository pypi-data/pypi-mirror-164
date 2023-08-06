try:
    from .base_search import *
except Exception as e:
    print(e)


def version():
    """
    # 更新说明

    - 初始化       # 0.0.1
    - ReadMe出现bug       # 0.0.2
    - 拉取更新. search方法从此支持queryset    # 0.0.3
    - 修复pypi没有上传txt文件的问题    # 0.0.4
    - 修复`get_total_occurance_times_by_keywords`的rank过滤条件为`gt`而不是`gte`的问题    # 0.0.5
    """
    return '0.0.5'


