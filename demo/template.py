# -*- coding: utf-8 -*-
from django.shortcuts import render
from toolkit.pre_load import pre_load_thu, neo_con, predict_labels
from toolkit.NER import get_NE, temporaryok, get_explain, get_detail_explain

# 测试接口
def test(request):
    ctx = {}
    if request.POST:
        key = request.POST['user_text']
        thu1 = pre_load_thu  # 提前加载好了
        # 使用thulac进行分词 TagList[i][0]代表第i个词
        # TagList[i][1]代表第i个词的词性
        key = key.strip()
        print('==key==', key)
        text = ""

        ctx['rlt'] = text

    return render(request, "template.html", ctx)
