import sublime, sublime_plugin

class PathToClipboardCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.set_clipboard(
			sublime.active_window().active_view().file_name().replace(
				sublime.active_window().folders()[0] + '/', ''
			)
		)