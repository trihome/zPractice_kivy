#-*- coding: shiftjis -*-
"""
Kivyアプリサンプル
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

# デフォルトに使用するフォントを変更する
#resource_add_path('./fonts')
#LabelBase.register(DEFAULT_FONT, 'mplus-2c-regular.ttf') #日本語が使用できるように日本語フォントを指定する


class TextWidget(Widget):
    """ウィジェット
    """
    #ウィンドウ上の動的変数
    text  = StringProperty()
    color = ListProperty([1,1,1,1])
    #スレッド用
    t = None

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = 'start'
        # スレッドを実行
        self.t = ThreadJob()
        self.t.daemon = True
        self.t.start()

    def buttonClicked(self):
        self.text = 'おはよう'
        self.color = [1, 0, 0 , 1]
        self.t.line = "OHAYOU"

    def buttonClicked2(self):
        self.text = 'こんにちは'
        self.color = [0, 1, 0 , 1 ]
        self.t.line = "KON_NICHIWA"

    def buttonClicked3(self):
        self.text = 'こんばんは'
        self.color = [0, 0, 1 , 1 ]
        self.t.line = "KON_BANWA"
        self.t.kill_flag = True

class TestApp(App):
    """アプリ本体
    """
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = '挨拶'

class ThreadJob(threading.Thread):
    """スレッド部
    参考:https://qiita.com/sky_jokerxx/items/0fbd6c3a6e17fb77d343
    """
    def __init__(self, v=""):
        """初期化
        """
        threading.Thread.__init__(self)
        #表示文字列を初期化
        self.line = v
        #スレッド停止フラグ
        self.kill_flag = False

    def run(self):
        """実装部
        """
        old = ""
        count = 0
        #初期のフラグ状態を表示
        print("\nthread start: {}".format(self.kill_flag))
        while not(self.kill_flag):
            if(self.line and self.line != old):
                #前回とは異なる文字の時だけ表示処理を進める
                print("\nthread: {}".format(self.line))
                old = self.line
            if(count % 1000000 == 0):
                #スレッド動作中をドットで表示
                #早すぎるのでN回に１回だけ表示とする
                print(".", end="")
            count += 1
        #終了時のフラグ状態を表示
        print("\nthread end: {}".format(self.kill_flag))


if __name__ == '__main__':

    try:
        TestApp().run()
    except(KeyboardInterrupt):
        pass
    finally:
        pass
