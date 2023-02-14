# -*- coding:utf-8 -*-
from django.shortcuts import render
from toolkit.pre_load import pre_load_thu
from toolkit.pre_load import neo_con
# from demo.demo.question_template import pattern
import random
import re
import logging

thu_lac = pre_load_thu
db = neo_con

pattern = [[r"目的是什么", r"有什么目的"],
           [r"依据是什么", r"根据是什么", r"有什么依据", r"有什么根据", r"是根据什么制定的"],
           [r"是什么", r"的定义是什么", r"指的是什么", r"解释是什么", r"解释为", r"的定义", r"定义为"],
           [r"适用范围是什么", r"适用于什么", r"适合用于什么范围", r"适合什么领域", r"适合用于什么活动"],
           [r"有什么权利", r"权利是"],
           [r"有什么奖励", r"奖励是"],
           [r"有什么处罚", r"有什么后果", r"有什么惩罚", r"后果是", r"会造成什么后果"],
           [r"包含什么", r"包括什么", r"分类为", r"分类是", r"分为那几类", r"包含什么内容", r"包含那几方面的内容",
            r"分为那几种", r"类别是", r"分为哪几类", r"分为哪几种", r"包含哪几方面的内容"],
           [r"有什么职责", r"有什么责任", r"职责是", r"责任是", r"有什么要求", r"要求是", r"有什么规定", r"规定是",
            r"需要做什么", r"应当具备什么条件", r"需要具备什么条件", r"应当提交什么材料", r"需要提交什么材料",
            r"必须具备什么条件",
            r"应该遵守什么", r"必须遵守", r"应该怎么做"],
           [r"性质是", r"有什么性质"],
           [r"提出时间是", r"发明时间是", r"提出时间", r"发明时间"],
           [r"提出者是", r"发明者是", r"发明人是", r"谁发明的"],
           [r"所属领域是", r"属于什么领域", r"属于那个领域"],
           [r"有什么应用", r"应用于"],
           [r"有什么优点", r"优点是"],
           [r"有什么缺点", r"缺点是"],
           [r"特点是", r"有什么特点"]
           ]

# 获取所查询的实体的目的
def get_aim(obj, ret_dict):
    aims = db.findOtherEntities(obj, "AIM")
    if (len(aims) > 0):
        # 结果数大于6则随机取6个
        if (len(aims) > 6):
            selected_index = []
            n = len(aims)
            m = 6
            for i in range(n):
                rand = random.randint(0, n - i - 1)
                if (rand < m):
                    m -= 1
                    selected_index.append(i)
        else:
            selected_index = [i for i in range(len(aims))]

        for index in selected_index:
            x = aims[index]['n2']['name']
            if (ret_dict.get('list') is None):
                ret_dict['list'] = [
                    {'entity1': obj, 'rel': '目的', 'entity2': x, 'entity1_type': '对象', 'entity2_type': '内容'}]
            else:
                ret_dict['list'].append(
                    {'entity1': obj, 'rel': '目的', 'entity2': x, 'entity1_type': '对象', 'entity2_type': '内容'})

            if (ret_dict.get('answer') is None):
                ret_dict['answer'] = [x]
            else:
                ret_dict['answer'].append(x)
    return ret_dict


# 获取所查询的实体的依据
def get_accord(obj, ret_dict):
    accords = db.findOtherEntities(obj, "ACCORD")
    print('accords', accords)
    if (len(accords) > 0):
        # 结果数大于6则随机取6个
        if (len(accords) > 6):
            selected_index = []
            n = len(accords)
            m = 6
            for i in range(n):
                rand = random.randint(0, n - i - 1)
                if (rand < m):
                    m -= 1
                    selected_index.append(i)
        else:
            selected_index = [i for i in range(len(accords))]

        for index in selected_index:
            x = accords[index]['n2']['name']
            if (ret_dict.get('list') is None):
                ret_dict['list'] = [
                    {'entity1': obj, 'rel': '依据', 'entity2': x, 'entity1_type': '对象', 'entity2_type': '内容'}]
            else:
                ret_dict['list'].append(
                    {'entity1': obj, 'rel': '依据', 'entity2': x, 'entity1_type': '对象', 'entity2_type': '内容'})

            if (ret_dict.get('answer') is None):
                ret_dict['answer'] = [x]
            else:
                ret_dict['answer'].append(x)
    return ret_dict


# 获取所查询实体的定义
def get_define(obj, ret_dict):
    defines = db.findOtherEntities(obj, "解释")
    if (len(defines) == 0):
        defines = db.findOtherEntities(obj, "解释")
    print('accords', defines)
    if (len(defines) > 0):
        # 结果数大于6则随机取6个
        if (len(defines) > 6):
            selected_index = []
            n = len(defines)
            m = 6
            for i in range(n):
                rand = random.randint(0, n - i - 1)
                if (rand < m):
                    m -= 1
                    selected_index.append(i)
        else:
            selected_index = [i for i in range(len(defines))]

        for index in selected_index:
            x = defines[index]['n2']['name']
            if (ret_dict.get('list') is None):
                ret_dict['list'] = [
                    {'entity1': obj, 'rel': '定义', 'entity2': x, 'entity1_type': '对象', 'entity2_type': '内容'}]
            else:
                ret_dict['list'].append(
                    {'entity1': obj, 'rel': '定义', 'entity2': x, 'entity1_type': '对象', 'entity2_type': '内容'})

            if (ret_dict.get('answer') is None):
                ret_dict['answer'] = [x]
            else:
                ret_dict['answer'].append(x)
    return ret_dict


# 获取所查询实体的适用范围
def get_scope(obj, ret_dict):
    scopes = db.findOtherEntities(obj, "SCOPE_OF_APPLICATION")
    if (len(scopes) > 0):
        # 结果数大于6则随机取6个
        if (len(scopes) > 6):
            selected_index = []
            n = len(scopes)
            m = 6
            for i in range(n):
                rand = random.randint(0, n - i - 1)
                if (rand < m):
                    m -= 1
                    selected_index.append(i)
        else:
            selected_index = [i for i in range(len(scopes))]

        for index in selected_index:
            x = scopes[index]['n2']['name']
            if (ret_dict.get('list') is None):
                ret_dict['list'] = [
                    {'entity1': obj, 'rel': '适用范围', 'entity2': x, 'entity1_type': '对象', 'entity2_type': '内容'}]
            else:
                ret_dict['list'].append(
                    {'entity1': obj, 'rel': '适用范围', 'entity2': x, 'entity1_type': '对象', 'entity2_type': '内容'})

            if (ret_dict.get('answer') is None):
                ret_dict['answer'] = [x]
            else:
                ret_dict['answer'].append(x)
    return ret_dict


# 获取所查询实体的权利
def get_right(obj, ret_dict):
    rights = db.findOtherEntities(obj, "RIGHT_AND_OBLIGATE")
    if (len(rights) > 0):
        # 结果数大于6则随机取6个
        if (len(rights) > 6):
            selected_index = []
            n = len(rights)
            m = 6
            for i in range(n):
                rand = random.randint(0, n - i - 1)
                if (rand < m):
                    m -= 1
                    selected_index.append(i)
        else:
            selected_index = [i for i in range(len(rights))]

        for index in selected_index:
            x = rights[index]['n2']['name']
            if (ret_dict.get('list') is None):
                ret_dict['list'] = [
                    {'entity1': obj, 'rel': '权利', 'entity2': x, 'entity1_type': '对象', 'entity2_type': '内容'}]
            else:
                ret_dict['list'].append(
                    {'entity1': obj, 'rel': '权利', 'entity2': x, 'entity1_type': '对象', 'entity2_type': '内容'})

            if (ret_dict.get('answer') is None):
                ret_dict['answer'] = [x]
            else:
                ret_dict['answer'].append(x)
    return ret_dict


# 获取所查询实体的奖励
def get_award(obj, ret_dict):
    awards = db.findOtherEntities(obj, "AWARD")
    if (len(awards) > 0):
        # 结果数大于6则随机取6个
        if (len(awards) > 6):
            selected_index = []
            n = len(awards)
            m = 6
            for i in range(n):
                rand = random.randint(0, n - i - 1)
                if (rand < m):
                    m -= 1
                    selected_index.append(i)
        else:
            selected_index = [i for i in range(len(awards))]

        for index in selected_index:
            x = awards[index]['n2']['name']
            if (ret_dict.get('list') is None):
                ret_dict['list'] = [
                    {'entity1': obj, 'rel': '奖励', 'entity2': x, 'entity1_type': '对象', 'entity2_type': '内容'}]
            else:
                ret_dict['list'].append(
                    {'entity1': obj, 'rel': '奖励', 'entity2': x, 'entity1_type': '对象', 'entity2_type': '内容'})

            if (ret_dict.get('answer') is None):
                ret_dict['answer'] = [x]
            else:
                ret_dict['answer'].append(x)
    return ret_dict


# 获取所查询实体的处罚/后果
def get_punishment(obj, ret_dict):
    punishments = db.findOtherEntities(obj, "PUNISHMENT")
    if (len(punishments) > 0):
        # 结果数大于6则随机取6个
        if (len(punishments) > 6):
            selected_index = []
            n = len(punishments)
            m = 6
            for i in range(n):
                rand = random.randint(0, n - i - 1)
                if (rand < m):
                    m -= 1
                    selected_index.append(i)
        else:
            selected_index = [i for i in range(len(punishments))]

        for index in selected_index:
            x = punishments[index]['n2']['name']
            if (ret_dict.get('list') is None):
                ret_dict['list'] = [
                    {'entity1': obj, 'rel': '处罚', 'entity2': x, 'entity1_type': '对象', 'entity2_type': '内容'}]
            else:
                ret_dict['list'].append(
                    {'entity1': obj, 'rel': '处罚', 'entity2': x, 'entity1_type': '对象', 'entity2_type': '内容'})

            if (ret_dict.get('answer') is None):
                ret_dict['answer'] = [x]
            else:
                ret_dict['answer'].append(x)
    return ret_dict


# 获取所查询实体的包含内容/分类
def get_classify(obj, ret_dict):
    # 查找核法律法规相关分类
    classify = db.findOtherEntities(obj, "CONTAIN")

    # 用户查询之后，如果能执行到这里，说明用户查询的是有关实体分类/包含的问题，如果classify=[],则说明用户查询的不是核法规相关，而是核综合知识相关
    if (len(classify) == 0):
        classify = db.findOtherEntities(obj, "分类")

    if (len(classify) > 0):
        # 结果数大于6则随机取6个
        if (len(classify) > 6):
            selected_index = []
            n = len(classify)
            m = 6
            for i in range(n):
                rand = random.randint(0, n - i - 1)
                if (rand < m):
                    m -= 1
                    selected_index.append(i)
        else:
            selected_index = [i for i in range(len(classify))]

        for index in selected_index:
            x = classify[index]['n2']['name']
            if (ret_dict.get('list') is None):
                ret_dict['list'] = [
                    {'entity1': obj, 'rel': '分类', 'entity2': x, 'entity1_type': '对象', 'entity2_type': '内容'}]
            else:
                ret_dict['list'].append(
                    {'entity1': obj, 'rel': '分类', 'entity2': x, 'entity1_type': '对象', 'entity2_type': '内容'})

            if (ret_dict.get('answer') is None):
                ret_dict['answer'] = [x]
            else:
                ret_dict['answer'].append(x)
    return ret_dict


# 获取所查询实体的职责/规定/要求
def get_duty(obj, ret_dict):
    duty = db.findOtherEntities(obj, "DUTY")
    if (len(duty) > 0):
        # 结果数大于6则随机取6个
        if (len(duty) > 6):
            selected_index = []
            n = len(duty)
            m = 6
            for i in range(n):
                rand = random.randint(0, n - i - 1)
                if (rand < m):
                    m -= 1
                    selected_index.append(i)
        else:
            selected_index = [i for i in range(len(duty))]

        for index in selected_index:
            x = duty[index]['n2']['name']
            if (ret_dict.get('list') is None):
                ret_dict['list'] = [
                    {'entity1': obj, 'rel': '责任/要求/规定', 'entity2': x, 'entity1_type': '对象',
                     'entity2_type': '内容'}]
            else:
                ret_dict['list'].append(
                    {'entity1': obj, 'rel': '责任/要求/规定', 'entity2': x, 'entity1_type': '对象',
                     'entity2_type': '内容'})

            if (ret_dict.get('answer') is None):
                ret_dict['answer'] = [x]
            else:
                ret_dict['answer'].append(x)
    return ret_dict


# 获取所查询实体的性质
def get_nature(obj, ret_dict):
    nature = db.findOtherEntities(obj, "性质")
    if (len(nature) > 0):
        # 结果数大于6则随机取6个
        if (len(nature) > 6):
            selected_index = []
            n = len(nature)
            m = 6
            for i in range(n):
                rand = random.randint(0, n - i - 1)
                if (rand < m):
                    m -= 1
                    selected_index.append(i)
        else:
            selected_index = [i for i in range(len(nature))]

        for index in selected_index:
            x = nature[index]['n2']['name']
            if (ret_dict.get('list') is None):
                ret_dict['list'] = [
                    {'entity1': obj, 'rel': '性质', 'entity2': x, 'entity1_type': '对象',
                     'entity2_type': '内容'}]
            else:
                ret_dict['list'].append(
                    {'entity1': obj, 'rel': '性质', 'entity2': x, 'entity1_type': '对象',
                     'entity2_type': '内容'})

            if (ret_dict.get('answer') is None):
                ret_dict['answer'] = [x]
            else:
                ret_dict['answer'].append(x)
    return ret_dict


# 获取所查询实体的发明时间
def get_propose_time(obj, ret_dict):
    propose_time = db.findOtherEntities(obj, "提出时间")
    if (len(propose_time) > 0):
        # 结果数大于6则随机取6个
        if (len(propose_time) > 6):
            selected_index = []
            n = len(propose_time)
            m = 6
            for i in range(n):
                rand = random.randint(0, n - i - 1)
                if (rand < m):
                    m -= 1
                    selected_index.append(i)
        else:
            selected_index = [i for i in range(len(propose_time))]

        for index in selected_index:
            x = propose_time[index]['n2']['name']
            if (ret_dict.get('list') is None):
                ret_dict['list'] = [
                    {'entity1': obj, 'rel': '发明时间', 'entity2': x, 'entity1_type': '对象',
                     'entity2_type': '内容'}]
            else:
                ret_dict['list'].append(
                    {'entity1': obj, 'rel': '发明时间', 'entity2': x, 'entity1_type': '对象',
                     'entity2_type': '内容'})

            if (ret_dict.get('answer') is None):
                ret_dict['answer'] = [x]
            else:
                ret_dict['answer'].append(x)
    return ret_dict


# 获取所查询实体的发明人
def get_propose_people(obj, ret_dict):
    propose_people = db.findOtherEntities(obj, "提出者")
    if (len(propose_people) > 0):
        # 结果数大于6则随机取6个
        if (len(propose_people) > 6):
            selected_index = []
            n = len(propose_people)
            m = 6
            for i in range(n):
                rand = random.randint(0, n - i - 1)
                if (rand < m):
                    m -= 1
                    selected_index.append(i)
        else:
            selected_index = [i for i in range(len(propose_people))]

        for index in selected_index:
            x = propose_people[index]['n2']['name']
            if (ret_dict.get('list') is None):
                ret_dict['list'] = [
                    {'entity1': obj, 'rel': '发明者/提出者', 'entity2': x, 'entity1_type': '对象',
                     'entity2_type': '内容'}]
            else:
                ret_dict['list'].append(
                    {'entity1': obj, 'rel': '发明者/提出者', 'entity2': x, 'entity1_type': '对象',
                     'entity2_type': '内容'})

            if (ret_dict.get('answer') is None):
                ret_dict['answer'] = [x]
            else:
                ret_dict['answer'].append(x)
    return ret_dict


# 获取所查询实体的所属领域
def get_field(obj, ret_dict):
    field = db.findOtherEntities(obj, "领域")
    if (len(field) > 0):
        # 结果数大于6则随机取6个
        if (len(field) > 6):
            selected_index = []
            n = len(field)
            m = 6
            for i in range(n):
                rand = random.randint(0, n - i - 1)
                if (rand < m):
                    m -= 1
                    selected_index.append(i)
        else:
            selected_index = [i for i in range(len(field))]

        for index in selected_index:
            x = field[index]['n2']['name']
            if (ret_dict.get('list') is None):
                ret_dict['list'] = [
                    {'entity1': obj, 'rel': '领域', 'entity2': x, 'entity1_type': '对象',
                     'entity2_type': '内容'}]
            else:
                ret_dict['list'].append(
                    {'entity1': obj, 'rel': '领域', 'entity2': x, 'entity1_type': '对象',
                     'entity2_type': '内容'})

            if (ret_dict.get('answer') is None):
                ret_dict['answer'] = [x]
            else:
                ret_dict['answer'].append(x)
    return ret_dict


# 获取所查询实体的应用
def get_application(obj, ret_dict):
    application = db.findOtherEntities(obj, "应用")
    if (len(application) > 0):
        # 结果数大于6则随机取6个
        if (len(application) > 6):
            selected_index = []
            n = len(application)
            m = 6
            for i in range(n):
                rand = random.randint(0, n - i - 1)
                if (rand < m):
                    m -= 1
                    selected_index.append(i)
        else:
            selected_index = [i for i in range(len(application))]

        for index in selected_index:
            x = application[index]['n2']['name']
            if (ret_dict.get('list') is None):
                ret_dict['list'] = [
                    {'entity1': obj, 'rel': '应用', 'entity2': x, 'entity1_type': '对象',
                     'entity2_type': '内容'}]
            else:
                ret_dict['list'].append(
                    {'entity1': obj, 'rel': '应用', 'entity2': x, 'entity1_type': '对象',
                     'entity2_type': '内容'})

            if (ret_dict.get('answer') is None):
                ret_dict['answer'] = [x]
            else:
                ret_dict['answer'].append(x)
    return ret_dict


# 获取所查询实体的优点
def get_advantage(obj, ret_dict):
    advantage = db.findOtherEntities(obj, "优点")
    if (len(advantage) > 0):
        # 结果数大于6则随机取6个
        if (len(advantage) > 6):
            selected_index = []
            n = len(advantage)
            m = 6
            for i in range(n):
                rand = random.randint(0, n - i - 1)
                if (rand < m):
                    m -= 1
                    selected_index.append(i)
        else:
            selected_index = [i for i in range(len(advantage))]

        for index in selected_index:
            x = advantage[index]['n2']['name']
            if (ret_dict.get('list') is None):
                ret_dict['list'] = [
                    {'entity1': obj, 'rel': '优点', 'entity2': x, 'entity1_type': '对象',
                     'entity2_type': '内容'}]
            else:
                ret_dict['list'].append(
                    {'entity1': obj, 'rel': '优点', 'entity2': x, 'entity1_type': '对象',
                     'entity2_type': '内容'})

            if (ret_dict.get('answer') is None):
                ret_dict['answer'] = [x]
            else:
                ret_dict['answer'].append(x)
    return ret_dict


# 获取所查询实体的缺点
def get_shortcoming(obj, ret_dict):
    shortcoming = db.findOtherEntities(obj, "缺点")
    if (len(shortcoming) > 0):
        # 结果数大于6则随机取6个
        if (len(shortcoming) > 6):
            selected_index = []
            n = len(shortcoming)
            m = 6
            for i in range(n):
                rand = random.randint(0, n - i - 1)
                if (rand < m):
                    m -= 1
                    selected_index.append(i)
        else:
            selected_index = [i for i in range(len(shortcoming))]

        for index in selected_index:
            x = shortcoming[index]['n2']['name']
            if (ret_dict.get('list') is None):
                ret_dict['list'] = [
                    {'entity1': obj, 'rel': '缺点', 'entity2': x, 'entity1_type': '对象',
                     'entity2_type': '内容'}]
            else:
                ret_dict['list'].append(
                    {'entity1': obj, 'rel': '缺点', 'entity2': x, 'entity1_type': '对象',
                     'entity2_type': '内容'})

            if (ret_dict.get('answer') is None):
                ret_dict['answer'] = [x]
            else:
                ret_dict['answer'].append(x)
    return ret_dict


# 获取所查询实体的特点
def get_feature(obj, ret_dict):
    feature = db.findOtherEntities(obj, "特点")
    if (len(feature) > 0):
        # 结果数大于6则随机取6个
        if (len(feature) > 6):
            selected_index = []
            n = len(feature)
            m = 6
            for i in range(n):
                rand = random.randint(0, n - i - 1)
                if (rand < m):
                    m -= 1
                    selected_index.append(i)
        else:
            selected_index = [i for i in range(len(feature))]

        for index in selected_index:
            x = feature[index]['n2']['name']
            if (ret_dict.get('list') is None):
                ret_dict['list'] = [
                    {'entity1': obj, 'rel': '特点', 'entity2': x, 'entity1_type': '对象',
                     'entity2_type': '内容'}]
            else:
                ret_dict['list'].append(
                    {'entity1': obj, 'rel': '特点', 'entity2': x, 'entity1_type': '对象',
                     'entity2_type': '内容'})

            if (ret_dict.get('answer') is None):
                ret_dict['answer'] = [x]
            else:
                ret_dict['answer'].append(x)
    return ret_dict


# 程序入口函数
def question_answering(request):  # index页面需要一开始就加载的内容写在这里
    context = {'ctx': ''}
    # logging.warning('发起请求页面执行到这里')
    if (request.GET):
        question = request.GET['question']
        print('question', question)
        cut_statement = thu_lac.cut(question, text=False)
        print('分词 词性标注', cut_statement)
        ret_dict = {}
        pos = -1
        q_type = -1
        for i in range(len(pattern)):
            for x in pattern[i]:
                # print('x', x)
                index = re.search(x, question)
                # print('index', index)
                if (index):
                    pos = index.span()[0]
                    q_type = i
                    break
            if (pos != -1):
                break
        print('pos', pos)
        print('q_type', q_type)

        # 匹配问题 xxx的目的是什么
        aim = ''
        if (q_type == 0):
            index = 0
            print('==cut_statement==', cut_statement)
            for x in cut_statement:
                if (index > pos):  # 如果当前词/字的索引大于抽取出的问题在问句中的索引，则终止循环
                    break
                index += len(x)
                # print('x1', x[1])
                if (x[1] == 'uw'):
                    # print('是名词', x[0])
                    aim = aim + x[0]
                    # print('aim', aim)
            if (len(aim) > 0):
                ret_dict = get_aim(aim, ret_dict)

        # 匹配问题 xxx的依据是什么
        accord = ''
        if (q_type == 1):
            print('q_type == 1')
            index = 0
            for x in cut_statement:
                if (index > pos):
                    break
                index += len(x)
                if (x[1] == 'uw'):
                    accord = accord + x[0]

            if (len(accord) > 0):
                print('accord > 0')
                ret_dict = get_accord(accord, ret_dict)

        # 匹配问题 xxx是什么
        define = ''
        if (q_type == 2):
            index = 0
            for x in cut_statement:
                if (index > pos):
                    break
                index += len(x)
                if (x[1] == 'uw'):
                    define = define + x[0]
                if (x[1] == 'n' or x[1] == 'id' or x[1] == 'nz' or x[1] == 'ns' or x[1] == 'x'):
                    define = define + x[0]

            if (len(define) > 0):
                ret_dict = get_define(define, ret_dict)

        # 匹配问题 xxx适用于什么范围
        scope = ''
        if (q_type == 3):
            index = 0
            for x in cut_statement:
                if (index > pos):
                    break
                index += len(x)
                if (x[1] == 'uw'):
                    scope = scope + x[0]

            if (len(scope) > 0):
                ret_dict = get_scope(scope, ret_dict)

        # 匹配问题 xxx有什么权利
        right = ''
        if (q_type == 4):
            index = 0
            for x in cut_statement:
                if (index > pos):
                    break
                index += len(x)
                if (x[1] == 'uw'):
                    right = right + x[0]

            if (len(right) > 0):
                ret_dict = get_right(right, ret_dict)

        # 匹配问题 xxx有什么奖励
        award = ''
        if (q_type == 5):
            index = 0
            for x in cut_statement:
                if (index > pos):
                    break
                index += len(x)
                if (x[1] == 'uw'):
                    award = award + x[0]

            if (len(award) > 0):
                ret_dict = get_award(award, ret_dict)

        # 匹配问题 xxx行为有什么处罚/后果
        punishment = ''
        if (q_type == 6):
            index = 0
            for x in cut_statement:
                if (index > pos):
                    break
                index += len(x)
                if (x[1] == 'uw'):
                    punishment = punishment + x[0]

            if (len(punishment) > 0):
                ret_dict = get_punishment(punishment, ret_dict)

        # 匹配问题 xxx包含什么
        classify = ''
        if (q_type == 7):
            index = 0
            for x in cut_statement:
                if (index > pos):
                    break
                index += len(x)
                if (x[1] == 'uw'):
                    classify = classify + x[0]
                if (x[1] == 'n' or x[1] == 'id' or x[1] == 'ns'):
                    classify = classify + x[0]

            if (len(classify) > 0):
                ret_dict = get_classify(classify, ret_dict)

        # 匹配问题 xxx的责任/要求/规定是什么
        duty = ''
        if (q_type == 8):
            index = 0
            for x in cut_statement:
                if (index > pos):
                    break
                index += len(x)
                if (x[1] == 'uw'):
                    duty = duty + x[0]

            if (len(duty) > 0):
                ret_dict = get_duty(duty, ret_dict)

        # 匹配问题 xxx的性质是什么
        nature = ''
        if (q_type == 9):
            index = 0
            for x in cut_statement:
                if (index > pos):
                    break
                index += len(x)
                if (x[1] == 'uw'):
                    nature = nature + x[0]
                if (x[1] == 'n'):
                    nature = nature + x[0]

            if (len(nature) > 0):
                ret_dict = get_nature(nature, ret_dict)

        # 匹配问题 xxx的提出时间是
        propose_time = ''
        if (q_type == 10):
            index = 0
            for x in cut_statement:
                if (index > pos):
                    break
                index += len(x)
                if (x[1] == 'uw'):
                    propose_time = propose_time + x[0]
                if (x[1] == 'id'):
                    propose_time = propose_time + x[0]
                if (x[1] == 'x'):
                    propose_time = propose_time + x[0]
                if (x[1] == 'nz'):
                    propose_time = propose_time + x[0]

            if (len(propose_time) > 0):
                ret_dict = get_propose_time(propose_time, ret_dict)

        # 匹配问题 xxx的发明人者/提出者是
        propose_people = ''
        if (q_type == 11):
            index = 0
            for x in cut_statement:
                if (index > pos):
                    break
                index += len(x)
                if (x[1] == 'uw'):
                    propose_people = propose_people + x[0]
                if (x[1] == 'id'):
                    propose_people = propose_people + x[0]
                if (x[1] == 'x'):
                    propose_people = propose_people + x[0]

            if (len(propose_people) > 0):
                ret_dict = get_propose_people(propose_people, ret_dict)

        # 匹配问题 xxx属于什么领域
        field = ''
        if (q_type == 12):
            index = 0
            for x in cut_statement:
                if (index > pos):
                    break
                index += len(x)
                if (x[1] == 'uw'):
                    field = field + x[0]

            if (len(field) > 0):
                ret_dict = get_field(field, ret_dict)

        # 匹配问题 xxx有什么应用/应用于
        application = ''
        if (q_type == 13):
            index = 0
            for x in cut_statement:
                if (index > pos):
                    break
                index += len(x)
                if (x[1] == 'uw'):
                    application = application + x[0]
                if (x[1] == 'n'):
                    application = application + x[0]

            if (len(application) > 0):
                ret_dict = get_application(application, ret_dict)

        # 匹配问题 xxx有什么优点
        advantage = ''
        if (q_type == 14):
            index = 0
            for x in cut_statement:
                if (index > pos):
                    break
                index += len(x)
                if (x[1] == 'uw'):
                    advantage = advantage + x[0]

            if (len(advantage) > 0):
                ret_dict = get_advantage(advantage, ret_dict)

        # 匹配问题 xxx有什么缺点
        shortcoming = ''
        if (q_type == 15):
            index = 0
            for x in cut_statement:
                if (index > pos):
                    break
                index += len(x)
                if (x[1] == 'uw'):
                    shortcoming = shortcoming + x[0]

            if (len(shortcoming) > 0):
                ret_dict = get_shortcoming(shortcoming, ret_dict)

        # 匹配问题 xxx有什么特点
        feature = ''
        if (q_type == 16):
            index = 0
            for x in cut_statement:
                if (index > pos):
                    break
                index += len(x)
                if (x[1] == 'uw'):
                    feature = feature + x[0]

            if (len(feature) > 0):
                ret_dict = get_feature(feature, ret_dict)

        print('====ret_dict====', ret_dict)

        if (len(ret_dict) != 0 and ret_dict != 0):
            return render(request, 'question_answering.html', {'ret': ret_dict})
        print('====context====', context)
        return render(request, 'question_answering.html', {'ctx': '抱歉，暂未找到答案'})
    return render(request, 'question_answering.html', context)
