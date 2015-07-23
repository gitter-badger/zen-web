# -*- coding: utf-8 -*-
#
# Licensed Materials - Property of esse.io
# 
# (C) Copyright esse.io. 2015 All Rights Reserved
#
# Author: Bryan HUANG (bryan@esse.io)
#
#


from zensite.widgets.link import *


def create_sidebar_items(frame):
    sidebar = frame.get_sidebar()
    # TODO: search sub folders for sidebar items recursively, need create a structure.
    
    eldm_tree = TreeView()
    eldm_tree.set_title(TreeTitle(u"决策支持系统"))
    eldm_tree_menu = TreeViewMenu()
    eldm_tree.set_treeview_menu(eldm_tree_menu)
    sidebar.append_menuitem(eldm_tree)

    ws_tree = TreeView()
    eldm_tree_menu.append_linkitem(ws_tree)
    ws_tree.set_title(TreeTitle(u"网站概况"))
    ws_tree_menu = TreeViewMenu()
    ws_tree.set_treeview_menu(ws_tree_menu)

    for i in [u'运营日报',u'运营周报',u'运营月报']:
        item = LinkItem("")
        item.set_href("#")
        item.set_icon("fa fa-circle-o")
        item.set_span("", i)
        ws_tree_menu.append_linkitem(item)

    ws_tree = TreeView()
    eldm_tree_menu.append_linkitem(ws_tree)
    ws_tree.set_title(TreeTitle(u"老用户"))
    ws_tree_menu = TreeViewMenu()
    ws_tree.set_treeview_menu(ws_tree_menu)

    for i in [u'用户角色分析',u'登录途径分析',u'用户活跃度分析',u'用户属性分析',u'用户细分分析']:
        item = LinkItem("")
        item.set_href("#")
        item.set_icon("fa fa-circle-o")
        item.set_span("", i)
        ws_tree_menu.append_linkitem(item)

    ws_tree = TreeView()
    eldm_tree_menu.append_linkitem(ws_tree)
    ws_tree.set_title(TreeTitle(u"新用户"))
    ws_tree_menu = TreeViewMenu()
    ws_tree.set_treeview_menu(ws_tree_menu)

    for i in [u'注册方式分析',u'用户来源分析',u'用户存留分析',u'充值转化分析',u'投资转化分析']:
        item = LinkItem("")
        item.set_href("#")
        item.set_icon("fa fa-circle-o")
        item.set_span("", i)
        ws_tree_menu.append_linkitem(item)

    ws_tree = TreeView()
    eldm_tree_menu.append_linkitem(ws_tree)
    ws_tree.set_title(TreeTitle(u"借款分析"))
    ws_tree_menu = TreeViewMenu()
    ws_tree.set_treeview_menu(ws_tree_menu)

    for i in [u'借款申请统计',u'借款审批统计',u'发布借款分析',u'借款流程分析',u'投资转化分析']:
        item = LinkItem("")
        item.set_href("#")
        item.set_icon("fa fa-circle-o")
        item.set_span("", i)
        ws_tree_menu.append_linkitem(item)

    ws_tree = TreeView()
    eldm_tree_menu.append_linkitem(ws_tree)
    ws_tree.set_title(TreeTitle(u"还款分析"))
    ws_tree_menu = TreeViewMenu()
    ws_tree.set_treeview_menu(ws_tree_menu)

    for i in [u'累计还款分析',u'借款人应还款分析',u'借款人还款分析',u'借款人逾期还款分析',u'翼存宝还款分析']:
        item = LinkItem("")
        item.set_href("#")
        item.set_icon("fa fa-circle-o")
        item.set_span("", i)
        ws_tree_menu.append_linkitem(item)

    ws_tree = TreeView()
    eldm_tree_menu.append_linkitem(ws_tree)
    ws_tree.set_title(TreeTitle(u"投资分析"))
    ws_tree_menu = TreeViewMenu()
    ws_tree.set_treeview_menu(ws_tree_menu)

    for i in [u'散标投资',u'翼存宝',u'翼存宝各期详情',u'新手专区',u'翼星计划']:
        item = LinkItem("")
        item.set_href("#")
        item.set_icon("fa fa-circle-o")
        item.set_span("", i)
        ws_tree_menu.append_linkitem(item)

    ws_tree = TreeView()
    eldm_tree_menu.append_linkitem(ws_tree)
    ws_tree.set_title(TreeTitle(u"债权转让"))
    ws_tree_menu = TreeViewMenu()
    ws_tree.set_treeview_menu(ws_tree_menu)

    for i in [u'债权转让']:
        item = LinkItem("")
        item.set_href("#")
        item.set_icon("fa fa-circle-o")
        item.set_span("", i)
        ws_tree_menu.append_linkitem(item)

    ws_tree = TreeView()
    eldm_tree_menu.append_linkitem(ws_tree)
    ws_tree.set_title(TreeTitle(u"风险分析"))
    ws_tree_menu = TreeViewMenu()
    ws_tree.set_treeview_menu(ws_tree_menu)

    for i in [u'风险分析']:
        item = LinkItem("")
        item.set_href("#")
        item.set_icon("fa fa-circle-o")
        item.set_span("", i)
        ws_tree_menu.append_linkitem(item)

    ws_tree = TreeView()
    eldm_tree_menu.append_linkitem(ws_tree)
    ws_tree.set_title(TreeTitle(u"加盟商分析"))
    ws_tree_menu = TreeViewMenu()
    ws_tree.set_treeview_menu(ws_tree_menu)

    for i in [u'地区排行榜',u'业绩排名',u'分布详情',u'业绩详情',u'业绩预测']:
        item = LinkItem("")
        item.set_href("#")
        item.set_icon("fa fa-circle-o")
        item.set_span("", i)
        ws_tree_menu.append_linkitem(item)

    ws_tree = TreeView()
    eldm_tree_menu.append_linkitem(ws_tree)
    ws_tree.set_title(TreeTitle(u"财务分析"))
    ws_tree_menu = TreeViewMenu()
    ws_tree.set_treeview_menu(ws_tree_menu)

    for i in [u'投资人提现情况',u'红包分析',u'财务分析',u'资金流动分析']:
        item = LinkItem("")
        item.set_href("#")
        item.set_icon("fa fa-circle-o")
        item.set_span("", i)
        ws_tree_menu.append_linkitem(item)


    ws_tree = TreeView()
    eldm_tree_menu.append_linkitem(ws_tree)
    ws_tree.set_title(TreeTitle(u"资金流动分析"))
    ws_tree_menu = TreeViewMenu()
    ws_tree.set_treeview_menu(ws_tree_menu)

    for i in [u'充值分析',u'提现分析',u'充值行为分析',u'提现行为分析',u'充值提现分析']:
        item = LinkItem("")
        item.set_href("#")
        item.set_icon("fa fa-circle-o")
        item.set_span("", i)
        ws_tree_menu.append_linkitem(item)
