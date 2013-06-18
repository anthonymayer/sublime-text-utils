import sublime, sublime_plugin

class PathToClipboardCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.set_clipboard(root_file_path())

class TestifyForCurrentPathToClipboardCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.set_clipboard('testify ' + root_file_path().replace('.py', '').replace('/', '.'))

def root_file_path():
	return sublime.active_window().active_view().file_name().replace(
		sublime.active_window().folders()[0] + '/', ''
	)