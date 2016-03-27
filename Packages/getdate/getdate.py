import sublime, sublime_plugin
import time

# 将文件中的yyyy-mm-dd替换为当前时间，并且将当前时间字符串显示在状态栏和剪贴板
# --胡祀鹏

class GetdateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        t = time.strftime('%Y-%m-%d',time.localtime(time.time()));
        sublime.status_message(t)                                       # 将时间显示在状态栏，显示一段时间后自动消失
        sublime.set_clipboard(t)                                        # 将当前时间放入剪贴板，可用于粘贴(ctrl+v)
        # 第一种方法
        # reg = sublime.Region(0, self.view.size())                       # 获取当前文件全部区域
        # text = self.view.substr(reg)                                    # 获取指定区域的文本
        # text = text.replace('yyyy-mm-dd',t)                             # 把text中yyyy-mm-dd替换为当前时间t
        # self.view.erase(edit,reg)                                       # 清除指定区域的文本
        # self.view.insert(edit,0,text)                                   # 将text插入本文档
        # 另一种方法，更简便
        reg = self.view.find("yyyy-mm-dd",0,sublime.IGNORECASE)
        self.view.replace(edit,reg,t)
