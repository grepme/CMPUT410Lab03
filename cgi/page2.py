#!/usr/bin/env python

import cgi

form_data = cgi.FieldStorage()

print "Content-Type: text/html\r\n"
print "\r\n"

print """
<!doctype html>
<html>
<head>
	<title>Page2</title>
</head>
<body>
"""

if "name" in form_data and "family" in form_data:
        print """
                <h1>Hello: {} from family: {} </h1>     

        """.format(form_data['name'].value, form_data['family'].value)

if "pie" in form_data:
	print "<p>Apparently you like pie.</p>"

print """
        <form method="post" action="/cgi/page1.py">
                <label>Birthday</label>
                <input type="date" name="birthdate">
                <br/>
                <label>Main Hobby</label>
                <input type="text" name="main hobby">
                <br/>
		<label>Are you lying?</label>
		<input type="checkbox" name="lying" value="lying">
		<br/>
                <input type="submit">
        </form>
</body>
</html>
"""
