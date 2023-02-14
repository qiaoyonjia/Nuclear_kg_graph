# from django.conf.urls import url
from django.urls import include, re_path
from . import index_view, index_ERform_view, detail_view
from . import tagging_data_view, tagging_data_writefile_view
from . import _404_view, overview_view
from . import relation_view
from . import tagging
from . import question_answering, decisions_making
from . import completion
from . import template

urlpatterns = [
    re_path(r'^$', index_view.index),
    re_path(r'^ER-post', index_ERform_view.ER_post),
    re_path(r'^detail', detail_view.showdetail),
    re_path(r'^tagging_data', tagging_data_view.showtagging_data),
    re_path(r'^tagging-get', tagging_data_writefile_view.tagging_push),
    re_path(r'^overview', overview_view.show_overview),
    re_path(r'^404', _404_view._404_),
    re_path(r'^search_entity', relation_view.search_entity),
    re_path(r'^tagging', tagging.tagging),
    re_path(r'^search_relation', relation_view.search_relation),
    re_path(r'^qa', question_answering.question_answering),
    re_path(r'^decision', decisions_making.decisions_making),
    re_path(r'^completion', completion.test),
    re_path(r'^template', template.test)
]
