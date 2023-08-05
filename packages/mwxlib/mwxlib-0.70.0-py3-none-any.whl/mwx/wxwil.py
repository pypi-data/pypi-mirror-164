#! python3
# -*- coding: utf-8 -*-
"""Local info list tool

Author: Kazuya O'moto <komoto@jeol.co.jp>
"""
import wx
from wx.py import dispatcher
from wx.lib.mixins.listctrl import ListCtrlAutoWidthMixin
try:
    from framework import CtrlInterface, Menu
    from controls import Icon, Clipboard
except ImportError:
    from .framework import CtrlInterface, Menu
    from .controls import Icon, Clipboard


class LocalsWatcher(wx.ListCtrl, ListCtrlAutoWidthMixin, CtrlInterface):
    """Locals info watcher
    
    Attributes:
        parent : shellframe
        target : locals:dict to watch
    """
    def __init__(self, parent, **kwargs):
        wx.ListCtrl.__init__(self, parent,
                          style=wx.LC_REPORT|wx.LC_HRULES, **kwargs)
        ListCtrlAutoWidthMixin.__init__(self)
        CtrlInterface.__init__(self)
        
        self.parent = parent
        self.target = {}
        
        self.__dir = True # sort direction
        self.__items = [] # list of data:str
        
        self.alist = (
            ("key", 140),
            ("value", 0),
        )
        for k, (header, w) in enumerate(self.alist):
            self.InsertColumn(k, header, width=w)
        
        self.Bind(wx.EVT_LIST_COL_CLICK, self.OnSortItems)
        self.Bind(wx.EVT_CONTEXT_MENU, self.OnContextMenu)
        
        dispatcher.connect(receiver=self._update, signal='Interpreter.push')
    
    def _update(self, *args, **kwargs):
        if not self:
            dispatcher.disconnect(receiver=self._update, signal='Interpreter.push')
            return
        self.update(self.target)
    
    def watch(self, locals):
        self.clear()
        if not isinstance(locals, dict):
            ## wx.MessageBox("Cannot watch the locals.\n\n"
            ##               "- {!r} is not a dict object.".format(locals))
            return
        self.target = locals
        self.update(self.target)
    
    def unwatch(self):
        self.target = None
    
    def clear(self):
        self.DeleteAllItems()
        del self.__items[:]
    
    def update(self, attr):
        if not attr:
            return
        data = self.__items
        n = len(data)
        for i, (k, v) in enumerate(data[::-1]):
            if k not in attr:
                j = n-i-1
                self.DeleteItem(j)
                del data[j]
        
        for key, value in attr.items():
            vstr = repr(value)
            i = next((i for i, item in enumerate(data)
                                    if item[0] == key), None)
            if i is not None:
                if data[i][1] == vstr:
                    continue
                data[i][1] = vstr # Update data to locals
            else:
                i = len(data)
                item = [key, vstr]
                data.append(item)
                self.InsertItem(i, key)
            self.SetItem(i, 1, vstr)
            self.blink(i)
            self.EnsureVisible(i)
    
    def blink(self, i):
        if self.GetItemBackgroundColour(i) != wx.Colour('yellow'):
            self.SetItemBackgroundColour(i, "yellow")
            def reset_color():
                if self and i < self.ItemCount:
                    self.SetItemBackgroundColour(i, 'white')
            wx.CallAfter(wx.CallLater, 1000, reset_color)
    
    def OnSortItems(self, evt): #<wx._controls.ListEvent>
        n = self.ItemCount
        if n < 2:
            return
        
        def _getitem(key):
            return [data[i] for i in range(n) if key(i)]
        
        data = self.__items
        ls = _getitem(self.IsSelected)
        f = data[self.FocusedItem]
        
        col = evt.Column
        self.__dir = not self.__dir
        data.sort(key=lambda v: v[col].upper(), reverse=self.__dir)
        
        for i, item in enumerate(data):
            for j, v in enumerate(item):
                self.SetItem(i, j, v)
            self.Select(i, item in ls)
            if item == f:
                self.Focus(i)
    
    def OnContextMenu(self, evt):
        def copy():
            def _T(i):
                return '\t'.join(self.__items[i])
            Clipboard.write('\n'.join(_T(i) for i in selected_items))
        
        selected_items = list(filter(self.IsSelected, range(self.ItemCount)))
        menu = [
            (1, "Copy data", Icon('copy'),
                lambda v: copy(),
                lambda v: v.Enable(selected_items != [])),
        ]
        Menu.Popup(self, menu)


if __name__ == "__main__":
    from framework import Frame
    
    app = wx.App()
    frm = Frame(None)
    frm.plug = LocalsWatcher(frm)
    frm.plug.watch(vars(frm))
    frm.Show()
    app.MainLoop()
