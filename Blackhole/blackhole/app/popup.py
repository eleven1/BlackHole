# -*- coding: utf-8 -*-
import urwid


class PopUpDialog(urwid.WidgetWrap):
    """A dialog that appears with nothing but a close button """
    signals = ['close']

    def __init__(self, message):
        close_button = urwid.Button(u"OK")
        urwid.connect_signal(close_button, 'click',
            lambda button: self._emit("close"))
        pile = urwid.Pile([urwid.Text(message, align='center'),
                           urwid.Padding(close_button, align='center', left=13, right=13)])
        fill = urwid.Filler(pile)
        self.__super.__init__(urwid.AttrMap(urwid.LineBox(fill), 'popup'))


class PopUpNotificationLauncher(urwid.PopUpLauncher):
    def __init__(self):
        self.__super.__init__(urwid.Text(u"", align='right'))
        self._message = None

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    def create_pop_up(self):
        pop_up = PopUpDialog(self._message)
        urwid.connect_signal(pop_up, 'close',
            lambda button: self.close_pop_up())
        return pop_up

    def get_pop_up_parameters(self):
        return {'left': 1, 'top': 1, 'overlay_width': 35, 'overlay_height': 7}

    def show_indicator(self, message):
        self.original_widget.set_text(message)