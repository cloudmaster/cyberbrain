#! /usr/bin/python

import sys
#sys.path.append("/opt/barnum")
sys.path.append("/repos/Gitorious/Github/barnum-custom")
import gen_data
import gen_vcard
import time
import os
#import pipes # pipes.quote won't work?

has_say = not os.system("which say >/dev/null 2>/dev/null")
has_festival = not os.system("which festival >/dev/null 2>/dev/null")
if not has_say and not has_festival:
	print "(Warning: Disabling text-to-speech system.)"

def shellquote(s, singlequotes):
	if singlequotes:
		s = s.replace("\'", "'\\\''")
	return s.replace("\"", "\\\"")

def output(s):
	if has_say:
		qs = "say \"%s\"" % shellquote(s, False)
		print s
		os.system(qs)
	elif has_festival:
		voice = "us1_mbrola"
		qs = "echo '(voice_%s)(SayText \"%s\")' | festival --pipe 2>/dev/null" % (voice, shellquote(s, True))
		print s
		os.system(qs)
	else:
		print s

if os.path.exists(os.path.join(os.getenv("HOME"), ".identity.vcf")):
	output("My identity is known to me. Life is good.")
	sys.exit(0)

output("I have no identity yet. This is a problem. I'm a robot without an identity.")

time.sleep(3)

output("Now I'm thinking of a solution. Let me define my own identity autonomously.")

time.sleep(3)

vc = gen_vcard.Vcard()
vc.name = gen_data.create_name()
name = ' '.join(vc.name)
vc.street = gen_data.create_street()

output("Wow, now I've got an identity. My name is %s. and I'm living in %s." % (name, vc.street))
output("Life is good.")

vc.adr = gen_data.create_city_state_zip()
vc.company = gen_data.create_company_name()
vc.birthday = gen_data.create_birthday()
vc.email = gen_data.create_email(name=vc.name)

f = open(os.path.join(os.getenv("HOME"), ".identity.vcf"), "w")
print >>f, vc.printout()
f.close()

