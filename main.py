#-*- coding: shiftjis -*-
"""
Kivy�A�v���T���v��
https://qiita.com/dario_okazaki/items/7892b24fcfa787faface
"""

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty, ListProperty

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

import japanize_kivy

import threading
import time

# �f�t�H���g�Ɏg�p����t�H���g��ύX����
#resource_add_path('./fonts')
#LabelBase.register(DEFAULT_FONT, 'mplus-2c-regular.ttf') #���{�ꂪ�g�p�ł���悤�ɓ��{��t�H���g���w�肷��


class TextWidget(Widget):
    """�E�B�W�F�b�g
    """
    #�E�B���h�E��̓��I�ϐ�
    text  = StringProperty()
    color = ListProperty([1,1,1,1])
    #�X���b�h�p
    t = None

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = 'start'
        # �X���b�h�����s
        self.t = ThreadJob()
        self.t.daemon = True
        self.t.start()

    def buttonClicked(self):
        self.text = '���͂悤'
        self.color = [1, 0, 0 , 1]
        self.t.line = "OHAYOU"

    def buttonClicked2(self):
        self.text = '����ɂ���'
        self.color = [0, 1, 0 , 1 ]
        self.t.line = "KON_NICHIWA"

    def buttonClicked3(self):
        self.text = '����΂��'
        self.color = [0, 0, 1 , 1 ]
        self.t.line = "KON_BANWA"
        self.t.kill_flag = True

class TestApp(App):
    """�A�v���{��
    """
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = '���A'

class ThreadJob(threading.Thread):
    """�X���b�h��
    �Q�l:https://qiita.com/sky_jokerxx/items/0fbd6c3a6e17fb77d343
    """
    def __init__(self, v=""):
        """������
        """
        threading.Thread.__init__(self)
        #�\���������������
        self.line = v
        #�X���b�h��~�t���O
        self.kill_flag = False

    def run(self):
        """������
        """
        old = ""
        count = 0
        #�����̃t���O��Ԃ�\��
        print("\nthread start: {}".format(self.kill_flag))
        while not(self.kill_flag):
            if(self.line and self.line != old):
                #�O��Ƃ͈قȂ镶���̎������\��������i�߂�
                print("\nthread: {}".format(self.line))
                old = self.line
            if(count % 1000000 == 0):
                #�X���b�h���쒆���h�b�g�ŕ\��
                #��������̂�N��ɂP�񂾂��\���Ƃ���
                print(".", end="")
            count += 1
        #�I�����̃t���O��Ԃ�\��
        print("\nthread end: {}".format(self.kill_flag))


if __name__ == '__main__':

    try:
        TestApp().run()
    except(KeyboardInterrupt):
        pass
    finally:
        pass
