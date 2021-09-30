import time
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

try:
    from config import *
except:
    print("\033[31mCorrupted config.py file")
    print("\033[0m")


class Window(Gtk.Window):
    def __init__(self):
        super().__init__(title="Screen time")
        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        header = Gtk.HeaderBar(title="Screen time")
        header.props.show_close_button = True

        if working_hours < 60:
            self.time_w = "minutes"

        if time_relax < 60:
            self.time_r = "minutes"

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)
        self.label = Gtk.Label()
        self.label.set_markup(f"<b>You have been sitting at the computer for {working_hours} {self.time_w}.\n" 
                              f"\t\tI advise you to rest for {time_relax} {self.time_r}</b>"
        )
        
        vbox.pack_start(self.label, True, True, 0)

        self.quit = Gtk.Button(label="Quit")
        self.quit.connect("clicked", self.on_quit_cliked)
        vbox.pack_start(self.quit, True, True, 0)

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)
        vbox.pack_start(stack_switcher, True, True, 0)
        vbox.pack_start(stack, True, True, 0)

        

        
    def on_quit_cliked(self, button):
        Gtk.main_quit()
        exit(0)

class Screen_time():
    def __init__(self):
        # преобразование минут в секунды
        if working_hours >= 1:
            self.working_hours = round(60 * int(working_hours) + (working_hours - int(working_hours)) * 100)
        else:
            self.working_hours = working_hours * 100

        if time_relax >= 1:
            self.time_relax = round(60 * int(time_relax) + (time_relax - int(time_relax)) * 100)
        else:
            self.time_relax = time_relax * 100
        
    def main(self):
        time.sleep(self.working_hours)
        print('\a')
        win = Window()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()
        

        while 1:
            time.sleep(self.working_hours + self.time_relax)
            print('\a')
            win = Window()
            win.connect("destroy", Gtk.main_quit)
            win.show_all()
            Gtk.main()



window = Screen_time()
window.main()







