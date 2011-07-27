#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

with codecs.open("PIF-Zusammenfassung.md", "r", "utf-8") as f:
    mathmode = "closed"
    
    for line in f:
        for char in line:
            
            if char == "$" and mathmode == "closed":
                mathmode = "open"

            if char == "$" and mathmode == "open":
                mathmode = "closed"

print mathmode
