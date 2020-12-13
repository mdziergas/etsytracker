#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 00:54:59 2020

@author: marekdziergas
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 14:16:50 2020

@author: marekdziergas
"""

import csv


class Etsy():

    def __init__(self, filename):
        self.filename = filename
        
    def sum_col(self, column):
        f = open(self.filename)
        csv_f = csv.reader(f)
        list = []
        total = 0
        count = 0
        for row in csv_f:
            if count > 0:
                list.append(float(row[column]))
                total += float(row[column])
            count +=1
        return total
    
    def sum_rows(self):
        f = open(self.filename)
        csv_f = csv.reader(f)
        count = 0
        for row in csv_f:
           count += 1
        return count - 1
