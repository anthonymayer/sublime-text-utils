import re

import sublime, sublime_plugin

class PathToClipboardCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.set_clipboard(root_file_path())

class TestifyForCurrentPathToClipboardCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.set_clipboard('testify -d ' + dotted_path() + get_selected_text(self))

class ImportForCurrentPathToClipboardCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.set_clipboard('from ' + dotted_path() + ' import ' + get_selected_text(self))

class DottedPathToClipboardCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selectedText = get_selected_text(self)
		dottedSelectedText = '.' + selectedText if selectedText else ''
		sublime.set_clipboard(dotted_path() + dottedSelectedText)

def root_file_path():
	return sublime.active_window().active_view().file_name().replace(
		sublime.active_window().folders()[0] + '/', ''
	)

def dotted_path():
	return re.sub(r'\.py|\.tmpl', '', root_file_path()).replace('/', '.')

def get_selected_text(sublime_plugin_text_command):
	sel = sublime_plugin_text_command.view.sel()
	return sublime_plugin_text_command.view.substr(sel[0]).strip() if sel else ''