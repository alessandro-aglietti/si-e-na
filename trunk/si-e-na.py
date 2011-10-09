#!/usr/bin/python
#Si.E.Na Signature Extractor and Navigator
import pygtk
pygtk.require('2.0')
import glib #qw{ TRUE FALSE }
import gtk
import gobject
import os
import re

class Siena(object):
	builder = None
	window_main = None
	
	def __init__(self):
		self.builder = gtk.Builder()
		self.builder.add_from_file( 'si-e-na.glade' )
		#self.builder.add_from_string( gtkbuilderui_xml )
		self.window_main = self.builder.get_object( 'window_main' )
		self.builder.connect_signals( self )
		self.initialize()
		self.window_main.show()
	
	def initialize(self):
		self.window_main.show()
		
	def on_imagemenuitem_about_activate(self, widget, data=None):
		about_dialog = gtk.AboutDialog()
		about_dialog.set_version("0.1.0")
		about_dialog.set_name("Si.E.Na.")
		about_dialog.set_license("testo della licenza")
		about_dialog.set_copyright("ccccccccc")
		about_dialog.set_comments("jjdf jdfkjshdfh sdhhf jsd fgs fgfsf")
		about_dialog.set_website("http://code.google.com/siena")
		about_dialog.show()
		about_dialog.connect('response', self.on_aboutdialog_response)
		
	def on_aboutdialog_response(self, widget, data=None):
		widget.destroy()
		
	def on_imagemenuitem_quit_activate(self, widget, data=None):
		self.on_window_main_destroy(self.window_main, data)
		
	def on_window_main_destroy(self, widget, data=None):
		print "EXITING"
		gtk.main_quit()




	#######################################################################################################
	def testMessageDialog(self):
		print "OK%d" %  gtk.RESPONSE_OK
		print "CANCEL%d" %  gtk.RESPONSE_CANCEL
		print "YES%d" %  gtk.RESPONSE_YES
		print "NO%d" %  gtk.RESPONSE_NO
		print "CLOSE%d" %  gtk.RESPONSE_CLOSE
		#dialog_test1 = gtk.MessageDialog(parent=self.window, flags=0, type=gtk.MESSAGE_INFO, buttons=gtk.BUTTONS_OK_CANCEL, message_format="messaggio")
		#dialog_test1.show()
		#dialog_test1.connect('response', self.on_message_dialog_response)
		#gtk.signal_connect()
		###dialog_test1.connect("response", self.on_siena_window_destroy)
		#resp = dialog_test1.run();
		#print "aaaaa%d" % resp
		#dialog_test1.hide()
		#dialog_test1a = gtk.MessageDialog(parent=self.window, flags=0, type=gtk.MESSAGE_INFO, buttons=gtk.BUTTONS_OK, message_format="aaaaaaa").show()
		#
		#dialog_test2 = gtk.MessageDialog(parent=self.window, flags=0, type=gtk.MESSAGE_INFO, buttons=gtk.BUTTONS_NONE, message_format="aaaaaaa")
		#dialog_test2.format_secondary_text("ccccccccc")
		#dialog_test2.set_property('secondary-text',"ggggg")
		#dialog_test2.set_property('title',"kkkk")
		##dialog_test2.set_title("kakkk")		
		#dialog_test2.show()
	#def on_message_dialog_response(self, widget, data=None):
	#	print "<<<<<<<%d<<<<<" % data
	#	if (data == gtk.RESPONSE_OK):
	#		print "OK"
	#	if (data == gtk.RESPONSE_CANCEL):
	#		print "CANCEL"
	#	widget.hide()
	
	def dummy(self, widget, data=None):
		print "---------"
		#ESEMPI VARI
		#POWER_PROFILES = {'LOW':"low", 'MID':"mid", 'HIGH':"high", 'AUTO':"auto", 'DEFAULT':"default"}
		#self.builder.get_object('radiobutton_method_' + current_method).set_active(True)
		#self.builder.get_object('radiobutton_profile_' + current_profile).set_active(True)
			
		#def update_title():
		#	info = self.get_info()
		#	self.window.set_title("%s (%s, mem: %s, %s)" % (self.WINDOW_TITLE_PREFIX, info['engine'], info['memory'], info['voltage']))
		#	return 1  # return 0 or 1 to kill/keep timer going
		#
		#id = glib.timeout_add(500, update_title)
	
		#radio_method_profile = self.builder.get_object('radiobutton_method_profile')
		#radio_auto = self.builder.get_object('radiobutton_profile_auto')
		#radio_low = self.builder.get_object('radiobutton_profile_low')
		#radio_mid = self.builder.get_object('radiobutton_profile_mid')
		#radio_high = self.builder.get_object('radiobutton_profile_high')
		#radio_default = self.builder.get_object('radiobutton_profile_default')
	
		#if (radio_auto.get_active()):
		#	profile = self.POWER_PROFILES['AUTO']
		#elif (radio_low.get_active()):
		#	profile = self.POWER_PROFILES['LOW']
		#elif (radio_mid.get_active()):
		#	profile = self.POWER_PROFILES['MID']
		#elif (radio_high.get_active()):
		#	profile = self.POWER_PROFILES['HIGH']
	
		#if (os.access(self.POWER_METHOD_FILE_PATH, os.R_OK)):
		#	return True
		#else:
		#	return False
		#
		#if (os.access(self.POWER_METHOD_FILE_PATH, os.W_OK)):
		#	return False
		#else:
		#	return True
		#
		#fileMethod = open(self.POWER_METHOD_FILE_PATH,"rt")
		#method = fileMethod.readline()
		#fileMethod.close()
		#return method.strip()
		#
		#fileProfile = open(self.POWER_PROFILE_FILE_PATH,"rt")
		#profile = fileProfile.readline()
		#fileProfile.close()
		#return profile.strip()
		#
		#fileMethod = open(self.POWER_METHOD_FILE_PATH,"wt")
		#fileMethod.write(method)
		#fileMethod.close()
		#
		#fileProfile = open(self.POWER_PROFILE_FILE_PATH,"wt")
		#fileProfile.write(profile)
		#fileProfile.close()
		#
		#if (os.path.exists(self.INFO_FILE_PATH)):
		#	file_info = open (self.INFO_FILE_PATH, "rt")
		#	while (True):
		#		line = file_info.readline();
		#		if (line == ""): break #stops at the end of the file
		#
		#		match = re.search("current engine clock: (.*)",line) 
		#		if (match):
		#			engine_clock = match.group(1).strip()
		#
		#		match = re.search("current memory clock: (.*)", line)
		#		if (match):
		#			memory_clock = match.group(1).strip()
		#
		#		match = re.search("voltage: (.*)", line)
		#		if (match):
		#			voltage = match.group(1).strip()

if __name__ == "__main__":
	app = Siena()
	gtk.main()

