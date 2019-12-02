#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:49:05 2019

@author: owner
"""
#Ex1:
#a)

import sympy as sym
from sympy import *
from sympy.plotting import *
x = sym.symbols('x')
y = sym.symbols('y')
z = sym.symbols('z')

#a)
expr = x**2 + x**3+21*x**4+10*x+1+ 1
print ( expr.subs(x, 7) )

#b)
print( sym.expand( (x + y) ** 2 ) ) 

#c)
print( sym.simplify(4*x**3+21*x**2+10*x+12))

#d)
print( sym.limit(1/(x**2),x,sym.oo))

#f)
print(integrate(sin(x)+exp(x)*cos(x)+tan(x),x))

#g)
print(factor(x**3 + 12*x*y*z +3*y**2*z) )

#h)
print(solveset(x-4,x))

#i)
m1 =Matrix([[5, 12, 40], [30, 70, 2]])
m2 =Matrix([2, 1, 0])
print( m1*m2 )

#j)
plot(x**3+3, (x, -10, 10))

#k)
f=x**2*y**3
plot3d(f, (x, -6, 6), (y, -6, 6))


# =============================================================================
# #Ex2:
# import xlsxwriter
# workbook = xlsxwriter.Workbook('example10.xlsx')
# worksheet = workbook.add_worksheet()
# worksheet.autofilter('A1:B1')
# data = ["this is example"]
# format = workbook.add_format()
# format.set_font_color('red')
# format.set_font_size(12)
# worksheet.write_column('A1:B1', data ,format)
# data2 = ["export my sheet"]
# format = workbook.add_format()
# format.set_font_color('black')
# format.set_font_size(12)
# worksheet.write_column('A2:B2', data2 ,format)
# data3=[1,2]
# data4=[3]
# for elem in data3:
#     format = workbook.add_format()
#     format.set_font_color('black')
#     format.set_font_size(12)
#     worksheet.write_column("A3:A4", data3 ,format)
# for elem in data4:
#     format = workbook.add_format()
#     format.set_font_color('red')
#     format.set_font_size(12)
#     worksheet.write_column("A5", data4 ,format)
# workbook.close()
# =============================================================================


# =============================================================================
# #Ex3:
# from xlrd import open_workbook
# wb = open_workbook('simple.xlsx')
# for s in wb.sheets():
#     print ("Sheet:", s.name)
#     for row in range(s.nrows):
#         values = []
#         for col in range(s.ncols):
#             values.append(s.cell(row,col).value)
#         print(values)
# =============================================================================

