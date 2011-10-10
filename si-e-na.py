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
	
	treestore_open_files = None
	treeview_open_files = None
	textbuffer_details = None
	textview_details = None
	filechooserdialog_add_files = None
		
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
		
		# INITIALIZE LEFT PANE: OPEN FILES TREESTORE
		self.treestore_open_files = gtk.TreeStore(gobject.TYPE_INT, gobject.TYPE_STRING, gobject.TYPE_STRING)
		
		self.treeview_open_files = gtk.TreeView(model=self.treestore_open_files)
		self.treeview_open_files.show()
		
		cellrendtext = gtk.CellRendererText()
		treeviewcol0 = gtk.TreeViewColumn('id', cellrendtext, text=0) #, foreground=3) #la colonna 3 contiene il colore
		treeviewcol1 = gtk.TreeViewColumn('name', cellrendtext, text=1) #, foreground=3) #la colonna 3 contiene il colore
		treeviewcol2 = gtk.TreeViewColumn('path', cellrendtext, text=2) #, foreground=3) #la colonna 3 contiene il colore
		
		self.treeview_open_files.append_column(treeviewcol0)
		self.treeview_open_files.append_column(treeviewcol1)
		self.treeview_open_files.append_column(treeviewcol2)
		
		scrolledwindow_open_files = self.builder.get_object('scrolledwindow_open_files')
		scrolledwindow_open_files.add(self.treeview_open_files)
		
		# INITIALIZE RIGHT PANE: DETAILSTEXTVIEW
		self.textbuffer_details = gtk.TextBuffer()
		self.textbuffer_details.set_text("")
		self.textview_details = gtk.TextView(self.textbuffer_details)
		self.textview_details.set_editable(False)
		self.textview_details.show()
		
		scrolledwindow_details = self.builder.get_object('scrolledwindow_details')
		scrolledwindow_details.add(self.textview_details)
		
		##############
		##SAMPLE FILLING
		#treestore_open_files.append(parent=None,row=(0,"prova0","aaa"))
		#treestore_open_files.append(parent=None,row=(0,"prova1","aaa"))
		#i = treestore_open_files.append(parent=None,row=(0,"prova2","aaa"))
		#i = treestore_open_files.append(parent=i,row=(0,"prova2","aaa"))
		
		self.textbuffer_details.set_text("----------")
	
	def on_toolbutton_add_clicked(self, widget, data=None):
		print "on_toolbutton_add_clicked"
		self.filechooserdialog_add_files = gtk.FileChooserDialog(title=None, parent=None, action=gtk.FILE_CHOOSER_ACTION_OPEN, buttons=(gtk.STOCK_OK, gtk.RESPONSE_ACCEPT, gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT), backend=None)
		self.filechooserdialog_add_files.set_property("select-multiple", True)
		self.filechooserdialog_add_files.show()
		self.filechooserdialog_add_files.connect('response', self.on_filechooserdialog_add_files_response)
		
	def on_filechooserdialog_add_files_response(self, widget, data=None):
		print "on_filechooserdialog_add_files_response"
		if (data==gtk.RESPONSE_ACCEPT):
			self.filechooserdialog_add_files.hide()
			files_to_add = self.filechooserdialog_add_files.get_filenames()
			print "FILES TO ADD: %s" % files_to_add
			for file_to_add in files_to_add:
				self.add_file(file_to_add)
		else:
			self.filechooserdialog_add_files.hide()	
	
	def on_toolbutton_delete_clicked(self, widget, data=None):
		print "on_toolbutton_delete_clicked"
		
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

	def add_file(self, filename):
		print "ADD FILE FUNCTION %s" % filename
		self.treestore_open_files.append(parent=None,row=(0, filename, filename))

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

