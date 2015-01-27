#!/usr/bin/env python

import cgi

print "Content-Type: text/html\r\n"
print "\r\n"
print """
<!doctype html>
<html>
<head>
	<title>Page1</title>
</head>
<body>
"""

form_data = cgi.FieldStorage()

if "birthdate" in form_data and "main hobby" in form_data:
	print """
		<h1>Your birthday is: {} and your favorite hobby is: {} </h1>
	""".format(form_data['birthdate'].value, form_data['main hobby'].value)

if "lying" in form_data:
	print "<p>Thank you for being honest about being dishonest!</p>"

print """
	<form method="post" action="/cgi/page2.py">
		<label>Name</label>
		<input type="text" name="name">
		<br/>
		<label>Family</label>
		<input type="text" name="family">
		<br/>
		<label>Do you like pie?</label>
		<input type="checkbox" name="pie" value="ilikepie">
		<br/>
		<input type="submit">
	</form>

</body>
</html>


"""
