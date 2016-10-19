import sublime, sublime_plugin
import time

# 胡祀鹏 设计制作

class GetdateCommand(sublime_plugin.TextCommand):
    '''将文件中的yyyy-mm-dd替换为当前时间，并且将当前时间字符串显示在状态栏和剪贴板'''
    def run(self, edit):
        t = time.strftime('%Y-%m-%d',time.localtime(time.time()));
        sublime.status_message(t)                                       # 将时间显示在状态栏，显示一段时间后自动消失
        sublime.set_clipboard(t)                                        # 将当前时间放入剪贴板，可用于粘贴(ctrl+v)
        date_str = "yyyy-mm-dd"
        # 第一种方法
        # reg = sublime.Region(0, self.view.size())                       # 获取当前文件全部区域
        # text = self.view.substr(reg)                                    # 获取指定区域的文本
        # text = text.replace(date_str,t)                                 # 把text中yyyy-mm-dd替换为当前时间t
        # self.view.erase(edit,reg)                                       # 清除指定区域的文本
        # self.view.insert(edit,0,text)                                   # 将text插入本文档

        # 另一种方法，更简便
        reg = self.view.find(date_str,0,sublime.IGNORECASE)
        if reg != None:                                                 # 不加这个条件也不会出错，最好加上
            self.view.replace(edit,reg,t)

        # 以下为将“module 模块名.v”替换为“module 模块名”，如果存在；用于配合verilog的module snippet
        file_full_name = self.view.file_name()                          # 这个文件名包括路径
        last_index = file_full_name.rfind('\\')                         # 得到最后一个\的位置
        file_name = file_full_name[last_index+1:]                       # 取得最后的文件名，不包括路径
        module_str = 'module '+ file_name
        reg = self.view.find(module_str,0,sublime.IGNORECASE)
        if reg != None:                                                 # 如果存在这个字符串
            self.view.replace(edit,reg,module_str[:-2])                 # 去掉后缀.v并插入

class CommentBackCommand(sublime_plugin.TextCommand):
    '''本命令在光标行（支持多行）在对齐rulers（默认值72）处添加注释
    测试命令：view.run_command('comment_back')'''
    def run(self, edit):
        comment_str = "//  "                                            # 注释字符
        if self.view.file_name()[-3:] == ".py":                         # 若为python更改注释字符
            comment_str = "# "
        pos = self.view.settings().get("rulers",[72])[0]                # 获取到设置中rulers的值，没有设定时默认为72
        for region in self.view.sel():                                  # 支持多行
            if region.empty():
                line = self.view.line(region)
                while len(line) < pos:
                    self.view.insert(edit, line.end(), ' ')             # 没有达到rulers处就一直在行末添加空格
                    line = self.view.line(region)
            self.view.insert(edit, line.end(), comment_str)
    def is_visible(self):
        return self.view.file_name() is not None and (
            self.view.file_name()[-2:] in [".v",".c"] or
            self.view.file_name()[-3:] in [".sv",".py"])                # 只有这些文件时才可用
