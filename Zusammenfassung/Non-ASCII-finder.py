#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

with codecs.open("PIF-Zusammenfassung.texEncoded", "r", "utf-8") as f:
    f2 = ""
    
    lineNum = 1
    for line in f:
        charPos = 1
        for char in line:
            
            f2 += char
            
            if ord(char) >= 128:
                
                # Handled by Makefile. Skip silently.
                if char == u"€": continue
                if char == u"£": continue
                
                if char == u"„": continue
                if char == u'"': continue

                if char == u"ü": continue
                if char == u"ö": continue
                if char == u"ä": continue
                if char == u"Ü": continue
                if char == u"Ö": continue
                if char == u"Ä": continue
                if char == u"ß": continue
                
                # To be replaced

                #if char == u"’":
                 #   f2 = f2[:-1] + "'"
                 #   continue
                    
                print "Found unknown non-ASCII-Character %s in line %s at position %s" % (char, lineNum, charPos)
            charPos += 1
        lineNum += 1

#    print f2
