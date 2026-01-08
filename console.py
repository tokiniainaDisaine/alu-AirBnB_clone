#!/usr/bin/python3
"""
doc: to fill later
"""
import cmd


class MyCommand(cmd.Cmd):
    """
    doc: to fill later
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        :param arg:
        :return: nothing
        """

        print('Quitting...')
        return True

    do_exit = do_quit
    do_EOF = do_quit


if __name__ == "__main__":
    MyCommand().cmdloop()
