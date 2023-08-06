# pgZhSearch简介

> django-postgresql环境下的中文全文检索, 基于倒排索引计算词向量相关度.


## QuickStart

- models.py
```
from pgZhSearch import BaseFullTextSearchModel


class Question(BaseFullTextSearchModel):
    # 综合检索设置
    search_field_conf = {
        'wen_ti': 'A',
        'fen_lei_ming': 'B',
        'da_an_nei_rong': 'C',
    }
    class Meta:
        indexes = BaseFullTextSearchModel.Meta.indexes
    
    fen_lei_ming = models.TextField(blank=True, null=True, verbose_name='分类名')
    wen_ti = models.TextField(blank=True, null=True, verbose_name='问题')
    da_an_nei_rong = models.TextField(blank=True, null=True, verbose_name='答案内容')

```

- admin.py
```
from bddjango import BaseAdmin
from pgZhSearch import BuildIndexAdminMixin


@admin.register(models.Question)
class Question(BaseAdmin, BuildIndexAdminMixin):
    actions = [rebuild_index']      # 批量导入时需要进入admin界面手动重置索引

```

- views.py
```
qs_ls = Question.filter(fen_lei_ming='婚姻家庭').search(keywords)
```


## 备注
- 调整权重参考末尾的参考文献--Django中文文档.
- 分词基于`jieba`实现, 实现方法位于`pgZhSearch.extract_keyword`路径
- 未检索到结果 or 没有新建索引的话, 会再次使用原始orm统计关键词频数来进行相关度排序. 此时rank值均大于1.


## 参考文献

- [Django中文文档-全文检索](https://cainiaojiaocheng.com/Django/docs/3.2.x/ref/contrib/postgres/search)
- [一个参考案例](https://juejin.cn/post/6844903480893636616)

