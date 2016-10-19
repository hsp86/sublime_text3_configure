import sublime, sublime_plugin # 插件主程序必须要引用这两个基础类库

# 这里实现了一个简单修改剪贴板内容的插件

"""
   每个菜单命令都对应于一个类。注意类名的写法，是把菜单命令的下划线去掉，改成驼峰式写法，并且在末尾加上Command。
    括号中 sublime_plugin.TextCommand 是此类的父类，表示此类是一个命令菜单的实际行为类。
    如果是象在 Package Control 提供的操作面板中通过点击面板产生的命令，就要用 sublime_plugin.WindowCommand 作为父类，表示是窗口命令类。
    可以在控制台（ctrl+`）使用view.run_command('hsp')来运行查看命令效果（注意class中为驼峰式而运行时用下划线分割）
"""
class hspCommand(sublime_plugin.TextCommand):
    def run(self, edit):                                                #  ST插件机制会自动调用指令类的run方法，所以必须重载实现此方法以供执行
        s = sublime.get_clipboard()                                     #  获取剪切板内容
        line_ending = sublime.platform()                                #  从ST文件视图配置中读取默认行结束符的类别（用操作系统表示:'windows','mac',unix / system）
        s = line_ending + s
        sublime.set_clipboard(s)                                        #  修改剪贴板内容，此方法可使剪贴过的剪贴板内容在别处也能使用
        sublime.status_message("测试插件--胡祀鹏")                      #  设置状态栏信息
        sublime.message_dialog("欢迎使用--胡祀鹏")                      #  显示消息框
