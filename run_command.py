import sublime
import sublime_plugin

class RunShell(sublime_plugin.WindowCommand):
  def run(self):
    self.window.show_input_panel("sh", "", lambda s: self.generate(s), None, None)

  def generate(self, argument):
    self.window.run_command("ruby_run_shell", { "command": argument, "caption": "Running:  " + argument } )
