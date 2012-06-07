#! /usr/bin/python

import sys
#sys.path.append("/opt/barnum-vcard")
sys.path.append("/repos/Gitorious/github-barnum-custom")
import gen_data
import time
import os
#import pipes # pipes.quote won't work?

def shellquote(s):
        return s.replace("\"", "\\\"")

def output(s):
        #print s
        os.system("say \"%s\"" % shellquote(s))

output("I have no identity yet. This is a problem. I'm a robot without an identity.")

time.sleep(3)

output("Now I'm thinking of a solution. Let me define my own identity autonomously.")

time.sleep(3)

names = gen_data.create_name()
name = ' '.join(names)
street = gen_data.create_street()

output("Wow, now I've got an identity. My name is %s. and I'm living in %s." % (name, street))
output("Life is good.")

