import os.path
import re

import sublime, sublime_plugin

class PathToClipboardCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.set_clipboard(root_file_path())

class TestifyForCurrentPathToClipboardCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.set_clipboard('testify -d ' + dotted_path() + ' ' + get_selected_text(self))

class ImportForCurrentPathToClipboardCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.set_clipboard('from ' + dotted_path() + ' import ' + get_selected_text(self))

class DottedPathToClipboardCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selectedText = get_selected_text(self)
        dottedSelectedText = '.' + selectedText if selectedText else ''
        sublime.set_clipboard(dotted_path() + dottedSelectedText)

class JsTestToClipboardCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        test_name = get_js_test_name()
        suite = re.match('yelp.test.(\w*)', test_name).group(1)
        sublime.set_clipboard('js-tester ' + suite + ' -s ' + test_name)

class JsTestBrowserToClipboardCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        test_name = get_js_test_name()
        sublime.set_clipboard('/js_tester/' + test_name)

def get_js_test_name():
    file_path = sublime.active_window().active_view().file_name()
    if not '.js' in file_path:
        return
    js_file = open(file_path, 'r')
    for line in js_file:
        re_match = re.match('describe\([\'"](.*)[\'"]', line)
        if re_match:
            test_name = re_match.group(1)
            break
    js_file.close()
    return test_name

def root_file_path():
    return sublime.active_window().active_view().file_name().replace(
        sublime.active_window().folders()[0] + os.path.sep, ''
    )

def dotted_path():
    return re.sub(r'\.py|\.tmpl', '', root_file_path()).replace(os.path.sep, '.')

def get_selected_text(sublime_plugin_text_command):
    sel = sublime_plugin_text_command.view.sel()
    return sublime_plugin_text_command.view.substr(sel[0]).strip() if sel else ''