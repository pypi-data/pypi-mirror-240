#!/usr/bin/env python
# coding: utf-8

# 第一部分：程序说明###################################################################################
# coding=utf-8
# 药械不良事件工作平台
# 开发人：蔡权周

# 第二部分：导入基本模块及初始化 ########################################################################

import tkinter as Tk #line:11
import os #line:12
import traceback #line:13
import ast #line:14
import re #line:15
import xlrd #line:16
import xlwt #line:17
import openpyxl #line:18
import pandas as pd #line:19
import numpy as np #line:20
import math #line:21
import scipy .stats as st #line:22
from tkinter import ttk ,Menu ,Frame ,Canvas ,StringVar ,LEFT ,RIGHT ,TOP ,BOTTOM ,BOTH ,Y ,X ,YES ,NO ,DISABLED ,END ,Button ,LabelFrame ,GROOVE ,Toplevel ,Label ,Entry ,Scrollbar ,Text ,filedialog ,dialog ,PhotoImage #line:23
import tkinter .font as tkFont #line:24
from tkinter .messagebox import showinfo #line:25
from tkinter .scrolledtext import ScrolledText #line:26
import matplotlib as plt #line:27
from matplotlib .backends .backend_tkagg import FigureCanvasTkAgg #line:28
from matplotlib .figure import Figure #line:29
from matplotlib .backends .backend_tkagg import NavigationToolbar2Tk #line:30
import collections #line:31
from collections import Counter #line:32
import datetime #line:33
from datetime import datetime ,timedelta #line:34
import xlsxwriter #line:35
import time #line:36
import threading #line:37
import warnings #line:38
from matplotlib .ticker import PercentFormatter #line:39
import sqlite3 #line:40
from sqlalchemy import create_engine #line:41
from sqlalchemy import text as sqltext #line:42
import webbrowser #line:44
global ori #line:47
ori =0 #line:48
global auto_guize #line:49
global biaozhun #line:52
global dishi #line:53
biaozhun =""#line:54
dishi =""#line:55
global ini #line:59
ini ={}#line:60
ini ["四个品种"]=1 #line:61
import random #line:64
import requests #line:65
global version_now #line:66
global usergroup #line:67
global setting_cfg #line:68
global csdir #line:69
global peizhidir #line:70
version_now ="0.0.8"#line:71
usergroup ="用户组=0"#line:72
setting_cfg =""#line:73
csdir =str (os .path .abspath (__file__ )).replace (str (__file__ ),"")#line:74
if csdir =="":#line:75
    csdir =str (os .path .dirname (__file__ ))#line:76
    csdir =csdir +csdir .split ("adrmdr")[0 ][-1 ]#line:77
title_all ="药械妆不良反应报表统计分析工作站 V"+version_now #line:80
title_all2 ="药械妆不良反应报表统计分析工作站 V"+version_now #line:81
def extract_zip_file (OO0OOOO0O0O0OOOO0 ,OOOO0O0OOO0O000O0 ):#line:88
    import zipfile #line:90
    if OOOO0O0OOO0O000O0 =="":#line:91
        return 0 #line:92
    with zipfile .ZipFile (OO0OOOO0O0O0OOOO0 ,'r')as OOOOOOO0OO00O0O00 :#line:93
        for O0000OO00OO0OOOO0 in OOOOOOO0OO00O0O00 .infolist ():#line:94
            O0000OO00OO0OOOO0 .filename =O0000OO00OO0OOOO0 .filename .encode ('cp437').decode ('gbk')#line:96
            OOOOOOO0OO00O0O00 .extract (O0000OO00OO0OOOO0 ,OOOO0O0OOO0O000O0 )#line:97
def get_directory_path (OO00000O0OO0O000O ):#line:103
    global csdir #line:105
    if not (os .path .isfile (os .path .join (OO00000O0OO0O000O ,'0（范例）比例失衡关键字库.xls'))):#line:107
        extract_zip_file (csdir +"def.py",OO00000O0OO0O000O )#line:112
    if OO00000O0OO0O000O =="":#line:114
        quit ()#line:115
    return OO00000O0OO0O000O #line:116
def convert_and_compare_dates (O0O0O0OO0OOO0OOO0 ):#line:120
    import datetime #line:121
    O0OOOOOO0O000O000 =datetime .datetime .now ()#line:122
    try :#line:124
       OOOOO0O0OOOO0000O =datetime .datetime .strptime (str (int (int (O0O0O0OO0OOO0OOO0 )/4 )),"%Y%m%d")#line:125
    except :#line:126
        print ("fail")#line:127
        return "已过期"#line:128
    if OOOOO0O0OOOO0000O >O0OOOOOO0O000O000 :#line:130
        return "未过期"#line:132
    else :#line:133
        return "已过期"#line:134
def read_setting_cfg ():#line:136
    global csdir #line:137
    if os .path .exists (csdir +'setting.cfg'):#line:139
        text .insert (END ,"已完成初始化\n")#line:140
        with open (csdir +'setting.cfg','r')as OO000O00O00O0000O :#line:141
            O0O000OO0O0O0OOOO =eval (OO000O00O00O0000O .read ())#line:142
    else :#line:143
        OOOO0OOOOO000O000 =csdir +'setting.cfg'#line:145
        with open (OOOO0OOOOO000O000 ,'w')as OO000O00O00O0000O :#line:146
            OO000O00O00O0000O .write ('{"settingdir": 0, "sidori": 0, "sidfinal": "11111180000808"}')#line:147
        text .insert (END ,"未初始化，正在初始化...\n")#line:148
        O0O000OO0O0O0OOOO =read_setting_cfg ()#line:149
    return O0O000OO0O0O0OOOO #line:150
def open_setting_cfg ():#line:153
    global csdir #line:154
    with open (csdir +"setting.cfg","r")as OOOOO000OOO00OOO0 :#line:156
        OO00OOO00O000000O =eval (OOOOO000OOO00OOO0 .read ())#line:158
    return OO00OOO00O000000O #line:159
def update_setting_cfg (O00O0OOO00OOO00O0 ,OO00O00O000OOO0O0 ):#line:161
    global csdir #line:162
    with open (csdir +"setting.cfg","r")as O0OO0O0OOOO00OO00 :#line:164
        OOOOO00O000O0OO0O =eval (O0OO0O0OOOO00OO00 .read ())#line:166
    if OOOOO00O000O0OO0O [O00O0OOO00OOO00O0 ]==0 or OOOOO00O000O0OO0O [O00O0OOO00OOO00O0 ]=="11111180000808":#line:168
        OOOOO00O000O0OO0O [O00O0OOO00OOO00O0 ]=OO00O00O000OOO0O0 #line:169
        with open (csdir +"setting.cfg","w")as O0OO0O0OOOO00OO00 :#line:171
            O0OO0O0OOOO00OO00 .write (str (OOOOO00O000O0OO0O ))#line:172
def generate_random_file ():#line:175
    OOO0O00O0O0OO000O =random .randint (200000 ,299999 )#line:177
    update_setting_cfg ("sidori",OOO0O00O0O0OO000O )#line:179
def display_random_number ():#line:181
    global csdir #line:182
    OOOO000OOOOO00000 =Toplevel ()#line:183
    OOOO000OOOOO00000 .title ("ID")#line:184
    OOOOO0000O000000O =OOOO000OOOOO00000 .winfo_screenwidth ()#line:186
    OO0000000O0OO0OOO =OOOO000OOOOO00000 .winfo_screenheight ()#line:187
    OOO0000OO0OOOOOOO =80 #line:189
    O0O0O000O000O0O0O =70 #line:190
    OO0OO0O0OOO000OO0 =(OOOOO0000O000000O -OOO0000OO0OOOOOOO )/2 #line:192
    OOOOO0OO0000OOOOO =(OO0000000O0OO0OOO -O0O0O000O000O0O0O )/2 #line:193
    OOOO000OOOOO00000 .geometry ("%dx%d+%d+%d"%(OOO0000OO0OOOOOOO ,O0O0O000O000O0O0O ,OO0OO0O0OOO000OO0 ,OOOOO0OO0000OOOOO ))#line:194
    with open (csdir +"setting.cfg","r")as O00000O0O0O0OO0OO :#line:197
        OO00OOOO00OO0O00O =eval (O00000O0O0O0OO0OO .read ())#line:199
    OO0OOOOO0OOOOO0OO =int (OO00OOOO00OO0O00O ["sidori"])#line:200
    O0O000OOOO0000000 =OO0OOOOO0OOOOO0OO *2 +183576 #line:201
    print (O0O000OOOO0000000 )#line:203
    OOOO0OOOO00O00OOO =ttk .Label (OOOO000OOOOO00000 ,text =f"机器码: {OO0OOOOO0OOOOO0OO}")#line:205
    OO0OOO0OOOOO00OO0 =ttk .Entry (OOOO000OOOOO00000 )#line:206
    OOOO0OOOO00O00OOO .pack ()#line:209
    OO0OOO0OOOOO00OO0 .pack ()#line:210
    ttk .Button (OOOO000OOOOO00000 ,text ="验证",command =lambda :check_input (OO0OOO0OOOOO00OO0 .get (),O0O000OOOO0000000 )).pack ()#line:214
def check_input (O0O0OOO0O0000O00O ,OO000OO000O0OO0O0 ):#line:216
    try :#line:220
        O0O0OOOO0OO0O0O00 =int (str (O0O0OOO0O0000O00O )[0 :6 ])#line:221
        O000OO000OOOO0000 =convert_and_compare_dates (str (O0O0OOO0O0000O00O )[6 :14 ])#line:222
    except :#line:223
        showinfo (title ="提示",message ="不匹配，注册失败。")#line:224
        return 0 #line:225
    if O0O0OOOO0OO0O0O00 ==OO000OO000O0OO0O0 and O000OO000OOOO0000 =="未过期":#line:227
        update_setting_cfg ("sidfinal",O0O0OOO0O0000O00O )#line:228
        showinfo (title ="提示",message ="注册成功,请重新启动程序。")#line:229
        quit ()#line:230
    else :#line:231
        showinfo (title ="提示",message ="不匹配，注册失败。")#line:232
def update_software (O0OOOO0OO00O0OO00 ):#line:237
    global version_now #line:239
    text .insert (END ,"当前版本为："+version_now +",正在检查更新...(您可以同时执行分析任务)")#line:240
    try :#line:241
        OOO0O00O0O0O000O0 =requests .get (f"https://pypi.org/pypi/{O0OOOO0OO00O0OO00}/json",timeout =2 ).json ()["info"]["version"]#line:242
    except :#line:243
        return "...更新失败。"#line:244
    if OOO0O00O0O0O000O0 >version_now :#line:245
        text .insert (END ,"\n最新版本为："+OOO0O00O0O0O000O0 +",正在尝试自动更新....")#line:246
        pip .main (['install',O0OOOO0OO00O0OO00 ,'--upgrade'])#line:248
        text .insert (END ,"\n您可以开展工作。")#line:249
        return "...更新成功。"#line:250
def TOOLS_ror_mode1 (O0O0OOO000OOO00OO ,OOOOO0O0O00OOO0OO ):#line:267
	OO0000O00OOO00000 =[]#line:268
	for OOOO0OO000OO000O0 in ("事件发生年份","性别","年龄段","报告类型-严重程度","停药减药后反应是否减轻或消失","再次使用可疑药是否出现同样反应","对原患疾病影响","不良反应结果","关联性评价"):#line:269
		O0O0OOO000OOO00OO [OOOO0OO000OO000O0 ]=O0O0OOO000OOO00OO [OOOO0OO000OO000O0 ].astype (str )#line:270
		O0O0OOO000OOO00OO [OOOO0OO000OO000O0 ]=O0O0OOO000OOO00OO [OOOO0OO000OO000O0 ].fillna ("不详")#line:271
		O0O0O00O00OOO0O0O =0 #line:273
		for O000OO0OOO0OO00O0 in O0O0OOO000OOO00OO [OOOOO0O0O00OOO0OO ].drop_duplicates ():#line:274
			O0O0O00O00OOO0O0O =O0O0O00O00OOO0O0O +1 #line:275
			O0OOOOOO0O0OO0000 =O0O0OOO000OOO00OO [(O0O0OOO000OOO00OO [OOOOO0O0O00OOO0OO ]==O000OO0OOO0OO00O0 )].copy ()#line:276
			O00O00OO00OO0OOOO =str (O000OO0OOO0OO00O0 )+"计数"#line:278
			OO0O0O0O000000OO0 =str (O000OO0OOO0OO00O0 )+"构成比(%)"#line:279
			OOO000OOOOO000O00 =O0OOOOOO0O0OO0000 .groupby (OOOO0OO000OO000O0 ).agg (计数 =("报告编码","nunique")).sort_values (by =OOOO0OO000OO000O0 ,ascending =[True ],na_position ="last").reset_index ()#line:280
			OOO000OOOOO000O00 [OO0O0O0O000000OO0 ]=round (100 *OOO000OOOOO000O00 ["计数"]/OOO000OOOOO000O00 ["计数"].sum (),2 )#line:281
			OOO000OOOOO000O00 =OOO000OOOOO000O00 .rename (columns ={OOOO0OO000OO000O0 :"项目"})#line:282
			OOO000OOOOO000O00 =OOO000OOOOO000O00 .rename (columns ={"计数":O00O00OO00OO0OOOO })#line:283
			if O0O0O00O00OOO0O0O >1 :#line:284
				OOOO0000O0000O00O =pd .merge (OOOO0000O0000O00O ,OOO000OOOOO000O00 ,on =["项目"],how ="outer")#line:285
			else :#line:286
				OOOO0000O0000O00O =OOO000OOOOO000O00 .copy ()#line:287
		OOOO0000O0000O00O ["类别"]=OOOO0OO000OO000O0 #line:289
		OO0000O00OOO00000 .append (OOOO0000O0000O00O .copy ().reset_index (drop =True ))#line:290
	O00OOO000000OO0O0 =pd .concat (OO0000O00OOO00000 ,ignore_index =True ).fillna (0 )#line:293
	O00OOO000000OO0O0 ["报表类型"]="KETI"#line:294
	TABLE_tree_Level_2 (O00OOO000000OO0O0 ,1 ,O00OOO000000OO0O0 )#line:295
def TOOLS_ror_mode2 (O0O000O0OO00OO000 ,OO00O0O0OO0OO0O0O ):#line:297
	OO00O000OO0O0OO0O =Countall (O0O000O0OO00OO000 ).df_ror (["产品类别",OO00O0O0OO0OO0O0O ]).reset_index ()#line:298
	OO00O000OO0O0OO0O ["四分表"]=OO00O000OO0O0OO0O ["四分表"].str .replace ("(","")#line:299
	OO00O000OO0O0OO0O ["四分表"]=OO00O000OO0O0OO0O ["四分表"].str .replace (")","")#line:300
	OO00O000OO0O0OO0O ["ROR信号（0-否，1-是）"]=0 #line:301
	OO00O000OO0O0OO0O ["PRR信号（0-否，1-是）"]=0 #line:302
	OO00O000OO0O0OO0O ["分母核验"]=0 #line:303
	for OOO00000OOO0O00OO ,O000OOOOOO000000O in OO00O000OO0O0OO0O .iterrows ():#line:304
		O00OOO0O0OOOOO00O =tuple (O000OOOOOO000000O ["四分表"].split (","))#line:305
		OO00O000OO0O0OO0O .loc [OOO00000OOO0O00OO ,"a"]=int (O00OOO0O0OOOOO00O [0 ])#line:306
		OO00O000OO0O0OO0O .loc [OOO00000OOO0O00OO ,"b"]=int (O00OOO0O0OOOOO00O [1 ])#line:307
		OO00O000OO0O0OO0O .loc [OOO00000OOO0O00OO ,"c"]=int (O00OOO0O0OOOOO00O [2 ])#line:308
		OO00O000OO0O0OO0O .loc [OOO00000OOO0O00OO ,"d"]=int (O00OOO0O0OOOOO00O [3 ])#line:309
		if int (O00OOO0O0OOOOO00O [1 ])*int (O00OOO0O0OOOOO00O [2 ])*int (O00OOO0O0OOOOO00O [3 ])*int (O00OOO0O0OOOOO00O [0 ])==0 :#line:310
			OO00O000OO0O0OO0O .loc [OOO00000OOO0O00OO ,"分母核验"]=1 #line:311
		if O000OOOOOO000000O ['ROR值的95%CI下限']>1 and O000OOOOOO000000O ['出现频次']>=3 :#line:312
			OO00O000OO0O0OO0O .loc [OOO00000OOO0O00OO ,"ROR信号（0-否，1-是）"]=1 #line:313
		if O000OOOOOO000000O ['PRR值的95%CI下限']>1 and O000OOOOOO000000O ['出现频次']>=3 :#line:314
			OO00O000OO0O0OO0O .loc [OOO00000OOO0O00OO ,"PRR信号（0-否，1-是）"]=1 #line:315
		OO00O000OO0O0OO0O .loc [OOO00000OOO0O00OO ,"事件分类"]=str (TOOLS_get_list (OO00O000OO0O0OO0O .loc [OOO00000OOO0O00OO ,"特定关键字"])[0 ])#line:316
	OO00O000OO0O0OO0O =pd .pivot_table (OO00O000OO0O0OO0O ,values =["出现频次",'ROR值',"ROR值的95%CI下限","ROR信号（0-否，1-是）",'PRR值',"PRR值的95%CI下限","PRR信号（0-否，1-是）","a","b","c","d","分母核验","风险评分"],index ='事件分类',columns =OO00O0O0OO0OO0O0O ,aggfunc ='sum').reset_index ().fillna (0 )#line:318
	try :#line:321
		O0O0OO0O0O0OOOO0O =peizhidir +"0（范例）比例失衡关键字库.xls"#line:322
		if "报告类型-新的"in O0O000O0OO00OO000 .columns :#line:323
			O0000000O0000OO0O ="药品"#line:324
		else :#line:325
			O0000000O0000OO0O ="器械"#line:326
		OO0O0OOO0OO0OO0OO =pd .read_excel (O0O0OO0O0O0OOOO0O ,header =0 ,sheet_name =O0000000O0000OO0O ).reset_index (drop =True )#line:327
	except :#line:328
		pass #line:329
	for OOO00000OOO0O00OO ,O000OOOOOO000000O in OO0O0OOO0OO0OO0OO .iterrows ():#line:331
		OO00O000OO0O0OO0O .loc [OO00O000OO0O0OO0O ["事件分类"].str .contains (O000OOOOOO000000O ["值"],na =False ),"器官系统损害"]=TOOLS_get_list (O000OOOOOO000000O ["值"])[0 ]#line:332
	try :#line:335
		O00O0O0OOOO0000OO =peizhidir +""+"0（范例）标准术语"+".xlsx"#line:336
		try :#line:337
			OO00O0O00O0O00000 =pd .read_excel (O00O0O0OOOO0000OO ,sheet_name ="onept",header =0 ,index_col =0 ).reset_index ()#line:338
		except :#line:339
			showinfo (title ="错误信息",message ="标准术语集无法加载。")#line:340
		try :#line:342
			O0O000O0O0000OO0O =pd .read_excel (O00O0O0OOOO0000OO ,sheet_name ="my",header =0 ,index_col =0 ).reset_index ()#line:343
		except :#line:344
			showinfo (title ="错误信息",message ="自定义术语集无法加载。")#line:345
		OO00O0O00O0O00000 =pd .concat ([O0O000O0O0000OO0O ,OO00O0O00O0O00000 ],ignore_index =True ).drop_duplicates ("code")#line:347
		OO00O0O00O0O00000 ["code"]=OO00O0O00O0O00000 ["code"].astype (str )#line:348
		OO00O000OO0O0OO0O ["事件分类"]=OO00O000OO0O0OO0O ["事件分类"].astype (str )#line:349
		OO00O0O00O0O00000 ["事件分类"]=OO00O0O00O0O00000 ["PT"]#line:350
		OOOO0OO0O00O0O0OO =pd .merge (OO00O000OO0O0OO0O ,OO00O0O00O0O00000 ,on =["事件分类"],how ="left")#line:351
		for OOO00000OOO0O00OO ,O000OOOOOO000000O in OOOO0OO0O00O0O0OO .iterrows ():#line:352
			OO00O000OO0O0OO0O .loc [OO00O000OO0O0OO0O ["事件分类"]==O000OOOOOO000000O ["事件分类"],"Chinese"]=O000OOOOOO000000O ["Chinese"]#line:353
			OO00O000OO0O0OO0O .loc [OO00O000OO0O0OO0O ["事件分类"]==O000OOOOOO000000O ["事件分类"],"PT"]=O000OOOOOO000000O ["PT"]#line:354
			OO00O000OO0O0OO0O .loc [OO00O000OO0O0OO0O ["事件分类"]==O000OOOOOO000000O ["事件分类"],"HLT"]=O000OOOOOO000000O ["HLT"]#line:355
			OO00O000OO0O0OO0O .loc [OO00O000OO0O0OO0O ["事件分类"]==O000OOOOOO000000O ["事件分类"],"HLGT"]=O000OOOOOO000000O ["HLGT"]#line:356
			OO00O000OO0O0OO0O .loc [OO00O000OO0O0OO0O ["事件分类"]==O000OOOOOO000000O ["事件分类"],"SOC"]=O000OOOOOO000000O ["SOC"]#line:357
	except :#line:358
		pass #line:359
	OO00O000OO0O0OO0O ["报表类型"]="KETI"#line:362
	TABLE_tree_Level_2 (OO00O000OO0O0OO0O ,1 ,OO00O000OO0O0OO0O )#line:363
def TOOLS_ror_mode3 (O0O0O00O000O0OOOO ,OOO0OO00O0O0O0000 ):#line:365
	O0O0O00O000O0OOOO ["css"]=0 #line:366
	TOOLS_ror_mode2 (O0O0O00O000O0OOOO ,OOO0OO00O0O0O0000 )#line:367
def TOOLS_ror_mode4 (OO00O00OO00O00OOO ,O00O0O0O0OO00OOOO ):#line:369
	OOOO00O00OOO0O0O0 =[]#line:370
	for OO0O00O0O0O0O0000 ,OO000OOOO000OO0O0 in data .drop_duplicates (O00O0O0O0OO00OOOO ).iterrows ():#line:371
		OO000OO0O0O000OO0 =data [(OO00O00OO00O00OOO [O00O0O0O0OO00OOOO ]==OO000OOOO000OO0O0 [O00O0O0O0OO00OOOO ])]#line:372
		OO00OOOO00000OOOO =Countall (OO000OO0O0O000OO0 ).df_psur ()#line:373
		OO00OOOO00000OOOO [O00O0O0O0OO00OOOO ]=OO000OOOO000OO0O0 [O00O0O0O0OO00OOOO ]#line:374
		if len (OO00OOOO00000OOOO )>0 :#line:375
			OOOO00O00OOO0O0O0 .append (OO00OOOO00000OOOO )#line:376
	OO0O0OO00OO0OOOOO =pd .concat (OOOO00O00OOO0O0O0 ,ignore_index =True ).sort_values (by ="关键字标记",ascending =[False ],na_position ="last").reset_index ()#line:378
	OO0O0OO00OO0OOOOO ["报表类型"]="KETI"#line:379
	TABLE_tree_Level_2 (OO0O0OO00OO0OOOOO ,1 ,OO0O0OO00OO0OOOOO )#line:380
def STAT_pinzhong (O0O0O00OO0O0OOO0O ,OO000OOO0O00OOOO0 ,OO0O0OO000OO0OOO0 ):#line:382
	O0OOOOOO0O0OOOO00 =[OO000OOO0O00OOOO0 ]#line:384
	if OO0O0OO000OO0OOO0 ==-1 :#line:385
		OOOOO0000O00O00OO =O0O0O00OO0O0OOO0O .drop_duplicates ("报告编码").copy ()#line:386
		OOO00O0OO00OOOOOO =OOOOO0000O00O00OO .groupby ([OO000OOO0O00OOOO0 ]).agg (计数 =("报告编码","nunique")).sort_values (by =OO000OOO0O00OOOO0 ,ascending =[True ],na_position ="last").reset_index ()#line:387
		OOO00O0OO00OOOOOO ["构成比(%)"]=round (100 *OOO00O0OO00OOOOOO ["计数"]/OOO00O0OO00OOOOOO ["计数"].sum (),2 )#line:388
		OOO00O0OO00OOOOOO [OO000OOO0O00OOOO0 ]=OOO00O0OO00OOOOOO [OO000OOO0O00OOOO0 ].astype (str )#line:389
		OOO00O0OO00OOOOOO ["报表类型"]="dfx_deepview"+"_"+str (O0OOOOOO0O0OOOO00 )#line:390
		TABLE_tree_Level_2 (OOO00O0OO00OOOOOO ,1 ,OOOOO0000O00O00OO )#line:391
	if OO0O0OO000OO0OOO0 ==1 :#line:393
		OOOOO0000O00O00OO =O0O0O00OO0O0OOO0O .copy ()#line:394
		OOO00O0OO00OOOOOO =OOOOO0000O00O00OO .groupby ([OO000OOO0O00OOOO0 ]).agg (计数 =("报告编码","nunique")).sort_values (by ="计数",ascending =[False ],na_position ="last").reset_index ()#line:395
		OOO00O0OO00OOOOOO ["构成比(%)"]=round (100 *OOO00O0OO00OOOOOO ["计数"]/OOO00O0OO00OOOOOO ["计数"].sum (),2 )#line:396
		OOO00O0OO00OOOOOO ["报表类型"]="dfx_deepview"+"_"+str (O0OOOOOO0O0OOOO00 )#line:397
		TABLE_tree_Level_2 (OOO00O0OO00OOOOOO ,1 ,OOOOO0000O00O00OO )#line:398
	if OO0O0OO000OO0OOO0 ==4 :#line:400
		OOOOO0000O00O00OO =O0O0O00OO0O0OOO0O .copy ()#line:401
		OOOOO0000O00O00OO .loc [OOOOO0000O00O00OO ["不良反应结果"].str .contains ("好转",na =False ),"不良反应结果2"]="好转"#line:402
		OOOOO0000O00O00OO .loc [OOOOO0000O00O00OO ["不良反应结果"].str .contains ("痊愈",na =False ),"不良反应结果2"]="痊愈"#line:403
		OOOOO0000O00O00OO .loc [OOOOO0000O00O00OO ["不良反应结果"].str .contains ("无进展",na =False ),"不良反应结果2"]="无进展"#line:404
		OOOOO0000O00O00OO .loc [OOOOO0000O00O00OO ["不良反应结果"].str .contains ("死亡",na =False ),"不良反应结果2"]="死亡"#line:405
		OOOOO0000O00O00OO .loc [OOOOO0000O00O00OO ["不良反应结果"].str .contains ("不详",na =False ),"不良反应结果2"]="不详"#line:406
		OOOOO0000O00O00OO .loc [OOOOO0000O00O00OO ["不良反应结果"].str .contains ("未好转",na =False ),"不良反应结果2"]="未好转"#line:407
		OOO00O0OO00OOOOOO =OOOOO0000O00O00OO .groupby (["不良反应结果2"]).agg (计数 =("报告编码","nunique")).sort_values (by ="计数",ascending =[False ],na_position ="last").reset_index ()#line:408
		OOO00O0OO00OOOOOO ["构成比(%)"]=round (100 *OOO00O0OO00OOOOOO ["计数"]/OOO00O0OO00OOOOOO ["计数"].sum (),2 )#line:409
		OOO00O0OO00OOOOOO ["报表类型"]="dfx_deepview"+"_"+str (["不良反应结果2"])#line:410
		TABLE_tree_Level_2 (OOO00O0OO00OOOOOO ,1 ,OOOOO0000O00O00OO )#line:411
	if OO0O0OO000OO0OOO0 ==5 :#line:413
		OOOOO0000O00O00OO =O0O0O00OO0O0OOO0O .copy ()#line:414
		OOOOO0000O00O00OO ["关联性评价汇总"]="("+OOOOO0000O00O00OO ["评价状态"].astype (str )+"("+OOOOO0000O00O00OO ["县评价"].astype (str )+"("+OOOOO0000O00O00OO ["市评价"].astype (str )+"("+OOOOO0000O00O00OO ["省评价"].astype (str )+"("+OOOOO0000O00O00OO ["国家评价"].astype (str )+")"#line:416
		OOOOO0000O00O00OO ["关联性评价汇总"]=OOOOO0000O00O00OO ["关联性评价汇总"].str .replace ("(nan","",regex =False )#line:417
		OOOOO0000O00O00OO ["关联性评价汇总"]=OOOOO0000O00O00OO ["关联性评价汇总"].str .replace ("nan)","",regex =False )#line:418
		OOOOO0000O00O00OO ["关联性评价汇总"]=OOOOO0000O00O00OO ["关联性评价汇总"].str .replace ("nan","",regex =False )#line:419
		OOOOO0000O00O00OO ['最终的关联性评价']=OOOOO0000O00O00OO ["关联性评价汇总"].str .extract ('.*\((.*)\).*',expand =False )#line:420
		OOO00O0OO00OOOOOO =OOOOO0000O00O00OO .groupby ('最终的关联性评价').agg (计数 =("报告编码","nunique")).sort_values (by ="计数",ascending =[False ],na_position ="last").reset_index ()#line:421
		OOO00O0OO00OOOOOO ["构成比(%)"]=round (100 *OOO00O0OO00OOOOOO ["计数"]/OOO00O0OO00OOOOOO ["计数"].sum (),2 )#line:422
		OOO00O0OO00OOOOOO ["报表类型"]="dfx_deepview"+"_"+str (['最终的关联性评价'])#line:423
		TABLE_tree_Level_2 (OOO00O0OO00OOOOOO ,1 ,OOOOO0000O00O00OO )#line:424
	if OO0O0OO000OO0OOO0 ==0 :#line:426
		O0O0O00OO0O0OOO0O [OO000OOO0O00OOOO0 ]=O0O0O00OO0O0OOO0O [OO000OOO0O00OOOO0 ].fillna ("未填写")#line:427
		O0O0O00OO0O0OOO0O [OO000OOO0O00OOOO0 ]=O0O0O00OO0O0OOO0O [OO000OOO0O00OOOO0 ].str .replace ("*","",regex =False )#line:428
		OOO0O0OO0OO0OO0O0 ="use("+str (OO000OOO0O00OOOO0 )+").file"#line:429
		O00O0OOO000000O0O =str (Counter (TOOLS_get_list0 (OOO0O0OO0OO0OO0O0 ,O0O0O00OO0O0OOO0O ,1000 ))).replace ("Counter({","{")#line:430
		O00O0OOO000000O0O =O00O0OOO000000O0O .replace ("})","}")#line:431
		O00O0OOO000000O0O =ast .literal_eval (O00O0OOO000000O0O )#line:432
		OOO00O0OO00OOOOOO =pd .DataFrame .from_dict (O00O0OOO000000O0O ,orient ="index",columns =["计数"]).reset_index ()#line:433
		OOO00O0OO00OOOOOO ["构成比(%)"]=round (100 *OOO00O0OO00OOOOOO ["计数"]/OOO00O0OO00OOOOOO ["计数"].sum (),2 )#line:435
		OOO00O0OO00OOOOOO ["报表类型"]="dfx_deepvie2"+"_"+str (O0OOOOOO0O0OOOO00 )#line:436
		TABLE_tree_Level_2 (OOO00O0OO00OOOOOO ,1 ,O0O0O00OO0O0OOO0O )#line:437
		return OOO00O0OO00OOOOOO #line:438
	if OO0O0OO000OO0OOO0 ==2 or OO0O0OO000OO0OOO0 ==3 :#line:442
		O0O0O00OO0O0OOO0O [OO000OOO0O00OOOO0 ]=O0O0O00OO0O0OOO0O [OO000OOO0O00OOOO0 ].astype (str )#line:443
		O0O0O00OO0O0OOO0O [OO000OOO0O00OOOO0 ]=O0O0O00OO0O0OOO0O [OO000OOO0O00OOOO0 ].fillna ("未填写")#line:444
		OOO0O0OO0OO0OO0O0 ="use("+str (OO000OOO0O00OOOO0 )+").file"#line:446
		O00O0OOO000000O0O =str (Counter (TOOLS_get_list0 (OOO0O0OO0OO0OO0O0 ,O0O0O00OO0O0OOO0O ,1000 ))).replace ("Counter({","{")#line:447
		O00O0OOO000000O0O =O00O0OOO000000O0O .replace ("})","}")#line:448
		O00O0OOO000000O0O =ast .literal_eval (O00O0OOO000000O0O )#line:449
		OOO00O0OO00OOOOOO =pd .DataFrame .from_dict (O00O0OOO000000O0O ,orient ="index",columns =["计数"]).reset_index ()#line:450
		print ("正在统计，请稍后...")#line:451
		OOOOOOO0OOOO00OO0 =peizhidir +""+"0（范例）标准术语"+".xlsx"#line:452
		try :#line:453
			OO0OOO0000000O000 =pd .read_excel (OOOOOOO0OOOO00OO0 ,sheet_name ="simple",header =0 ,index_col =0 ).reset_index ()#line:454
		except :#line:455
			showinfo (title ="错误信息",message ="标准术语集无法加载。")#line:456
			return 0 #line:457
		try :#line:458
			O0OOOO000O0OO0O0O =pd .read_excel (OOOOOOO0OOOO00OO0 ,sheet_name ="my",header =0 ,index_col =0 ).reset_index ()#line:459
		except :#line:460
			showinfo (title ="错误信息",message ="自定义术语集无法加载。")#line:461
			return 0 #line:462
		OO0OOO0000000O000 =pd .concat ([O0OOOO000O0OO0O0O ,OO0OOO0000000O000 ],ignore_index =True ).drop_duplicates ("code")#line:463
		OO0OOO0000000O000 ["code"]=OO0OOO0000000O000 ["code"].astype (str )#line:464
		OOO00O0OO00OOOOOO ["index"]=OOO00O0OO00OOOOOO ["index"].astype (str )#line:465
		OOO00O0OO00OOOOOO =OOO00O0OO00OOOOOO .rename (columns ={"index":"code"})#line:467
		OOO00O0OO00OOOOOO =pd .merge (OOO00O0OO00OOOOOO ,OO0OOO0000000O000 ,on =["code"],how ="left")#line:468
		OOO00O0OO00OOOOOO ["code构成比(%)"]=round (100 *OOO00O0OO00OOOOOO ["计数"]/OOO00O0OO00OOOOOO ["计数"].sum (),2 )#line:469
		O0OO0O0OOOO00OO0O =OOO00O0OO00OOOOOO .groupby ("SOC").agg (SOC计数 =("计数","sum")).sort_values (by ="SOC计数",ascending =[False ],na_position ="last").reset_index ()#line:470
		O0OO0O0OOOO00OO0O ["soc构成比(%)"]=round (100 *O0OO0O0OOOO00OO0O ["SOC计数"]/O0OO0O0OOOO00OO0O ["SOC计数"].sum (),2 )#line:471
		O0OO0O0OOOO00OO0O ["SOC计数"]=O0OO0O0OOOO00OO0O ["SOC计数"].astype (int )#line:472
		OOO00O0OO00OOOOOO =pd .merge (OOO00O0OO00OOOOOO ,O0OO0O0OOOO00OO0O ,on =["SOC"],how ="left")#line:473
		if OO0O0OO000OO0OOO0 ==3 :#line:475
			O0OO0O0OOOO00OO0O ["具体名称"]=""#line:476
			for OO00O0O0OOOO00000 ,OOO00OOO0O000O0O0 in O0OO0O0OOOO00OO0O .iterrows ():#line:477
				O00OO00OOO000OO0O =""#line:478
				OO0O0O0OOOOOO0000 =OOO00O0OO00OOOOOO .loc [OOO00O0OO00OOOOOO ["SOC"].str .contains (OOO00OOO0O000O0O0 ["SOC"],na =False )].copy ()#line:479
				for OO000O00OO00OOO0O ,O0OO0OOO0OO00000O in OO0O0O0OOOOOO0000 .iterrows ():#line:480
					O00OO00OOO000OO0O =O00OO00OOO000OO0O +str (O0OO0OOO0OO00000O ["PT"])+"("+str (O0OO0OOO0OO00000O ["计数"])+")、"#line:481
				O0OO0O0OOOO00OO0O .loc [OO00O0O0OOOO00000 ,"具体名称"]=O00OO00OOO000OO0O #line:482
			O0OO0O0OOOO00OO0O ["报表类型"]="dfx_deepvie2"+"_"+str (["SOC"])#line:483
			TABLE_tree_Level_2 (O0OO0O0OOOO00OO0O ,1 ,OOO00O0OO00OOOOOO )#line:484
		if OO0O0OO000OO0OOO0 ==2 :#line:486
			OOO00O0OO00OOOOOO ["报表类型"]="dfx_deepvie2"+"_"+str (O0OOOOOO0O0OOOO00 )#line:487
			TABLE_tree_Level_2 (OOO00O0OO00OOOOOO ,1 ,O0O0O00OO0O0OOO0O )#line:488
	pass #line:491
def DRAW_pre (O00O0O0OO0OO00000 ):#line:493
	""#line:494
	OOOOOOOO0OO0OOOO0 =list (O00O0O0OO0OO00000 ["报表类型"])[0 ].replace ("1","")#line:502
	if "dfx_org监测机构"in OOOOOOOO0OO0OOOO0 :#line:504
		O00O0O0OO0OO00000 =O00O0O0OO0OO00000 [:-1 ]#line:505
		DRAW_make_one (O00O0O0OO0OO00000 ,"报告图","监测机构","报告数量","超级托帕斯图(严重伤害数)")#line:506
	elif "dfx_org市级监测机构"in OOOOOOOO0OO0OOOO0 :#line:507
		O00O0O0OO0OO00000 =O00O0O0OO0OO00000 [:-1 ]#line:508
		DRAW_make_one (O00O0O0OO0OO00000 ,"报告图","市级监测机构","报告数量","超级托帕斯图(严重伤害数)")#line:509
	elif "dfx_user"in OOOOOOOO0OO0OOOO0 :#line:510
		O00O0O0OO0OO00000 =O00O0O0OO0OO00000 [:-1 ]#line:511
		DRAW_make_one (O00O0O0OO0OO00000 ,"报告单位图","单位名称","报告数量","超级托帕斯图(严重伤害数)")#line:512
	elif "dfx_deepview"in OOOOOOOO0OO0OOOO0 :#line:515
		DRAW_make_one (O00O0O0OO0OO00000 ,"柱状图",O00O0O0OO0OO00000 .columns [0 ],"计数","柱状图")#line:516
	elif "dfx_chiyouren"in OOOOOOOO0OO0OOOO0 :#line:518
		O00O0O0OO0OO00000 =O00O0O0OO0OO00000 [:-1 ]#line:519
		DRAW_make_one (O00O0O0OO0OO00000 ,"涉及持有人图","上市许可持有人名称","总报告数","超级托帕斯图(总待评价数量)")#line:520
	elif "dfx_zhenghao"in OOOOOOOO0OO0OOOO0 :#line:522
		O00O0O0OO0OO00000 ["产品"]=O00O0O0OO0OO00000 ["产品名称"]+"("+O00O0O0OO0OO00000 ["注册证编号/曾用注册证编号"]+")"#line:523
		DRAW_make_one (O00O0O0OO0OO00000 ,"涉及产品图","产品","证号计数","超级托帕斯图(严重伤害数)")#line:524
	elif "dfx_pihao"in OOOOOOOO0OO0OOOO0 :#line:526
		if len (O00O0O0OO0OO00000 ["注册证编号/曾用注册证编号"].drop_duplicates ())>1 :#line:527
			O00O0O0OO0OO00000 ["产品"]=O00O0O0OO0OO00000 ["产品名称"]+"("+O00O0O0OO0OO00000 ["注册证编号/曾用注册证编号"]+"--"+O00O0O0OO0OO00000 ["产品批号"]+")"#line:528
			DRAW_make_one (O00O0O0OO0OO00000 ,"涉及批号图","产品","批号计数","超级托帕斯图(严重伤害数)")#line:529
		else :#line:530
			DRAW_make_one (O00O0O0OO0OO00000 ,"涉及批号图","产品批号","批号计数","超级托帕斯图(严重伤害数)")#line:531
	elif "dfx_xinghao"in OOOOOOOO0OO0OOOO0 :#line:533
		if len (O00O0O0OO0OO00000 ["注册证编号/曾用注册证编号"].drop_duplicates ())>1 :#line:534
			O00O0O0OO0OO00000 ["产品"]=O00O0O0OO0OO00000 ["产品名称"]+"("+O00O0O0OO0OO00000 ["注册证编号/曾用注册证编号"]+"--"+O00O0O0OO0OO00000 ["型号"]+")"#line:535
			DRAW_make_one (O00O0O0OO0OO00000 ,"涉及型号图","产品","型号计数","超级托帕斯图(严重伤害数)")#line:536
		else :#line:537
			DRAW_make_one (O00O0O0OO0OO00000 ,"涉及型号图","型号","型号计数","超级托帕斯图(严重伤害数)")#line:538
	elif "dfx_guige"in OOOOOOOO0OO0OOOO0 :#line:540
		if len (O00O0O0OO0OO00000 ["注册证编号/曾用注册证编号"].drop_duplicates ())>1 :#line:541
			O00O0O0OO0OO00000 ["产品"]=O00O0O0OO0OO00000 ["产品名称"]+"("+O00O0O0OO0OO00000 ["注册证编号/曾用注册证编号"]+"--"+O00O0O0OO0OO00000 ["规格"]+")"#line:542
			DRAW_make_one (O00O0O0OO0OO00000 ,"涉及规格图","产品","规格计数","超级托帕斯图(严重伤害数)")#line:543
		else :#line:544
			DRAW_make_one (O00O0O0OO0OO00000 ,"涉及规格图","规格","规格计数","超级托帕斯图(严重伤害数)")#line:545
	elif "PSUR"in OOOOOOOO0OO0OOOO0 :#line:547
		DRAW_make_mutibar (O00O0O0OO0OO00000 ,"总数量","严重","事件分类","总数量","严重","表现分类统计图")#line:548
	elif "keyword_findrisk"in OOOOOOOO0OO0OOOO0 :#line:550
		OO000OOOO00OOOO00 =O00O0O0OO0OO00000 .columns .to_list ()#line:552
		OO0000OOO000O0O00 =OO000OOOO00OOOO00 [OO000OOOO00OOOO00 .index ("关键字")+1 ]#line:553
		O0OO0O0OO0O0O00O0 =pd .pivot_table (O00O0O0OO0OO00000 ,index =OO0000OOO000O0O00 ,columns ="关键字",values =["计数"],aggfunc ={"计数":"sum"},fill_value ="0",margins =True ,dropna =False ,)#line:564
		O0OO0O0OO0O0O00O0 .columns =O0OO0O0OO0O0O00O0 .columns .droplevel (0 )#line:565
		O0OO0O0OO0O0O00O0 =O0OO0O0OO0O0O00O0 [:-1 ].reset_index ()#line:566
		O0OO0O0OO0O0O00O0 =pd .merge (O0OO0O0OO0O0O00O0 ,O00O0O0OO0OO00000 [[OO0000OOO000O0O00 ,"该元素总数量"]].drop_duplicates (OO0000OOO000O0O00 ),on =[OO0000OOO000O0O00 ],how ="left")#line:568
		del O0OO0O0OO0O0O00O0 ["All"]#line:570
		DRAW_make_risk_plot (O0OO0O0OO0O0O00O0 ,OO0000OOO000O0O00 ,[O0O000OOOO000000O for O0O000OOOO000000O in O0OO0O0OO0O0O00O0 .columns if O0O000OOOO000000O !=OO0000OOO000O0O00 ],"关键字趋势图",100 )#line:575
def DRAW_make_risk_plot (O0O0O000O0000OOOO ,OO0000OOO000O0OOO ,OO00O0OOO00O000OO ,O000O0000000O0000 ,O0000O0000O00OOOO ,*O0OOO00O0O00OOOOO ):#line:580
    ""#line:581
    OOO0000O0O00OOO0O =Toplevel ()#line:584
    OOO0000O0O00OOO0O .title (O000O0000000O0000 )#line:585
    O0OOOO00OO00O0OO0 =ttk .Frame (OOO0000O0O00OOO0O ,height =20 )#line:586
    O0OOOO00OO00O0OO0 .pack (side =TOP )#line:587
    OOO0000O000OO0000 =Figure (figsize =(12 ,6 ),dpi =100 )#line:589
    OO0O0OO00OO000OOO =FigureCanvasTkAgg (OOO0000O000OO0000 ,master =OOO0000O0O00OOO0O )#line:590
    OO0O0OO00OO000OOO .draw ()#line:591
    OO0O0OO00OO000OOO .get_tk_widget ().pack (expand =1 )#line:592
    plt .rcParams ["font.sans-serif"]=["SimHei"]#line:594
    plt .rcParams ['axes.unicode_minus']=False #line:595
    O0000000O0O00OOO0 =NavigationToolbar2Tk (OO0O0OO00OO000OOO ,OOO0000O0O00OOO0O )#line:597
    O0000000O0O00OOO0 .update ()#line:598
    OO0O0OO00OO000OOO .get_tk_widget ().pack ()#line:599
    OO0OOO00OOO00OOOO =OOO0000O000OO0000 .add_subplot (111 )#line:601
    OO0OOO00OOO00OOOO .set_title (O000O0000000O0000 )#line:603
    OOO0000OO00OO0OOO =O0O0O000O0000OOOO [OO0000OOO000O0OOO ]#line:604
    if O0000O0000O00OOOO !=999 :#line:607
        OO0OOO00OOO00OOOO .set_xticklabels (OOO0000OO00OO0OOO ,rotation =-90 ,fontsize =8 )#line:608
    O0000O0OO0O0O0OO0 =range (0 ,len (OOO0000OO00OO0OOO ),1 )#line:611
    try :#line:616
        OO0OOO00OOO00OOOO .bar (OOO0000OO00OO0OOO ,O0O0O000O0000OOOO ["报告总数"],color ='skyblue',label ="报告总数")#line:617
        OO0OOO00OOO00OOOO .bar (OOO0000OO00OO0OOO ,height =O0O0O000O0000OOOO ["严重伤害数"],color ="orangered",label ="严重伤害数")#line:618
    except :#line:619
        pass #line:620
    for O0OO000OO0O0OO000 in OO00O0OOO00O000OO :#line:623
        OOO000O0O0OOOO0O0 =O0O0O000O0000OOOO [O0OO000OO0O0OO000 ].astype (float )#line:624
        if O0OO000OO0O0OO000 =="关注区域":#line:626
            OO0OOO00OOO00OOOO .plot (list (OOO0000OO00OO0OOO ),list (OOO000O0O0OOOO0O0 ),label =str (O0OO000OO0O0OO000 ),color ="red")#line:627
        else :#line:628
            OO0OOO00OOO00OOOO .plot (list (OOO0000OO00OO0OOO ),list (OOO000O0O0OOOO0O0 ),label =str (O0OO000OO0O0OO000 ))#line:629
        if O0000O0000O00OOOO ==100 :#line:632
            for OOOOO000OO0000OO0 ,OO00OO000OO0O0O00 in zip (OOO0000OO00OO0OOO ,OOO000O0O0OOOO0O0 ):#line:633
                if OO00OO000OO0O0O00 ==max (OOO000O0O0OOOO0O0 )and OO00OO000OO0O0O00 >=3 :#line:634
                     OO0OOO00OOO00OOOO .text (OOOOO000OO0000OO0 ,OO00OO000OO0O0O00 ,(str (O0OO000OO0O0OO000 )+":"+str (int (OO00OO000OO0O0O00 ))),color ='black',size =8 )#line:635
    try :#line:645
        if O0OOO00O0O00OOOOO [0 ]:#line:646
            OO0O0OO0O000OO00O =O0OOO00O0O00OOOOO [0 ]#line:647
    except :#line:648
        OO0O0OO0O000OO00O ="ucl"#line:649
    if len (OO00O0OOO00O000OO )==1 :#line:651
        if OO0O0OO0O000OO00O =="更多控制线分位数":#line:653
            OOO0OO00O0O0O0OOO =O0O0O000O0000OOOO [OO00O0OOO00O000OO ].astype (float ).values #line:654
            O000OO00O0OO0OOOO =np .where (OOO0OO00O0O0O0OOO >0 ,1 ,0 )#line:655
            O0000OO000000OO00 =np .nonzero (O000OO00O0OO0OOOO )#line:656
            OOO0OO00O0O0O0OOO =OOO0OO00O0O0O0OOO [O0000OO000000OO00 ]#line:657
            O0O0OOOO00OO0000O =np .median (OOO0OO00O0O0O0OOO )#line:658
            OO0O00O00OO0O0OO0 =np .percentile (OOO0OO00O0O0O0OOO ,25 )#line:659
            O0OO0OO0O0OO00OOO =np .percentile (OOO0OO00O0O0O0OOO ,75 )#line:660
            O000000000OO000O0 =O0OO0OO0O0OO00OOO -OO0O00O00OO0O0OO0 #line:661
            OOOOOO00O00OO0OOO =O0OO0OO0O0OO00OOO +1.5 *O000000000OO000O0 #line:662
            O0OOO0OO0O0OOO000 =OO0O00O00OO0O0OO0 -1.5 *O000000000OO000O0 #line:663
            OO0OOO00OOO00OOOO .axhline (O0OOO0OO0O0OOO000 ,color ='c',linestyle ='--',label ='异常下限')#line:666
            OO0OOO00OOO00OOOO .axhline (OO0O00O00OO0O0OO0 ,color ='r',linestyle ='--',label ='第25百分位数')#line:668
            OO0OOO00OOO00OOOO .axhline (O0O0OOOO00OO0000O ,color ='g',linestyle ='--',label ='中位数')#line:669
            OO0OOO00OOO00OOOO .axhline (O0OO0OO0O0OO00OOO ,color ='r',linestyle ='--',label ='第75百分位数')#line:670
            OO0OOO00OOO00OOOO .axhline (OOOOOO00O00OO0OOO ,color ='c',linestyle ='--',label ='异常上限')#line:672
            OOOOOOO0000O00O00 =ttk .Label (OOO0000O0O00OOO0O ,text ="中位数="+str (O0O0OOOO00OO0000O )+"; 第25百分位数="+str (OO0O00O00OO0O0OO0 )+"; 第75百分位数="+str (O0OO0OO0O0OO00OOO )+"; 异常上限(第75百分位数+1.5IQR)="+str (OOOOOO00O00OO0OOO )+"; IQR="+str (O000000000OO000O0 ))#line:673
            OOOOOOO0000O00O00 .pack ()#line:674
        elif OO0O0OO0O000OO00O =="更多控制线STD":#line:676
            OOO0OO00O0O0O0OOO =O0O0O000O0000OOOO [OO00O0OOO00O000OO ].astype (float ).values #line:677
            O000OO00O0OO0OOOO =np .where (OOO0OO00O0O0O0OOO >0 ,1 ,0 )#line:678
            O0000OO000000OO00 =np .nonzero (O000OO00O0OO0OOOO )#line:679
            OOO0OO00O0O0O0OOO =OOO0OO00O0O0O0OOO [O0000OO000000OO00 ]#line:680
            OOOOOOO0O0OO0OO00 =OOO0OO00O0O0O0OOO .mean ()#line:682
            OO00O00O0OO00OOOO =OOO0OO00O0O0O0OOO .std (ddof =1 )#line:683
            OO0000O0OOOO0000O =OOOOOOO0O0OO0OO00 +3 *OO00O00O0OO00OOOO #line:684
            O00OOOOOO000OO0O0 =OO00O00O0OO00OOOO -3 *OO00O00O0OO00OOOO #line:685
            if len (OOO0OO00O0O0O0OOO )<30 :#line:687
                OOOO00OOOO00O000O =st .t .interval (0.95 ,df =len (OOO0OO00O0O0O0OOO )-1 ,loc =np .mean (OOO0OO00O0O0O0OOO ),scale =st .sem (OOO0OO00O0O0O0OOO ))#line:688
            else :#line:689
                OOOO00OOOO00O000O =st .norm .interval (0.95 ,loc =np .mean (OOO0OO00O0O0O0OOO ),scale =st .sem (OOO0OO00O0O0O0OOO ))#line:690
            OOOO00OOOO00O000O =OOOO00OOOO00O000O [1 ]#line:691
            OO0OOO00OOO00OOOO .axhline (OO0000O0OOOO0000O ,color ='r',linestyle ='--',label ='UCL')#line:692
            OO0OOO00OOO00OOOO .axhline (OOOOOOO0O0OO0OO00 +2 *OO00O00O0OO00OOOO ,color ='m',linestyle ='--',label ='μ+2σ')#line:693
            OO0OOO00OOO00OOOO .axhline (OOOOOOO0O0OO0OO00 +OO00O00O0OO00OOOO ,color ='m',linestyle ='--',label ='μ+σ')#line:694
            OO0OOO00OOO00OOOO .axhline (OOOOOOO0O0OO0OO00 ,color ='g',linestyle ='--',label ='CL')#line:695
            OO0OOO00OOO00OOOO .axhline (OOOOOOO0O0OO0OO00 -OO00O00O0OO00OOOO ,color ='m',linestyle ='--',label ='μ-σ')#line:696
            OO0OOO00OOO00OOOO .axhline (OOOOOOO0O0OO0OO00 -2 *OO00O00O0OO00OOOO ,color ='m',linestyle ='--',label ='μ-2σ')#line:697
            OO0OOO00OOO00OOOO .axhline (O00OOOOOO000OO0O0 ,color ='r',linestyle ='--',label ='LCL')#line:698
            OO0OOO00OOO00OOOO .axhline (OOOO00OOOO00O000O ,color ='g',linestyle ='-',label ='95CI')#line:699
            OO00000OOOO0OOO00 =ttk .Label (OOO0000O0O00OOO0O ,text ="mean="+str (OOOOOOO0O0OO0OO00 )+"; std="+str (OO00O00O0OO00OOOO )+"; 99.73%:UCL(μ+3σ)="+str (OO0000O0OOOO0000O )+"; LCL(μ-3σ)="+str (O00OOOOOO000OO0O0 )+"; 95%CI="+str (OOOO00OOOO00O000O ))#line:700
            OO00000OOOO0OOO00 .pack ()#line:701
            OOOOOOO0000O00O00 =ttk .Label (OOO0000O0O00OOO0O ,text ="68.26%:μ+σ="+str (OOOOOOO0O0OO0OO00 +OO00O00O0OO00OOOO )+"; 95.45%:μ+2σ="+str (OOOOOOO0O0OO0OO00 +2 *OO00O00O0OO00OOOO ))#line:703
            OOOOOOO0000O00O00 .pack ()#line:704
        else :#line:706
            OOO0OO00O0O0O0OOO =O0O0O000O0000OOOO [OO00O0OOO00O000OO ].astype (float ).values #line:707
            O000OO00O0OO0OOOO =np .where (OOO0OO00O0O0O0OOO >0 ,1 ,0 )#line:708
            O0000OO000000OO00 =np .nonzero (O000OO00O0OO0OOOO )#line:709
            OOO0OO00O0O0O0OOO =OOO0OO00O0O0O0OOO [O0000OO000000OO00 ]#line:710
            OOOOOOO0O0OO0OO00 =OOO0OO00O0O0O0OOO .mean ()#line:711
            OO00O00O0OO00OOOO =OOO0OO00O0O0O0OOO .std (ddof =1 )#line:712
            OO0000O0OOOO0000O =OOOOOOO0O0OO0OO00 +3 *OO00O00O0OO00OOOO #line:713
            O00OOOOOO000OO0O0 =OO00O00O0OO00OOOO -3 *OO00O00O0OO00OOOO #line:714
            OO0OOO00OOO00OOOO .axhline (OO0000O0OOOO0000O ,color ='r',linestyle ='--',label ='UCL')#line:715
            OO0OOO00OOO00OOOO .axhline (OOOOOOO0O0OO0OO00 ,color ='g',linestyle ='--',label ='CL')#line:716
            OO0OOO00OOO00OOOO .axhline (O00OOOOOO000OO0O0 ,color ='r',linestyle ='--',label ='LCL')#line:717
            OO00000OOOO0OOO00 =ttk .Label (OOO0000O0O00OOO0O ,text ="mean="+str (OOOOOOO0O0OO0OO00 )+"; std="+str (OO00O00O0OO00OOOO )+"; UCL(μ+3σ)="+str (OO0000O0OOOO0000O )+"; LCL(μ-3σ)="+str (O00OOOOOO000OO0O0 ))#line:718
            OO00000OOOO0OOO00 .pack ()#line:719
    OO0OOO00OOO00OOOO .set_title ("控制图")#line:722
    OO0OOO00OOO00OOOO .set_xlabel ("项")#line:723
    OOO0000O000OO0000 .tight_layout (pad =0.4 ,w_pad =3.0 ,h_pad =3.0 )#line:724
    OOO0O0000O00O00OO =OO0OOO00OOO00OOOO .get_position ()#line:725
    OO0OOO00OOO00OOOO .set_position ([OOO0O0000O00O00OO .x0 ,OOO0O0000O00O00OO .y0 ,OOO0O0000O00O00OO .width *0.7 ,OOO0O0000O00O00OO .height ])#line:726
    OO0OOO00OOO00OOOO .legend (loc =2 ,bbox_to_anchor =(1.05 ,1.0 ),fontsize =10 ,borderaxespad =0.0 )#line:727
    O0OO0000O00OOOO00 =StringVar ()#line:730
    OOOO0O000OOOOOO00 =ttk .Combobox (O0OOOO00OO00O0OO0 ,width =15 ,textvariable =O0OO0000O00OOOO00 ,state ='readonly')#line:731
    OOOO0O000OOOOOO00 ['values']=OO00O0OOO00O000OO #line:732
    OOOO0O000OOOOOO00 .pack (side =LEFT )#line:733
    OOOO0O000OOOOOO00 .current (0 )#line:734
    OO0O0OO0000OO0000 =Button (O0OOOO00OO00O0OO0 ,text ="控制图（单项-UCL(μ+3σ)）",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :DRAW_make_risk_plot (O0O0O000O0000OOOO ,OO0000OOO000O0OOO ,[O0O000000O00O000O for O0O000000O00O000O in OO00O0OOO00O000OO if O0OO0000O00OOOO00 .get ()in O0O000000O00O000O ],O000O0000000O0000 ,O0000O0000O00OOOO ))#line:744
    OO0O0OO0000OO0000 .pack (side =LEFT ,anchor ="ne")#line:745
    O000O0O0OO0000O00 =Button (O0OOOO00OO00O0OO0 ,text ="控制图（单项-UCL(标准差法)）",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :DRAW_make_risk_plot (O0O0O000O0000OOOO ,OO0000OOO000O0OOO ,[O0O00O0000O0O0OO0 for O0O00O0000O0O0OO0 in OO00O0OOO00O000OO if O0OO0000O00OOOO00 .get ()in O0O00O0000O0O0OO0 ],O000O0000000O0000 ,O0000O0000O00OOOO ,"更多控制线STD"))#line:753
    O000O0O0OO0000O00 .pack (side =LEFT ,anchor ="ne")#line:754
    O000O0O0OO0000O00 =Button (O0OOOO00OO00O0OO0 ,text ="控制图（单项-分位数）",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :DRAW_make_risk_plot (O0O0O000O0000OOOO ,OO0000OOO000O0OOO ,[OOO0O0OO00OOO0000 for OOO0O0OO00OOO0000 in OO00O0OOO00O000OO if O0OO0000O00OOOO00 .get ()in OOO0O0OO00OOO0000 ],O000O0000000O0000 ,O0000O0000O00OOOO ,"更多控制线分位数"))#line:762
    O000O0O0OO0000O00 .pack (side =LEFT ,anchor ="ne")#line:763
    OO0OOOOOO0OOO00O0 =Button (O0OOOO00OO00O0OO0 ,text ="去除标记",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :DRAW_make_risk_plot (O0O0O000O0000OOOO ,OO0000OOO000O0OOO ,OO00O0OOO00O000OO ,O000O0000000O0000 ,0 ))#line:772
    OO0OOOOOO0OOO00O0 .pack (side =LEFT ,anchor ="ne")#line:774
    OO0O0OO00OO000OOO .draw ()#line:775
def DRAW_make_one (OO0O0O0OOO0OOO00O ,OOO00OOOOOOOO0O00 ,O00O0O0O000O0O0OO ,O0OOO00O00O0O0O00 ,O00O0OO0O0O00O0O0 ):#line:779
    ""#line:780
    warnings .filterwarnings ("ignore")#line:781
    O0OOOOO0O0O00O0O0 =Toplevel ()#line:782
    O0OOOOO0O0O00O0O0 .title (OOO00OOOOOOOO0O00 )#line:783
    O00000OO0O0000O00 =ttk .Frame (O0OOOOO0O0O00O0O0 ,height =20 )#line:784
    O00000OO0O0000O00 .pack (side =TOP )#line:785
    O000O00O0OO000OOO =Figure (figsize =(12 ,6 ),dpi =100 )#line:787
    O0O0OOO0OOOO00O00 =FigureCanvasTkAgg (O000O00O0OO000OOO ,master =O0OOOOO0O0O00O0O0 )#line:788
    O0O0OOO0OOOO00O00 .draw ()#line:789
    O0O0OOO0OOOO00O00 .get_tk_widget ().pack (expand =1 )#line:790
    OOO0O0000O0O0O00O =O000O00O0OO000OOO .add_subplot (111 )#line:791
    plt .rcParams ["font.sans-serif"]=["SimHei"]#line:793
    plt .rcParams ['axes.unicode_minus']=False #line:794
    O000O000000OOOO0O =NavigationToolbar2Tk (O0O0OOO0OOOO00O00 ,O0OOOOO0O0O00O0O0 )#line:796
    O000O000000OOOO0O .update ()#line:797
    O0O0OOO0OOOO00O00 .get_tk_widget ().pack ()#line:799
    try :#line:802
        O0O00O00O0000000O =OO0O0O0OOO0OOO00O .columns #line:803
        OO0O0O0OOO0OOO00O =OO0O0O0OOO0OOO00O .sort_values (by =O0OOO00O00O0O0O00 ,ascending =[False ],na_position ="last")#line:804
    except :#line:805
        O00O000O0O00O000O =eval (OO0O0O0OOO0OOO00O )#line:806
        O00O000O0O00O000O =pd .DataFrame .from_dict (O00O000O0O00O000O ,orient =O00O0O0O000O0O0OO ,columns =[O0OOO00O00O0O0O00 ]).reset_index ()#line:809
        OO0O0O0OOO0OOO00O =O00O000O0O00O000O .sort_values (by =O0OOO00O00O0O0O00 ,ascending =[False ],na_position ="last")#line:810
    if ("日期"in OOO00OOOOOOOO0O00 or "时间"in OOO00OOOOOOOO0O00 or "季度"in OOO00OOOOOOOO0O00 )and "饼图"not in O00O0OO0O0O00O0O0 :#line:814
        OO0O0O0OOO0OOO00O [O00O0O0O000O0O0OO ]=pd .to_datetime (OO0O0O0OOO0OOO00O [O00O0O0O000O0O0OO ],format ="%Y/%m/%d").dt .date #line:815
        OO0O0O0OOO0OOO00O =OO0O0O0OOO0OOO00O .sort_values (by =O00O0O0O000O0O0OO ,ascending =[True ],na_position ="last")#line:816
    elif "批号"in OOO00OOOOOOOO0O00 :#line:817
        OO0O0O0OOO0OOO00O [O00O0O0O000O0O0OO ]=OO0O0O0OOO0OOO00O [O00O0O0O000O0O0OO ].astype (str )#line:818
        OO0O0O0OOO0OOO00O =OO0O0O0OOO0OOO00O .sort_values (by =O00O0O0O000O0O0OO ,ascending =[True ],na_position ="last")#line:819
        OOO0O0000O0O0O00O .set_xticklabels (OO0O0O0OOO0OOO00O [O00O0O0O000O0O0OO ],rotation =-90 ,fontsize =8 )#line:820
    else :#line:821
        OO0O0O0OOO0OOO00O [O00O0O0O000O0O0OO ]=OO0O0O0OOO0OOO00O [O00O0O0O000O0O0OO ].astype (str )#line:822
        OOO0O0000O0O0O00O .set_xticklabels (OO0O0O0OOO0OOO00O [O00O0O0O000O0O0OO ],rotation =-90 ,fontsize =8 )#line:823
    O0O0OO0000O0OOOOO =OO0O0O0OOO0OOO00O [O0OOO00O00O0O0O00 ]#line:825
    O0O00O00000OO0O0O =range (0 ,len (O0O0OO0000O0OOOOO ),1 )#line:826
    OOO0O0000O0O0O00O .set_title (OOO00OOOOOOOO0O00 )#line:828
    if O00O0OO0O0O00O0O0 =="柱状图":#line:832
        OOO0O0000O0O0O00O .bar (x =OO0O0O0OOO0OOO00O [O00O0O0O000O0O0OO ],height =O0O0OO0000O0OOOOO ,width =0.2 ,color ="#87CEFA")#line:833
    elif O00O0OO0O0O00O0O0 =="饼图":#line:834
        OOO0O0000O0O0O00O .pie (x =O0O0OO0000O0OOOOO ,labels =OO0O0O0OOO0OOO00O [O00O0O0O000O0O0OO ],autopct ="%0.2f%%")#line:835
    elif O00O0OO0O0O00O0O0 =="折线图":#line:836
        OOO0O0000O0O0O00O .plot (OO0O0O0OOO0OOO00O [O00O0O0O000O0O0OO ],O0O0OO0000O0OOOOO ,lw =0.5 ,ls ='-',c ="r",alpha =0.5 )#line:837
    elif "托帕斯图"in str (O00O0OO0O0O00O0O0 ):#line:839
        O0OOOOO0O000OOOOO =OO0O0O0OOO0OOO00O [O0OOO00O00O0O0O00 ].fillna (0 )#line:840
        OO0O00OO000OO00O0 =O0OOOOO0O000OOOOO .cumsum ()/O0OOOOO0O000OOOOO .sum ()*100 #line:844
        OOO0O00OOOO00OOO0 =OO0O00OO000OO00O0 [OO0O00OO000OO00O0 >0.8 ].index [0 ]#line:846
        O0OO0000O0O000O00 =O0OOOOO0O000OOOOO .index .tolist ().index (OOO0O00OOOO00OOO0 )#line:847
        OOO0O0000O0O0O00O .bar (x =OO0O0O0OOO0OOO00O [O00O0O0O000O0O0OO ],height =O0OOOOO0O000OOOOO ,color ="C0",label =O0OOO00O00O0O0O00 )#line:851
        O00OO00OOO00O00OO =OOO0O0000O0O0O00O .twinx ()#line:852
        O00OO00OOO00O00OO .plot (OO0O0O0OOO0OOO00O [O00O0O0O000O0O0OO ],OO0O00OO000OO00O0 ,color ="C1",alpha =0.6 ,label ="累计比例")#line:853
        O00OO00OOO00O00OO .yaxis .set_major_formatter (PercentFormatter ())#line:854
        OOO0O0000O0O0O00O .tick_params (axis ="y",colors ="C0")#line:859
        O00OO00OOO00O00OO .tick_params (axis ="y",colors ="C1")#line:860
        if "超级托帕斯图"in str (O00O0OO0O0O00O0O0 ):#line:863
            OO000000OO0000O0O =re .compile (r'[(](.*?)[)]',re .S )#line:864
            O0OO000000OOO0O00 =re .findall (OO000000OO0000O0O ,O00O0OO0O0O00O0O0 )[0 ]#line:865
            OOO0O0000O0O0O00O .bar (x =OO0O0O0OOO0OOO00O [O00O0O0O000O0O0OO ],height =OO0O0O0OOO0OOO00O [O0OO000000OOO0O00 ],color ="orangered",label =O0OO000000OOO0O00 )#line:866
    O000O00O0OO000OOO .tight_layout (pad =0.4 ,w_pad =3.0 ,h_pad =3.0 )#line:868
    OO000OOO0OOOOO000 =OOO0O0000O0O0O00O .get_position ()#line:869
    OOO0O0000O0O0O00O .set_position ([OO000OOO0OOOOO000 .x0 ,OO000OOO0OOOOO000 .y0 ,OO000OOO0OOOOO000 .width *0.7 ,OO000OOO0OOOOO000 .height ])#line:870
    OOO0O0000O0O0O00O .legend (loc =2 ,bbox_to_anchor =(1.05 ,1.0 ),fontsize =10 ,borderaxespad =0.0 )#line:871
    O0O0OOO0OOOO00O00 .draw ()#line:874
    if len (O0O0OO0000O0OOOOO )<=20 and O00O0OO0O0O00O0O0 !="饼图":#line:877
        for O000O0O000OO0O0OO ,O0O0O00O0O0OOOO0O in zip (O0O00O00000OO0O0O ,O0O0OO0000O0OOOOO ):#line:878
            OO000O0O00OOOOOOO =str (O0O0O00O0O0OOOO0O )#line:879
            O00OOOO0OO0000OOO =(O000O0O000OO0O0OO ,O0O0O00O0O0OOOO0O +0.3 )#line:880
            OOO0O0000O0O0O00O .annotate (OO000O0O00OOOOOOO ,xy =O00OOOO0OO0000OOO ,fontsize =8 ,color ="black",ha ="center",va ="baseline")#line:881
    O00OO00000000OO0O =Button (O00000OO0O0000O00 ,relief =GROOVE ,activebackground ="green",text ="保存原始数据",command =lambda :TOOLS_save_dict (OO0O0O0OOO0OOO00O ),)#line:891
    O00OO00000000OO0O .pack (side =RIGHT )#line:892
    O0OO00O0O0OO00000 =Button (O00000OO0O0000O00 ,relief =GROOVE ,text ="查看原始数据",command =lambda :TOOLS_view_dict (OO0O0O0OOO0OOO00O ,0 ))#line:896
    O0OO00O0O0OO00000 .pack (side =RIGHT )#line:897
    OO0OOOO0O00O0OOOO =Button (O00000OO0O0000O00 ,relief =GROOVE ,text ="饼图",command =lambda :DRAW_make_one (OO0O0O0OOO0OOO00O ,OOO00OOOOOOOO0O00 ,O00O0O0O000O0O0OO ,O0OOO00O00O0O0O00 ,"饼图"),)#line:905
    OO0OOOO0O00O0OOOO .pack (side =LEFT )#line:906
    OO0OOOO0O00O0OOOO =Button (O00000OO0O0000O00 ,relief =GROOVE ,text ="柱状图",command =lambda :DRAW_make_one (OO0O0O0OOO0OOO00O ,OOO00OOOOOOOO0O00 ,O00O0O0O000O0O0OO ,O0OOO00O00O0O0O00 ,"柱状图"),)#line:913
    OO0OOOO0O00O0OOOO .pack (side =LEFT )#line:914
    OO0OOOO0O00O0OOOO =Button (O00000OO0O0000O00 ,relief =GROOVE ,text ="折线图",command =lambda :DRAW_make_one (OO0O0O0OOO0OOO00O ,OOO00OOOOOOOO0O00 ,O00O0O0O000O0O0OO ,O0OOO00O00O0O0O00 ,"折线图"),)#line:920
    OO0OOOO0O00O0OOOO .pack (side =LEFT )#line:921
    OO0OOOO0O00O0OOOO =Button (O00000OO0O0000O00 ,relief =GROOVE ,text ="托帕斯图",command =lambda :DRAW_make_one (OO0O0O0OOO0OOO00O ,OOO00OOOOOOOO0O00 ,O00O0O0O000O0O0OO ,O0OOO00O00O0O0O00 ,"托帕斯图"),)#line:928
    OO0OOOO0O00O0OOOO .pack (side =LEFT )#line:929
def DRAW_make_mutibar (O0O0OOOO0OOOOO0O0 ,O0OO0000O0O0O00O0 ,OO0000OOOOOOO0O00 ,O0OOO0000OOO00OOO ,OO00O0O00O000O0O0 ,OOOOO0O00OO0OO0O0 ,OO0OO00O0OO0OOO0O ):#line:930
    ""#line:931
    OOOO0O0O0OOO000O0 =Toplevel ()#line:932
    OOOO0O0O0OOO000O0 .title (OO0OO00O0OO0OOO0O )#line:933
    O0OOOO000OOOO000O =ttk .Frame (OOOO0O0O0OOO000O0 ,height =20 )#line:934
    O0OOOO000OOOO000O .pack (side =TOP )#line:935
    O0OO000OO0O00000O =0.2 #line:937
    O0O000OO00O0O00OO =Figure (figsize =(12 ,6 ),dpi =100 )#line:938
    OOOOOOO00000O0OO0 =FigureCanvasTkAgg (O0O000OO00O0O00OO ,master =OOOO0O0O0OOO000O0 )#line:939
    OOOOOOO00000O0OO0 .draw ()#line:940
    OOOOOOO00000O0OO0 .get_tk_widget ().pack (expand =1 )#line:941
    OO00000000OO00O0O =O0O000OO00O0O00OO .add_subplot (111 )#line:942
    plt .rcParams ["font.sans-serif"]=["SimHei"]#line:944
    plt .rcParams ['axes.unicode_minus']=False #line:945
    O0OO00OOOO00000O0 =NavigationToolbar2Tk (OOOOOOO00000O0OO0 ,OOOO0O0O0OOO000O0 )#line:947
    O0OO00OOOO00000O0 .update ()#line:948
    OOOOOOO00000O0OO0 .get_tk_widget ().pack ()#line:950
    O0OO0000O0O0O00O0 =O0O0OOOO0OOOOO0O0 [O0OO0000O0O0O00O0 ]#line:951
    OO0000OOOOOOO0O00 =O0O0OOOO0OOOOO0O0 [OO0000OOOOOOO0O00 ]#line:952
    O0OOO0000OOO00OOO =O0O0OOOO0OOOOO0O0 [O0OOO0000OOO00OOO ]#line:953
    O00OOO00000OOOOOO =range (0 ,len (O0OO0000O0O0O00O0 ),1 )#line:955
    OO00000000OO00O0O .set_xticklabels (O0OOO0000OOO00OOO ,rotation =-90 ,fontsize =8 )#line:956
    OO00000000OO00O0O .bar (O00OOO00000OOOOOO ,O0OO0000O0O0O00O0 ,align ="center",tick_label =O0OOO0000OOO00OOO ,label =OO00O0O00O000O0O0 )#line:959
    OO00000000OO00O0O .bar (O00OOO00000OOOOOO ,OO0000OOOOOOO0O00 ,align ="center",label =OOOOO0O00OO0OO0O0 )#line:962
    OO00000000OO00O0O .set_title (OO0OO00O0OO0OOO0O )#line:963
    OO00000000OO00O0O .set_xlabel ("项")#line:964
    OO00000000OO00O0O .set_ylabel ("数量")#line:965
    O0O000OO00O0O00OO .tight_layout (pad =0.4 ,w_pad =3.0 ,h_pad =3.0 )#line:967
    O0000OO00O0O0OOOO =OO00000000OO00O0O .get_position ()#line:968
    OO00000000OO00O0O .set_position ([O0000OO00O0O0OOOO .x0 ,O0000OO00O0O0OOOO .y0 ,O0000OO00O0O0OOOO .width *0.7 ,O0000OO00O0O0OOOO .height ])#line:969
    OO00000000OO00O0O .legend (loc =2 ,bbox_to_anchor =(1.05 ,1.0 ),fontsize =10 ,borderaxespad =0.0 )#line:970
    OOOOOOO00000O0OO0 .draw ()#line:972
    O000OOOOO00000OO0 =Button (O0OOOO000OOOO000O ,relief =GROOVE ,activebackground ="green",text ="保存原始数据",command =lambda :TOOLS_save_dict (O0O0OOOO0OOOOO0O0 ),)#line:979
    O000OOOOO00000OO0 .pack (side =RIGHT )#line:980
def CLEAN_hzp (OO000000000O0OOO0 ):#line:985
    ""#line:986
    if "报告编码"not in OO000000000O0OOO0 .columns :#line:987
            OO000000000O0OOO0 ["特殊化妆品注册证书编号/普通化妆品备案编号"]=OO000000000O0OOO0 ["特殊化妆品注册证书编号/普通化妆品备案编号"].fillna ("-未填写-")#line:988
            OO000000000O0OOO0 ["省级评价结果"]=OO000000000O0OOO0 ["省级评价结果"].fillna ("-未填写-")#line:989
            OO000000000O0OOO0 ["生产企业"]=OO000000000O0OOO0 ["生产企业"].fillna ("-未填写-")#line:990
            OO000000000O0OOO0 ["提交人"]="不适用"#line:991
            OO000000000O0OOO0 ["医疗机构类别"]="不适用"#line:992
            OO000000000O0OOO0 ["经营企业或使用单位"]="不适用"#line:993
            OO000000000O0OOO0 ["报告状态"]="报告单位评价"#line:994
            OO000000000O0OOO0 ["所属地区"]="不适用"#line:995
            OO000000000O0OOO0 ["医院名称"]="不适用"#line:996
            OO000000000O0OOO0 ["报告地区名称"]="不适用"#line:997
            OO000000000O0OOO0 ["提交人"]="不适用"#line:998
            OO000000000O0OOO0 ["型号"]=OO000000000O0OOO0 ["化妆品分类"]#line:999
            OO000000000O0OOO0 ["关联性评价"]=OO000000000O0OOO0 ["上报单位评价结果"]#line:1000
            OO000000000O0OOO0 ["规格"]="不适用"#line:1001
            OO000000000O0OOO0 ["器械故障表现"]=OO000000000O0OOO0 ["初步判断"]#line:1002
            OO000000000O0OOO0 ["伤害表现"]=OO000000000O0OOO0 ["自觉症状"]+OO000000000O0OOO0 ["皮损部位"]+OO000000000O0OOO0 ["皮损形态"]#line:1003
            OO000000000O0OOO0 ["事件原因分析"]="不适用"#line:1004
            OO000000000O0OOO0 ["事件原因分析描述"]="不适用"#line:1005
            OO000000000O0OOO0 ["调查情况"]="不适用"#line:1006
            OO000000000O0OOO0 ["具体控制措施"]="不适用"#line:1007
            OO000000000O0OOO0 ["未采取控制措施原因"]="不适用"#line:1008
            OO000000000O0OOO0 ["报告地区名称"]="不适用"#line:1009
            OO000000000O0OOO0 ["上报单位所属地区"]="不适用"#line:1010
            OO000000000O0OOO0 ["持有人报告状态"]="不适用"#line:1011
            OO000000000O0OOO0 ["年龄类型"]="岁"#line:1012
            OO000000000O0OOO0 ["经营企业使用单位报告状态"]="不适用"#line:1013
            OO000000000O0OOO0 ["产品归属"]="化妆品"#line:1014
            OO000000000O0OOO0 ["管理类别"]="不适用"#line:1015
            OO000000000O0OOO0 ["超时标记"]="不适用"#line:1016
            OO000000000O0OOO0 =OO000000000O0OOO0 .rename (columns ={"报告表编号":"报告编码","报告类型":"伤害","报告地区":"监测机构","报告单位名称":"单位名称","患者/消费者姓名":"姓名","不良反应发生日期":"事件发生日期","过程描述补充说明":"使用过程","化妆品名称":"产品名称","化妆品分类":"产品类别","生产企业":"上市许可持有人名称","生产批号":"产品批号","特殊化妆品注册证书编号/普通化妆品备案编号":"注册证编号/曾用注册证编号",})#line:1035
            OO000000000O0OOO0 ["时隔"]=pd .to_datetime (OO000000000O0OOO0 ["事件发生日期"])-pd .to_datetime (OO000000000O0OOO0 ["开始使用日期"])#line:1036
            OO000000000O0OOO0 .loc [(OO000000000O0OOO0 ["省级评价结果"]!="-未填写-"),"有效报告"]=1 #line:1037
            OO000000000O0OOO0 ["伤害"]=OO000000000O0OOO0 ["伤害"].str .replace ("严重","严重伤害",regex =False )#line:1038
            try :#line:1039
	            OO000000000O0OOO0 =TOOL_guizheng (OO000000000O0OOO0 ,4 ,True )#line:1040
            except :#line:1041
                pass #line:1042
            return OO000000000O0OOO0 #line:1043
def CLEAN_yp (O000000O0O0O0OOO0 ):#line:1048
    ""#line:1049
    if "报告编码"not in O000000O0O0O0OOO0 .columns :#line:1050
        if "反馈码"in O000000O0O0O0OOO0 .columns and "报告表编码"not in O000000O0O0O0OOO0 .columns :#line:1052
            O000000O0O0O0OOO0 ["提交人"]="不适用"#line:1054
            O000000O0O0O0OOO0 ["经营企业或使用单位"]="不适用"#line:1055
            O000000O0O0O0OOO0 ["报告状态"]="报告单位评价"#line:1056
            O000000O0O0O0OOO0 ["所属地区"]="不适用"#line:1057
            O000000O0O0O0OOO0 ["产品类别"]="无源"#line:1058
            O000000O0O0O0OOO0 ["医院名称"]="不适用"#line:1059
            O000000O0O0O0OOO0 ["报告地区名称"]="不适用"#line:1060
            O000000O0O0O0OOO0 ["提交人"]="不适用"#line:1061
            O000000O0O0O0OOO0 =O000000O0O0O0OOO0 .rename (columns ={"反馈码":"报告表编码","序号":"药品序号","新的":"报告类型-新的","报告类型":"报告类型-严重程度","用药-日数":"用法-日","用药-次数":"用法-次",})#line:1074
        if "唯一标识"not in O000000O0O0O0OOO0 .columns :#line:1079
            O000000O0O0O0OOO0 ["报告编码"]=O000000O0O0O0OOO0 ["报告表编码"].astype (str )+O000000O0O0O0OOO0 ["患者姓名"].astype (str )#line:1080
        if "唯一标识"in O000000O0O0O0OOO0 .columns :#line:1081
            O000000O0O0O0OOO0 ["唯一标识"]=O000000O0O0O0OOO0 ["唯一标识"].astype (str )#line:1082
            O000000O0O0O0OOO0 =O000000O0O0O0OOO0 .rename (columns ={"唯一标识":"报告编码"})#line:1083
        if "医疗机构类别"not in O000000O0O0O0OOO0 .columns :#line:1084
            O000000O0O0O0OOO0 ["医疗机构类别"]="医疗机构"#line:1085
            O000000O0O0O0OOO0 ["经营企业使用单位报告状态"]="已提交"#line:1086
        try :#line:1087
            O000000O0O0O0OOO0 ["年龄和单位"]=O000000O0O0O0OOO0 ["年龄"].astype (str )+O000000O0O0O0OOO0 ["年龄单位"]#line:1088
        except :#line:1089
            O000000O0O0O0OOO0 ["年龄和单位"]=O000000O0O0O0OOO0 ["年龄"].astype (str )+O000000O0O0O0OOO0 ["年龄类型"]#line:1090
        O000000O0O0O0OOO0 .loc [(O000000O0O0O0OOO0 ["报告类型-新的"]=="新的"),"管理类别"]="Ⅲ类"#line:1091
        O000000O0O0O0OOO0 .loc [(O000000O0O0O0OOO0 ["报告类型-严重程度"]=="严重"),"管理类别"]="Ⅲ类"#line:1092
        text .insert (END ,"剔除已删除报告和重复报告...")#line:1093
        if "删除标识"in O000000O0O0O0OOO0 .columns :#line:1094
            O000000O0O0O0OOO0 =O000000O0O0O0OOO0 [(O000000O0O0O0OOO0 ["删除标识"]!="删除")]#line:1095
        if "重复报告"in O000000O0O0O0OOO0 .columns :#line:1096
            O000000O0O0O0OOO0 =O000000O0O0O0OOO0 [(O000000O0O0O0OOO0 ["重复报告"]!="重复报告")]#line:1097
        O000000O0O0O0OOO0 ["报告类型-新的"]=O000000O0O0O0OOO0 ["报告类型-新的"].fillna (" ")#line:1100
        O000000O0O0O0OOO0 .loc [(O000000O0O0O0OOO0 ["报告类型-严重程度"]=="严重"),"伤害"]="严重伤害"#line:1101
        O000000O0O0O0OOO0 ["伤害"]=O000000O0O0O0OOO0 ["伤害"].fillna ("所有一般")#line:1102
        O000000O0O0O0OOO0 ["伤害PSUR"]=O000000O0O0O0OOO0 ["报告类型-新的"].astype (str )+O000000O0O0O0OOO0 ["报告类型-严重程度"].astype (str )#line:1103
        O000000O0O0O0OOO0 ["用量用量单位"]=O000000O0O0O0OOO0 ["用量"].astype (str )+O000000O0O0O0OOO0 ["用量单位"].astype (str )#line:1104
        O000000O0O0O0OOO0 ["规格"]="不适用"#line:1106
        O000000O0O0O0OOO0 ["事件原因分析"]="不适用"#line:1107
        O000000O0O0O0OOO0 ["事件原因分析描述"]="不适用"#line:1108
        O000000O0O0O0OOO0 ["初步处置情况"]="不适用"#line:1109
        O000000O0O0O0OOO0 ["伤害表现"]=O000000O0O0O0OOO0 ["不良反应名称"]#line:1110
        O000000O0O0O0OOO0 ["产品类别"]="无源"#line:1111
        O000000O0O0O0OOO0 ["调查情况"]="不适用"#line:1112
        O000000O0O0O0OOO0 ["具体控制措施"]="不适用"#line:1113
        O000000O0O0O0OOO0 ["上报单位所属地区"]=O000000O0O0O0OOO0 ["报告地区名称"]#line:1114
        O000000O0O0O0OOO0 ["未采取控制措施原因"]="不适用"#line:1115
        O000000O0O0O0OOO0 ["报告单位评价"]=O000000O0O0O0OOO0 ["报告类型-新的"].astype (str )+O000000O0O0O0OOO0 ["报告类型-严重程度"].astype (str )#line:1116
        O000000O0O0O0OOO0 .loc [(O000000O0O0O0OOO0 ["报告类型-新的"]=="新的"),"持有人报告状态"]="待评价"#line:1117
        O000000O0O0O0OOO0 ["用法temp日"]="日"#line:1118
        O000000O0O0O0OOO0 ["用法temp次"]="次"#line:1119
        O000000O0O0O0OOO0 ["用药频率"]=(O000000O0O0O0OOO0 ["用法-日"].astype (str )+O000000O0O0O0OOO0 ["用法temp日"]+O000000O0O0O0OOO0 ["用法-次"].astype (str )+O000000O0O0O0OOO0 ["用法temp次"])#line:1125
        try :#line:1126
            O000000O0O0O0OOO0 ["相关疾病信息[疾病名称]-术语"]=O000000O0O0O0OOO0 ["原患疾病"]#line:1127
            O000000O0O0O0OOO0 ["治疗适应症-术语"]=O000000O0O0O0OOO0 ["用药原因"]#line:1128
        except :#line:1129
            pass #line:1130
        try :#line:1132
            O000000O0O0O0OOO0 =O000000O0O0O0OOO0 .rename (columns ={"提交日期":"报告日期"})#line:1133
            O000000O0O0O0OOO0 =O000000O0O0O0OOO0 .rename (columns ={"提交人":"报告人"})#line:1134
            O000000O0O0O0OOO0 =O000000O0O0O0OOO0 .rename (columns ={"报告状态":"持有人报告状态"})#line:1135
            O000000O0O0O0OOO0 =O000000O0O0O0OOO0 .rename (columns ={"所属地区":"使用单位、经营企业所属监测机构"})#line:1136
            O000000O0O0O0OOO0 =O000000O0O0O0OOO0 .rename (columns ={"医院名称":"单位名称"})#line:1137
            O000000O0O0O0OOO0 =O000000O0O0O0OOO0 .rename (columns ={"批准文号":"注册证编号/曾用注册证编号"})#line:1138
            O000000O0O0O0OOO0 =O000000O0O0O0OOO0 .rename (columns ={"通用名称":"产品名称"})#line:1139
            O000000O0O0O0OOO0 =O000000O0O0O0OOO0 .rename (columns ={"生产厂家":"上市许可持有人名称"})#line:1140
            O000000O0O0O0OOO0 =O000000O0O0O0OOO0 .rename (columns ={"不良反应发生时间":"事件发生日期"})#line:1141
            O000000O0O0O0OOO0 =O000000O0O0O0OOO0 .rename (columns ={"不良反应名称":"器械故障表现"})#line:1142
            O000000O0O0O0OOO0 =O000000O0O0O0OOO0 .rename (columns ={"不良反应过程描述":"使用过程"})#line:1143
            O000000O0O0O0OOO0 =O000000O0O0O0OOO0 .rename (columns ={"生产批号":"产品批号"})#line:1144
            O000000O0O0O0OOO0 =O000000O0O0O0OOO0 .rename (columns ={"报告地区名称":"使用单位、经营企业所属监测机构"})#line:1145
            O000000O0O0O0OOO0 =O000000O0O0O0OOO0 .rename (columns ={"剂型":"型号"})#line:1146
            O000000O0O0O0OOO0 =O000000O0O0O0OOO0 .rename (columns ={"报告人评价":"关联性评价"})#line:1147
            O000000O0O0O0OOO0 =O000000O0O0O0OOO0 .rename (columns ={"年龄单位":"年龄类型"})#line:1148
        except :#line:1149
            text .insert (END ,"数据规整失败。")#line:1150
            return 0 #line:1151
        O000000O0O0O0OOO0 ['报告日期']=O000000O0O0O0OOO0 ['报告日期'].str .strip ()#line:1154
        O000000O0O0O0OOO0 ['事件发生日期']=O000000O0O0O0OOO0 ['事件发生日期'].str .strip ()#line:1155
        O000000O0O0O0OOO0 ['用药开始时间']=O000000O0O0O0OOO0 ['用药开始时间'].str .strip ()#line:1156
        return O000000O0O0O0OOO0 #line:1158
    if "报告编码"in O000000O0O0O0OOO0 .columns :#line:1159
        return O000000O0O0O0OOO0 #line:1160
def CLEAN_qx (O00O00000OOO0OOOO ):#line:1162
		""#line:1163
		if "使用单位、经营企业所属监测机构"not in O00O00000OOO0OOOO .columns and "监测机构"not in O00O00000OOO0OOOO .columns :#line:1165
			O00O00000OOO0OOOO ["使用单位、经营企业所属监测机构"]="本地"#line:1166
		if "上市许可持有人名称"not in O00O00000OOO0OOOO .columns :#line:1167
			O00O00000OOO0OOOO ["上市许可持有人名称"]=O00O00000OOO0OOOO ["单位名称"]#line:1168
		if "注册证编号/曾用注册证编号"not in O00O00000OOO0OOOO .columns :#line:1169
			O00O00000OOO0OOOO ["注册证编号/曾用注册证编号"]=O00O00000OOO0OOOO ["注册证编号"]#line:1170
		if "事件原因分析描述"not in O00O00000OOO0OOOO .columns :#line:1171
			O00O00000OOO0OOOO ["事件原因分析描述"]="  "#line:1172
		if "初步处置情况"not in O00O00000OOO0OOOO .columns :#line:1173
			O00O00000OOO0OOOO ["初步处置情况"]="  "#line:1174
		text .insert (END ,"\n正在执行格式规整和增加有关时间、年龄、性别等统计列...")#line:1177
		O00O00000OOO0OOOO =O00O00000OOO0OOOO .rename (columns ={"使用单位、经营企业所属监测机构":"监测机构"})#line:1178
		O00O00000OOO0OOOO ["报告编码"]=O00O00000OOO0OOOO ["报告编码"].astype ("str")#line:1179
		O00O00000OOO0OOOO ["产品批号"]=O00O00000OOO0OOOO ["产品批号"].astype ("str")#line:1180
		O00O00000OOO0OOOO ["型号"]=O00O00000OOO0OOOO ["型号"].astype ("str")#line:1181
		O00O00000OOO0OOOO ["规格"]=O00O00000OOO0OOOO ["规格"].astype ("str")#line:1182
		O00O00000OOO0OOOO ["注册证编号/曾用注册证编号"]=O00O00000OOO0OOOO ["注册证编号/曾用注册证编号"].str .replace ("(","（",regex =False )#line:1183
		O00O00000OOO0OOOO ["注册证编号/曾用注册证编号"]=O00O00000OOO0OOOO ["注册证编号/曾用注册证编号"].str .replace (")","）",regex =False )#line:1184
		O00O00000OOO0OOOO ["注册证编号/曾用注册证编号"]=O00O00000OOO0OOOO ["注册证编号/曾用注册证编号"].str .replace ("*","※",regex =False )#line:1185
		O00O00000OOO0OOOO ["注册证编号/曾用注册证编号"]=O00O00000OOO0OOOO ["注册证编号/曾用注册证编号"].fillna ("-未填写-")#line:1186
		O00O00000OOO0OOOO ["产品名称"]=O00O00000OOO0OOOO ["产品名称"].str .replace ("*","※",regex =False )#line:1187
		O00O00000OOO0OOOO ["产品批号"]=O00O00000OOO0OOOO ["产品批号"].str .replace ("(","（",regex =False )#line:1188
		O00O00000OOO0OOOO ["产品批号"]=O00O00000OOO0OOOO ["产品批号"].str .replace (")","）",regex =False )#line:1189
		O00O00000OOO0OOOO ["产品批号"]=O00O00000OOO0OOOO ["产品批号"].str .replace ("*","※",regex =False )#line:1190
		O00O00000OOO0OOOO ["上市许可持有人名称"]=O00O00000OOO0OOOO ["上市许可持有人名称"].fillna ("-未填写-")#line:1194
		O00O00000OOO0OOOO ["产品类别"]=O00O00000OOO0OOOO ["产品类别"].fillna ("-未填写-")#line:1195
		O00O00000OOO0OOOO ["产品名称"]=O00O00000OOO0OOOO ["产品名称"].fillna ("-未填写-")#line:1196
		O00O00000OOO0OOOO ["注册证编号/曾用注册证编号"]=O00O00000OOO0OOOO ["注册证编号/曾用注册证编号"].fillna ("-未填写-")#line:1197
		O00O00000OOO0OOOO ["产品批号"]=O00O00000OOO0OOOO ["产品批号"].fillna ("-未填写-")#line:1198
		O00O00000OOO0OOOO ["型号"]=O00O00000OOO0OOOO ["型号"].fillna ("-未填写-")#line:1199
		O00O00000OOO0OOOO ["规格"]=O00O00000OOO0OOOO ["规格"].fillna ("-未填写-")#line:1200
		O00O00000OOO0OOOO ["伤害与评价"]=O00O00000OOO0OOOO ["伤害"]+O00O00000OOO0OOOO ["持有人报告状态"]#line:1203
		O00O00000OOO0OOOO ["注册证备份"]=O00O00000OOO0OOOO ["注册证编号/曾用注册证编号"]#line:1204
		O00O00000OOO0OOOO ['报告日期']=pd .to_datetime (O00O00000OOO0OOOO ['报告日期'],format ='%Y-%m-%d',errors ='coerce')#line:1207
		O00O00000OOO0OOOO ['事件发生日期']=pd .to_datetime (O00O00000OOO0OOOO ['事件发生日期'],format ='%Y-%m-%d',errors ='coerce')#line:1208
		O00O00000OOO0OOOO ["报告月份"]=O00O00000OOO0OOOO ["报告日期"].dt .to_period ("M").astype (str )#line:1210
		O00O00000OOO0OOOO ["报告季度"]=O00O00000OOO0OOOO ["报告日期"].dt .to_period ("Q").astype (str )#line:1211
		O00O00000OOO0OOOO ["报告年份"]=O00O00000OOO0OOOO ["报告日期"].dt .to_period ("Y").astype (str )#line:1212
		O00O00000OOO0OOOO ["事件发生月份"]=O00O00000OOO0OOOO ["事件发生日期"].dt .to_period ("M").astype (str )#line:1213
		O00O00000OOO0OOOO ["事件发生季度"]=O00O00000OOO0OOOO ["事件发生日期"].dt .to_period ("Q").astype (str )#line:1214
		O00O00000OOO0OOOO ["事件发生年份"]=O00O00000OOO0OOOO ["事件发生日期"].dt .to_period ("Y").astype (str )#line:1215
		if ini ["模式"]=="器械":#line:1219
			O00O00000OOO0OOOO ['发现或获知日期']=pd .to_datetime (O00O00000OOO0OOOO ['发现或获知日期'],format ='%Y-%m-%d',errors ='coerce')#line:1220
			O00O00000OOO0OOOO ["时隔"]=pd .to_datetime (O00O00000OOO0OOOO ["发现或获知日期"])-pd .to_datetime (O00O00000OOO0OOOO ["事件发生日期"])#line:1221
			O00O00000OOO0OOOO ["报告时限"]=pd .to_datetime (O00O00000OOO0OOOO ["报告日期"])-pd .to_datetime (O00O00000OOO0OOOO ["发现或获知日期"])#line:1222
			O00O00000OOO0OOOO ["报告时限"]=O00O00000OOO0OOOO ["报告时限"].dt .days #line:1223
			O00O00000OOO0OOOO .loc [(O00O00000OOO0OOOO ["报告时限"]>20 )&(O00O00000OOO0OOOO ["伤害"]=="严重伤害"),"超时标记"]=1 #line:1224
			O00O00000OOO0OOOO .loc [(O00O00000OOO0OOOO ["报告时限"]>30 )&(O00O00000OOO0OOOO ["伤害"]=="其他"),"超时标记"]=1 #line:1225
			O00O00000OOO0OOOO .loc [(O00O00000OOO0OOOO ["报告时限"]>7 )&(O00O00000OOO0OOOO ["伤害"]=="死亡"),"超时标记"]=1 #line:1226
			O00O00000OOO0OOOO .loc [(O00O00000OOO0OOOO ["经营企业使用单位报告状态"]=="审核通过"),"有效报告"]=1 #line:1228
		if ini ["模式"]=="药品":#line:1231
			O00O00000OOO0OOOO ['用药开始时间']=pd .to_datetime (O00O00000OOO0OOOO ['用药开始时间'],format ='%Y-%m-%d',errors ='coerce')#line:1232
			O00O00000OOO0OOOO ["时隔"]=pd .to_datetime (O00O00000OOO0OOOO ["事件发生日期"])-pd .to_datetime (O00O00000OOO0OOOO ["用药开始时间"])#line:1233
			O00O00000OOO0OOOO ["报告时限"]=pd .to_datetime (O00O00000OOO0OOOO ["报告日期"])-pd .to_datetime (O00O00000OOO0OOOO ["事件发生日期"])#line:1234
			O00O00000OOO0OOOO ["报告时限"]=O00O00000OOO0OOOO ["报告时限"].dt .days #line:1235
			O00O00000OOO0OOOO .loc [(O00O00000OOO0OOOO ["报告时限"]>15 )&(O00O00000OOO0OOOO ["报告类型-严重程度"]=="严重"),"超时标记"]=1 #line:1236
			O00O00000OOO0OOOO .loc [(O00O00000OOO0OOOO ["报告时限"]>30 )&(O00O00000OOO0OOOO ["报告类型-严重程度"]=="一般"),"超时标记"]=1 #line:1237
			O00O00000OOO0OOOO .loc [(O00O00000OOO0OOOO ["报告时限"]>15 )&(O00O00000OOO0OOOO ["报告类型-新的"]=="新的"),"超时标记"]=1 #line:1238
			O00O00000OOO0OOOO .loc [(O00O00000OOO0OOOO ["报告时限"]>1 )&(O00O00000OOO0OOOO ["报告类型-严重程度"]=="死亡"),"超时标记"]=1 #line:1239
			O00O00000OOO0OOOO .loc [(O00O00000OOO0OOOO ["评价状态"]!="未评价"),"有效报告"]=1 #line:1241
		O00O00000OOO0OOOO .loc [((O00O00000OOO0OOOO ["年龄"]=="未填写")|O00O00000OOO0OOOO ["年龄"].isnull ()),"年龄"]=-1 #line:1243
		O00O00000OOO0OOOO ["年龄"]=O00O00000OOO0OOOO ["年龄"].astype (float )#line:1244
		O00O00000OOO0OOOO ["年龄"]=O00O00000OOO0OOOO ["年龄"].fillna (-1 )#line:1245
		O00O00000OOO0OOOO ["性别"]=O00O00000OOO0OOOO ["性别"].fillna ("未填写")#line:1246
		O00O00000OOO0OOOO ["年龄段"]="未填写"#line:1247
		try :#line:1248
			O00O00000OOO0OOOO .loc [(O00O00000OOO0OOOO ["年龄类型"]=="月"),"年龄"]=O00O00000OOO0OOOO ["年龄"].values /12 #line:1249
			O00O00000OOO0OOOO .loc [(O00O00000OOO0OOOO ["年龄类型"]=="月"),"年龄类型"]="岁"#line:1250
		except :#line:1251
			pass #line:1252
		try :#line:1253
			O00O00000OOO0OOOO .loc [(O00O00000OOO0OOOO ["年龄类型"]=="天"),"年龄"]=O00O00000OOO0OOOO ["年龄"].values /365 #line:1254
			O00O00000OOO0OOOO .loc [(O00O00000OOO0OOOO ["年龄类型"]=="天"),"年龄类型"]="岁"#line:1255
		except :#line:1256
			pass #line:1257
		O00O00000OOO0OOOO .loc [(O00O00000OOO0OOOO ["年龄"].values <=4 ),"年龄段"]="0-婴幼儿（0-4）"#line:1258
		O00O00000OOO0OOOO .loc [(O00O00000OOO0OOOO ["年龄"].values >=5 ),"年龄段"]="1-少儿（5-14）"#line:1259
		O00O00000OOO0OOOO .loc [(O00O00000OOO0OOOO ["年龄"].values >=15 ),"年龄段"]="2-青壮年（15-44）"#line:1260
		O00O00000OOO0OOOO .loc [(O00O00000OOO0OOOO ["年龄"].values >=45 ),"年龄段"]="3-中年期（45-64）"#line:1261
		O00O00000OOO0OOOO .loc [(O00O00000OOO0OOOO ["年龄"].values >=65 ),"年龄段"]="4-老年期（≥65）"#line:1262
		O00O00000OOO0OOOO .loc [(O00O00000OOO0OOOO ["年龄"].values ==-1 ),"年龄段"]="未填写"#line:1263
		O00O00000OOO0OOOO ["规整后品类"]="N"#line:1267
		O00O00000OOO0OOOO =TOOL_guizheng (O00O00000OOO0OOOO ,2 ,True )#line:1268
		if ini ['模式']in ["器械"]:#line:1271
			O00O00000OOO0OOOO =TOOL_guizheng (O00O00000OOO0OOOO ,3 ,True )#line:1272
		O00O00000OOO0OOOO =TOOL_guizheng (O00O00000OOO0OOOO ,"课题",True )#line:1276
		try :#line:1278
			O00O00000OOO0OOOO ["注册证编号/曾用注册证编号"]=O00O00000OOO0OOOO ["注册证编号/曾用注册证编号"].fillna ("未填写")#line:1279
		except :#line:1280
			pass #line:1281
		O00O00000OOO0OOOO ["数据清洗完成标记"]="是"#line:1283
		O0OOO0O0OO00O000O =O00O00000OOO0OOOO .loc [:]#line:1284
		return O00O00000OOO0OOOO #line:1285
def TOOLS_fileopen ():#line:1291
    ""#line:1292
    warnings .filterwarnings ('ignore')#line:1293
    O00OOOOOO0OOO00OO =filedialog .askopenfilenames (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:1294
    O0OO00O0O00OO000O =Useful_tools_openfiles (O00OOOOOO0OOO00OO ,0 )#line:1295
    try :#line:1296
        O0OO00O0O00OO000O =O0OO00O0O00OO000O .loc [:,~O0OO00O0O00OO000O .columns .str .contains ("^Unnamed")]#line:1297
    except :#line:1298
        pass #line:1299
    ini ["模式"]="其他"#line:1301
    O00O0OOOO00O00000 =O0OO00O0O00OO000O #line:1302
    TABLE_tree_Level_2 (O00O0OOOO00O00000 ,0 ,O00O0OOOO00O00000 )#line:1303
def TOOLS_pinzhong (O0OOO0OOO00O0O00O ):#line:1306
    ""#line:1307
    O0OOO0OOO00O0O00O ["患者姓名"]=O0OOO0OOO00O0O00O ["报告表编码"]#line:1308
    O0OOO0OOO00O0O00O ["用量"]=O0OOO0OOO00O0O00O ["用法用量"]#line:1309
    O0OOO0OOO00O0O00O ["评价状态"]=O0OOO0OOO00O0O00O ["报告单位评价"]#line:1310
    O0OOO0OOO00O0O00O ["用量单位"]=""#line:1311
    O0OOO0OOO00O0O00O ["单位名称"]="不适用"#line:1312
    O0OOO0OOO00O0O00O ["报告地区名称"]="不适用"#line:1313
    O0OOO0OOO00O0O00O ["用法-日"]="不适用"#line:1314
    O0OOO0OOO00O0O00O ["用法-次"]="不适用"#line:1315
    O0OOO0OOO00O0O00O ["不良反应发生时间"]=O0OOO0OOO00O0O00O ["不良反应发生时间"].str [0 :10 ]#line:1316
    O0OOO0OOO00O0O00O ["持有人报告状态"]="待评价"#line:1318
    O0OOO0OOO00O0O00O =O0OOO0OOO00O0O00O .rename (columns ={"是否非预期":"报告类型-新的","不良反应-术语":"不良反应名称","持有人/生产厂家":"上市许可持有人名称"})#line:1323
    return O0OOO0OOO00O0O00O #line:1324
def Useful_tools_openfiles (O0OO0OOO0OO0O000O ,O000O00OO0OOOO0OO ):#line:1329
    ""#line:1330
    O000O0O00000OO0OO =[pd .read_excel (OOOOO0OO000O00000 ,header =0 ,sheet_name =O000O00OO0OOOO0OO )for OOOOO0OO000O00000 in O0OO0OOO0OO0O000O ]#line:1331
    OO00O00OOO0OO0O00 =pd .concat (O000O0O00000OO0OO ,ignore_index =True ).drop_duplicates ()#line:1332
    return OO00O00OOO0OO0O00 #line:1333
def TOOLS_allfileopen ():#line:1335
    ""#line:1336
    global ori #line:1337
    global ini #line:1338
    global data #line:1339
    ini ["原始模式"]="否"#line:1340
    warnings .filterwarnings ('ignore')#line:1341
    OO00OO00O0OO0O00O =filedialog .askopenfilenames (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:1343
    ori =Useful_tools_openfiles (OO00OO00O0OO0O00O ,0 )#line:1344
    try :#line:1348
        OO00O0O0O0O000OOO =Useful_tools_openfiles (OO00OO00O0OO0O00O ,"报告信息")#line:1349
        if "是否非预期"in OO00O0O0O0O000OOO .columns :#line:1350
            ori =TOOLS_pinzhong (OO00O0O0O0O000OOO )#line:1351
    except :#line:1352
        pass #line:1353
    ini ["模式"]="其他"#line:1355
    try :#line:1357
        ori =Useful_tools_openfiles (OO00OO00O0OO0O00O ,"字典数据")#line:1358
        ini ["原始模式"]="是"#line:1359
        if "UDI"in ori .columns :#line:1360
            ini ["模式"]="器械"#line:1361
            data =ori #line:1362
        if "报告类型-新的"in ori .columns :#line:1363
            ini ["模式"]="药品"#line:1364
            data =ori #line:1365
        else :#line:1366
            ini ["模式"]="其他"#line:1367
    except :#line:1368
        pass #line:1369
    try :#line:1372
        ori =ori .loc [:,~ori .columns .str .contains ("^Unnamed")]#line:1373
    except :#line:1374
        pass #line:1375
    if "UDI"in ori .columns and ini ["原始模式"]!="是":#line:1379
        text .insert (END ,"识别出为器械报表,正在进行数据规整...")#line:1380
        ini ["模式"]="器械"#line:1381
        ori =CLEAN_qx (ori )#line:1382
        data =ori #line:1383
    if "报告类型-新的"in ori .columns and ini ["原始模式"]!="是":#line:1384
        text .insert (END ,"识别出为药品报表,正在进行数据规整...")#line:1385
        ini ["模式"]="药品"#line:1386
        ori =CLEAN_yp (ori )#line:1387
        ori =CLEAN_qx (ori )#line:1388
        data =ori #line:1389
    if "光斑贴试验"in ori .columns and ini ["原始模式"]!="是":#line:1390
        text .insert (END ,"识别出为化妆品报表,正在进行数据规整...")#line:1391
        ini ["模式"]="化妆品"#line:1392
        ori =CLEAN_hzp (ori )#line:1393
        ori =CLEAN_qx (ori )#line:1394
        data =ori #line:1395
    if ini ["模式"]=="其他":#line:1398
        text .insert (END ,"\n数据读取成功，行数："+str (len (ori )))#line:1399
        data =ori #line:1400
        OOO0OO000O0000000 =Menu (root )#line:1401
        root .config (menu =OOO0OO000O0000000 )#line:1402
        try :#line:1403
            ini ["button"][0 ].pack_forget ()#line:1404
            ini ["button"][1 ].pack_forget ()#line:1405
            ini ["button"][2 ].pack_forget ()#line:1406
            ini ["button"][3 ].pack_forget ()#line:1407
            ini ["button"][4 ].pack_forget ()#line:1408
        except :#line:1409
            pass #line:1410
    else :#line:1412
        ini ["清洗后的文件"]=data #line:1413
        ini ["证号"]=Countall (data ).df_zhenghao ()#line:1414
        text .insert (END ,"\n数据读取成功，行数："+str (len (data )))#line:1415
        PROGRAM_Menubar (root ,data ,0 ,data )#line:1416
        try :#line:1417
            ini ["button"][0 ].pack_forget ()#line:1418
            ini ["button"][1 ].pack_forget ()#line:1419
            ini ["button"][2 ].pack_forget ()#line:1420
            ini ["button"][3 ].pack_forget ()#line:1421
            ini ["button"][4 ].pack_forget ()#line:1422
        except :#line:1423
            pass #line:1424
        O00OO0OO0O0O00000 =Button (frame0 ,text ="地市统计",bg ="white",height =2 ,width =12 ,font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (data ).df_org ("市级监测机构"),1 ,ori ),)#line:1435
        O00OO0OO0O0O00000 .pack ()#line:1436
        O00000O000000000O =Button (frame0 ,text ="县区统计",bg ="white",height =2 ,width =12 ,font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (data ).df_org ("监测机构"),1 ,ori ),)#line:1449
        O00000O000000000O .pack ()#line:1450
        OO0OOOO00000OOOO0 =Button (frame0 ,text ="上报单位",bg ="white",height =2 ,width =12 ,font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (data ).df_user (),1 ,ori ),)#line:1463
        OO0OOOO00000OOOO0 .pack ()#line:1464
        OOO0000000O0O000O =Button (frame0 ,text ="生产企业",bg ="white",height =2 ,width =12 ,font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (data ).df_chiyouren (),1 ,ori ),)#line:1475
        OOO0000000O0O000O .pack ()#line:1476
        OOOO0000O00OOO00O =Button (frame0 ,text ="产品统计",bg ="white",height =2 ,width =12 ,font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (ini ["证号"],1 ,ori ,ori ,"dfx_zhenghao"),)#line:1487
        OOOO0000O00OOO00O .pack ()#line:1488
        ini ["button"]=[O00OO0OO0O0O00000 ,O00000O000000000O ,OO0OOOO00000OOOO0 ,OOO0000000O0O000O ,OOOO0000O00OOO00O ]#line:1489
    text .insert (END ,"\n")#line:1491
def TOOLS_sql (OOOO000OOOO0OOOOO ):#line:1493
    ""#line:1494
    warnings .filterwarnings ("ignore")#line:1495
    try :#line:1496
        O00000O0O00OO0OO0 =OOOO000OOOO0OOOOO .columns #line:1497
    except :#line:1498
        return 0 #line:1499
    def OO0O0000O0OO00OO0 (O0OOOO00O00OO0000 ):#line:1501
        try :#line:1502
            O000O0000OOOO00OO =pd .read_sql_query (sqltext (O0OOOO00O00OO0000 ),con =OO0000OOOO0OOOO00 )#line:1503
        except :#line:1504
            showinfo (title ="提示",message ="SQL语句有误。")#line:1505
            return 0 #line:1506
        try :#line:1507
            del O000O0000OOOO00OO ["level_0"]#line:1508
        except :#line:1509
            pass #line:1510
        TABLE_tree_Level_2 (O000O0000OOOO00OO ,1 ,OOOO000OOOO0OOOOO )#line:1511
    OO000000OOOOO0O0O ='sqlite://'#line:1515
    OO000O0000OO00OOO =create_engine (OO000000OOOOO0O0O )#line:1516
    try :#line:1517
        OOOO000OOOO0OOOOO .to_sql ('data',con =OO000O0000OO00OOO ,chunksize =10000 ,if_exists ='replace',index =True )#line:1518
    except :#line:1519
        showinfo (title ="提示",message ="不支持该表格。")#line:1520
        return 0 #line:1521
    OO0000OOOO0OOOO00 =OO000O0000OO00OOO .connect ()#line:1523
    OO00OO000OO000O0O ="select * from data"#line:1524
    OO0000OOOO00O0OOO =Toplevel ()#line:1527
    OO0000OOOO00O0OOO .title ("SQL查询")#line:1528
    OO0000OOOO00O0OOO .geometry ("700x500")#line:1529
    O00000OO000OOO00O =ttk .Frame (OO0000OOOO00O0OOO ,width =700 ,height =20 )#line:1531
    O00000OO000OOO00O .pack (side =TOP )#line:1532
    OOOOOO0O000OOO0O0 =ttk .Frame (OO0000OOOO00O0OOO ,width =700 ,height =20 )#line:1533
    OOOOOO0O000OOO0O0 .pack (side =BOTTOM )#line:1534
    try :#line:1537
        O0O0000O0O000OO0O =StringVar ()#line:1538
        O0O0000O0O000OO0O .set ("select * from data WHERE 单位名称='佛山市第一人民医院'")#line:1539
        O0O0000O00O00O00O =Label (O00000OO000OOO00O ,text ="SQL查询",anchor ='w')#line:1541
        O0O0000O00O00O00O .pack (side =LEFT )#line:1542
        O0OOO000OOOOO00OO =Label (O00000OO000OOO00O ,text ="检索：")#line:1543
        OOO00O00O0OO000O0 =Button (OOOOOO0O000OOO0O0 ,text ="执行",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",width =700 ,command =lambda :OO0O0000O0OO00OO0 (OO000O000O0OOOO00 .get ("1.0","end")),)#line:1557
        OOO00O00O0OO000O0 .pack (side =LEFT )#line:1558
    except EE :#line:1561
        pass #line:1562
    O0O0OOO00O00O0000 =Scrollbar (OO0000OOOO00O0OOO )#line:1564
    OO000O000O0OOOO00 =Text (OO0000OOOO00O0OOO ,height =80 ,width =150 ,bg ="#FFFFFF",font ="微软雅黑")#line:1565
    O0O0OOO00O00O0000 .pack (side =RIGHT ,fill =Y )#line:1566
    OO000O000O0OOOO00 .pack ()#line:1567
    O0O0OOO00O00O0000 .config (command =OO000O000O0OOOO00 .yview )#line:1568
    OO000O000O0OOOO00 .config (yscrollcommand =O0O0OOO00O00O0000 .set )#line:1569
    def OO0000000OO0O0O0O (event =None ):#line:1570
        OO000O000O0OOOO00 .event_generate ('<<Copy>>')#line:1571
    def O0OOO00OO000O0O0O (event =None ):#line:1572
        OO000O000O0OOOO00 .event_generate ('<<Paste>>')#line:1573
    def OOOOO00OO0O0O0O00 (OO00O00O0OO00000O ,O00OOO00O000O0O00 ):#line:1574
         TOOLS_savetxt (OO00O00O0OO00000O ,O00OOO00O000O0O00 ,1 )#line:1575
    OOOO00O00OO0000OO =Menu (OO000O000O0OOOO00 ,tearoff =False ,)#line:1576
    OOOO00O00OO0000OO .add_command (label ="复制",command =OO0000000OO0O0O0O )#line:1577
    OOOO00O00OO0000OO .add_command (label ="粘贴",command =O0OOO00OO000O0O0O )#line:1578
    OOOO00O00OO0000OO .add_command (label ="源文件列",command =lambda :PROGRAM_helper (OOOO000OOOO0OOOOO .columns .to_list ()))#line:1579
    def OO00OO0000OOOO00O (OO0O000OOOOO00O0O ):#line:1580
         OOOO00O00OO0000OO .post (OO0O000OOOOO00O0O .x_root ,OO0O000OOOOO00O0O .y_root )#line:1581
    OO000O000O0OOOO00 .bind ("<Button-3>",OO00OO0000OOOO00O )#line:1582
    OO000O000O0OOOO00 .insert (END ,OO00OO000OO000O0O )#line:1586
def TOOLS_view_dict (OOOOOOOOOOO00OOO0 ,OO0O0OO000OO0O00O ):#line:1590
    ""#line:1591
    O00000OO0OOO0OOOO =Toplevel ()#line:1592
    O00000OO0OOO0OOOO .title ("查看数据")#line:1593
    O00000OO0OOO0OOOO .geometry ("700x500")#line:1594
    OOO000O000O0O00O0 =Scrollbar (O00000OO0OOO0OOOO )#line:1596
    O0OOOO0OOO0OO0000 =Text (O00000OO0OOO0OOOO ,height =100 ,width =150 )#line:1597
    OOO000O000O0O00O0 .pack (side =RIGHT ,fill =Y )#line:1598
    O0OOOO0OOO0OO0000 .pack ()#line:1599
    OOO000O000O0O00O0 .config (command =O0OOOO0OOO0OO0000 .yview )#line:1600
    O0OOOO0OOO0OO0000 .config (yscrollcommand =OOO000O000O0O00O0 .set )#line:1601
    if OO0O0OO000OO0O00O ==1 :#line:1602
        O0OOOO0OOO0OO0000 .insert (END ,OOOOOOOOOOO00OOO0 )#line:1604
        O0OOOO0OOO0OO0000 .insert (END ,"\n\n")#line:1605
        return 0 #line:1606
    for OO00O00OOOOOOOO00 in range (len (OOOOOOOOOOO00OOO0 )):#line:1607
        O0OOOO0OOO0OO0000 .insert (END ,OOOOOOOOOOO00OOO0 .iloc [OO00O00OOOOOOOO00 ,0 ])#line:1608
        O0OOOO0OOO0OO0000 .insert (END ,":")#line:1609
        O0OOOO0OOO0OO0000 .insert (END ,OOOOOOOOOOO00OOO0 .iloc [OO00O00OOOOOOOO00 ,1 ])#line:1610
        O0OOOO0OOO0OO0000 .insert (END ,"\n\n")#line:1611
def TOOLS_save_dict (O0O0O0O00OO00O0O0 ):#line:1613
    ""#line:1614
    OOO0O0000OO0OO000 =filedialog .asksaveasfilename (title =u"保存文件",initialfile ="排序后的原始数据",defaultextension ="xls",filetypes =[("Excel 97-2003 工作簿","*.xls")],)#line:1620
    try :#line:1621
        O0O0O0O00OO00O0O0 ["详细描述T"]=O0O0O0O00OO00O0O0 ["详细描述T"].astype (str )#line:1622
    except :#line:1623
        pass #line:1624
    try :#line:1625
        O0O0O0O00OO00O0O0 ["报告编码"]=O0O0O0O00OO00O0O0 ["报告编码"].astype (str )#line:1626
    except :#line:1627
        pass #line:1628
    OOO00O0O0O000OO0O =pd .ExcelWriter (OOO0O0000OO0OO000 ,engine ="xlsxwriter")#line:1630
    O0O0O0O00OO00O0O0 .to_excel (OOO00O0O0O000OO0O ,sheet_name ="字典数据")#line:1631
    OOO00O0O0O000OO0O .close ()#line:1632
    showinfo (title ="提示",message ="文件写入成功。")#line:1633
def TOOLS_savetxt (O000000OO000OOOO0 ,OO00O0OO0O00OO0OO ,OOOOOOOO0O0OO0OOO ):#line:1635
	""#line:1636
	O00OOOOO0OO00000O =open (OO00O0OO0O00OO0OO ,"w",encoding ='utf-8')#line:1637
	O00OOOOO0OO00000O .write (O000000OO000OOOO0 )#line:1638
	O00OOOOO0OO00000O .flush ()#line:1640
	if OOOOOOOO0O0OO0OOO ==1 :#line:1641
		showinfo (title ="提示信息",message ="保存成功。")#line:1642
def TOOLS_deep_view (OO00O0O0O0OO000OO ,O000OOOO000O0O00O ,O0OO00O0000OOO000 ,OOO0000000OOOO0OO ):#line:1645
    ""#line:1646
    if OOO0000000OOOO0OO ==0 :#line:1647
        try :#line:1648
            OO00O0O0O0OO000OO [O000OOOO000O0O00O ]=OO00O0O0O0OO000OO [O000OOOO000O0O00O ].fillna ("这个没有填写")#line:1649
        except :#line:1650
            pass #line:1651
        O0OOOOO0O00OOO000 =OO00O0O0O0OO000OO .groupby (O000OOOO000O0O00O ).agg (计数 =(O0OO00O0000OOO000 [0 ],O0OO00O0000OOO000 [1 ]))#line:1652
    if OOO0000000OOOO0OO ==1 :#line:1653
            O0OOOOO0O00OOO000 =pd .pivot_table (OO00O0O0O0OO000OO ,index =O000OOOO000O0O00O [:-1 ],columns =O000OOOO000O0O00O [-1 ],values =[O0OO00O0000OOO000 [0 ]],aggfunc ={O0OO00O0000OOO000 [0 ]:O0OO00O0000OOO000 [1 ]},fill_value ="0",margins =True ,dropna =False ,)#line:1664
            O0OOOOO0O00OOO000 .columns =O0OOOOO0O00OOO000 .columns .droplevel (0 )#line:1665
            O0OOOOO0O00OOO000 =O0OOOOO0O00OOO000 .rename (columns ={"All":"计数"})#line:1666
    if "日期"in O000OOOO000O0O00O or "时间"in O000OOOO000O0O00O or "季度"in O000OOOO000O0O00O :#line:1669
        O0OOOOO0O00OOO000 =O0OOOOO0O00OOO000 .sort_values ([O000OOOO000O0O00O ],ascending =False ,na_position ="last")#line:1672
    else :#line:1673
        O0OOOOO0O00OOO000 =O0OOOOO0O00OOO000 .sort_values (by =["计数"],ascending =False ,na_position ="last")#line:1677
    O0OOOOO0O00OOO000 =O0OOOOO0O00OOO000 .reset_index ()#line:1678
    O0OOOOO0O00OOO000 ["构成比(%)"]=round (100 *O0OOOOO0O00OOO000 ["计数"]/O0OOOOO0O00OOO000 ["计数"].sum (),2 )#line:1679
    if OOO0000000OOOO0OO ==0 :#line:1680
        O0OOOOO0O00OOO000 ["报表类型"]="dfx_deepview"+"_"+str (O000OOOO000O0O00O )#line:1681
    if OOO0000000OOOO0OO ==1 :#line:1682
        O0OOOOO0O00OOO000 ["报表类型"]="dfx_deepview"+"_"+str (O000OOOO000O0O00O [:-1 ])#line:1683
    return O0OOOOO0O00OOO000 #line:1684
def TOOLS_easyreadT (O0O0OOOOO0O0O00O0 ):#line:1688
    ""#line:1689
    O0O0OOOOO0O0O00O0 ["#####分隔符#########"]="######################################################################"#line:1692
    O0O0OO0OOO00OO000 =O0O0OOOOO0O0O00O0 .stack (dropna =False )#line:1693
    O0O0OO0OOO00OO000 =pd .DataFrame (O0O0OO0OOO00OO000 ).reset_index ()#line:1694
    O0O0OO0OOO00OO000 .columns =["序号","条目","详细描述T"]#line:1695
    O0O0OO0OOO00OO000 ["逐条查看"]="逐条查看"#line:1696
    return O0O0OO0OOO00OO000 #line:1697
def TOOLS_data_masking (OO00O0O00O0O0OOO0 ):#line:1699
    ""#line:1700
    from random import choices #line:1701
    from string import ascii_letters ,digits #line:1702
    OO00O0O00O0O0OOO0 =OO00O0O00O0O0OOO0 .reset_index (drop =True )#line:1704
    if "单位名称.1"in OO00O0O00O0O0OOO0 .columns :#line:1705
        OOO00OO0OOOO00O0O ="器械"#line:1706
    else :#line:1707
        OOO00OO0OOOO00O0O ="药品"#line:1708
    O0OOO00OOOO0000O0 =peizhidir +""+"0（范例）数据脱敏"+".xls"#line:1709
    try :#line:1710
        O00OOOO00O00O0OOO =pd .read_excel (O0OOO00OOOO0000O0 ,sheet_name =OOO00OO0OOOO00O0O ,header =0 ,index_col =0 ).reset_index ()#line:1713
    except :#line:1714
        showinfo (title ="错误信息",message ="该功能需要配置文件才能使用！")#line:1715
        return 0 #line:1716
    OO00000O00O0O000O =0 #line:1717
    OOO00O0OO0OOOOOOO =len (OO00O0O00O0O0OOO0 )#line:1718
    OO00O0O00O0O0OOO0 ["abcd"]="□"#line:1719
    for OOOOO0OOOO0OOO0OO in O00OOOO00O00O0OOO ["要脱敏的列"]:#line:1720
        OO00000O00O0O000O =OO00000O00O0O000O +1 #line:1721
        PROGRAM_change_schedule (OO00000O00O0O000O ,OOO00O0OO0OOOOOOO )#line:1722
        text .insert (END ,"\n正在对以下列进行脱敏处理：")#line:1723
        text .see (END )#line:1724
        text .insert (END ,OOOOO0OOOO0OOO0OO )#line:1725
        try :#line:1726
            OOO0O00000O0OOOOO =set (OO00O0O00O0O0OOO0 [OOOOO0OOOO0OOO0OO ])#line:1727
        except :#line:1728
            showinfo (title ="提示",message ="脱敏文件配置错误，请修改配置表。")#line:1729
            return 0 #line:1730
        O00O0O0000O00OOO0 ={O00O000OOO000O0OO :"".join (choices (digits ,k =10 ))for O00O000OOO000O0OO in OOO0O00000O0OOOOO }#line:1731
        OO00O0O00O0O0OOO0 [OOOOO0OOOO0OOO0OO ]=OO00O0O00O0O0OOO0 [OOOOO0OOOO0OOO0OO ].map (O00O0O0000O00OOO0 )#line:1732
        OO00O0O00O0O0OOO0 [OOOOO0OOOO0OOO0OO ]=OO00O0O00O0O0OOO0 ["abcd"]+OO00O0O00O0O0OOO0 [OOOOO0OOOO0OOO0OO ].astype (str )#line:1733
    try :#line:1734
        PROGRAM_change_schedule (10 ,10 )#line:1735
        del OO00O0O00O0O0OOO0 ["abcd"]#line:1736
        O000O00OOO00O0OO0 =filedialog .asksaveasfilename (title =u"保存脱敏后的文件",initialfile ="脱敏后的文件",defaultextension ="xlsx",filetypes =[("Excel 工作簿","*.xlsx"),("Excel 97-2003 工作簿","*.xls")],)#line:1742
        OO0O000O00OOO00OO =pd .ExcelWriter (O000O00OOO00O0OO0 ,engine ="xlsxwriter")#line:1743
        OO00O0O00O0O0OOO0 .to_excel (OO0O000O00OOO00OO ,sheet_name ="sheet0")#line:1744
        OO0O000O00OOO00OO .close ()#line:1745
    except :#line:1746
        text .insert (END ,"\n文件未保存，但导入的数据已按要求脱敏。")#line:1747
    text .insert (END ,"\n脱敏操作完成。")#line:1748
    text .see (END )#line:1749
    return OO00O0O00O0O0OOO0 #line:1750
def TOOLS_get_new (O000OO0O0000OOO0O ,O00O0O00O0O0O0O00 ):#line:1752
	""#line:1753
	def OOOOOO0O0OOOO00OO (OO00000OO00O0O0OO ):#line:1754
		""#line:1755
		OO00000OO00O0O0OO =OO00000OO00O0O0OO .drop_duplicates ("报告编码")#line:1756
		OOOOOOO00OO00000O =str (Counter (TOOLS_get_list0 ("use(器械故障表现).file",OO00000OO00O0O0OO ,1000 ))).replace ("Counter({","{")#line:1757
		OOOOOOO00OO00000O =OOOOOOO00OO00000O .replace ("})","}")#line:1758
		import ast #line:1759
		O0OO00O0OOO0O00OO =ast .literal_eval (OOOOOOO00OO00000O )#line:1760
		O0O0O00O0OOOO00OO =TOOLS_easyreadT (pd .DataFrame ([O0OO00O0OOO0O00OO ]))#line:1761
		O0O0O00O0OOOO00OO =O0O0O00O0OOOO00OO .rename (columns ={"逐条查看":"ADR名称规整"})#line:1762
		return O0O0O00O0OOOO00OO #line:1763
	if O00O0O00O0O0O0O00 =="证号":#line:1764
		root .attributes ("-topmost",True )#line:1765
		root .attributes ("-topmost",False )#line:1766
		OO00OO00OOOOO000O =O000OO0O0000OOO0O .groupby (["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号"]).agg (计数 =("报告编码","nunique")).reset_index ()#line:1767
		O0OO00OO0OOOOO0O0 =OO00OO00OOOOO000O .drop_duplicates ("注册证编号/曾用注册证编号").copy ()#line:1768
		O0OO00OO0OOOOO0O0 ["所有不良反应"]=""#line:1769
		O0OO00OO0OOOOO0O0 ["关注建议"]=""#line:1770
		O0OO00OO0OOOOO0O0 ["疑似新的"]=""#line:1771
		O0OO00OO0OOOOO0O0 ["疑似旧的"]=""#line:1772
		O0OO00OO0OOOOO0O0 ["疑似新的（高敏）"]=""#line:1773
		O0OO00OO0OOOOO0O0 ["疑似旧的（高敏）"]=""#line:1774
		O0O0OO0O0O0000000 =1 #line:1775
		O0O0OOOOO0000O000 =int (len (O0OO00OO0OOOOO0O0 ))#line:1776
		for OO00O00OOO0O0O00O ,O0OO00O0O00O0OOOO in O0OO00OO0OOOOO0O0 .iterrows ():#line:1777
			OO0O00OOO0OOOO0OO =O000OO0O0000OOO0O [(O000OO0O0000OOO0O ["注册证编号/曾用注册证编号"]==O0OO00O0O00O0OOOO ["注册证编号/曾用注册证编号"])]#line:1778
			O00OO0O0000OOO000 =OO0O00OOO0OOOO0OO .loc [OO0O00OOO0OOOO0OO ["报告类型-新的"].str .contains ("新",na =False )].copy ()#line:1779
			OO00O0O000000O00O =OO0O00OOO0OOOO0OO .loc [~OO0O00OOO0OOOO0OO ["报告类型-新的"].str .contains ("新",na =False )].copy ()#line:1780
			OO000OOO0000O0OO0 =OOOOOO0O0OOOO00OO (O00OO0O0000OOO000 )#line:1781
			OO00OO0O00OO000OO =OOOOOO0O0OOOO00OO (OO00O0O000000O00O )#line:1782
			O00000O00O00OO0O0 =OOOOOO0O0OOOO00OO (OO0O00OOO0OOOO0OO )#line:1783
			PROGRAM_change_schedule (O0O0OO0O0O0000000 ,O0O0OOOOO0000O000 )#line:1784
			O0O0OO0O0O0000000 =O0O0OO0O0O0000000 +1 #line:1785
			for OO00OO0000OOOOO0O ,OOO00OOOO0000OOOO in O00000O00O00OO0O0 .iterrows ():#line:1787
					if "分隔符"not in OOO00OOOO0000OOOO ["条目"]:#line:1788
						OO0O0OOOO0OO0OO00 ="'"+str (OOO00OOOO0000OOOO ["条目"])+"':"+str (OOO00OOOO0000OOOO ["详细描述T"])+","#line:1789
						O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"所有不良反应"]=O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"所有不良反应"]+OO0O0OOOO0OO0OO00 #line:1790
			for OO00OO0000OOOOO0O ,OOO00OOOO0000OOOO in OO00OO0O00OO000OO .iterrows ():#line:1792
					if "分隔符"not in OOO00OOOO0000OOOO ["条目"]:#line:1793
						OO0O0OOOO0OO0OO00 ="'"+str (OOO00OOOO0000OOOO ["条目"])+"':"+str (OOO00OOOO0000OOOO ["详细描述T"])+","#line:1794
						O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"疑似旧的"]=O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"疑似旧的"]+OO0O0OOOO0OO0OO00 #line:1795
					if "分隔符"not in OOO00OOOO0000OOOO ["条目"]and int (OOO00OOOO0000OOOO ["详细描述T"])>=2 :#line:1797
						OO0O0OOOO0OO0OO00 ="'"+str (OOO00OOOO0000OOOO ["条目"])+"':"+str (OOO00OOOO0000OOOO ["详细描述T"])+","#line:1798
						O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"疑似旧的（高敏）"]=O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"疑似旧的（高敏）"]+OO0O0OOOO0OO0OO00 #line:1799
			for OO00OO0000OOOOO0O ,OOO00OOOO0000OOOO in OO000OOO0000O0OO0 .iterrows ():#line:1801
				if str (OOO00OOOO0000OOOO ["条目"]).strip ()not in str (O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"疑似旧的"])and "分隔符"not in str (OOO00OOOO0000OOOO ["条目"]):#line:1802
					OO0O0OOOO0OO0OO00 ="'"+str (OOO00OOOO0000OOOO ["条目"])+"':"+str (OOO00OOOO0000OOOO ["详细描述T"])+","#line:1803
					O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"疑似新的"]=O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"疑似新的"]+OO0O0OOOO0OO0OO00 #line:1804
					if int (OOO00OOOO0000OOOO ["详细描述T"])>=3 :#line:1805
						O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"关注建议"]=O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"关注建议"]+"！"#line:1806
					if int (OOO00OOOO0000OOOO ["详细描述T"])>=5 :#line:1807
						O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"关注建议"]=O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"关注建议"]+"●"#line:1808
				if str (OOO00OOOO0000OOOO ["条目"]).strip ()not in str (O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"疑似旧的（高敏）"])and "分隔符"not in str (OOO00OOOO0000OOOO ["条目"])and int (OOO00OOOO0000OOOO ["详细描述T"])>=2 :#line:1810
					OO0O0OOOO0OO0OO00 ="'"+str (OOO00OOOO0000OOOO ["条目"])+"':"+str (OOO00OOOO0000OOOO ["详细描述T"])+","#line:1811
					O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"疑似新的（高敏）"]=O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"疑似新的（高敏）"]+OO0O0OOOO0OO0OO00 #line:1812
		O0OO00OO0OOOOO0O0 ["疑似新的"]="{"+O0OO00OO0OOOOO0O0 ["疑似新的"]+"}"#line:1814
		O0OO00OO0OOOOO0O0 ["疑似旧的"]="{"+O0OO00OO0OOOOO0O0 ["疑似旧的"]+"}"#line:1815
		O0OO00OO0OOOOO0O0 ["所有不良反应"]="{"+O0OO00OO0OOOOO0O0 ["所有不良反应"]+"}"#line:1816
		O0OO00OO0OOOOO0O0 ["疑似新的（高敏）"]="{"+O0OO00OO0OOOOO0O0 ["疑似新的（高敏）"]+"}"#line:1817
		O0OO00OO0OOOOO0O0 ["疑似旧的（高敏）"]="{"+O0OO00OO0OOOOO0O0 ["疑似旧的（高敏）"]+"}"#line:1818
		O0OO00OO0OOOOO0O0 =O0OO00OO0OOOOO0O0 .rename (columns ={"器械待评价(药品新的报告比例)":"新的报告比例"})#line:1820
		O0OO00OO0OOOOO0O0 =O0OO00OO0OOOOO0O0 .rename (columns ={"严重伤害待评价比例(药品严重中新的比例)":"严重报告中新的比例"})#line:1821
		O0OO00OO0OOOOO0O0 ["报表类型"]="dfx_zhenghao"#line:1822
		OO0O0OOOOOO00OO00 =pd .pivot_table (O000OO0O0000OOO0O ,values =["报告编码"],index =["注册证编号/曾用注册证编号"],columns ="报告单位评价",aggfunc ={"报告编码":"nunique"},fill_value ="0",margins =True ,dropna =False ,).rename (columns ={"报告编码":"数量"})#line:1824
		OO0O0OOOOOO00OO00 .columns =OO0O0OOOOOO00OO00 .columns .droplevel (0 )#line:1825
		O0OO00OO0OOOOO0O0 =pd .merge (O0OO00OO0OOOOO0O0 ,OO0O0OOOOOO00OO00 .reset_index (),on =["注册证编号/曾用注册证编号"],how ="left")#line:1826
		TABLE_tree_Level_2 (O0OO00OO0OOOOO0O0 .sort_values (by ="计数",ascending =[False ],na_position ="last"),1 ,O000OO0O0000OOO0O )#line:1830
	if O00O0O00O0O0O0O00 =="品种":#line:1831
		root .attributes ("-topmost",True )#line:1832
		root .attributes ("-topmost",False )#line:1833
		OO00OO00OOOOO000O =O000OO0O0000OOO0O .groupby (["产品类别","产品名称"]).agg (计数 =("报告编码","nunique")).reset_index ()#line:1834
		O0OO00OO0OOOOO0O0 =OO00OO00OOOOO000O .drop_duplicates ("产品名称").copy ()#line:1835
		O0OO00OO0OOOOO0O0 ["产品名称"]=O0OO00OO0OOOOO0O0 ["产品名称"].str .replace ("*","",regex =False )#line:1836
		O0OO00OO0OOOOO0O0 ["所有不良反应"]=""#line:1837
		O0OO00OO0OOOOO0O0 ["关注建议"]=""#line:1838
		O0OO00OO0OOOOO0O0 ["疑似新的"]=""#line:1839
		O0OO00OO0OOOOO0O0 ["疑似旧的"]=""#line:1840
		O0OO00OO0OOOOO0O0 ["疑似新的（高敏）"]=""#line:1841
		O0OO00OO0OOOOO0O0 ["疑似旧的（高敏）"]=""#line:1842
		O0O0OO0O0O0000000 =1 #line:1843
		O0O0OOOOO0000O000 =int (len (O0OO00OO0OOOOO0O0 ))#line:1844
		for OO00O00OOO0O0O00O ,O0OO00O0O00O0OOOO in O0OO00OO0OOOOO0O0 .iterrows ():#line:1847
			OO0O00OOO0OOOO0OO =O000OO0O0000OOO0O [(O000OO0O0000OOO0O ["产品名称"]==O0OO00O0O00O0OOOO ["产品名称"])]#line:1849
			O00OO0O0000OOO000 =OO0O00OOO0OOOO0OO .loc [OO0O00OOO0OOOO0OO ["报告类型-新的"].str .contains ("新",na =False )].copy ()#line:1851
			OO00O0O000000O00O =OO0O00OOO0OOOO0OO .loc [~OO0O00OOO0OOOO0OO ["报告类型-新的"].str .contains ("新",na =False )].copy ()#line:1852
			O00000O00O00OO0O0 =OOOOOO0O0OOOO00OO (OO0O00OOO0OOOO0OO )#line:1853
			OO000OOO0000O0OO0 =OOOOOO0O0OOOO00OO (O00OO0O0000OOO000 )#line:1854
			OO00OO0O00OO000OO =OOOOOO0O0OOOO00OO (OO00O0O000000O00O )#line:1855
			PROGRAM_change_schedule (O0O0OO0O0O0000000 ,O0O0OOOOO0000O000 )#line:1856
			O0O0OO0O0O0000000 =O0O0OO0O0O0000000 +1 #line:1857
			for OO00OO0000OOOOO0O ,OOO00OOOO0000OOOO in O00000O00O00OO0O0 .iterrows ():#line:1859
					if "分隔符"not in OOO00OOOO0000OOOO ["条目"]:#line:1860
						OO0O0OOOO0OO0OO00 ="'"+str (OOO00OOOO0000OOOO ["条目"])+"':"+str (OOO00OOOO0000OOOO ["详细描述T"])+","#line:1861
						O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"所有不良反应"]=O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"所有不良反应"]+OO0O0OOOO0OO0OO00 #line:1862
			for OO00OO0000OOOOO0O ,OOO00OOOO0000OOOO in OO00OO0O00OO000OO .iterrows ():#line:1865
					if "分隔符"not in OOO00OOOO0000OOOO ["条目"]:#line:1866
						OO0O0OOOO0OO0OO00 ="'"+str (OOO00OOOO0000OOOO ["条目"])+"':"+str (OOO00OOOO0000OOOO ["详细描述T"])+","#line:1867
						O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"疑似旧的"]=O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"疑似旧的"]+OO0O0OOOO0OO0OO00 #line:1868
					if "分隔符"not in OOO00OOOO0000OOOO ["条目"]and int (OOO00OOOO0000OOOO ["详细描述T"])>=2 :#line:1870
						OO0O0OOOO0OO0OO00 ="'"+str (OOO00OOOO0000OOOO ["条目"])+"':"+str (OOO00OOOO0000OOOO ["详细描述T"])+","#line:1871
						O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"疑似旧的（高敏）"]=O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"疑似旧的（高敏）"]+OO0O0OOOO0OO0OO00 #line:1872
			for OO00OO0000OOOOO0O ,OOO00OOOO0000OOOO in OO000OOO0000O0OO0 .iterrows ():#line:1874
				if str (OOO00OOOO0000OOOO ["条目"]).strip ()not in str (O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"疑似旧的"])and "分隔符"not in str (OOO00OOOO0000OOOO ["条目"]):#line:1875
					OO0O0OOOO0OO0OO00 ="'"+str (OOO00OOOO0000OOOO ["条目"])+"':"+str (OOO00OOOO0000OOOO ["详细描述T"])+","#line:1876
					O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"疑似新的"]=O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"疑似新的"]+OO0O0OOOO0OO0OO00 #line:1877
					if int (OOO00OOOO0000OOOO ["详细描述T"])>=3 :#line:1878
						O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"关注建议"]=O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"关注建议"]+"！"#line:1879
					if int (OOO00OOOO0000OOOO ["详细描述T"])>=5 :#line:1880
						O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"关注建议"]=O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"关注建议"]+"●"#line:1881
				if str (OOO00OOOO0000OOOO ["条目"]).strip ()not in str (O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"疑似旧的（高敏）"])and "分隔符"not in str (OOO00OOOO0000OOOO ["条目"])and int (OOO00OOOO0000OOOO ["详细描述T"])>=2 :#line:1883
					OO0O0OOOO0OO0OO00 ="'"+str (OOO00OOOO0000OOOO ["条目"])+"':"+str (OOO00OOOO0000OOOO ["详细描述T"])+","#line:1884
					O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"疑似新的（高敏）"]=O0OO00OO0OOOOO0O0 .loc [OO00O00OOO0O0O00O ,"疑似新的（高敏）"]+OO0O0OOOO0OO0OO00 #line:1885
		O0OO00OO0OOOOO0O0 ["疑似新的"]="{"+O0OO00OO0OOOOO0O0 ["疑似新的"]+"}"#line:1887
		O0OO00OO0OOOOO0O0 ["疑似旧的"]="{"+O0OO00OO0OOOOO0O0 ["疑似旧的"]+"}"#line:1888
		O0OO00OO0OOOOO0O0 ["所有不良反应"]="{"+O0OO00OO0OOOOO0O0 ["所有不良反应"]+"}"#line:1889
		O0OO00OO0OOOOO0O0 ["疑似新的（高敏）"]="{"+O0OO00OO0OOOOO0O0 ["疑似新的（高敏）"]+"}"#line:1890
		O0OO00OO0OOOOO0O0 ["疑似旧的（高敏）"]="{"+O0OO00OO0OOOOO0O0 ["疑似旧的（高敏）"]+"}"#line:1891
		O0OO00OO0OOOOO0O0 ["报表类型"]="dfx_chanpin"#line:1892
		OO0O0OOOOOO00OO00 =pd .pivot_table (O000OO0O0000OOO0O ,values =["报告编码"],index =["产品名称"],columns ="报告单位评价",aggfunc ={"报告编码":"nunique"},fill_value ="0",margins =True ,dropna =False ,).rename (columns ={"报告编码":"数量"})#line:1894
		OO0O0OOOOOO00OO00 .columns =OO0O0OOOOOO00OO00 .columns .droplevel (0 )#line:1895
		O0OO00OO0OOOOO0O0 =pd .merge (O0OO00OO0OOOOO0O0 ,OO0O0OOOOOO00OO00 .reset_index (),on =["产品名称"],how ="left")#line:1896
		TABLE_tree_Level_2 (O0OO00OO0OOOOO0O0 .sort_values (by ="计数",ascending =[False ],na_position ="last"),1 ,O000OO0O0000OOO0O )#line:1897
	if O00O0O00O0O0O0O00 =="页面":#line:1899
		O0OO0OOOOOOOO0O0O =""#line:1900
		OO00OO0OO00O000O0 =""#line:1901
		O00OO0O0000OOO000 =O000OO0O0000OOO0O .loc [O000OO0O0000OOO0O ["报告类型-新的"].str .contains ("新",na =False )].copy ()#line:1902
		OO00O0O000000O00O =O000OO0O0000OOO0O .loc [~O000OO0O0000OOO0O ["报告类型-新的"].str .contains ("新",na =False )].copy ()#line:1903
		OO000OOO0000O0OO0 =OOOOOO0O0OOOO00OO (O00OO0O0000OOO000 )#line:1904
		OO00OO0O00OO000OO =OOOOOO0O0OOOO00OO (OO00O0O000000O00O )#line:1905
		if 1 ==1 :#line:1906
			for OO00OO0000OOOOO0O ,OOO00OOOO0000OOOO in OO00OO0O00OO000OO .iterrows ():#line:1907
					if "分隔符"not in OOO00OOOO0000OOOO ["条目"]:#line:1908
						OO0O0OOOO0OO0OO00 ="'"+str (OOO00OOOO0000OOOO ["条目"])+"':"+str (OOO00OOOO0000OOOO ["详细描述T"])+","#line:1909
						OO00OO0OO00O000O0 =OO00OO0OO00O000O0 +OO0O0OOOO0OO0OO00 #line:1910
			for OO00OO0000OOOOO0O ,OOO00OOOO0000OOOO in OO000OOO0000O0OO0 .iterrows ():#line:1911
				if str (OOO00OOOO0000OOOO ["条目"]).strip ()not in OO00OO0OO00O000O0 and "分隔符"not in str (OOO00OOOO0000OOOO ["条目"]):#line:1912
					OO0O0OOOO0OO0OO00 ="'"+str (OOO00OOOO0000OOOO ["条目"])+"':"+str (OOO00OOOO0000OOOO ["详细描述T"])+","#line:1913
					O0OO0OOOOOOOO0O0O =O0OO0OOOOOOOO0O0O +OO0O0OOOO0OO0OO00 #line:1914
		OO00OO0OO00O000O0 ="{"+OO00OO0OO00O000O0 +"}"#line:1915
		O0OO0OOOOOOOO0O0O ="{"+O0OO0OOOOOOOO0O0O +"}"#line:1916
		OO00000000OOOO0OO ="\n可能是新的不良反应：\n\n"+O0OO0OOOOOOOO0O0O +"\n\n\n可能不是新的不良反应：\n\n"+OO00OO0OO00O000O0 #line:1917
		TOOLS_view_dict (OO00000000OOOO0OO ,1 )#line:1918
def TOOLS_strdict_to_pd (O00OO0OO0OO00OO00 ):#line:1920
	""#line:1921
	return pd .DataFrame .from_dict (eval (O00OO0OO0OO00OO00 ),orient ="index",columns =["content"]).reset_index ()#line:1922
def TOOLS_xuanze (O00O00O00000OOOOO ,O0O0O00OO00OO00OO ):#line:1924
    ""#line:1925
    if O0O0O00OO00OO00OO ==0 :#line:1926
        O0O000OOO00OOO000 =pd .read_excel (filedialog .askopenfilename (filetypes =[("XLS",".xls")]),sheet_name =0 ,header =0 ,index_col =0 ,).reset_index ()#line:1927
    else :#line:1928
        O0O000OOO00OOO000 =pd .read_excel (peizhidir +"0（范例）批量筛选.xls",sheet_name =0 ,header =0 ,index_col =0 ,).reset_index ()#line:1929
    O00O00O00000OOOOO ["temppr"]=""#line:1930
    for O00O0OO00OOOO00O0 in O0O000OOO00OOO000 .columns .tolist ():#line:1931
        O00O00O00000OOOOO ["temppr"]=O00O00O00000OOOOO ["temppr"]+"----"+O00O00O00000OOOOO [O00O0OO00OOOO00O0 ]#line:1932
    OOOO00OO00O00OOOO ="测试字段MMMMM"#line:1933
    for O00O0OO00OOOO00O0 in O0O000OOO00OOO000 .columns .tolist ():#line:1934
        for OOO0O0OOO000OO0OO in O0O000OOO00OOO000 [O00O0OO00OOOO00O0 ].drop_duplicates ():#line:1936
            if OOO0O0OOO000OO0OO :#line:1937
                OOOO00OO00O00OOOO =OOOO00OO00O00OOOO +"|"+str (OOO0O0OOO000OO0OO )#line:1938
    O00O00O00000OOOOO =O00O00O00000OOOOO .loc [O00O00O00000OOOOO ["temppr"].str .contains (OOOO00OO00O00OOOO ,na =False )].copy ()#line:1939
    del O00O00O00000OOOOO ["temppr"]#line:1940
    O00O00O00000OOOOO =O00O00O00000OOOOO .reset_index (drop =True )#line:1941
    TABLE_tree_Level_2 (O00O00O00000OOOOO ,0 ,O00O00O00000OOOOO )#line:1943
def TOOLS_add_c (OO0OOO000OOOOOO00 ,O0OO0O00O00O0O000 ):#line:1945
			OO0OOO000OOOOOO00 ["关键字查找列o"]=""#line:1946
			for OOOOO00OO0OO00000 in TOOLS_get_list (O0OO0O00O00O0O000 ["查找列"]):#line:1947
				OO0OOO000OOOOOO00 ["关键字查找列o"]=OO0OOO000OOOOOO00 ["关键字查找列o"]+OO0OOO000OOOOOO00 [OOOOO00OO0OO00000 ].astype ("str")#line:1948
			if O0OO0O00O00O0O000 ["条件"]=="等于":#line:1949
				OO0OOO000OOOOOO00 .loc [(OO0OOO000OOOOOO00 [O0OO0O00O00O0O000 ["查找列"]].astype (str )==str (O0OO0O00O00O0O000 ["条件值"])),O0OO0O00O00O0O000 ["赋值列名"]]=O0OO0O00O00O0O000 ["赋值"]#line:1950
			if O0OO0O00O00O0O000 ["条件"]=="大于":#line:1951
				OO0OOO000OOOOOO00 .loc [(OO0OOO000OOOOOO00 [O0OO0O00O00O0O000 ["查找列"]].astype (float )>O0OO0O00O00O0O000 ["条件值"]),O0OO0O00O00O0O000 ["赋值列名"]]=O0OO0O00O00O0O000 ["赋值"]#line:1952
			if O0OO0O00O00O0O000 ["条件"]=="小于":#line:1953
				OO0OOO000OOOOOO00 .loc [(OO0OOO000OOOOOO00 [O0OO0O00O00O0O000 ["查找列"]].astype (float )<O0OO0O00O00O0O000 ["条件值"]),O0OO0O00O00O0O000 ["赋值列名"]]=O0OO0O00O00O0O000 ["赋值"]#line:1954
			if O0OO0O00O00O0O000 ["条件"]=="介于":#line:1955
				O0O000OO0O000O000 =TOOLS_get_list (O0OO0O00O00O0O000 ["条件值"])#line:1956
				OO0OOO000OOOOOO00 .loc [((OO0OOO000OOOOOO00 [O0OO0O00O00O0O000 ["查找列"]].astype (float )<float (O0O000OO0O000O000 [1 ]))&(OO0OOO000OOOOOO00 [O0OO0O00O00O0O000 ["查找列"]].astype (float )>float (O0O000OO0O000O000 [0 ]))),O0OO0O00O00O0O000 ["赋值列名"]]=O0OO0O00O00O0O000 ["赋值"]#line:1957
			if O0OO0O00O00O0O000 ["条件"]=="不含":#line:1958
				OO0OOO000OOOOOO00 .loc [(~OO0OOO000OOOOOO00 ["关键字查找列o"].str .contains (O0OO0O00O00O0O000 ["条件值"])),O0OO0O00O00O0O000 ["赋值列名"]]=O0OO0O00O00O0O000 ["赋值"]#line:1959
			if O0OO0O00O00O0O000 ["条件"]=="包含":#line:1960
				OO0OOO000OOOOOO00 .loc [OO0OOO000OOOOOO00 ["关键字查找列o"].str .contains (O0OO0O00O00O0O000 ["条件值"],na =False ),O0OO0O00O00O0O000 ["赋值列名"]]=O0OO0O00O00O0O000 ["赋值"]#line:1961
			if O0OO0O00O00O0O000 ["条件"]=="同时包含":#line:1962
				O00O0OO0OO0O00O00 =TOOLS_get_list0 (O0OO0O00O00O0O000 ["条件值"],0 )#line:1963
				if len (O00O0OO0OO0O00O00 )==1 :#line:1964
				    OO0OOO000OOOOOO00 .loc [OO0OOO000OOOOOO00 ["关键字查找列o"].str .contains (O00O0OO0OO0O00O00 [0 ],na =False ),O0OO0O00O00O0O000 ["赋值列名"]]=O0OO0O00O00O0O000 ["赋值"]#line:1965
				if len (O00O0OO0OO0O00O00 )==2 :#line:1966
				    OO0OOO000OOOOOO00 .loc [(OO0OOO000OOOOOO00 ["关键字查找列o"].str .contains (O00O0OO0OO0O00O00 [0 ],na =False ))&(OO0OOO000OOOOOO00 ["关键字查找列o"].str .contains (O00O0OO0OO0O00O00 [1 ],na =False )),O0OO0O00O00O0O000 ["赋值列名"]]=O0OO0O00O00O0O000 ["赋值"]#line:1967
				if len (O00O0OO0OO0O00O00 )==3 :#line:1968
				    OO0OOO000OOOOOO00 .loc [(OO0OOO000OOOOOO00 ["关键字查找列o"].str .contains (O00O0OO0OO0O00O00 [0 ],na =False ))&(OO0OOO000OOOOOO00 ["关键字查找列o"].str .contains (O00O0OO0OO0O00O00 [1 ],na =False ))&(OO0OOO000OOOOOO00 ["关键字查找列o"].str .contains (O00O0OO0OO0O00O00 [2 ],na =False )),O0OO0O00O00O0O000 ["赋值列名"]]=O0OO0O00O00O0O000 ["赋值"]#line:1969
				if len (O00O0OO0OO0O00O00 )==4 :#line:1970
				    OO0OOO000OOOOOO00 .loc [(OO0OOO000OOOOOO00 ["关键字查找列o"].str .contains (O00O0OO0OO0O00O00 [0 ],na =False ))&(OO0OOO000OOOOOO00 ["关键字查找列o"].str .contains (O00O0OO0OO0O00O00 [1 ],na =False ))&(OO0OOO000OOOOOO00 ["关键字查找列o"].str .contains (O00O0OO0OO0O00O00 [2 ],na =False ))&(OO0OOO000OOOOOO00 ["关键字查找列o"].str .contains (O00O0OO0OO0O00O00 [3 ],na =False )),O0OO0O00O00O0O000 ["赋值列名"]]=O0OO0O00O00O0O000 ["赋值"]#line:1971
				if len (O00O0OO0OO0O00O00 )==5 :#line:1972
				    OO0OOO000OOOOOO00 .loc [(OO0OOO000OOOOOO00 ["关键字查找列o"].str .contains (O00O0OO0OO0O00O00 [0 ],na =False ))&(OO0OOO000OOOOOO00 ["关键字查找列o"].str .contains (O00O0OO0OO0O00O00 [1 ],na =False ))&(OO0OOO000OOOOOO00 ["关键字查找列o"].str .contains (O00O0OO0OO0O00O00 [2 ],na =False ))&(OO0OOO000OOOOOO00 ["关键字查找列o"].str .contains (O00O0OO0OO0O00O00 [3 ],na =False ))&(OO0OOO000OOOOOO00 ["关键字查找列o"].str .contains (O00O0OO0OO0O00O00 [4 ],na =False )),O0OO0O00O00O0O000 ["赋值列名"]]=O0OO0O00O00O0O000 ["赋值"]#line:1973
			return OO0OOO000OOOOOO00 #line:1974
def TOOL_guizheng (O0O0OO0OO0OOOO0O0 ,O0000000O0OO0OO0O ,OO0OOO0OO0OOO000O ):#line:1977
	""#line:1978
	if O0000000O0OO0OO0O ==0 :#line:1979
		OO0O0OOOO0O000OO0 =pd .read_excel (filedialog .askopenfilename (filetypes =[("XLSX",".xlsx")]),sheet_name =0 ,header =0 ,index_col =0 ,).reset_index ()#line:1980
		OO0O0OOOO0O000OO0 =OO0O0OOOO0O000OO0 [(OO0O0OOOO0O000OO0 ["执行标记"]=="是")].reset_index ()#line:1981
		for OO0O000OO000OO000 ,O000OO000OOO00000 in OO0O0OOOO0O000OO0 .iterrows ():#line:1982
			O0O0OO0OO0OOOO0O0 =TOOLS_add_c (O0O0OO0OO0OOOO0O0 ,O000OO000OOO00000 )#line:1983
		del O0O0OO0OO0OOOO0O0 ["关键字查找列o"]#line:1984
	elif O0000000O0OO0OO0O ==1 :#line:1986
		OO0O0OOOO0O000OO0 =pd .read_excel (peizhidir +"0（范例）数据规整.xlsx",sheet_name =0 ,header =0 ,index_col =0 ,).reset_index ()#line:1987
		OO0O0OOOO0O000OO0 =OO0O0OOOO0O000OO0 [(OO0O0OOOO0O000OO0 ["执行标记"]=="是")].reset_index ()#line:1988
		for OO0O000OO000OO000 ,O000OO000OOO00000 in OO0O0OOOO0O000OO0 .iterrows ():#line:1989
			O0O0OO0OO0OOOO0O0 =TOOLS_add_c (O0O0OO0OO0OOOO0O0 ,O000OO000OOO00000 )#line:1990
		del O0O0OO0OO0OOOO0O0 ["关键字查找列o"]#line:1991
	elif O0000000O0OO0OO0O =="课题":#line:1993
		OO0O0OOOO0O000OO0 =pd .read_excel (peizhidir +"0（范例）品类规整.xlsx",sheet_name =0 ,header =0 ,index_col =0 ,).reset_index ()#line:1994
		OO0O0OOOO0O000OO0 =OO0O0OOOO0O000OO0 [(OO0O0OOOO0O000OO0 ["执行标记"]=="是")].reset_index ()#line:1995
		for OO0O000OO000OO000 ,O000OO000OOO00000 in OO0O0OOOO0O000OO0 .iterrows ():#line:1996
			O0O0OO0OO0OOOO0O0 =TOOLS_add_c (O0O0OO0OO0OOOO0O0 ,O000OO000OOO00000 )#line:1997
		del O0O0OO0OO0OOOO0O0 ["关键字查找列o"]#line:1998
	elif O0000000O0OO0OO0O ==2 :#line:2000
		text .insert (END ,"\n开展报告单位和监测机构名称规整...")#line:2001
		O00OOOOOOO0O0000O =pd .read_excel (peizhidir +"0（范例）上报单位.xls",sheet_name ="报告单位",header =0 ,index_col =0 ,).fillna ("没有定义好X").reset_index ()#line:2002
		O00OO00O00OOOO00O =pd .read_excel (peizhidir +"0（范例）上报单位.xls",sheet_name ="监测机构",header =0 ,index_col =0 ,).fillna ("没有定义好X").reset_index ()#line:2003
		OOOOO0O0OO0OOO0OO =pd .read_excel (peizhidir +"0（范例）上报单位.xls",sheet_name ="地市清单",header =0 ,index_col =0 ,).fillna ("没有定义好X").reset_index ()#line:2004
		for OO0O000OO000OO000 ,O000OO000OOO00000 in O00OOOOOOO0O0000O .iterrows ():#line:2005
			O0O0OO0OO0OOOO0O0 .loc [(O0O0OO0OO0OOOO0O0 ["单位名称"]==O000OO000OOO00000 ["曾用名1"]),"单位名称"]=O000OO000OOO00000 ["单位名称"]#line:2006
			O0O0OO0OO0OOOO0O0 .loc [(O0O0OO0OO0OOOO0O0 ["单位名称"]==O000OO000OOO00000 ["曾用名2"]),"单位名称"]=O000OO000OOO00000 ["单位名称"]#line:2007
			O0O0OO0OO0OOOO0O0 .loc [(O0O0OO0OO0OOOO0O0 ["单位名称"]==O000OO000OOO00000 ["曾用名3"]),"单位名称"]=O000OO000OOO00000 ["单位名称"]#line:2008
			O0O0OO0OO0OOOO0O0 .loc [(O0O0OO0OO0OOOO0O0 ["单位名称"]==O000OO000OOO00000 ["曾用名4"]),"单位名称"]=O000OO000OOO00000 ["单位名称"]#line:2009
			O0O0OO0OO0OOOO0O0 .loc [(O0O0OO0OO0OOOO0O0 ["单位名称"]==O000OO000OOO00000 ["曾用名5"]),"单位名称"]=O000OO000OOO00000 ["单位名称"]#line:2010
			O0O0OO0OO0OOOO0O0 .loc [(O0O0OO0OO0OOOO0O0 ["单位名称"]==O000OO000OOO00000 ["单位名称"]),"医疗机构类别"]=O000OO000OOO00000 ["医疗机构类别"]#line:2012
			O0O0OO0OO0OOOO0O0 .loc [(O0O0OO0OO0OOOO0O0 ["单位名称"]==O000OO000OOO00000 ["单位名称"]),"监测机构"]=O000OO000OOO00000 ["监测机构"]#line:2013
		for OO0O000OO000OO000 ,O000OO000OOO00000 in O00OO00O00OOOO00O .iterrows ():#line:2015
			O0O0OO0OO0OOOO0O0 .loc [(O0O0OO0OO0OOOO0O0 ["监测机构"]==O000OO000OOO00000 ["曾用名1"]),"监测机构"]=O000OO000OOO00000 ["监测机构"]#line:2016
			O0O0OO0OO0OOOO0O0 .loc [(O0O0OO0OO0OOOO0O0 ["监测机构"]==O000OO000OOO00000 ["曾用名2"]),"监测机构"]=O000OO000OOO00000 ["监测机构"]#line:2017
			O0O0OO0OO0OOOO0O0 .loc [(O0O0OO0OO0OOOO0O0 ["监测机构"]==O000OO000OOO00000 ["曾用名3"]),"监测机构"]=O000OO000OOO00000 ["监测机构"]#line:2018
		for OOOO000OO00OO0O0O in OOOOO0O0OO0OOO0OO ["地市列表"]:#line:2020
			O0O0OO0OO0OOOO0O0 .loc [(O0O0OO0OO0OOOO0O0 ["上报单位所属地区"].str .contains (OOOO000OO00OO0O0O ,na =False )),"市级监测机构"]=OOOO000OO00OO0O0O #line:2021
		O0O0OO0OO0OOOO0O0 .loc [(O0O0OO0OO0OOOO0O0 ["上报单位所属地区"].str .contains ("顺德",na =False )),"市级监测机构"]="佛山"#line:2024
		O0O0OO0OO0OOOO0O0 ["市级监测机构"]=O0O0OO0OO0OOOO0O0 ["市级监测机构"].fillna ("-未规整的-")#line:2025
	elif O0000000O0OO0OO0O ==3 :#line:2027
			OO0OOOO00OOO0O000 =(O0O0OO0OO0OOOO0O0 .groupby (["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号"]).aggregate ({"报告编码":"count"}).reset_index ())#line:2032
			OO0OOOO00OOO0O000 =OO0OOOO00OOO0O000 .sort_values (by =["注册证编号/曾用注册证编号","报告编码"],ascending =[False ,False ],na_position ="last").reset_index ()#line:2035
			text .insert (END ,"\n开展产品名称规整..")#line:2036
			del OO0OOOO00OOO0O000 ["报告编码"]#line:2037
			OO0OOOO00OOO0O000 =OO0OOOO00OOO0O000 .drop_duplicates (["注册证编号/曾用注册证编号"])#line:2038
			O0O0OO0OO0OOOO0O0 =O0O0OO0OO0OOOO0O0 .rename (columns ={"上市许可持有人名称":"上市许可持有人名称（规整前）","产品类别":"产品类别（规整前）","产品名称":"产品名称（规整前）"})#line:2040
			O0O0OO0OO0OOOO0O0 =pd .merge (O0O0OO0OO0OOOO0O0 ,OO0OOOO00OOO0O000 ,on =["注册证编号/曾用注册证编号"],how ="left")#line:2041
	elif O0000000O0OO0OO0O ==4 :#line:2043
		text .insert (END ,"\n正在开展化妆品注册单位规整...")#line:2044
		O00OO00O00OOOO00O =pd .read_excel (peizhidir +"0（范例）注册单位.xlsx",sheet_name ="机构列表",header =0 ,index_col =0 ,).reset_index ()#line:2045
		for OO0O000OO000OO000 ,O000OO000OOO00000 in O00OO00O00OOOO00O .iterrows ():#line:2047
			O0O0OO0OO0OOOO0O0 .loc [(O0O0OO0OO0OOOO0O0 ["单位名称"]==O000OO000OOO00000 ["中文全称"]),"监测机构"]=O000OO000OOO00000 ["归属地区"]#line:2048
			O0O0OO0OO0OOOO0O0 .loc [(O0O0OO0OO0OOOO0O0 ["单位名称"]==O000OO000OOO00000 ["中文全称"]),"市级监测机构"]=O000OO000OOO00000 ["地市"]#line:2049
		O0O0OO0OO0OOOO0O0 ["监测机构"]=O0O0OO0OO0OOOO0O0 ["监测机构"].fillna ("未规整")#line:2050
		O0O0OO0OO0OOOO0O0 ["市级监测机构"]=O0O0OO0OO0OOOO0O0 ["市级监测机构"].fillna ("未规整")#line:2051
	if OO0OOO0OO0OOO000O ==True :#line:2052
		return O0O0OO0OO0OOOO0O0 #line:2053
	else :#line:2054
		TABLE_tree_Level_2 (O0O0OO0OO0OOOO0O0 ,0 ,O0O0OO0OO0OOOO0O0 )#line:2055
def TOOL_person (OO00OOOOO0O00OO00 ):#line:2057
	""#line:2058
	OO00O000O00O00OOO =pd .read_excel (peizhidir +"0（范例）注册单位.xlsx",sheet_name ="专家列表",header =0 ,index_col =0 ,).reset_index ()#line:2059
	for OO0OO0000000OOO0O ,O00OOO0O00O0O0OO0 in OO00O000O00O00OOO .iterrows ():#line:2060
		OO00OOOOO0O00OO00 .loc [(OO00OOOOO0O00OO00 ["市级监测机构"]==O00OOO0O00O0O0OO0 ["市级监测机构"]),"评表人员"]=O00OOO0O00O0O0OO0 ["评表人员"]#line:2061
		OO00OOOOO0O00OO00 ["评表人员"]=OO00OOOOO0O00OO00 ["评表人员"].fillna ("未规整")#line:2062
		OO00O0O0O00OO00O0 =OO00OOOOO0O00OO00 .groupby (["评表人员"]).agg (报告数量 =("报告编码","nunique"),地市 =("市级监测机构",STAT_countx ),).sort_values (by ="报告数量",ascending =[False ],na_position ="last").reset_index ()#line:2066
	TABLE_tree_Level_2 (OO00O0O0O00OO00O0 ,0 ,OO00O0O0O00OO00O0 )#line:2067
def TOOLS_get_list (OO000O00000000OOO ):#line:2069
    ""#line:2070
    OO000O00000000OOO =str (OO000O00000000OOO )#line:2071
    OOOO000O0OOOOO0O0 =[]#line:2072
    OOOO000O0OOOOO0O0 .append (OO000O00000000OOO )#line:2073
    OOOO000O0OOOOO0O0 =",".join (OOOO000O0OOOOO0O0 )#line:2074
    OOOO000O0OOOOO0O0 =OOOO000O0OOOOO0O0 .split ("|")#line:2075
    OO000O0000O00OO0O =OOOO000O0OOOOO0O0 [:]#line:2076
    OOOO000O0OOOOO0O0 =list (set (OOOO000O0OOOOO0O0 ))#line:2077
    OOOO000O0OOOOO0O0 .sort (key =OO000O0000O00OO0O .index )#line:2078
    return OOOO000O0OOOOO0O0 #line:2079
def TOOLS_get_list0 (OOOOOOOOO0O0OO0O0 ,OOOO00OO000OOO0O0 ,*O0O0O0OO0O0OO0000 ):#line:2081
    ""#line:2082
    OOOOOOOOO0O0OO0O0 =str (OOOOOOOOO0O0OO0O0 )#line:2083
    if pd .notnull (OOOOOOOOO0O0OO0O0 ):#line:2085
        try :#line:2086
            if "use("in str (OOOOOOOOO0O0OO0O0 ):#line:2087
                OO0O00OO00O000OOO =OOOOOOOOO0O0OO0O0 #line:2088
                O0000000OO0OO00O0 =re .compile (r"[(](.*?)[)]",re .S )#line:2089
                OOOOO00O0O00OOOOO =re .findall (O0000000OO0OO00O0 ,OO0O00OO00O000OOO )#line:2090
                OO00OOOO00O00OO0O =[]#line:2091
                if ").list"in OOOOOOOOO0O0OO0O0 :#line:2092
                    O0OOO00O00O0OOO00 =peizhidir +""+str (OOOOO00O0O00OOOOO [0 ])+".xls"#line:2093
                    O0O00O00O000OOO00 =pd .read_excel (O0OOO00O00O0OOO00 ,sheet_name =OOOOO00O0O00OOOOO [0 ],header =0 ,index_col =0 ).reset_index ()#line:2096
                    O0O00O00O000OOO00 ["检索关键字"]=O0O00O00O000OOO00 ["检索关键字"].astype (str )#line:2097
                    OO00OOOO00O00OO0O =O0O00O00O000OOO00 ["检索关键字"].tolist ()+OO00OOOO00O00OO0O #line:2098
                if ").file"in OOOOOOOOO0O0OO0O0 :#line:2099
                    OO00OOOO00O00OO0O =OOOO00OO000OOO0O0 [OOOOO00O0O00OOOOO [0 ]].astype (str ).tolist ()+OO00OOOO00O00OO0O #line:2101
                try :#line:2104
                    if "报告类型-新的"in OOOO00OO000OOO0O0 .columns :#line:2105
                        OO00OOOO00O00OO0O =",".join (OO00OOOO00O00OO0O )#line:2106
                        OO00OOOO00O00OO0O =OO00OOOO00O00OO0O .split (";")#line:2107
                        OO00OOOO00O00OO0O =",".join (OO00OOOO00O00OO0O )#line:2108
                        OO00OOOO00O00OO0O =OO00OOOO00O00OO0O .split ("；")#line:2109
                        OO00OOOO00O00OO0O =[O0OOOOO0000O0O00O .replace ("（严重）","")for O0OOOOO0000O0O00O in OO00OOOO00O00OO0O ]#line:2110
                        OO00OOOO00O00OO0O =[O0OOO0O00OOOO000O .replace ("（一般）","")for O0OOO0O00OOOO000O in OO00OOOO00O00OO0O ]#line:2111
                except :#line:2112
                    pass #line:2113
                OO00OOOO00O00OO0O =",".join (OO00OOOO00O00OO0O )#line:2115
                OO00OOOO00O00OO0O =OO00OOOO00O00OO0O .split (";")#line:2116
                OO00OOOO00O00OO0O =",".join (OO00OOOO00O00OO0O )#line:2117
                OO00OOOO00O00OO0O =OO00OOOO00O00OO0O .split ("；")#line:2118
                OO00OOOO00O00OO0O =",".join (OO00OOOO00O00OO0O )#line:2119
                OO00OOOO00O00OO0O =OO00OOOO00O00OO0O .split ("、")#line:2120
                OO00OOOO00O00OO0O =",".join (OO00OOOO00O00OO0O )#line:2121
                OO00OOOO00O00OO0O =OO00OOOO00O00OO0O .split ("，")#line:2122
                OO00OOOO00O00OO0O =",".join (OO00OOOO00O00OO0O )#line:2123
                OO00OOOO00O00OO0O =OO00OOOO00O00OO0O .split (",")#line:2124
                OO0OO0O0O000O0O0O =OO00OOOO00O00OO0O [:]#line:2127
                try :#line:2128
                    if O0O0O0OO0O0OO0000 [0 ]==1000 :#line:2129
                      pass #line:2130
                except :#line:2131
                      OO00OOOO00O00OO0O =list (set (OO00OOOO00O00OO0O ))#line:2132
                OO00OOOO00O00OO0O .sort (key =OO0OO0O0O000O0O0O .index )#line:2133
            else :#line:2135
                OOOOOOOOO0O0OO0O0 =str (OOOOOOOOO0O0OO0O0 )#line:2136
                OO00OOOO00O00OO0O =[]#line:2137
                OO00OOOO00O00OO0O .append (OOOOOOOOO0O0OO0O0 )#line:2138
                OO00OOOO00O00OO0O =",".join (OO00OOOO00O00OO0O )#line:2139
                OO00OOOO00O00OO0O =OO00OOOO00O00OO0O .split ("、")#line:2140
                OO00OOOO00O00OO0O =",".join (OO00OOOO00O00OO0O )#line:2141
                OO00OOOO00O00OO0O =OO00OOOO00O00OO0O .split ("，")#line:2142
                OO00OOOO00O00OO0O =",".join (OO00OOOO00O00OO0O )#line:2143
                OO00OOOO00O00OO0O =OO00OOOO00O00OO0O .split (",")#line:2144
                OO0OO0O0O000O0O0O =OO00OOOO00O00OO0O [:]#line:2146
                try :#line:2147
                    if O0O0O0OO0O0OO0000 [0 ]==1000 :#line:2148
                      OO00OOOO00O00OO0O =list (set (OO00OOOO00O00OO0O ))#line:2149
                except :#line:2150
                      pass #line:2151
                OO00OOOO00O00OO0O .sort (key =OO0OO0O0O000O0O0O .index )#line:2152
                OO00OOOO00O00OO0O .sort (key =OO0OO0O0O000O0O0O .index )#line:2153
        except ValueError2 :#line:2155
            showinfo (title ="提示信息",message ="创建单元格支持多个甚至表单（文件）传入的方法，返回一个经过整理的清单出错，任务终止。")#line:2156
            return False #line:2157
    return OO00OOOO00O00OO0O #line:2159
def TOOLS_easyread2 (OOOOO0O00OOO0000O ):#line:2161
    ""#line:2162
    OOOOO0O00OOO0000O ["分隔符"]="●"#line:2164
    OOOOO0O00OOO0000O ["上报机构描述"]=(OOOOO0O00OOO0000O ["使用过程"].astype ("str")+OOOOO0O00OOO0000O ["分隔符"]+OOOOO0O00OOO0000O ["事件原因分析"].astype ("str")+OOOOO0O00OOO0000O ["分隔符"]+OOOOO0O00OOO0000O ["事件原因分析描述"].astype ("str")+OOOOO0O00OOO0000O ["分隔符"]+OOOOO0O00OOO0000O ["初步处置情况"].astype ("str"))#line:2173
    OOOOO0O00OOO0000O ["持有人处理描述"]=(OOOOO0O00OOO0000O ["关联性评价"].astype ("str")+OOOOO0O00OOO0000O ["分隔符"]+OOOOO0O00OOO0000O ["调查情况"].astype ("str")+OOOOO0O00OOO0000O ["分隔符"]+OOOOO0O00OOO0000O ["事件原因分析"].astype ("str")+OOOOO0O00OOO0000O ["分隔符"]+OOOOO0O00OOO0000O ["具体控制措施"].astype ("str")+OOOOO0O00OOO0000O ["分隔符"]+OOOOO0O00OOO0000O ["未采取控制措施原因"].astype ("str"))#line:2184
    O000O0OOOOO0O00OO =OOOOO0O00OOO0000O [["报告编码","事件发生日期","报告日期","单位名称","产品名称","注册证编号/曾用注册证编号","产品批号","型号","规格","上市许可持有人名称","管理类别","伤害","伤害表现","器械故障表现","上报机构描述","持有人处理描述","经营企业使用单位报告状态","监测机构","产品类别","医疗机构类别","年龄","年龄类型","性别"]]#line:2211
    O000O0OOOOO0O00OO =O000O0OOOOO0O00OO .sort_values (by =["事件发生日期"],ascending =[False ],na_position ="last",)#line:2216
    O000O0OOOOO0O00OO =O000O0OOOOO0O00OO .rename (columns ={"报告编码":"规整编码"})#line:2217
    return O000O0OOOOO0O00OO #line:2218
def fenci0 (O000OO0O00O00O000 ):#line:2221
	""#line:2222
	OO0OO00O00OOO0O0O =Toplevel ()#line:2223
	OO0OO00O00OOO0O0O .title ('词频统计')#line:2224
	OO0OO0OO00OOOOO00 =OO0OO00O00OOO0O0O .winfo_screenwidth ()#line:2225
	O000000O00000000O =OO0OO00O00OOO0O0O .winfo_screenheight ()#line:2227
	O0O00O0OOO00O0O00 =400 #line:2229
	OOOOO000O00O0O00O =120 #line:2230
	O00000O0O00O00OOO =(OO0OO0OO00OOOOO00 -O0O00O0OOO00O0O00 )/2 #line:2232
	OOOOOO00000000000 =(O000000O00000000O -OOOOO000O00O0O00O )/2 #line:2233
	OO0OO00O00OOO0O0O .geometry ("%dx%d+%d+%d"%(O0O00O0OOO00O0O00 ,OOOOO000O00O0O00O ,O00000O0O00O00OOO ,OOOOOO00000000000 ))#line:2234
	OO00OO0OOO0O0000O =Label (OO0OO00O00OOO0O0O ,text ="配置文件：")#line:2235
	OO00OO0OOO0O0000O .pack ()#line:2236
	O00OO00O0OO0OOOOO =Label (OO0OO00O00OOO0O0O ,text ="需要分词的列：")#line:2237
	OO0000O000OOOO00O =Entry (OO0OO00O00OOO0O0O ,width =80 )#line:2239
	OO0000O000OOOO00O .insert (0 ,peizhidir +"0（范例）中文分词工作文件.xls")#line:2240
	OOO0OO00OOO00O0O0 =Entry (OO0OO00O00OOO0O0O ,width =80 )#line:2241
	OOO0OO00OOO00O0O0 .insert (0 ,"器械故障表现，伤害表现")#line:2242
	OO0000O000OOOO00O .pack ()#line:2243
	O00OO00O0OO0OOOOO .pack ()#line:2244
	OOO0OO00OOO00O0O0 .pack ()#line:2245
	OO00000O0O0O00000 =LabelFrame (OO0OO00O00OOO0O0O )#line:2246
	O00O0000OOOO0000O =Button (OO00000O0O0O00000 ,text ="确定",width =10 ,command =lambda :PROGRAM_thread_it (tree_Level_2 ,fenci (OO0000O000OOOO00O .get (),OOO0OO00OOO00O0O0 .get (),O000OO0O00O00O000 ),1 ,0 ))#line:2247
	O00O0000OOOO0000O .pack (side =LEFT ,padx =1 ,pady =1 )#line:2248
	OO00000O0O0O00000 .pack ()#line:2249
def fenci (OO000000OO0O00OOO ,OOOO0O000OO0000O0 ,OO00OOO0OO00OOOO0 ):#line:2251
    ""#line:2252
    import glob #line:2253
    import jieba #line:2254
    import random #line:2255
    try :#line:2257
        OO00OOO0OO00OOOO0 =OO00OOO0OO00OOOO0 .drop_duplicates (["报告编码"])#line:2258
    except :#line:2259
        pass #line:2260
    def O00OO0000O00000O0 (O0000O0O0000OO000 ,OO0O0OOO0O00O0OOO ):#line:2261
        O000O0OO0OO0OO00O ={}#line:2262
        for OO000O0O0OOOOO00O in O0000O0O0000OO000 :#line:2263
            O000O0OO0OO0OO00O [OO000O0O0OOOOO00O ]=O000O0OO0OO0OO00O .get (OO000O0O0OOOOO00O ,0 )+1 #line:2264
        return sorted (O000O0OO0OO0OO00O .items (),key =lambda O0OO0O000OOOO0000 :O0OO0O000OOOO0000 [1 ],reverse =True )[:OO0O0OOO0O00O0OOO ]#line:2265
    O00O0OOO00O00OO0O =pd .read_excel (OO000000OO0O00OOO ,sheet_name ="初始化",header =0 ,index_col =0 ).reset_index ()#line:2269
    OO0OOOOO0O00OOO0O =O00O0OOO00O00OO0O .iloc [0 ,2 ]#line:2271
    O0O000OO000OO0O00 =pd .read_excel (OO000000OO0O00OOO ,sheet_name ="停用词",header =0 ,index_col =0 ).reset_index ()#line:2274
    O0O000OO000OO0O00 ["停用词"]=O0O000OO000OO0O00 ["停用词"].astype (str )#line:2276
    O00000O00O0O000OO =[OOO00OOO000O0OOO0 .strip ()for OOO00OOO000O0OOO0 in O0O000OO000OO0O00 ["停用词"]]#line:2277
    O00OO0OOO0OOO0O0O =pd .read_excel (OO000000OO0O00OOO ,sheet_name ="本地词库",header =0 ,index_col =0 ).reset_index ()#line:2280
    OO00O0O00OO00OO0O =O00OO0OOO0OOO0O0O ["本地词库"]#line:2281
    jieba .load_userdict (OO00O0O00OO00OO0O )#line:2282
    OO0O00OO0O0O00OOO =""#line:2285
    OOOOOOO000O00OOO0 =get_list0 (OOOO0O000OO0000O0 ,OO00OOO0OO00OOOO0 )#line:2288
    try :#line:2289
        for OOOOOO000OO0OO0O0 in OOOOOOO000O00OOO0 :#line:2290
            for O000O0O0O0OO000O0 in OO00OOO0OO00OOOO0 [OOOOOO000OO0OO0O0 ]:#line:2291
                OO0O00OO0O0O00OOO =OO0O00OO0O0O00OOO +str (O000O0O0O0OO000O0 )#line:2292
    except :#line:2293
        text .insert (END ,"分词配置文件未正确设置，将对整个表格进行分词。")#line:2294
        for OOOOOO000OO0OO0O0 in OO00OOO0OO00OOOO0 .columns .tolist ():#line:2295
            for O000O0O0O0OO000O0 in OO00OOO0OO00OOOO0 [OOOOOO000OO0OO0O0 ]:#line:2296
                OO0O00OO0O0O00OOO =OO0O00OO0O0O00OOO +str (O000O0O0O0OO000O0 )#line:2297
    O0O0OO000O0O0OOO0 =[]#line:2298
    O0O0OO000O0O0OOO0 =O0O0OO000O0O0OOO0 +[O0O000O0000OOO00O for O0O000O0000OOO00O in jieba .cut (OO0O00OO0O0O00OOO )if O0O000O0000OOO00O not in O00000O00O0O000OO ]#line:2299
    OOO0O00O00O000000 =dict (O00OO0000O00000O0 (O0O0OO000O0O0OOO0 ,OO0OOOOO0O00OOO0O ))#line:2300
    O0O0000000O00OO0O =pd .DataFrame ([OOO0O00O00O000000 ]).T #line:2301
    O0O0000000O00OO0O =O0O0000000O00OO0O .reset_index ()#line:2302
    return O0O0000000O00OO0O #line:2303
def TOOLS_time (OO0000O0OOOOO0O00 ,OO0OO0O00O0O0O0O0 ,OO0OOO0OOOOOO0OOO ):#line:2305
	""#line:2306
	OOOOOOO0O0OO00OO0 =OO0000O0OOOOO0O00 .drop_duplicates (["报告编码"]).groupby ([OO0OO0O00O0O0O0O0 ]).agg (报告总数 =("报告编码","nunique"),严重伤害数 =("伤害",lambda OO0O0OO00O0OO0O00 :STAT_countpx (OO0O0OO00O0OO0O00 .values ,"严重伤害")),死亡数量 =("伤害",lambda O0O0O0OOO0O000OO0 :STAT_countpx (O0O0O0OOO0O000OO0 .values ,"死亡")),).sort_values (by =OO0OO0O00O0O0O0O0 ,ascending =[True ],na_position ="last").reset_index ()#line:2311
	OOOOOOO0O0OO00OO0 =OOOOOOO0O0OO00OO0 .set_index (OO0OO0O00O0O0O0O0 )#line:2315
	OOOOOOO0O0OO00OO0 =OOOOOOO0O0OO00OO0 .resample ('D').asfreq (fill_value =0 )#line:2317
	OOOOOOO0O0OO00OO0 ["time"]=OOOOOOO0O0OO00OO0 .index .values #line:2319
	OOOOOOO0O0OO00OO0 ["time"]=pd .to_datetime (OOOOOOO0O0OO00OO0 ["time"],format ="%Y/%m/%d").dt .date #line:2320
	if OO0OOO0OOOOOO0OOO ==1 :#line:2322
		return OOOOOOO0O0OO00OO0 .reset_index (drop =True )#line:2324
	OOOOOOO0O0OO00OO0 ["30天累计数"]=OOOOOOO0O0OO00OO0 ["报告总数"].rolling (30 ,min_periods =1 ).agg (lambda OO00O000O0O000OO0 :sum (OO00O000O0O000OO0 )).astype (int )#line:2326
	OOOOOOO0O0OO00OO0 ["30天严重伤害累计数"]=OOOOOOO0O0OO00OO0 ["严重伤害数"].rolling (30 ,min_periods =1 ).agg (lambda OOO0OO00O0O00OO0O :sum (OOO0OO00O0O00OO0O )).astype (int )#line:2327
	OOOOOOO0O0OO00OO0 ["30天死亡累计数"]=OOOOOOO0O0OO00OO0 ["死亡数量"].rolling (30 ,min_periods =1 ).agg (lambda O0OOOOO0OO00000OO :sum (O0OOOOO0OO00000OO )).astype (int )#line:2328
	OOOOOOO0O0OO00OO0 .loc [(((OOOOOOO0O0OO00OO0 ["30天累计数"]>=3 )&(OOOOOOO0O0OO00OO0 ["30天严重伤害累计数"]>=1 ))|(OOOOOOO0O0OO00OO0 ["30天累计数"]>=5 )|(OOOOOOO0O0OO00OO0 ["30天死亡累计数"]>=1 )),"关注区域"]=OOOOOOO0O0OO00OO0 ["30天累计数"]#line:2349
	DRAW_make_risk_plot (OOOOOOO0O0OO00OO0 ,"time",["30天累计数","30天严重伤害累计数","关注区域"],"折线图",999 )#line:2354
def TOOLS_keti (OOOO00O0O0O0O000O ):#line:2358
	""#line:2359
	import datetime #line:2360
	def OOOOOO000000O0O0O (O0OOOO0OOOO0OO0OO ,OO00OOOO0OOO00000 ):#line:2362
		if ini ["模式"]=="药品":#line:2363
			OOOOOOO00OOOO0O00 =pd .read_excel (peizhidir +"0（范例）预警参数.xlsx",header =0 ,sheet_name ="药品").reset_index (drop =True )#line:2364
		if ini ["模式"]=="器械":#line:2365
			OOOOOOO00OOOO0O00 =pd .read_excel (peizhidir +"0（范例）预警参数.xlsx",header =0 ,sheet_name ="器械").reset_index (drop =True )#line:2366
		if ini ["模式"]=="化妆品":#line:2367
			OOOOOOO00OOOO0O00 =pd .read_excel (peizhidir +"0（范例）预警参数.xlsx",header =0 ,sheet_name ="化妆品").reset_index (drop =True )#line:2368
		OO0O0000O0O00OO00 =OOOOOOO00OOOO0O00 ["权重"][0 ]#line:2369
		OOO0O0000000O0O00 =OOOOOOO00OOOO0O00 ["权重"][1 ]#line:2370
		O00OO0OO0OOO00OO0 =OOOOOOO00OOOO0O00 ["权重"][2 ]#line:2371
		OO0OO0OOO00OO0O0O =OOOOOOO00OOOO0O00 ["权重"][3 ]#line:2372
		OOO000OOO0000OO00 =OOOOOOO00OOOO0O00 ["值"][3 ]#line:2373
		OO0OO0O00O0O000O0 =OOOOOOO00OOOO0O00 ["权重"][4 ]#line:2375
		OO000O0OO0OOOOOO0 =OOOOOOO00OOOO0O00 ["值"][4 ]#line:2376
		O0OO0O000O0O00OO0 =OOOOOOO00OOOO0O00 ["权重"][5 ]#line:2378
		OOOO00OOOO0O0O0OO =OOOOOOO00OOOO0O00 ["值"][5 ]#line:2379
		OOOO0000O0O00OOOO =OOOOOOO00OOOO0O00 ["权重"][6 ]#line:2381
		O0O00OO0O000O00O0 =OOOOOOO00OOOO0O00 ["值"][6 ]#line:2382
		OO0O0O0O0000O0OOO =pd .to_datetime (O0OOOO0OOOO0OO0OO )#line:2384
		O0O00000000O0O00O =OO00OOOO0OOO00000 .copy ().set_index ('报告日期')#line:2385
		O0O00000000O0O00O =O0O00000000O0O00O .sort_index ()#line:2386
		if ini ["模式"]=="器械":#line:2387
			O0O00000000O0O00O ["关键字查找列"]=O0O00000000O0O00O ["器械故障表现"].astype (str )+O0O00000000O0O00O ["伤害表现"].astype (str )+O0O00000000O0O00O ["使用过程"].astype (str )+O0O00000000O0O00O ["事件原因分析描述"].astype (str )+O0O00000000O0O00O ["初步处置情况"].astype (str )#line:2388
		else :#line:2389
			O0O00000000O0O00O ["关键字查找列"]=O0O00000000O0O00O ["器械故障表现"].astype (str )#line:2390
		O0O00000000O0O00O .loc [O0O00000000O0O00O ["关键字查找列"].str .contains (OOO000OOO0000OO00 ,na =False ),"高度关注关键字"]=1 #line:2391
		O0O00000000O0O00O .loc [O0O00000000O0O00O ["关键字查找列"].str .contains (OO000O0OO0OOOOOO0 ,na =False ),"二级敏感词"]=1 #line:2392
		O0O00000000O0O00O .loc [O0O00000000O0O00O ["关键字查找列"].str .contains (OOOO00OOOO0O0O0OO ,na =False ),"减分项"]=1 #line:2393
		O0O0O000000000OOO =O0O00000000O0O00O .loc [OO0O0O0O0000O0OOO -pd .Timedelta (days =30 ):OO0O0O0O0000O0OOO ].reset_index ()#line:2395
		OO00O0O0O0OOO000O =O0O00000000O0O00O .loc [OO0O0O0O0000O0OOO -pd .Timedelta (days =365 ):OO0O0O0O0000O0OOO ].reset_index ()#line:2396
		O0OOOO00OOO0O0O00 =O0O0O000000000OOO .groupby (["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号"]).agg (证号计数 =("报告编码","nunique"),批号个数 =("产品批号","nunique"),批号列表 =("产品批号",STAT_countx ),型号个数 =("型号","nunique"),型号列表 =("型号",STAT_countx ),规格个数 =("规格","nunique"),规格列表 =("规格",STAT_countx ),).sort_values (by ="证号计数",ascending =[False ],na_position ="last").reset_index ()#line:2409
		O0000O00000OO00O0 =O0O0O000000000OOO .drop_duplicates (["报告编码"]).groupby (["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号"]).agg (严重伤害数 =("伤害",lambda O00OO0OOO0O00O0O0 :STAT_countpx (O00OO0OOO0O00O0O0 .values ,"严重伤害")),死亡数量 =("伤害",lambda O00O0OO0O000O00OO :STAT_countpx (O00O0OO0O000O00OO .values ,"死亡")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),待评价数 =("持有人报告状态",lambda OOO000OO000O0O0O0 :STAT_countpx (OOO000OO000O0O0O0 .values ,"待评价")),严重伤害待评价数 =("伤害与评价",lambda OO00O00O000000O0O :STAT_countpx (OO00O00O000000O0O .values ,"严重伤害待评价")),高度关注关键字 =("高度关注关键字","sum"),二级敏感词 =("二级敏感词","sum"),减分项 =("减分项","sum"),).reset_index ()#line:2421
		OO00000O0OOO0O00O =pd .merge (O0OOOO00OOO0O0O00 ,O0000O00000OO00O0 ,on =["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号"],how ="left")#line:2423
		O00O0O0O000000O00 =O0O0O000000000OOO .groupby (["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","型号"]).agg (型号计数 =("报告编码","nunique"),).sort_values (by ="型号计数",ascending =[False ],na_position ="last").reset_index ()#line:2430
		O00O0O0O000000O00 =O00O0O0O000000O00 .drop_duplicates ("注册证编号/曾用注册证编号")#line:2431
		O00O00000OOO0O000 =O0O0O000000000OOO .drop_duplicates (["报告编码"]).groupby (["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","产品批号"]).agg (批号计数 =("报告编码","nunique"),严重伤害数 =("伤害",lambda O0OOOO000O0000000 :STAT_countpx (O0OOOO000O0000000 .values ,"严重伤害")),).sort_values (by ="批号计数",ascending =[False ],na_position ="last").reset_index ()#line:2436
		O00O00000OOO0O000 ["风险评分-影响"]=0 #line:2440
		O00O00000OOO0O000 ["评分说明"]=""#line:2441
		O00O00000OOO0O000 .loc [((O00O00000OOO0O000 ["批号计数"]>=3 )&(O00O00000OOO0O000 ["严重伤害数"]>=1 )&(O00O00000OOO0O000 ["产品类别"]!="有源"))|((O00O00000OOO0O000 ["批号计数"]>=5 )&(O00O00000OOO0O000 ["产品类别"]!="有源")),"风险评分-影响"]=O00O00000OOO0O000 ["风险评分-影响"]+3 #line:2442
		O00O00000OOO0O000 .loc [(O00O00000OOO0O000 ["风险评分-影响"]>=3 ),"评分说明"]=O00O00000OOO0O000 ["评分说明"]+"●符合省中心无源规则+3;"#line:2443
		O00O00000OOO0O000 =O00O00000OOO0O000 .sort_values (by ="风险评分-影响",ascending =[False ],na_position ="last").reset_index (drop =True )#line:2447
		O00O00000OOO0O000 =O00O00000OOO0O000 .drop_duplicates ("注册证编号/曾用注册证编号")#line:2448
		O00O0O0O000000O00 =O00O0O0O000000O00 [["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","型号","型号计数"]]#line:2449
		O00O00000OOO0O000 =O00O00000OOO0O000 [["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","产品批号","批号计数","风险评分-影响","评分说明"]]#line:2450
		OO00000O0OOO0O00O =pd .merge (OO00000O0OOO0O00O ,O00O0O0O000000O00 ,on =["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号"],how ="left")#line:2451
		OO00000O0OOO0O00O =pd .merge (OO00000O0OOO0O00O ,O00O00000OOO0O000 ,on =["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号"],how ="left")#line:2453
		OO00000O0OOO0O00O .loc [((OO00000O0OOO0O00O ["证号计数"]>=3 )&(OO00000O0OOO0O00O ["严重伤害数"]>=1 )&(OO00000O0OOO0O00O ["产品类别"]=="有源"))|((OO00000O0OOO0O00O ["证号计数"]>=5 )&(OO00000O0OOO0O00O ["产品类别"]=="有源")),"风险评分-影响"]=OO00000O0OOO0O00O ["风险评分-影响"]+3 #line:2457
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["风险评分-影响"]>=3 )&(OO00000O0OOO0O00O ["产品类别"]=="有源"),"评分说明"]=OO00000O0OOO0O00O ["评分说明"]+"●符合省中心有源规则+3;"#line:2458
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["死亡数量"]>=1 ),"风险评分-影响"]=OO00000O0OOO0O00O ["风险评分-影响"]+10 #line:2463
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["风险评分-影响"]>=10 ),"评分说明"]=OO00000O0OOO0O00O ["评分说明"]+"存在死亡报告;"#line:2464
		O0OO0OO000O0O0O0O =round (OO0O0000O0O00OO00 *(OO00000O0OOO0O00O ["严重伤害数"]/OO00000O0OOO0O00O ["证号计数"]),2 )#line:2467
		OO00000O0OOO0O00O ["风险评分-影响"]=OO00000O0OOO0O00O ["风险评分-影响"]+O0OO0OO000O0O0O0O #line:2468
		OO00000O0OOO0O00O ["评分说明"]=OO00000O0OOO0O00O ["评分说明"]+"严重比评分"+O0OO0OO000O0O0O0O .astype (str )+";"#line:2469
		OO0O0OOOO0000OO00 =round (OOO0O0000000O0O00 *(np .log (OO00000O0OOO0O00O ["单位个数"])),2 )#line:2472
		OO00000O0OOO0O00O ["风险评分-影响"]=OO00000O0OOO0O00O ["风险评分-影响"]+OO0O0OOOO0000OO00 #line:2473
		OO00000O0OOO0O00O ["评分说明"]=OO00000O0OOO0O00O ["评分说明"]+"报告单位评分"+OO0O0OOOO0000OO00 .astype (str )+";"#line:2474
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["产品类别"]=="有源")&(OO00000O0OOO0O00O ["证号计数"]>=3 ),"风险评分-影响"]=OO00000O0OOO0O00O ["风险评分-影响"]+O00OO0OO0OOO00OO0 *OO00000O0OOO0O00O ["型号计数"]/OO00000O0OOO0O00O ["证号计数"]#line:2477
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["产品类别"]=="有源")&(OO00000O0OOO0O00O ["证号计数"]>=3 ),"评分说明"]=OO00000O0OOO0O00O ["评分说明"]+"型号集中度评分"+(round (O00OO0OO0OOO00OO0 *OO00000O0OOO0O00O ["型号计数"]/OO00000O0OOO0O00O ["证号计数"],2 )).astype (str )+";"#line:2478
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["产品类别"]!="有源")&(OO00000O0OOO0O00O ["证号计数"]>=3 ),"风险评分-影响"]=OO00000O0OOO0O00O ["风险评分-影响"]+O00OO0OO0OOO00OO0 *OO00000O0OOO0O00O ["批号计数"]/OO00000O0OOO0O00O ["证号计数"]#line:2479
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["产品类别"]!="有源")&(OO00000O0OOO0O00O ["证号计数"]>=3 ),"评分说明"]=OO00000O0OOO0O00O ["评分说明"]+"批号集中度评分"+(round (O00OO0OO0OOO00OO0 *OO00000O0OOO0O00O ["批号计数"]/OO00000O0OOO0O00O ["证号计数"],2 )).astype (str )+";"#line:2480
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["高度关注关键字"]>=1 ),"风险评分-影响"]=OO00000O0OOO0O00O ["风险评分-影响"]+OO0OO0OOO00OO0O0O #line:2483
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["高度关注关键字"]>=1 ),"评分说明"]=OO00000O0OOO0O00O ["评分说明"]+"●含有高度关注关键字评分"+str (OO0OO0OOO00OO0O0O )+"；"#line:2484
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["二级敏感词"]>=1 ),"风险评分-影响"]=OO00000O0OOO0O00O ["风险评分-影响"]+OO0OO0O00O0O000O0 #line:2487
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["二级敏感词"]>=1 ),"评分说明"]=OO00000O0OOO0O00O ["评分说明"]+"含有二级敏感词评分"+str (OO0OO0O00O0O000O0 )+"；"#line:2488
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["减分项"]>=1 ),"风险评分-影响"]=OO00000O0OOO0O00O ["风险评分-影响"]+O0OO0O000O0O00OO0 #line:2491
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["减分项"]>=1 ),"评分说明"]=OO00000O0OOO0O00O ["评分说明"]+"减分项评分"+str (O0OO0O000O0O00OO0 )+"；"#line:2492
		O0OOOO0OO0O0O0OO0 =Countall (OO00O0O0O0OOO000O ).df_findrisk ("事件发生月份")#line:2495
		O0OOOO0OO0O0O0OO0 =O0OOOO0OO0O0O0OO0 .drop_duplicates ("注册证编号/曾用注册证编号")#line:2496
		O0OOOO0OO0O0O0OO0 =O0OOOO0OO0O0O0OO0 [["注册证编号/曾用注册证编号","均值","标准差","CI上限"]]#line:2497
		OO00000O0OOO0O00O =pd .merge (OO00000O0OOO0O00O ,O0OOOO0OO0O0O0OO0 ,on =["注册证编号/曾用注册证编号"],how ="left")#line:2498
		OO00000O0OOO0O00O ["风险评分-月份"]=1 #line:2500
		OO00000O0OOO0O00O ["mfc"]=""#line:2501
		OO00000O0OOO0O00O .loc [((OO00000O0OOO0O00O ["证号计数"]>OO00000O0OOO0O00O ["均值"])&(OO00000O0OOO0O00O ["标准差"].astype (str )=="nan")),"风险评分-月份"]=OO00000O0OOO0O00O ["风险评分-月份"]+1 #line:2502
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["证号计数"]>OO00000O0OOO0O00O ["均值"]),"mfc"]="月份计数超过历史均值"+OO00000O0OOO0O00O ["均值"].astype (str )+"；"#line:2503
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["证号计数"]>=(OO00000O0OOO0O00O ["均值"]+OO00000O0OOO0O00O ["标准差"]))&(OO00000O0OOO0O00O ["证号计数"]>=3 ),"风险评分-月份"]=OO00000O0OOO0O00O ["风险评分-月份"]+1 #line:2505
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["证号计数"]>=(OO00000O0OOO0O00O ["均值"]+OO00000O0OOO0O00O ["标准差"]))&(OO00000O0OOO0O00O ["证号计数"]>=3 ),"mfc"]="月份计数超过3例超过历史均值一个标准差("+OO00000O0OOO0O00O ["标准差"].astype (str )+")；"#line:2506
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["证号计数"]>=OO00000O0OOO0O00O ["CI上限"])&(OO00000O0OOO0O00O ["证号计数"]>=3 ),"风险评分-月份"]=OO00000O0OOO0O00O ["风险评分-月份"]+2 #line:2508
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["证号计数"]>=OO00000O0OOO0O00O ["CI上限"])&(OO00000O0OOO0O00O ["证号计数"]>=3 ),"mfc"]="月份计数超过3例且超过历史95%CI上限("+OO00000O0OOO0O00O ["CI上限"].astype (str )+")；"#line:2509
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["证号计数"]>=OO00000O0OOO0O00O ["CI上限"])&(OO00000O0OOO0O00O ["证号计数"]>=5 ),"风险评分-月份"]=OO00000O0OOO0O00O ["风险评分-月份"]+1 #line:2511
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["证号计数"]>=OO00000O0OOO0O00O ["CI上限"])&(OO00000O0OOO0O00O ["证号计数"]>=5 ),"mfc"]="月份计数超过5例且超过历史95%CI上限("+OO00000O0OOO0O00O ["CI上限"].astype (str )+")；"#line:2512
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["证号计数"]>=OO00000O0OOO0O00O ["CI上限"])&(OO00000O0OOO0O00O ["证号计数"]>=7 ),"风险评分-月份"]=OO00000O0OOO0O00O ["风险评分-月份"]+1 #line:2514
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["证号计数"]>=OO00000O0OOO0O00O ["CI上限"])&(OO00000O0OOO0O00O ["证号计数"]>=7 ),"mfc"]="月份计数超过7例且超过历史95%CI上限("+OO00000O0OOO0O00O ["CI上限"].astype (str )+")；"#line:2515
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["证号计数"]>=OO00000O0OOO0O00O ["CI上限"])&(OO00000O0OOO0O00O ["证号计数"]>=9 ),"风险评分-月份"]=OO00000O0OOO0O00O ["风险评分-月份"]+1 #line:2517
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["证号计数"]>=OO00000O0OOO0O00O ["CI上限"])&(OO00000O0OOO0O00O ["证号计数"]>=9 ),"mfc"]="月份计数超过9例且超过历史95%CI上限("+OO00000O0OOO0O00O ["CI上限"].astype (str )+")；"#line:2518
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["证号计数"]>=3 )&(OO00000O0OOO0O00O ["标准差"].astype (str )=="nan"),"风险评分-月份"]=3 #line:2522
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["证号计数"]>=3 )&(OO00000O0OOO0O00O ["标准差"].astype (str )=="nan"),"mfc"]="无历史数据但数量超过3例；"#line:2523
		OO00000O0OOO0O00O ["评分说明"]=OO00000O0OOO0O00O ["评分说明"]+"●●证号数量："+OO00000O0OOO0O00O ["证号计数"].astype (str )+";"+OO00000O0OOO0O00O ["mfc"]#line:2526
		del OO00000O0OOO0O00O ["mfc"]#line:2527
		OO00000O0OOO0O00O =OO00000O0OOO0O00O .rename (columns ={"均值":"月份均值","标准差":"月份标准差","CI上限":"月份CI上限"})#line:2528
		O0OOOO0OO0O0O0OO0 =Countall (OO00O0O0O0OOO000O ).df_findrisk ("产品批号")#line:2532
		O0OOOO0OO0O0O0OO0 =O0OOOO0OO0O0O0OO0 .drop_duplicates ("注册证编号/曾用注册证编号")#line:2533
		O0OOOO0OO0O0O0OO0 =O0OOOO0OO0O0O0OO0 [["注册证编号/曾用注册证编号","均值","标准差","CI上限"]]#line:2534
		OO00000O0OOO0O00O =pd .merge (OO00000O0OOO0O00O ,O0OOOO0OO0O0O0OO0 ,on =["注册证编号/曾用注册证编号"],how ="left")#line:2535
		OO00000O0OOO0O00O ["风险评分-批号"]=1 #line:2537
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["产品类别"]!="有源"),"评分说明"]=OO00000O0OOO0O00O ["评分说明"]+"●●高峰批号数量："+OO00000O0OOO0O00O ["批号计数"].astype (str )+";"#line:2538
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["批号计数"]>OO00000O0OOO0O00O ["均值"]),"风险评分-批号"]=OO00000O0OOO0O00O ["风险评分-批号"]+1 #line:2540
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["批号计数"]>OO00000O0OOO0O00O ["均值"]),"评分说明"]=OO00000O0OOO0O00O ["评分说明"]+"高峰批号计数超过历史均值"+OO00000O0OOO0O00O ["均值"].astype (str )+"；"#line:2541
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["批号计数"]>(OO00000O0OOO0O00O ["均值"]+OO00000O0OOO0O00O ["标准差"]))&(OO00000O0OOO0O00O ["批号计数"]>=3 ),"风险评分-批号"]=OO00000O0OOO0O00O ["风险评分-批号"]+1 #line:2542
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["批号计数"]>(OO00000O0OOO0O00O ["均值"]+OO00000O0OOO0O00O ["标准差"]))&(OO00000O0OOO0O00O ["批号计数"]>=3 ),"评分说明"]=OO00000O0OOO0O00O ["评分说明"]+"高峰批号计数超过3例超过历史均值一个标准差("+OO00000O0OOO0O00O ["标准差"].astype (str )+")；"#line:2543
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["批号计数"]>OO00000O0OOO0O00O ["CI上限"])&(OO00000O0OOO0O00O ["批号计数"]>=3 ),"风险评分-批号"]=OO00000O0OOO0O00O ["风险评分-批号"]+1 #line:2544
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["批号计数"]>OO00000O0OOO0O00O ["CI上限"])&(OO00000O0OOO0O00O ["批号计数"]>=3 ),"评分说明"]=OO00000O0OOO0O00O ["评分说明"]+"高峰批号计数超过3例且超过历史95%CI上限("+OO00000O0OOO0O00O ["CI上限"].astype (str )+")；"#line:2545
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["批号计数"]>=3 )&(OO00000O0OOO0O00O ["标准差"].astype (str )=="nan"),"风险评分-月份"]=3 #line:2547
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["批号计数"]>=3 )&(OO00000O0OOO0O00O ["标准差"].astype (str )=="nan"),"评分说明"]=OO00000O0OOO0O00O ["评分说明"]+"无历史数据但数量超过3例；"#line:2548
		OO00000O0OOO0O00O =OO00000O0OOO0O00O .rename (columns ={"均值":"高峰批号均值","标准差":"高峰批号标准差","CI上限":"高峰批号CI上限"})#line:2549
		OO00000O0OOO0O00O ["风险评分-影响"]=round (OO00000O0OOO0O00O ["风险评分-影响"],2 )#line:2552
		OO00000O0OOO0O00O ["风险评分-月份"]=round (OO00000O0OOO0O00O ["风险评分-月份"],2 )#line:2553
		OO00000O0OOO0O00O ["风险评分-批号"]=round (OO00000O0OOO0O00O ["风险评分-批号"],2 )#line:2554
		OO00000O0OOO0O00O ["总体评分"]=OO00000O0OOO0O00O ["风险评分-影响"].copy ()#line:2556
		OO00000O0OOO0O00O ["关注建议"]=""#line:2557
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["风险评分-影响"]>=3 ),"关注建议"]=OO00000O0OOO0O00O ["关注建议"]+"●建议关注(影响范围)；"#line:2558
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["风险评分-月份"]>=3 ),"关注建议"]=OO00000O0OOO0O00O ["关注建议"]+"●建议关注(当月数量异常)；"#line:2559
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["风险评分-批号"]>=3 ),"关注建议"]=OO00000O0OOO0O00O ["关注建议"]+"●建议关注(高峰批号数量异常)。"#line:2560
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["风险评分-月份"]>=OO00000O0OOO0O00O ["风险评分-批号"]),"总体评分"]=OO00000O0OOO0O00O ["风险评分-影响"]*OO00000O0OOO0O00O ["风险评分-月份"]#line:2564
		OO00000O0OOO0O00O .loc [(OO00000O0OOO0O00O ["风险评分-月份"]<OO00000O0OOO0O00O ["风险评分-批号"]),"总体评分"]=OO00000O0OOO0O00O ["风险评分-影响"]*OO00000O0OOO0O00O ["风险评分-批号"]#line:2565
		OO00000O0OOO0O00O ["总体评分"]=round (OO00000O0OOO0O00O ["总体评分"],2 )#line:2567
		OO00000O0OOO0O00O ["评分说明"]=OO00000O0OOO0O00O ["关注建议"]+OO00000O0OOO0O00O ["评分说明"]#line:2568
		OO00000O0OOO0O00O =OO00000O0OOO0O00O .sort_values (by =["总体评分","风险评分-影响"],ascending =[False ,False ],na_position ="last").reset_index (drop =True )#line:2569
		OO00000O0OOO0O00O ["主要故障分类"]=""#line:2572
		for OO00OOOOOO00O00O0 ,OO0OOO000OOO0000O in OO00000O0OOO0O00O .iterrows ():#line:2573
			O0O00OOO0OOOO0000 =O0O0O000000000OOO [(O0O0O000000000OOO ["注册证编号/曾用注册证编号"]==OO0OOO000OOO0000O ["注册证编号/曾用注册证编号"])].copy ()#line:2574
			if OO0OOO000OOO0000O ["总体评分"]>=float (OOOO0000O0O00OOOO ):#line:2575
				if OO0OOO000OOO0000O ["规整后品类"]!="N":#line:2576
					O0O00OO0OOO0O0O00 =Countall (O0O00OOO0OOOO0000 ).df_psur ("特定品种",OO0OOO000OOO0000O ["规整后品类"])#line:2577
				elif OO0OOO000OOO0000O ["产品类别"]=="无源":#line:2578
					O0O00OO0OOO0O0O00 =Countall (O0O00OOO0OOOO0000 ).df_psur ("通用无源")#line:2579
				elif OO0OOO000OOO0000O ["产品类别"]=="有源":#line:2580
					O0O00OO0OOO0O0O00 =Countall (O0O00OOO0OOOO0000 ).df_psur ("通用有源")#line:2581
				elif OO0OOO000OOO0000O ["产品类别"]=="体外诊断试剂":#line:2582
					O0O00OO0OOO0O0O00 =Countall (O0O00OOO0OOOO0000 ).df_psur ("体外诊断试剂")#line:2583
				O0O000OOO00OO0OO0 =O0O00OO0OOO0O0O00 [["事件分类","总数量"]].copy ()#line:2585
				OO0OO000O0OO0OOOO =""#line:2586
				for OOOOOOOOOOO0O000O ,OO0O0000O0O0O0OO0 in O0O000OOO00OO0OO0 .iterrows ():#line:2587
					OO0OO000O0OO0OOOO =OO0OO000O0OO0OOOO +str (OO0O0000O0O0O0OO0 ["事件分类"])+":"+str (OO0O0000O0O0O0OO0 ["总数量"])+";"#line:2588
				OO00000O0OOO0O00O .loc [OO00OOOOOO00O00O0 ,"主要故障分类"]=OO0OO000O0OO0OOOO #line:2589
			else :#line:2590
				break #line:2591
		OO00000O0OOO0O00O =OO00000O0OOO0O00O [["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号","证号计数","严重伤害数","死亡数量","总体评分","风险评分-影响","风险评分-月份","风险评分-批号","主要故障分类","评分说明","单位个数","单位列表","批号个数","批号列表","型号个数","型号列表","规格个数","规格列表","待评价数","严重伤害待评价数","高度关注关键字","二级敏感词","月份均值","月份标准差","月份CI上限","高峰批号均值","高峰批号标准差","高峰批号CI上限","型号","型号计数","产品批号","批号计数"]]#line:2595
		OO00000O0OOO0O00O ["报表类型"]="dfx_zhenghao"#line:2596
		TABLE_tree_Level_2 (OO00000O0OOO0O00O ,1 ,O0O0O000000000OOO ,OO00O0O0O0OOO000O )#line:2597
		pass #line:2598
	O0OOO0OO0OOO0000O =Toplevel ()#line:2601
	O0OOO0OO0OOO0000O .title ('风险预警')#line:2602
	OO0000O0OO0O00OOO =O0OOO0OO0OOO0000O .winfo_screenwidth ()#line:2603
	OOO0O0OOOO00OO00O =O0OOO0OO0OOO0000O .winfo_screenheight ()#line:2605
	OOO000OO00OOO000O =350 #line:2607
	O0OOO0O000000O0O0 =35 #line:2608
	OO000O00000000000 =(OO0000O0OO0O00OOO -OOO000OO00OOO000O )/2 #line:2610
	OO0O00O0O0OOOOO00 =(OOO0O0OOOO00OO00O -O0OOO0O000000O0O0 )/2 #line:2611
	O0OOO0OO0OOO0000O .geometry ("%dx%d+%d+%d"%(OOO000OO00OOO000O ,O0OOO0O000000O0O0 ,OO000O00000000000 ,OO0O00O0O0OOOOO00 ))#line:2612
	O00O000O00O0OO00O =Label (O0OOO0OO0OOO0000O ,text ="预警日期：")#line:2614
	O00O000O00O0OO00O .grid (row =1 ,column =0 ,sticky ="w")#line:2615
	OOO00O000O0O00000 =Entry (O0OOO0OO0OOO0000O ,width =30 )#line:2616
	OOO00O000O0O00000 .insert (0 ,datetime .date .today ())#line:2617
	OOO00O000O0O00000 .grid (row =1 ,column =1 ,sticky ="w")#line:2618
	O0OO0OOO00OOOOOO0 =Button (O0OOO0OO0OOO0000O ,text ="确定",width =10 ,command =lambda :TABLE_tree_Level_2 (OOOOOO000000O0O0O (OOO00O000O0O00000 .get (),OOOO00O0O0O0O000O ),1 ,OOOO00O0O0O0O000O ))#line:2622
	O0OO0OOO00OOOOOO0 .grid (row =1 ,column =3 ,sticky ="w")#line:2623
	pass #line:2625
def TOOLS_count_elements (OOOOOOO00O0OO000O ,OOO0O0OOO0O0OOOO0 ,O0OO00O0000000O00 ):#line:2627
    ""#line:2628
    OO000OOOOO00O0O00 =pd .DataFrame (columns =[O0OO00O0000000O00 ,'count'])#line:2630
    OO0O00O0000OOO000 =[]#line:2631
    O0O0O0O00O0OOOO00 =[]#line:2632
    for O00OOOO00O0OO00O0 in TOOLS_get_list (OOO0O0OOO0O0OOOO0 ):#line:2635
        O0OOO0OO00O0O00OO =OOOOOOO00O0OO000O [OOOOOOO00O0OO000O [O0OO00O0000000O00 ].str .contains (O00OOOO00O0OO00O0 )].shape [0 ]#line:2637
        if O0OOO0OO00O0O00OO >0 :#line:2640
            OO0O00O0000OOO000 .append (O0OOO0OO00O0O00OO )#line:2641
            O0O0O0O00O0OOOO00 .append (O00OOOO00O0OO00O0 )#line:2642
    OO0OOOO0O0OO00O0O =pd .DataFrame ({"index":O0O0O0O00O0OOOO00 ,'计数':OO0O00O0000OOO000 })#line:2643
    OO0OOOO0O0OO00O0O ["构成比(%)"]=round (100 *OO0OOOO0O0OO00O0O ["计数"]/OO0OOOO0O0OO00O0O ["计数"].sum (),2 )#line:2644
    OO0OOOO0O0OO00O0O ["报表类型"]="dfx_deepvie2"+"_"+str ([O0OO00O0000000O00 ])#line:2645
    return OO0OOOO0O0OO00O0O #line:2647
def TOOLS_autocount (O0O000O000O000OOO ,OO00OO0OO0000OO0O ):#line:2649
    ""#line:2650
    O0O000OOOOO00000O =pd .read_excel (peizhidir +"0（范例）上报单位.xls",sheet_name ="监测机构",header =0 ,index_col =0 ).reset_index ()#line:2653
    O0O00OOO00000OO00 =pd .read_excel (peizhidir +"0（范例）上报单位.xls",sheet_name ="报告单位",header =0 ,index_col =0 ).reset_index ()#line:2656
    O00OO00OO00O0OO0O =O0O00OOO00000OO00 [(O0O00OOO00000OO00 ["是否属于二级以上医疗机构"]=="是")]#line:2657
    if OO00OO0OO0000OO0O =="药品":#line:2660
        O0O000O000O000OOO =O0O000O000O000OOO .reset_index (drop =True )#line:2661
        if "再次使用可疑药是否出现同样反应"not in O0O000O000O000OOO .columns :#line:2662
            showinfo (title ="错误信息",message ="导入的疑似不是药品报告表。")#line:2663
            return 0 #line:2664
        O0OO0O000OO00O00O =Countall (O0O000O000O000OOO ).df_org ("监测机构")#line:2666
        O0OO0O000OO00O00O =pd .merge (O0OO0O000OO00O00O ,O0O000OOOOO00000O ,on ="监测机构",how ="left")#line:2667
        O0OO0O000OO00O00O =O0OO0O000OO00O00O [["监测机构序号","监测机构","药品数量指标","报告数量","审核通过数","新严比","严重比","超时比"]].sort_values (by =["监测机构序号"],ascending =True ,na_position ="last").fillna (0 )#line:2668
        OO0OOO00OO0O0O0OO =["药品数量指标","审核通过数","报告数量"]#line:2669
        O0OO0O000OO00O00O [OO0OOO00OO0O0O0OO ]=O0OO0O000OO00O00O [OO0OOO00OO0O0O0OO ].apply (lambda O00OOOOO0OOOOO0O0 :O00OOOOO0OOOOO0O0 .astype (int ))#line:2670
        O00O0OO0O00O0O0O0 =Countall (O0O000O000O000OOO ).df_user ()#line:2672
        O00O0OO0O00O0O0O0 =pd .merge (O00O0OO0O00O0O0O0 ,O0O00OOO00000OO00 ,on =["监测机构","单位名称"],how ="left")#line:2673
        O00O0OO0O00O0O0O0 =pd .merge (O00O0OO0O00O0O0O0 ,O0O000OOOOO00000O [["监测机构序号","监测机构"]],on ="监测机构",how ="left")#line:2674
        O00O0OO0O00O0O0O0 =O00O0OO0O00O0O0O0 [["监测机构序号","监测机构","单位名称","药品数量指标","报告数量","审核通过数","新严比","严重比","超时比"]].sort_values (by =["监测机构序号","报告数量"],ascending =[True ,False ],na_position ="last").fillna (0 )#line:2676
        OO0OOO00OO0O0O0OO =["药品数量指标","审核通过数","报告数量"]#line:2677
        O00O0OO0O00O0O0O0 [OO0OOO00OO0O0O0OO ]=O00O0OO0O00O0O0O0 [OO0OOO00OO0O0O0OO ].apply (lambda O0O00000OO0O0OOO0 :O0O00000OO0O0OOO0 .astype (int ))#line:2678
        OO0O0O00OOOO0O00O =pd .merge (O00OO00OO00O0OO0O ,O00O0OO0O00O0O0O0 ,on =["监测机构","单位名称"],how ="left").sort_values (by =["监测机构"],ascending =True ,na_position ="last").fillna (0 )#line:2680
        OO0O0O00OOOO0O00O =OO0O0O00OOOO0O00O [(OO0O0O00OOOO0O00O ["审核通过数"]<1 )]#line:2681
        OO0O0O00OOOO0O00O =OO0O0O00OOOO0O00O [["监测机构","单位名称","报告数量","审核通过数","严重比","超时比"]]#line:2682
    if OO00OO0OO0000OO0O =="器械":#line:2684
        O0O000O000O000OOO =O0O000O000O000OOO .reset_index (drop =True )#line:2685
        if "产品编号"not in O0O000O000O000OOO .columns :#line:2686
            showinfo (title ="错误信息",message ="导入的疑似不是器械报告表。")#line:2687
            return 0 #line:2688
        O0OO0O000OO00O00O =Countall (O0O000O000O000OOO ).df_org ("监测机构")#line:2690
        O0OO0O000OO00O00O =pd .merge (O0OO0O000OO00O00O ,O0O000OOOOO00000O ,on ="监测机构",how ="left")#line:2691
        O0OO0O000OO00O00O =O0OO0O000OO00O00O [["监测机构序号","监测机构","器械数量指标","报告数量","审核通过数","严重比","超时比"]].sort_values (by =["监测机构序号"],ascending =True ,na_position ="last").fillna (0 )#line:2692
        OO0OOO00OO0O0O0OO =["器械数量指标","审核通过数","报告数量"]#line:2693
        O0OO0O000OO00O00O [OO0OOO00OO0O0O0OO ]=O0OO0O000OO00O00O [OO0OOO00OO0O0O0OO ].apply (lambda OO00OOO0OO00000O0 :OO00OOO0OO00000O0 .astype (int ))#line:2694
        O00O0OO0O00O0O0O0 =Countall (O0O000O000O000OOO ).df_user ()#line:2696
        O00O0OO0O00O0O0O0 =pd .merge (O00O0OO0O00O0O0O0 ,O0O00OOO00000OO00 ,on =["监测机构","单位名称"],how ="left")#line:2697
        O00O0OO0O00O0O0O0 =pd .merge (O00O0OO0O00O0O0O0 ,O0O000OOOOO00000O [["监测机构序号","监测机构"]],on ="监测机构",how ="left")#line:2698
        O00O0OO0O00O0O0O0 =O00O0OO0O00O0O0O0 [["监测机构序号","监测机构","单位名称","器械数量指标","报告数量","审核通过数","严重比","超时比"]].sort_values (by =["监测机构序号","报告数量"],ascending =[True ,False ],na_position ="last").fillna (0 )#line:2700
        OO0OOO00OO0O0O0OO =["器械数量指标","审核通过数","报告数量"]#line:2701
        O00O0OO0O00O0O0O0 [OO0OOO00OO0O0O0OO ]=O00O0OO0O00O0O0O0 [OO0OOO00OO0O0O0OO ].apply (lambda O0O0OOO0OO00O0OO0 :O0O0OOO0OO00O0OO0 .astype (int ))#line:2703
        OO0O0O00OOOO0O00O =pd .merge (O00OO00OO00O0OO0O ,O00O0OO0O00O0O0O0 ,on =["监测机构","单位名称"],how ="left").sort_values (by =["监测机构"],ascending =True ,na_position ="last").fillna (0 )#line:2705
        OO0O0O00OOOO0O00O =OO0O0O00OOOO0O00O [(OO0O0O00OOOO0O00O ["审核通过数"]<1 )]#line:2706
        OO0O0O00OOOO0O00O =OO0O0O00OOOO0O00O [["监测机构","单位名称","报告数量","审核通过数","严重比","超时比"]]#line:2707
    if OO00OO0OO0000OO0O =="化妆品":#line:2710
        O0O000O000O000OOO =O0O000O000O000OOO .reset_index (drop =True )#line:2711
        if "初步判断"not in O0O000O000O000OOO .columns :#line:2712
            showinfo (title ="错误信息",message ="导入的疑似不是化妆品报告表。")#line:2713
            return 0 #line:2714
        O0OO0O000OO00O00O =Countall (O0O000O000O000OOO ).df_org ("监测机构")#line:2716
        O0OO0O000OO00O00O =pd .merge (O0OO0O000OO00O00O ,O0O000OOOOO00000O ,on ="监测机构",how ="left")#line:2717
        O0OO0O000OO00O00O =O0OO0O000OO00O00O [["监测机构序号","监测机构","化妆品数量指标","报告数量","审核通过数"]].sort_values (by =["监测机构序号"],ascending =True ,na_position ="last").fillna (0 )#line:2718
        OO0OOO00OO0O0O0OO =["化妆品数量指标","审核通过数","报告数量"]#line:2719
        O0OO0O000OO00O00O [OO0OOO00OO0O0O0OO ]=O0OO0O000OO00O00O [OO0OOO00OO0O0O0OO ].apply (lambda O0OO0O0O0OOOO0000 :O0OO0O0O0OOOO0000 .astype (int ))#line:2720
        O00O0OO0O00O0O0O0 =Countall (O0O000O000O000OOO ).df_user ()#line:2722
        O00O0OO0O00O0O0O0 =pd .merge (O00O0OO0O00O0O0O0 ,O0O00OOO00000OO00 ,on =["监测机构","单位名称"],how ="left")#line:2723
        O00O0OO0O00O0O0O0 =pd .merge (O00O0OO0O00O0O0O0 ,O0O000OOOOO00000O [["监测机构序号","监测机构"]],on ="监测机构",how ="left")#line:2724
        O00O0OO0O00O0O0O0 =O00O0OO0O00O0O0O0 [["监测机构序号","监测机构","单位名称","化妆品数量指标","报告数量","审核通过数"]].sort_values (by =["监测机构序号","报告数量"],ascending =[True ,False ],na_position ="last").fillna (0 )#line:2725
        OO0OOO00OO0O0O0OO =["化妆品数量指标","审核通过数","报告数量"]#line:2726
        O00O0OO0O00O0O0O0 [OO0OOO00OO0O0O0OO ]=O00O0OO0O00O0O0O0 [OO0OOO00OO0O0O0OO ].apply (lambda OOOOO00O0O0000O0O :OOOOO00O0O0000O0O .astype (int ))#line:2727
        OO0O0O00OOOO0O00O =pd .merge (O00OO00OO00O0OO0O ,O00O0OO0O00O0O0O0 ,on =["监测机构","单位名称"],how ="left").sort_values (by =["监测机构"],ascending =True ,na_position ="last").fillna (0 )#line:2729
        OO0O0O00OOOO0O00O =OO0O0O00OOOO0O00O [(OO0O0O00OOOO0O00O ["审核通过数"]<1 )]#line:2730
        OO0O0O00OOOO0O00O =OO0O0O00OOOO0O00O [["监测机构","单位名称","报告数量","审核通过数"]]#line:2731
    OO00O0OO0O0OO0O00 =filedialog .asksaveasfilename (title =u"保存文件",initialfile =OO00OO0OO0000OO0O ,defaultextension ="xls",filetypes =[("Excel 97-2003 工作簿","*.xls")],)#line:2738
    OO0OO0OO0OO0O0OO0 =pd .ExcelWriter (OO00O0OO0O0OO0O00 ,engine ="xlsxwriter")#line:2739
    O0OO0O000OO00O00O .to_excel (OO0OO0OO0OO0O0OO0 ,sheet_name ="监测机构")#line:2740
    O00O0OO0O00O0O0O0 .to_excel (OO0OO0OO0OO0O0OO0 ,sheet_name ="上报单位")#line:2741
    OO0O0O00OOOO0O00O .to_excel (OO0OO0OO0OO0O0OO0 ,sheet_name ="未上报的二级以上医疗机构")#line:2742
    OO0OO0OO0OO0O0OO0 .close ()#line:2743
    showinfo (title ="提示",message ="文件写入成功。")#line:2744
def TOOLS_web_view (OO0O0OO0OOO0OOOO0 ):#line:2746
    ""#line:2747
    import pybi as pbi #line:2748
    OO0000OOO000OO000 =pd .ExcelWriter ("temp_webview.xls")#line:2749
    OO0O0OO0OOO0OOOO0 .to_excel (OO0000OOO000OO000 ,sheet_name ="temp_webview")#line:2750
    OO0000OOO000OO000 .close ()#line:2751
    OO0O0OO0OOO0OOOO0 =pd .read_excel ("temp_webview.xls",header =0 ,sheet_name =0 ).reset_index (drop =True )#line:2752
    OO000O0O00OOO0OO0 =pbi .set_source (OO0O0OO0OOO0OOOO0 )#line:2753
    with pbi .flowBox ():#line:2754
        for O00OOOOOOOO00OOO0 in OO0O0OO0OOO0OOOO0 .columns :#line:2755
            pbi .add_slicer (OO000O0O00OOO0OO0 [O00OOOOOOOO00OOO0 ])#line:2756
    pbi .add_table (OO000O0O00OOO0OO0 )#line:2757
    OO0O0OO0OO00OOOO0 ="temp_webview.html"#line:2758
    pbi .to_html (OO0O0OO0OO00OOOO0 )#line:2759
    webbrowser .open_new_tab (OO0O0OO0OO00OOOO0 )#line:2760
def TOOLS_Autotable_0 (OOOOO00OO0O0O00OO ,OOO0OOOO0O0O0O00O ,*O0OO00OO0O00000OO ):#line:2765
    ""#line:2766
    OO000O00OOO0OOOO0 =[O0OO00OO0O00000OO [0 ],O0OO00OO0O00000OO [1 ],O0OO00OO0O00000OO [2 ]]#line:2768
    OOOOO0O0OOO0000OO =list (set ([OOO0O0O00O0O00O0O for OOO0O0O00O0O00O0O in OO000O00OOO0OOOO0 if OOO0O0O00O0O00O0O !='']))#line:2770
    OOOOO0O0OOO0000OO .sort (key =OO000O00OOO0OOOO0 .index )#line:2771
    if len (OOOOO0O0OOO0000OO )==0 :#line:2772
        showinfo (title ="提示信息",message ="分组项请选择至少一列。")#line:2773
        return 0 #line:2774
    OOO0OOO000OO0OO0O =[O0OO00OO0O00000OO [3 ],O0OO00OO0O00000OO [4 ]]#line:2775
    if (O0OO00OO0O00000OO [3 ]==""or O0OO00OO0O00000OO [4 ]=="")and OOO0OOOO0O0O0O00O in ["数据透视","分组统计"]:#line:2776
        if "报告编码"in OOOOO00OO0O0O00OO .columns :#line:2777
            OOO0OOO000OO0OO0O [0 ]="报告编码"#line:2778
            OOO0OOO000OO0OO0O [1 ]="nunique"#line:2779
            text .insert (END ,"值项未配置,将使用报告编码进行唯一值计数。")#line:2780
        else :#line:2781
            showinfo (title ="提示信息",message ="值项未配置。")#line:2782
            return 0 #line:2783
    if O0OO00OO0O00000OO [4 ]=="计数":#line:2785
        OOO0OOO000OO0OO0O [1 ]="count"#line:2786
    elif O0OO00OO0O00000OO [4 ]=="求和":#line:2787
        OOO0OOO000OO0OO0O [1 ]="sum"#line:2788
    elif O0OO00OO0O00000OO [4 ]=="唯一值计数":#line:2789
        OOO0OOO000OO0OO0O [1 ]="nunique"#line:2790
    if OOO0OOOO0O0O0O00O =="分组统计":#line:2793
        TABLE_tree_Level_2 (TOOLS_deep_view (OOOOO00OO0O0O00OO ,OOOOO0O0OOO0000OO ,OOO0OOO000OO0OO0O ,0 ),1 ,OOOOO00OO0O0O00OO )#line:2794
    if OOO0OOOO0O0O0O00O =="数据透视":#line:2796
        TABLE_tree_Level_2 (TOOLS_deep_view (OOOOO00OO0O0O00OO ,OOOOO0O0OOO0000OO ,OOO0OOO000OO0OO0O ,1 ),1 ,OOOOO00OO0O0O00OO )#line:2797
    if OOO0OOOO0O0O0O00O =="描述性统计":#line:2799
        TABLE_tree_Level_2 (OOOOO00OO0O0O00OO [OOOOO0O0OOO0000OO ].describe ().reset_index (),1 ,OOOOO00OO0O0O00OO )#line:2800
    if OOO0OOOO0O0O0O00O =="单列多项拆分统计(统计列)":#line:2803
        TABLE_tree_Level_2 (STAT_pinzhong (OOOOO00OO0O0O00OO ,O0OO00OO0O00000OO [0 ],0 ))#line:2804
    if OOO0OOOO0O0O0O00O =="单列多项拆分统计(透视列-统计列)":#line:2805
        TABLE_tree_Level_2 (Countall (OOOOO00OO0O0O00OO ).df_psur2 (O0OO00OO0O00000OO [0 ],O0OO00OO0O00000OO [1 ]),1 ,0 )#line:2806
    if OOO0OOOO0O0O0O00O =="单列多项拆分统计(透视列-统计列-字典)":#line:2808
        OO0000O0O0OO00000 =OOOOO00OO0O0O00OO .copy ()#line:2811
        OO0000O0O0OO00000 ["c"]="c"#line:2812
        OO00O0O0OOO0OOO0O =OO0000O0O0OO00000 .groupby ([O0OO00OO0O00000OO [0 ]]).agg (计数 =("c","count")).reset_index ()#line:2813
        OOO00000O0OO0O0O0 =OO00O0O0OOO0OOO0O .copy ()#line:2814
        OOO00000O0OO0O0O0 [O0OO00OO0O00000OO [0 ]]=OOO00000O0OO0O0O0 [O0OO00OO0O00000OO [0 ]].str .replace ("*","",regex =False )#line:2815
        OOO00000O0OO0O0O0 ["所有项目"]=""#line:2816
        O0OOO0OOO0O00OO0O =1 #line:2817
        OOOO0000OO0OOO0O0 =int (len (OOO00000O0OO0O0O0 ))#line:2818
        for OO000000OOO00O000 ,OO00OOO00O0O00OOO in OOO00000O0OO0O0O0 .iterrows ():#line:2819
            O0O00OO0O00OOO0OO =OO0000O0O0OO00000 [(OO0000O0O0OO00000 [O0OO00OO0O00000OO [0 ]]==OO00OOO00O0O00OOO [O0OO00OO0O00000OO [0 ]])]#line:2821
            O0O0OOO0OOO0O0O00 =str (Counter (TOOLS_get_list0 ("use("+str (O0OO00OO0O00000OO [1 ])+").file",O0O00OO0O00OOO0OO ,1000 ))).replace ("Counter({","{")#line:2823
            O0O0OOO0OOO0O0O00 =O0O0OOO0OOO0O0O00 .replace ("})","}")#line:2824
            import ast #line:2825
            O000OO00O00OO0O0O =ast .literal_eval (O0O0OOO0OOO0O0O00 )#line:2826
            OOO0O00000OOOO00O =TOOLS_easyreadT (pd .DataFrame ([O000OO00O00OO0O0O ]))#line:2827
            OOO0O00000OOOO00O =OOO0O00000OOOO00O .rename (columns ={"逐条查看":"名称规整"})#line:2828
            PROGRAM_change_schedule (O0OOO0OOO0O00OO0O ,OOOO0000OO0OOO0O0 )#line:2830
            O0OOO0OOO0O00OO0O =O0OOO0OOO0O00OO0O +1 #line:2831
            for OO00OO000O0OO00OO ,OOO0OOOO0000O00OO in OOO0O00000OOOO00O .iterrows ():#line:2832
                    if "分隔符"not in OOO0OOOO0000O00OO ["条目"]:#line:2833
                        O0000000O00OOOO0O ="'"+str (OOO0OOOO0000O00OO ["条目"])+"':"+str (OOO0OOOO0000O00OO ["详细描述T"])+","#line:2834
                        OOO00000O0OO0O0O0 .loc [OO000000OOO00O000 ,"所有项目"]=OOO00000O0OO0O0O0 .loc [OO000000OOO00O000 ,"所有项目"]+O0000000O00OOOO0O #line:2835
        OOO00000O0OO0O0O0 ["所有项目"]="{"+OOO00000O0OO0O0O0 ["所有项目"]+"}"#line:2837
        OOO00000O0OO0O0O0 ["报表类型"]="dfx_chanpin"#line:2838
        TABLE_tree_Level_2 (OOO00000O0OO0O0O0 .sort_values (by ="计数",ascending =[False ],na_position ="last"),1 ,OO0000O0O0OO00000 )#line:2840
    if OOO0OOOO0O0O0O00O =="追加外部表格信息":#line:2842
        O0O0OOOO0OOO00OO0 =filedialog .askopenfilenames (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:2845
        O0OOO0OOO0O00OO0O =[pd .read_excel (O0O0O0O0O0O0O00O0 ,header =0 ,sheet_name =0 )for O0O0O0O0O0O0O00O0 in O0O0OOOO0OOO00OO0 ]#line:2846
        O0OOO0OOO00000O00 =pd .concat (O0OOO0OOO0O00OO0O ,ignore_index =True ).drop_duplicates (OOOOO0O0OOO0000OO )#line:2847
        OOO000OO0OO0OOO00 =pd .merge (OOOOO00OO0O0O00OO ,O0OOO0OOO00000O00 ,on =OOOOO0O0OOO0000OO ,how ="left")#line:2848
        TABLE_tree_Level_2 (OOO000OO0OO0OOO00 ,1 ,OOO000OO0OO0OOO00 )#line:2849
    if OOO0OOOO0O0O0O00O =="添加到外部表格":#line:2851
        O0O0OOOO0OOO00OO0 =filedialog .askopenfilenames (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:2854
        O0OOO0OOO0O00OO0O =[pd .read_excel (O00O00000O0OO000O ,header =0 ,sheet_name =0 )for O00O00000O0OO000O in O0O0OOOO0OOO00OO0 ]#line:2855
        O0OOO0OOO00000O00 =pd .concat (O0OOO0OOO0O00OO0O ,ignore_index =True ).drop_duplicates ()#line:2856
        OOO000OO0OO0OOO00 =pd .merge (O0OOO0OOO00000O00 ,OOOOO00OO0O0O00OO .drop_duplicates (OOOOO0O0OOO0000OO ),on =OOOOO0O0OOO0000OO ,how ="left")#line:2857
        TABLE_tree_Level_2 (OOO000OO0OO0OOO00 ,1 ,OOO000OO0OO0OOO00 )#line:2858
    if OOO0OOOO0O0O0O00O =="饼图(XY)":#line:2861
        DRAW_make_one (OOOOO00OO0O0O00OO ,"饼图",O0OO00OO0O00000OO [0 ],O0OO00OO0O00000OO [1 ],"饼图")#line:2862
    if OOO0OOOO0O0O0O00O =="柱状图(XY)":#line:2863
        DRAW_make_one (OOOOO00OO0O0O00OO ,"柱状图",O0OO00OO0O00000OO [0 ],O0OO00OO0O00000OO [1 ],"柱状图")#line:2864
    if OOO0OOOO0O0O0O00O =="折线图(XY)":#line:2865
        DRAW_make_one (OOOOO00OO0O0O00OO ,"折线图",O0OO00OO0O00000OO [0 ],O0OO00OO0O00000OO [1 ],"折线图")#line:2866
    if OOO0OOOO0O0O0O00O =="托帕斯图(XY)":#line:2867
        DRAW_make_one (OOOOO00OO0O0O00OO ,"托帕斯图",O0OO00OO0O00000OO [0 ],O0OO00OO0O00000OO [1 ],"托帕斯图")#line:2868
    if OOO0OOOO0O0O0O00O =="堆叠柱状图（X-YZ）":#line:2869
        DRAW_make_mutibar (OOOOO00OO0O0O00OO ,OO000O00OOO0OOOO0 [1 ],OO000O00OOO0OOOO0 [2 ],OO000O00OOO0OOOO0 [0 ],OO000O00OOO0OOOO0 [1 ],OO000O00OOO0OOOO0 [2 ],"堆叠柱状图")#line:2870
def STAT_countx (O0000O00OOOOO0OOO ):#line:2880
	""#line:2881
	return O0000O00OOOOO0OOO .value_counts ().to_dict ()#line:2882
def STAT_countpx (OOO0OOOOO00O00OO0 ,O0OO000OO0000O0OO ):#line:2884
	""#line:2885
	return len (OOO0OOOOO00O00OO0 [(OOO0OOOOO00O00OO0 ==O0OO000OO0000O0OO )])#line:2886
def STAT_countnpx (OOOOOOO0OOOOOOO0O ,O0O00OO0OOO0OO00O ):#line:2888
	""#line:2889
	return len (OOOOOOO0OOOOOOO0O [(OOOOOOO0OOOOOOO0O not in O0O00OO0OOO0OO00O )])#line:2890
def STAT_get_max (O00O0OO0OOOO0O0OO ):#line:2892
	""#line:2893
	return O00O0OO0OOOO0O0OO .value_counts ().max ()#line:2894
def STAT_get_mean (OOOOO0O0O00O0OO0O ):#line:2896
	""#line:2897
	return round (OOOOO0O0O00O0OO0O .value_counts ().mean (),2 )#line:2898
def STAT_get_std (OOOO00000O00000O0 ):#line:2900
	""#line:2901
	return round (OOOO00000O00000O0 .value_counts ().std (ddof =1 ),2 )#line:2902
def STAT_get_95ci (O0000O00OO0OO000O ):#line:2904
	""#line:2905
	OO0O0OO0OOOOO0OO0 =0.95 #line:2906
	OOOOO0000O00000O0 =O0000O00OO0OO000O .value_counts ().tolist ()#line:2907
	if len (OOOOO0000O00000O0 )<30 :#line:2908
		O0O0OOOOOOO0000O0 =st .t .interval (OO0O0OO0OOOOO0OO0 ,df =len (OOOOO0000O00000O0 )-1 ,loc =np .mean (OOOOO0000O00000O0 ),scale =st .sem (OOOOO0000O00000O0 ))#line:2909
	else :#line:2910
		O0O0OOOOOOO0000O0 =st .norm .interval (OO0O0OO0OOOOO0OO0 ,loc =np .mean (OOOOO0000O00000O0 ),scale =st .sem (OOOOO0000O00000O0 ))#line:2911
	return round (O0O0OOOOOOO0000O0 [1 ],2 )#line:2912
def STAT_get_mean_std_ci (OO00OOO00O0000O00 ,OOOO00O000000OO0O ):#line:2914
	""#line:2915
	warnings .filterwarnings ("ignore")#line:2916
	O0OOOO0OOO00OOOO0 =TOOLS_strdict_to_pd (str (OO00OOO00O0000O00 ))["content"].values /OOOO00O000000OO0O #line:2917
	OO0OOOOO0OOO0000O =round (O0OOOO0OOO00OOOO0 .mean (),2 )#line:2918
	OO0O00000O00OO00O =round (O0OOOO0OOO00OOOO0 .std (ddof =1 ),2 )#line:2919
	if len (O0OOOO0OOO00OOOO0 )<30 :#line:2921
		O0OO0OOOO0000O0OO =st .t .interval (0.95 ,df =len (O0OOOO0OOO00OOOO0 )-1 ,loc =np .mean (O0OOOO0OOO00OOOO0 ),scale =st .sem (O0OOOO0OOO00OOOO0 ))#line:2922
	else :#line:2923
		O0OO0OOOO0000O0OO =st .norm .interval (0.95 ,loc =np .mean (O0OOOO0OOO00OOOO0 ),scale =st .sem (O0OOOO0OOO00OOOO0 ))#line:2924
	return pd .Series ((OO0OOOOO0OOO0000O ,OO0O00000O00OO00O ,O0OO0OOOO0000O0OO [1 ]))#line:2928
def STAT_findx_value (OO000OO0OOO0O0O0O ,OO000OO0O00OOO00O ):#line:2930
	""#line:2931
	warnings .filterwarnings ("ignore")#line:2932
	O00O0000OOO00O0O0 =TOOLS_strdict_to_pd (str (OO000OO0OOO0O0O0O ))#line:2933
	OO00000O0O0O0O0O0 =O00O0000OOO00O0O0 .where (O00O0000OOO00O0O0 ["index"]==str (OO000OO0O00OOO00O ))#line:2935
	print (OO00000O0O0O0O0O0 )#line:2936
	return OO00000O0O0O0O0O0 #line:2937
def STAT_judge_x (OOOO000OO0O00OOOO ,OO0OOOOO0O0O0OOO0 ):#line:2939
	""#line:2940
	for OO000OO0O0OO00000 in OO0OOOOO0O0O0OOO0 :#line:2941
		if OOOO000OO0O00OOOO .find (OO000OO0O0OO00000 )>-1 :#line:2942
			return 1 #line:2943
def STAT_recent30 (OOOO00OOO0O00O0O0 ,OOOO0O0OO00OO000O ):#line:2945
	""#line:2946
	import datetime #line:2947
	O00OO00O0OO0OOO0O =OOOO00OOO0O00O0O0 [(OOOO00OOO0O00O0O0 ["报告日期"].dt .date >(datetime .date .today ()-datetime .timedelta (days =30 )))]#line:2951
	OOOOOO0O0O00OO0O0 =O00OO00O0OO0OOO0O .drop_duplicates (["报告编码"]).groupby (OOOO0O0OO00OO000O ).agg (最近30天报告数 =("报告编码","nunique"),最近30天报告严重伤害数 =("伤害",lambda O00O000OO0O0O00OO :STAT_countpx (O00O000OO0O0O00OO .values ,"严重伤害")),最近30天报告死亡数量 =("伤害",lambda OO0OOOO0O0OOOOO00 :STAT_countpx (OO0OOOO0O0OOOOO00 .values ,"死亡")),最近30天报告单位个数 =("单位名称","nunique"),).reset_index ()#line:2958
	OOOOOO0O0O00OO0O0 =STAT_basic_risk (OOOOOO0O0O00OO0O0 ,"最近30天报告数","最近30天报告严重伤害数","最近30天报告死亡数量","最近30天报告单位个数").fillna (0 )#line:2959
	OOOOOO0O0O00OO0O0 =OOOOOO0O0O00OO0O0 .rename (columns ={"风险评分":"最近30天风险评分"})#line:2961
	return OOOOOO0O0O00OO0O0 #line:2962
def STAT_PPR_ROR_1 (OO0000O0OO00OO0OO ,O00OOOO00OO00OOOO ,O0OOOOO0O00O00OO0 ,O0O00OOO0000O00O0 ,O00O00O0OO00OOOOO ):#line:2965
    ""#line:2966
    OOO00OO0000OOO0OO =O00O00O0OO00OOOOO [(O00O00O0OO00OOOOO [OO0000O0OO00OO0OO ]==O00OOOO00OO00OOOO )]#line:2969
    O0OOOO0OO000OOO00 =OOO00OO0000OOO0OO .loc [OOO00OO0000OOO0OO [O0OOOOO0O00O00OO0 ].str .contains (O0O00OOO0000O00O0 ,na =False )]#line:2970
    O0OOOOO0O0O00OOOO =O00O00O0OO00OOOOO [(O00O00O0OO00OOOOO [OO0000O0OO00OO0OO ]!=O00OOOO00OO00OOOO )]#line:2971
    O0OO00O00000OOO00 =O0OOOOO0O0O00OOOO .loc [O0OOOOO0O0O00OOOO [O0OOOOO0O00O00OO0 ].str .contains (O0O00OOO0000O00O0 ,na =False )]#line:2972
    OO0O0O00OO0OO0OOO =(len (O0OOOO0OO000OOO00 ),(len (OOO00OO0000OOO0OO )-len (O0OOOO0OO000OOO00 )),len (O0OO00O00000OOO00 ),(len (O0OOOOO0O0O00OOOO )-len (O0OO00O00000OOO00 )))#line:2973
    if len (O0OOOO0OO000OOO00 )>0 :#line:2974
        OOO00OO000OO0OOO0 =STAT_PPR_ROR_0 (len (O0OOOO0OO000OOO00 ),(len (OOO00OO0000OOO0OO )-len (O0OOOO0OO000OOO00 )),len (O0OO00O00000OOO00 ),(len (O0OOOOO0O0O00OOOO )-len (O0OO00O00000OOO00 )))#line:2975
    else :#line:2976
        OOO00OO000OO0OOO0 =(0 ,0 ,0 ,0 ,0 )#line:2977
    O00000OOOOO00O0OO =len (OOO00OO0000OOO0OO )#line:2980
    if O00000OOOOO00O0OO ==0 :#line:2981
        O00000OOOOO00O0OO =0.5 #line:2982
    return (O0O00OOO0000O00O0 ,len (O0OOOO0OO000OOO00 ),round (len (O0OOOO0OO000OOO00 )/O00000OOOOO00O0OO *100 ,2 ),round (OOO00OO000OO0OOO0 [0 ],2 ),round (OOO00OO000OO0OOO0 [1 ],2 ),round (OOO00OO000OO0OOO0 [2 ],2 ),round (OOO00OO000OO0OOO0 [3 ],2 ),round (OOO00OO000OO0OOO0 [4 ],2 ),str (OO0O0O00OO0OO0OOO ),)#line:2993
def STAT_basic_risk (OOO0OOOOO00OO0000 ,O0OO000OO0O00OOO0 ,OO0000OOO000OOOO0 ,OO00O0O0OO0O00000 ,O0OOOOO0O0O0O0000 ):#line:2997
	""#line:2998
	OOO0OOOOO00OO0000 ["风险评分"]=0 #line:2999
	OOO0OOOOO00OO0000 .loc [((OOO0OOOOO00OO0000 [O0OO000OO0O00OOO0 ]>=3 )&(OOO0OOOOO00OO0000 [OO0000OOO000OOOO0 ]>=1 ))|(OOO0OOOOO00OO0000 [O0OO000OO0O00OOO0 ]>=5 ),"风险评分"]=OOO0OOOOO00OO0000 ["风险评分"]+5 #line:3000
	OOO0OOOOO00OO0000 .loc [(OOO0OOOOO00OO0000 [OO0000OOO000OOOO0 ]>=3 ),"风险评分"]=OOO0OOOOO00OO0000 ["风险评分"]+1 #line:3001
	OOO0OOOOO00OO0000 .loc [(OOO0OOOOO00OO0000 [OO00O0O0OO0O00000 ]>=1 ),"风险评分"]=OOO0OOOOO00OO0000 ["风险评分"]+10 #line:3002
	OOO0OOOOO00OO0000 ["风险评分"]=OOO0OOOOO00OO0000 ["风险评分"]+OOO0OOOOO00OO0000 [O0OOOOO0O0O0O0000 ]/100 #line:3003
	return OOO0OOOOO00OO0000 #line:3004
def STAT_PPR_ROR_0 (O00O0O0OO000OO00O ,OOOO0O000OO0OO0O0 ,O00O0OO0OOOOO000O ,O0OOO00000O0O0OO0 ):#line:3007
    ""#line:3008
    if O00O0O0OO000OO00O *OOOO0O000OO0OO0O0 *O00O0OO0OOOOO000O *O0OOO00000O0O0OO0 ==0 :#line:3013
        O00O0O0OO000OO00O =O00O0O0OO000OO00O +1 #line:3014
        OOOO0O000OO0OO0O0 =OOOO0O000OO0OO0O0 +1 #line:3015
        O00O0OO0OOOOO000O =O00O0OO0OOOOO000O +1 #line:3016
        O0OOO00000O0O0OO0 =O0OOO00000O0O0OO0 +1 #line:3017
    O0OOOOOOOOOOOOOO0 =(O00O0O0OO000OO00O /(O00O0O0OO000OO00O +OOOO0O000OO0OO0O0 ))/(O00O0OO0OOOOO000O /(O00O0OO0OOOOO000O +O0OOO00000O0O0OO0 ))#line:3018
    OOO00O0OO00O00000 =math .sqrt (1 /O00O0O0OO000OO00O -1 /(O00O0O0OO000OO00O +OOOO0O000OO0OO0O0 )+1 /O00O0OO0OOOOO000O -1 /(O00O0OO0OOOOO000O +O0OOO00000O0O0OO0 ))#line:3019
    O0O0O00OOO0OOO0OO =(math .exp (math .log (O0OOOOOOOOOOOOOO0 )-1.96 *OOO00O0OO00O00000 ),math .exp (math .log (O0OOOOOOOOOOOOOO0 )+1.96 *OOO00O0OO00O00000 ),)#line:3023
    OOOO000O000OOO00O =(O00O0O0OO000OO00O /O00O0OO0OOOOO000O )/(OOOO0O000OO0OO0O0 /O0OOO00000O0O0OO0 )#line:3024
    OOOOOOOO00OOOOO00 =math .sqrt (1 /O00O0O0OO000OO00O +1 /OOOO0O000OO0OO0O0 +1 /O00O0OO0OOOOO000O +1 /O0OOO00000O0O0OO0 )#line:3025
    OOO0O00O00OO00000 =(math .exp (math .log (OOOO000O000OOO00O )-1.96 *OOOOOOOO00OOOOO00 ),math .exp (math .log (OOOO000O000OOO00O )+1.96 *OOOOOOOO00OOOOO00 ),)#line:3029
    OO0O0000OO0OO0O0O =((O00O0O0OO000OO00O *OOOO0O000OO0OO0O0 -OOOO0O000OO0OO0O0 *O00O0OO0OOOOO000O )*(O00O0O0OO000OO00O *OOOO0O000OO0OO0O0 -OOOO0O000OO0OO0O0 *O00O0OO0OOOOO000O )*(O00O0O0OO000OO00O +OOOO0O000OO0OO0O0 +O00O0OO0OOOOO000O +O0OOO00000O0O0OO0 ))/((O00O0O0OO000OO00O +OOOO0O000OO0OO0O0 )*(O00O0OO0OOOOO000O +O0OOO00000O0O0OO0 )*(O00O0O0OO000OO00O +O00O0OO0OOOOO000O )*(OOOO0O000OO0OO0O0 +O0OOO00000O0O0OO0 ))#line:3032
    return OOOO000O000OOO00O ,OOO0O00O00OO00000 [0 ],O0OOOOOOOOOOOOOO0 ,O0O0O00OOO0OOO0OO [0 ],OO0O0000OO0OO0O0O #line:3033
def STAT_find_keyword_risk (O000O0OO0OOOOOOO0 ,OO0O0000O0OOO0O00 ,OOO000000OOO0OO0O ,O0O0OO0O0OO0O0000 ,OOOOO0OO00OO0O000 ):#line:3035
		""#line:3036
		O000O0OO0OOOOOOO0 =O000O0OO0OOOOOOO0 .drop_duplicates (["报告编码"]).reset_index (drop =True )#line:3037
		OOO0O000OO00OOOOO =O000O0OO0OOOOOOO0 .groupby (OO0O0000O0OOO0O00 ).agg (证号关键字总数量 =(OOO000000OOO0OO0O ,"count"),包含元素个数 =(O0O0OO0O0OO0O0000 ,"nunique"),包含元素 =(O0O0OO0O0OO0O0000 ,STAT_countx ),).reset_index ()#line:3042
		O00OOOOOO0OOOO0O0 =OO0O0000O0OOO0O00 .copy ()#line:3044
		O00OOOOOO0OOOO0O0 .append (O0O0OO0O0OO0O0000 )#line:3045
		OOOO0O00OO0O0000O =O000O0OO0OOOOOOO0 .groupby (O00OOOOOO0OOOO0O0 ).agg (计数 =(O0O0OO0O0OO0O0000 ,"count"),严重伤害数 =("伤害",lambda O000OOO00OOO0OOOO :STAT_countpx (O000OOO00OOO0OOOO .values ,"严重伤害")),死亡数量 =("伤害",lambda O0OO000O0000000OO :STAT_countpx (O0OO000O0000000OO .values ,"死亡")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),).reset_index ()#line:3052
		OOOOOO0O000O0000O =O00OOOOOO0OOOO0O0 .copy ()#line:3055
		OOOOOO0O000O0000O .remove ("关键字")#line:3056
		OO0000O0OO0OOO00O =O000O0OO0OOOOOOO0 .groupby (OOOOOO0O000O0000O ).agg (该元素总数 =(O0O0OO0O0OO0O0000 ,"count"),).reset_index ()#line:3059
		OOOO0O00OO0O0000O ["证号总数"]=OOOOO0OO00OO0O000 #line:3061
		O0O00OOOO0OO0O0OO =pd .merge (OOOO0O00OO0O0000O ,OOO0O000OO00OOOOO ,on =OO0O0000O0OOO0O00 ,how ="left")#line:3062
		if len (O0O00OOOO0OO0O0OO )>0 :#line:3067
			O0O00OOOO0OO0O0OO [['数量均值','数量标准差','数量CI']]=O0O00OOOO0OO0O0OO .包含元素 .apply (lambda O0O0OO0OO0OOO00O0 :STAT_get_mean_std_ci (O0O0OO0OO0OOO00O0 ,1 ))#line:3068
		return O0O00OOOO0OO0O0OO #line:3071
def STAT_find_risk (OO000OOO00O0O00OO ,OOOO0OO0OOOOOO00O ,OOOO0OOOO00O0OOO0 ,OO00O0OOOO0O0OOO0 ):#line:3077
		""#line:3078
		OO000OOO00O0O00OO =OO000OOO00O0O00OO .drop_duplicates (["报告编码"]).reset_index (drop =True )#line:3079
		OO00OOOO0O0O0O000 =OO000OOO00O0O00OO .groupby (OOOO0OO0OOOOOO00O ).agg (证号总数量 =(OOOO0OOOO00O0OOO0 ,"count"),包含元素个数 =(OO00O0OOOO0O0OOO0 ,"nunique"),包含元素 =(OO00O0OOOO0O0OOO0 ,STAT_countx ),均值 =(OO00O0OOOO0O0OOO0 ,STAT_get_mean ),标准差 =(OO00O0OOOO0O0OOO0 ,STAT_get_std ),CI上限 =(OO00O0OOOO0O0OOO0 ,STAT_get_95ci ),).reset_index ()#line:3087
		O0O000OOOOO000OO0 =OOOO0OO0OOOOOO00O .copy ()#line:3089
		O0O000OOOOO000OO0 .append (OO00O0OOOO0O0OOO0 )#line:3090
		OO0O00OOOOOOO000O =OO000OOO00O0O00OO .groupby (O0O000OOOOO000OO0 ).agg (计数 =(OO00O0OOOO0O0OOO0 ,"count"),严重伤害数 =("伤害",lambda O0O00O0O0OO00000O :STAT_countpx (O0O00O0O0OO00000O .values ,"严重伤害")),死亡数量 =("伤害",lambda OOOO0O000O0O000O0 :STAT_countpx (OOOO0O000O0O000O0 .values ,"死亡")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),).reset_index ()#line:3097
		O00OO0OOO0OOO000O =pd .merge (OO0O00OOOOOOO000O ,OO00OOOO0O0O0O000 ,on =OOOO0OO0OOOOOO00O ,how ="left")#line:3099
		O00OO0OOO0OOO000O ["风险评分"]=0 #line:3101
		O00OO0OOO0OOO000O ["报表类型"]="dfx_findrisk"+OO00O0OOOO0O0OOO0 #line:3102
		O00OO0OOO0OOO000O .loc [((O00OO0OOO0OOO000O ["计数"]>=3 )&(O00OO0OOO0OOO000O ["严重伤害数"]>=1 )|(O00OO0OOO0OOO000O ["计数"]>=5 )),"风险评分"]=O00OO0OOO0OOO000O ["风险评分"]+5 #line:3103
		O00OO0OOO0OOO000O .loc [(O00OO0OOO0OOO000O ["计数"]>=(O00OO0OOO0OOO000O ["均值"]+O00OO0OOO0OOO000O ["标准差"])),"风险评分"]=O00OO0OOO0OOO000O ["风险评分"]+1 #line:3104
		O00OO0OOO0OOO000O .loc [(O00OO0OOO0OOO000O ["计数"]>=O00OO0OOO0OOO000O ["CI上限"]),"风险评分"]=O00OO0OOO0OOO000O ["风险评分"]+1 #line:3105
		O00OO0OOO0OOO000O .loc [(O00OO0OOO0OOO000O ["严重伤害数"]>=3 )&(O00OO0OOO0OOO000O ["风险评分"]>=7 ),"风险评分"]=O00OO0OOO0OOO000O ["风险评分"]+1 #line:3106
		O00OO0OOO0OOO000O .loc [(O00OO0OOO0OOO000O ["死亡数量"]>=1 ),"风险评分"]=O00OO0OOO0OOO000O ["风险评分"]+10 #line:3107
		O00OO0OOO0OOO000O ["风险评分"]=O00OO0OOO0OOO000O ["风险评分"]+O00OO0OOO0OOO000O ["单位个数"]/100 #line:3108
		O00OO0OOO0OOO000O =O00OO0OOO0OOO000O .sort_values (by ="风险评分",ascending =[False ],na_position ="last").reset_index (drop =True )#line:3109
		return O00OO0OOO0OOO000O #line:3111
def TABLE_tree_Level_2 (OO0OO0OOO0O0OOO00 ,OO0OOOOO0O00OO0OO ,O0O00OOOOOOO0OO00 ,*OO0000OO00OOO0O00 ):#line:3118
    ""#line:3119
    try :#line:3121
        O00O0OO0OOOOO00OO =OO0OO0OOO0O0OOO00 .columns #line:3122
    except :#line:3123
        return 0 #line:3124
    if "报告编码"in OO0OO0OOO0O0OOO00 .columns :#line:3126
        OO0OOOOO0O00OO0OO =0 #line:3127
    try :#line:3128
        O0O00O0O0O0OOOOO0 =len (np .unique (OO0OO0OOO0O0OOO00 ["注册证编号/曾用注册证编号"].values ))#line:3129
    except :#line:3130
        O0O00O0O0O0OOOOO0 =10 #line:3131
    O0OO0O000O0O0O00O =Toplevel ()#line:3134
    O0OO0O000O0O0O00O .title ("报表查看器")#line:3135
    OOO00OO00O00000OO =O0OO0O000O0O0O00O .winfo_screenwidth ()#line:3136
    OOO0O00OOOOO00O00 =O0OO0O000O0O0O00O .winfo_screenheight ()#line:3138
    O00O00O0O0OO0000O =1310 #line:3140
    O0O00000OO0000OOO =600 #line:3141
    OOOOO0O0OO0000O0O =(OOO00OO00O00000OO -O00O00O0O0OO0000O )/2 #line:3143
    OOO00O0OOO0OO00O0 =(OOO0O00OOOOO00O00 -O0O00000OO0000OOO )/2 #line:3144
    O0OO0O000O0O0O00O .geometry ("%dx%d+%d+%d"%(O00O00O0O0OO0000O ,O0O00000OO0000OOO ,OOOOO0O0OO0000O0O ,OOO00O0OOO0OO00O0 ))#line:3145
    OOO00000OO0O0O000 =ttk .Frame (O0OO0O000O0O0O00O ,width =1310 ,height =20 )#line:3148
    OOO00000OO0O0O000 .pack (side =TOP )#line:3149
    O000O0O0000O00000 =ttk .Frame (O0OO0O000O0O0O00O ,width =1310 ,height =20 )#line:3150
    O000O0O0000O00000 .pack (side =BOTTOM )#line:3151
    OOO0O0OO00000OOO0 =ttk .Frame (O0OO0O000O0O0O00O ,width =1310 ,height =600 )#line:3152
    OOO0O0OO00000OOO0 .pack (fill ="both",expand ="false")#line:3153
    if OO0OOOOO0O00OO0OO ==0 :#line:3157
        PROGRAM_Menubar (O0OO0O000O0O0O00O ,OO0OO0OOO0O0OOO00 ,OO0OOOOO0O00OO0OO ,O0O00OOOOOOO0OO00 )#line:3158
    try :#line:3161
        OOO00O0OO00OOO00O =StringVar ()#line:3162
        OOO00O0OO00OOO00O .set ("产品类别")#line:3163
        def OO0000OO00O0O000O (*O0000OO0O0OOOO000 ):#line:3164
            OOO00O0OO00OOO00O .set (OOOOOO000O0OO0000 .get ())#line:3165
        OOO00OO000O00O0OO =StringVar ()#line:3166
        OOO00OO000O00O0OO .set ("无源|诊断试剂")#line:3167
        OO0O0O00000000O00 =Label (OOO00000OO0O0O000 ,text ="")#line:3168
        OO0O0O00000000O00 .pack (side =LEFT )#line:3169
        OO0O0O00000000O00 =Label (OOO00000OO0O0O000 ,text ="位置：")#line:3170
        OO0O0O00000000O00 .pack (side =LEFT )#line:3171
        O0OO0OOO00OOOO0O0 =StringVar ()#line:3172
        OOOOOO000O0OO0000 =ttk .Combobox (OOO00000OO0O0O000 ,width =12 ,height =30 ,state ="readonly",textvariable =O0OO0OOO00OOOO0O0 )#line:3175
        OOOOOO000O0OO0000 ["values"]=OO0OO0OOO0O0OOO00 .columns .tolist ()#line:3176
        OOOOOO000O0OO0000 .current (0 )#line:3177
        OOOOOO000O0OO0000 .bind ("<<ComboboxSelected>>",OO0000OO00O0O000O )#line:3178
        OOOOOO000O0OO0000 .pack (side =LEFT )#line:3179
        OO0O000O0OOOO0OOO =Label (OOO00000OO0O0O000 ,text ="检索：")#line:3180
        OO0O000O0OOOO0OOO .pack (side =LEFT )#line:3181
        O00OOOOO0O0O0OO00 =Entry (OOO00000OO0O0O000 ,width =12 ,textvariable =OOO00OO000O00O0OO ).pack (side =LEFT )#line:3182
        def O00OOO0OOOO00OOO0 ():#line:3184
            pass #line:3185
        OOOO0O0OOO0OOO000 =Button (OOO00000OO0O0O000 ,text ="导出",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TOOLS_save_dict (OO0OO0OOO0O0OOO00 ),)#line:3199
        OOOO0O0OOO0OOO000 .pack (side =LEFT )#line:3200
        OO0000O00O0O00O00 =Button (OOO00000OO0O0O000 ,text ="视图",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (TOOLS_easyreadT (OO0OO0OOO0O0OOO00 ),1 ,O0O00OOOOOOO0OO00 ),)#line:3209
        if "详细描述T"not in OO0OO0OOO0O0OOO00 .columns :#line:3210
            OO0000O00O0O00O00 .pack (side =LEFT )#line:3211
        OO0000O00O0O00O00 =Button (OOO00000OO0O0O000 ,text ="网",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TOOLS_web_view (OO0OO0OOO0O0OOO00 ),)#line:3221
        if "详细描述T"not in OO0OO0OOO0O0OOO00 .columns :#line:3222
            OO0000O00O0O00O00 .pack (side =LEFT )#line:3223
        O00OOOOOO00OO0000 =Button (OOO00000OO0O0O000 ,text ="含",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OO0OO0OOO0O0OOO00 .loc [OO0OO0OOO0O0OOO00 [OOO00O0OO00OOO00O .get ()].astype (str ).str .contains (str (OOO00OO000O00O0OO .get ()),na =False )],1 ,O0O00OOOOOOO0OO00 ,),)#line:3241
        O00OOOOOO00OO0000 .pack (side =LEFT )#line:3242
        O00OOOOOO00OO0000 =Button (OOO00000OO0O0O000 ,text ="无",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OO0OO0OOO0O0OOO00 .loc [~OO0OO0OOO0O0OOO00 [OOO00O0OO00OOO00O .get ()].astype (str ).str .contains (str (OOO00OO000O00O0OO .get ()),na =False )],1 ,O0O00OOOOOOO0OO00 ,),)#line:3259
        O00OOOOOO00OO0000 .pack (side =LEFT )#line:3260
        O00OOOOOO00OO0000 =Button (OOO00000OO0O0O000 ,text ="大",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OO0OO0OOO0O0OOO00 .loc [OO0OO0OOO0O0OOO00 [OOO00O0OO00OOO00O .get ()].astype (float )>float (OOO00OO000O00O0OO .get ())],1 ,O0O00OOOOOOO0OO00 ,),)#line:3275
        O00OOOOOO00OO0000 .pack (side =LEFT )#line:3276
        O00OOOOOO00OO0000 =Button (OOO00000OO0O0O000 ,text ="小",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OO0OO0OOO0O0OOO00 .loc [OO0OO0OOO0O0OOO00 [OOO00O0OO00OOO00O .get ()].astype (float )<float (OOO00OO000O00O0OO .get ())],1 ,O0O00OOOOOOO0OO00 ,),)#line:3291
        O00OOOOOO00OO0000 .pack (side =LEFT )#line:3292
        O00OOOOOO00OO0000 =Button (OOO00000OO0O0O000 ,text ="等",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OO0OO0OOO0O0OOO00 .loc [OO0OO0OOO0O0OOO00 [OOO00O0OO00OOO00O .get ()].astype (float )==float (OOO00OO000O00O0OO .get ())],1 ,O0O00OOOOOOO0OO00 ,),)#line:3307
        O00OOOOOO00OO0000 .pack (side =LEFT )#line:3308
        O00OOOOOO00OO0000 =Button (OOO00000OO0O0O000 ,text ="式",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TOOLS_findin (OO0OO0OOO0O0OOO00 ,O0O00OOOOOOO0OO00 ))#line:3317
        O00OOOOOO00OO0000 .pack (side =LEFT )#line:3318
        O00OOOOOO00OO0000 =Button (OOO00000OO0O0O000 ,text ="前",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OO0OO0OOO0O0OOO00 .head (int (OOO00OO000O00O0OO .get ())),1 ,O0O00OOOOOOO0OO00 ,),)#line:3333
        O00OOOOOO00OO0000 .pack (side =LEFT )#line:3334
        O00OOOOOO00OO0000 =Button (OOO00000OO0O0O000 ,text ="升",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OO0OO0OOO0O0OOO00 .sort_values (by =(OOO00O0OO00OOO00O .get ()),ascending =[True ],na_position ="last"),1 ,O0O00OOOOOOO0OO00 ,),)#line:3349
        O00OOOOOO00OO0000 .pack (side =LEFT )#line:3350
        O00OOOOOO00OO0000 =Button (OOO00000OO0O0O000 ,text ="降",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OO0OO0OOO0O0OOO00 .sort_values (by =(OOO00O0OO00OOO00O .get ()),ascending =[False ],na_position ="last"),1 ,O0O00OOOOOOO0OO00 ,),)#line:3365
        O00OOOOOO00OO0000 .pack (side =LEFT )#line:3366
        O00OOOOOO00OO0000 =Button (OOO00000OO0O0O000 ,text ="SQL",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TOOLS_sql (OO0OO0OOO0O0OOO00 ),)#line:3376
        O00OOOOOO00OO0000 .pack (side =LEFT )#line:3377
    except :#line:3380
        pass #line:3381
    if ini ["模式"]!="其他":#line:3384
        OOOOO0O0OO0OOO000 =Button (OOO00000OO0O0O000 ,text ="近月",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OO0OO0OOO0O0OOO00 [(OO0OO0OOO0O0OOO00 ["最近30天报告单位个数"]>=1 )],1 ,O0O00OOOOOOO0OO00 ,),)#line:3397
        if "最近30天报告数"in OO0OO0OOO0O0OOO00 .columns :#line:3398
            OOOOO0O0OO0OOO000 .pack (side =LEFT )#line:3399
        O00OOOOOO00OO0000 =Button (OOO00000OO0O0O000 ,text ="图表",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :DRAW_pre (OO0OO0OOO0O0OOO00 ),)#line:3411
        if OO0OOOOO0O00OO0OO !=0 :#line:3412
            O00OOOOOO00OO0000 .pack (side =LEFT )#line:3413
        def O0000OO0O0OO00O00 ():#line:3418
            pass #line:3419
        if OO0OOOOO0O00OO0OO ==0 :#line:3422
            OOOOO0O0OO0OOO000 =Button (OOO00000OO0O0O000 ,text ="精简",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (TOOLS_easyread2 (OO0OO0OOO0O0OOO00 ),1 ,O0O00OOOOOOO0OO00 ,),)#line:3436
            OOOOO0O0OO0OOO000 .pack (side =LEFT )#line:3437
        if OO0OOOOO0O00OO0OO ==0 :#line:3440
            OOOOO0O0OO0OOO000 =Button (OOO00000OO0O0O000 ,text ="证号",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OO0OO0OOO0O0OOO00 ).df_zhenghao (),1 ,O0O00OOOOOOO0OO00 ,),)#line:3454
            OOOOO0O0OO0OOO000 .pack (side =LEFT )#line:3455
            OOOOO0O0OO0OOO000 =Button (OOO00000OO0O0O000 ,text ="图",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :DRAW_pre (Countall (OO0OO0OOO0O0OOO00 ).df_zhenghao ()))#line:3464
            OOOOO0O0OO0OOO000 .pack (side =LEFT )#line:3465
            OOOOO0O0OO0OOO000 =Button (OOO00000OO0O0O000 ,text ="批号",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OO0OO0OOO0O0OOO00 ).df_pihao (),1 ,O0O00OOOOOOO0OO00 ,),)#line:3480
            OOOOO0O0OO0OOO000 .pack (side =LEFT )#line:3481
            OOOOO0O0OO0OOO000 =Button (OOO00000OO0O0O000 ,text ="图",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :DRAW_pre (Countall (OO0OO0OOO0O0OOO00 ).df_pihao ()))#line:3490
            OOOOO0O0OO0OOO000 .pack (side =LEFT )#line:3491
            OOOOO0O0OO0OOO000 =Button (OOO00000OO0O0O000 ,text ="型号",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OO0OO0OOO0O0OOO00 ).df_xinghao (),1 ,O0O00OOOOOOO0OO00 ,),)#line:3506
            OOOOO0O0OO0OOO000 .pack (side =LEFT )#line:3507
            OOOOO0O0OO0OOO000 =Button (OOO00000OO0O0O000 ,text ="图",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :DRAW_pre (Countall (OO0OO0OOO0O0OOO00 ).df_xinghao ()))#line:3516
            OOOOO0O0OO0OOO000 .pack (side =LEFT )#line:3517
            OOOOO0O0OO0OOO000 =Button (OOO00000OO0O0O000 ,text ="规格",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OO0OO0OOO0O0OOO00 ).df_guige (),1 ,O0O00OOOOOOO0OO00 ,),)#line:3532
            OOOOO0O0OO0OOO000 .pack (side =LEFT )#line:3533
            OOOOO0O0OO0OOO000 =Button (OOO00000OO0O0O000 ,text ="图",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :DRAW_pre (Countall (OO0OO0OOO0O0OOO00 ).df_guige ()))#line:3542
            OOOOO0O0OO0OOO000 .pack (side =LEFT )#line:3543
            OOOOO0O0OO0OOO000 =Button (OOO00000OO0O0O000 ,text ="企业",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OO0OO0OOO0O0OOO00 ).df_chiyouren (),1 ,O0O00OOOOOOO0OO00 ,),)#line:3558
            OOOOO0O0OO0OOO000 .pack (side =LEFT )#line:3559
            OOOOO0O0OO0OOO000 =Button (OOO00000OO0O0O000 ,text ="县区",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OO0OO0OOO0O0OOO00 ).df_org ("监测机构"),1 ,O0O00OOOOOOO0OO00 ,),)#line:3575
            OOOOO0O0OO0OOO000 .pack (side =LEFT )#line:3576
            OOOOO0O0OO0OOO000 =Button (OOO00000OO0O0O000 ,text ="单位",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OO0OO0OOO0O0OOO00 ).df_user (),1 ,O0O00OOOOOOO0OO00 ,),)#line:3589
            OOOOO0O0OO0OOO000 .pack (side =LEFT )#line:3590
            OOOOO0O0OO0OOO000 =Button (OOO00000OO0O0O000 ,text ="年龄",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OO0OO0OOO0O0OOO00 ).df_age (),1 ,O0O00OOOOOOO0OO00 ,),)#line:3604
            OOOOO0O0OO0OOO000 .pack (side =LEFT )#line:3605
            OOOOO0O0OO0OOO000 =Button (OOO00000OO0O0O000 ,text ="时隔",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (TOOLS_deep_view (OO0OO0OOO0O0OOO00 ,["时隔"],["报告编码","nunique"],0 ),1 ,O0O00OOOOOOO0OO00 ,),)#line:3619
            OOOOO0O0OO0OOO000 .pack (side =LEFT )#line:3620
            OOOOO0O0OO0OOO000 =Button (OOO00000OO0O0O000 ,text ="表现",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OO0OO0OOO0O0OOO00 ).df_psur (),1 ,O0O00OOOOOOO0OO00 ,),)#line:3634
            if "UDI"not in OO0OO0OOO0O0OOO00 .columns :#line:3635
                OOOOO0O0OO0OOO000 .pack (side =LEFT )#line:3636
            OOOOO0O0OO0OOO000 =Button (OOO00000OO0O0O000 ,text ="表现",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (TOOLS_get_guize2 (OO0OO0OOO0O0OOO00 ),1 ,O0O00OOOOOOO0OO00 ,),)#line:3649
            if "UDI"in OO0OO0OOO0O0OOO00 .columns :#line:3650
                OOOOO0O0OO0OOO000 .pack (side =LEFT )#line:3651
            OOOOO0O0OO0OOO000 =Button (OOO00000OO0O0O000 ,text ="发生时间",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TOOLS_time (OO0OO0OOO0O0OOO00 ,"事件发生日期",0 ),)#line:3660
            OOOOO0O0OO0OOO000 .pack (side =LEFT )#line:3661
            OOOOO0O0OO0OOO000 =Button (OOO00000OO0O0O000 ,text ="报告时间",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :DRAW_make_one (TOOLS_time (OO0OO0OOO0O0OOO00 ,"报告日期",1 ),"时间托帕斯图","time","报告总数","超级托帕斯图(严重伤害数)"),)#line:3671
            OOOOO0O0OO0OOO000 .pack (side =LEFT )#line:3672
    try :#line:3678
        OOOO00O0OO00000OO =ttk .Label (O000O0O0000O00000 ,text ="方法：")#line:3680
        OOOO00O0OO00000OO .pack (side =LEFT )#line:3681
        OO000000OO0000O00 =StringVar ()#line:3682
        O0OO0000O0O0OO0O0 =ttk .Combobox (O000O0O0000O00000 ,width =15 ,textvariable =OO000000OO0000O00 ,state ='readonly')#line:3683
        O0OO0000O0O0OO0O0 ['values']=("分组统计","数据透视","描述性统计","饼图(XY)","柱状图(XY)","折线图(XY)","托帕斯图(XY)","堆叠柱状图（X-YZ）","单列多项拆分统计(统计列)","单列多项拆分统计(透视列-统计列)","单列多项拆分统计(透视列-统计列-字典)","追加外部表格信息","添加到外部表格")#line:3684
        O0OO0000O0O0OO0O0 .pack (side =LEFT )#line:3688
        O0OO0000O0O0OO0O0 .current (0 )#line:3689
        O0O0OOOO0OO00OOOO =ttk .Label (O000O0O0000O00000 ,text ="分组列（X-Y-Z）:")#line:3690
        O0O0OOOO0OO00OOOO .pack (side =LEFT )#line:3691
        O000OOO00O0OO0O00 =StringVar ()#line:3694
        OO0000O00OO0O00O0 =ttk .Combobox (O000O0O0000O00000 ,width =15 ,textvariable =O000OOO00O0OO0O00 ,state ='readonly')#line:3695
        OO0000O00OO0O00O0 ['values']=OO0OO0OOO0O0OOO00 .columns .tolist ()#line:3696
        OO0000O00OO0O00O0 .pack (side =LEFT )#line:3697
        O0000O00OOO000O0O =StringVar ()#line:3698
        O0O0OO000O0OO000O =ttk .Combobox (O000O0O0000O00000 ,width =15 ,textvariable =O0000O00OOO000O0O ,state ='readonly')#line:3699
        O0O0OO000O0OO000O ['values']=OO0OO0OOO0O0OOO00 .columns .tolist ()#line:3700
        O0O0OO000O0OO000O .pack (side =LEFT )#line:3701
        OO0OOO00000O0000O =StringVar ()#line:3702
        OOO0O000OOO000000 =ttk .Combobox (O000O0O0000O00000 ,width =15 ,textvariable =OO0OOO00000O0000O ,state ='readonly')#line:3703
        OOO0O000OOO000000 ['values']=OO0OO0OOO0O0OOO00 .columns .tolist ()#line:3704
        OOO0O000OOO000000 .pack (side =LEFT )#line:3705
        O0OO0O00O000000O0 =StringVar ()#line:3706
        OOOOO0O00O0OO0O0O =StringVar ()#line:3707
        O0O0OOOO0OO00OOOO =ttk .Label (O000O0O0000O00000 ,text ="计算列（V-M）:")#line:3708
        O0O0OOOO0OO00OOOO .pack (side =LEFT )#line:3709
        OOO00OOO00O000000 =ttk .Combobox (O000O0O0000O00000 ,width =10 ,textvariable =O0OO0O00O000000O0 ,state ='readonly')#line:3711
        OOO00OOO00O000000 ['values']=OO0OO0OOO0O0OOO00 .columns .tolist ()#line:3712
        OOO00OOO00O000000 .pack (side =LEFT )#line:3713
        OO00OOO00OOO0000O =ttk .Combobox (O000O0O0000O00000 ,width =10 ,textvariable =OOOOO0O00O0OO0O0O ,state ='readonly')#line:3714
        OO00OOO00OOO0000O ['values']=["计数","求和","唯一值计数"]#line:3715
        OO00OOO00OOO0000O .pack (side =LEFT )#line:3716
        O00OO00000O0OOOOO =Button (O000O0O0000O00000 ,text ="自助报表",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TOOLS_Autotable_0 (OO0OO0OOO0O0OOO00 ,O0OO0000O0O0OO0O0 .get (),O000OOO00O0OO0O00 .get (),O0000O00OOO000O0O .get (),OO0OOO00000O0000O .get (),O0OO0O00O000000O0 .get (),OOOOO0O00O0OO0O0O .get (),OO0OO0OOO0O0OOO00 ))#line:3718
        O00OO00000O0OOOOO .pack (side =LEFT )#line:3719
        O00OOOOOO00OO0000 =Button (O000O0O0000O00000 ,text ="去首行",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OO0OO0OOO0O0OOO00 [1 :],1 ,O0O00OOOOOOO0OO00 ,))#line:3736
        O00OOOOOO00OO0000 .pack (side =LEFT )#line:3737
        O00OOOOOO00OO0000 =Button (O000O0O0000O00000 ,text ="去尾行",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OO0OO0OOO0O0OOO00 [:-1 ],1 ,O0O00OOOOOOO0OO00 ,),)#line:3752
        O00OOOOOO00OO0000 .pack (side =LEFT )#line:3753
        OOOOO0O0OO0OOO000 =Button (O000O0O0000O00000 ,text ="行数:"+str (len (OO0OO0OOO0O0OOO00 )),bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",)#line:3763
        OOOOO0O0OO0OOO000 .pack (side =LEFT )#line:3764
    except :#line:3767
        showinfo (title ="提示信息",message ="界面初始化失败。")#line:3768
    OOO000000000000OO =OO0OO0OOO0O0OOO00 .values .tolist ()#line:3774
    OO000000O0OOOO00O =OO0OO0OOO0O0OOO00 .columns .values .tolist ()#line:3775
    O0O00O0OOOO00O0OO =ttk .Treeview (OOO0O0OO00000OOO0 ,columns =OO000000O0OOOO00O ,show ="headings",height =45 )#line:3776
    for OO0O0OO00OO0O0O0O in OO000000O0OOOO00O :#line:3779
        O0O00O0OOOO00O0OO .heading (OO0O0OO00OO0O0O0O ,text =OO0O0OO00OO0O0O0O )#line:3780
    for O0000OO00000O0OOO in OOO000000000000OO :#line:3781
        O0O00O0OOOO00O0OO .insert ("","end",values =O0000OO00000O0OOO )#line:3782
    for O0O0OOOO0000OO000 in OO000000O0OOOO00O :#line:3784
        try :#line:3785
            O0O00O0OOOO00O0OO .column (O0O0OOOO0000OO000 ,minwidth =0 ,width =80 ,stretch =NO )#line:3786
            if "只剩"in O0O0OOOO0000OO000 :#line:3787
                O0O00O0OOOO00O0OO .column (O0O0OOOO0000OO000 ,minwidth =0 ,width =150 ,stretch =NO )#line:3788
        except :#line:3789
            pass #line:3790
    O00O0O0O0OOO0OOO0 =["评分说明"]#line:3794
    O000OO00O00OO0O00 =["该单位喜好上报的品种统计","报告编码","产品名称","上报机构描述","持有人处理描述","该注册证编号/曾用注册证编号报告数量","通用名称","该批准文号报告数量","上市许可持有人名称",]#line:3807
    OO0OOOOOO0O0000OO =["注册证编号/曾用注册证编号","监测机构","报告月份","报告季度","单位列表","单位名称",]#line:3815
    OOO00O0OOOO000000 =["管理类别",]#line:3819
    for O0O0OOOO0000OO000 in O000OO00O00OO0O00 :#line:3822
        try :#line:3823
            O0O00O0OOOO00O0OO .column (O0O0OOOO0000OO000 ,minwidth =0 ,width =200 ,stretch =NO )#line:3824
        except :#line:3825
            pass #line:3826
    for O0O0OOOO0000OO000 in OO0OOOOOO0O0000OO :#line:3829
        try :#line:3830
            O0O00O0OOOO00O0OO .column (O0O0OOOO0000OO000 ,minwidth =0 ,width =140 ,stretch =NO )#line:3831
        except :#line:3832
            pass #line:3833
    for O0O0OOOO0000OO000 in OOO00O0OOOO000000 :#line:3834
        try :#line:3835
            O0O00O0OOOO00O0OO .column (O0O0OOOO0000OO000 ,minwidth =0 ,width =40 ,stretch =NO )#line:3836
        except :#line:3837
            pass #line:3838
    for O0O0OOOO0000OO000 in O00O0O0O0OOO0OOO0 :#line:3839
        try :#line:3840
            O0O00O0OOOO00O0OO .column (O0O0OOOO0000OO000 ,minwidth =0 ,width =800 ,stretch =NO )#line:3841
        except :#line:3842
            pass #line:3843
    try :#line:3845
        O0O00O0OOOO00O0OO .column ("请选择需要查看的表格",minwidth =1 ,width =300 ,stretch =NO )#line:3848
    except :#line:3849
        pass #line:3850
    try :#line:3852
        O0O00O0OOOO00O0OO .column ("详细描述T",minwidth =1 ,width =2300 ,stretch =NO )#line:3855
    except :#line:3856
        pass #line:3857
    O0O0O0O00O00OO0OO =Scrollbar (OOO0O0OO00000OOO0 ,orient ="vertical")#line:3859
    O0O0O0O00O00OO0OO .pack (side =RIGHT ,fill =Y )#line:3860
    O0O0O0O00O00OO0OO .config (command =O0O00O0OOOO00O0OO .yview )#line:3861
    O0O00O0OOOO00O0OO .config (yscrollcommand =O0O0O0O00O00OO0OO .set )#line:3862
    OOO0OOO00OO0OOOO0 =Scrollbar (OOO0O0OO00000OOO0 ,orient ="horizontal")#line:3864
    OOO0OOO00OO0OOOO0 .pack (side =BOTTOM ,fill =X )#line:3865
    OOO0OOO00OO0OOOO0 .config (command =O0O00O0OOOO00O0OO .xview )#line:3866
    O0O00O0OOOO00O0OO .config (yscrollcommand =O0O0O0O00O00OO0OO .set )#line:3867
    def OO0O0O00O0OOO0OOO (OO00OOO00O000OO0O ,OOOO00OO000OO00OO ,O00OO0O00000OO00O ):#line:3870
        for OOOO0O0000O0000OO in O0O00O0OOOO00O0OO .selection ():#line:3872
            O000OO0O0000O0O0O =O0O00O0OOOO00O0OO .item (OOOO0O0000O0000OO ,"values")#line:3873
        O00O0OOO00O0O0OO0 =dict (zip (OOOO00OO000OO00OO ,O000OO0O0000O0O0O ))#line:3874
        if "详细描述T"in OOOO00OO000OO00OO and "{"in O00O0OOO00O0O0OO0 ["详细描述T"]:#line:3878
            OO0O0OO000O0000O0 =eval (O00O0OOO00O0O0OO0 ["详细描述T"])#line:3879
            OO0O0OO000O0000O0 =pd .DataFrame .from_dict (OO0O0OO000O0000O0 ,orient ="index",columns =["content"]).reset_index ()#line:3880
            OO0O0OO000O0000O0 =OO0O0OO000O0000O0 .sort_values (by ="content",ascending =[False ],na_position ="last")#line:3881
            DRAW_make_one (OO0O0OO000O0000O0 ,O00O0OOO00O0O0OO0 ["条目"],"index","content","饼图")#line:3882
            return 0 #line:3883
        if "dfx_deepview"in O00O0OOO00O0O0OO0 ["报表类型"]:#line:3888
            O00OOOOO000OOOO00 =eval (O00O0OOO00O0O0OO0 ["报表类型"][13 :])#line:3889
            OO0OOO0OOOO0OO0OO =O00OO0O00000OO00O .copy ()#line:3890
            for O00O000OO0O00O00O in O00OOOOO000OOOO00 :#line:3891
                OO0OOO0OOOO0OO0OO =OO0OOO0OOOO0OO0OO [(OO0OOO0OOOO0OO0OO [O00O000OO0O00O00O ].astype (str )==O000OO0O0000O0O0O [O00OOOOO000OOOO00 .index (O00O000OO0O00O00O )])].copy ()#line:3892
            OO0OOO0OOOO0OO0OO ["报表类型"]="ori_dfx_deepview"#line:3893
            TABLE_tree_Level_2 (OO0OOO0OOOO0OO0OO ,0 ,OO0OOO0OOOO0OO0OO )#line:3894
            return 0 #line:3895
        if "dfx_deepvie2"in O00O0OOO00O0O0OO0 ["报表类型"]:#line:3898
            O00OOOOO000OOOO00 =eval (O00O0OOO00O0O0OO0 ["报表类型"][13 :])#line:3899
            OO0OOO0OOOO0OO0OO =O00OO0O00000OO00O .copy ()#line:3900
            for O00O000OO0O00O00O in O00OOOOO000OOOO00 :#line:3901
                OO0OOO0OOOO0OO0OO =OO0OOO0OOOO0OO0OO [OO0OOO0OOOO0OO0OO [O00O000OO0O00O00O ].str .contains (O000OO0O0000O0O0O [O00OOOOO000OOOO00 .index (O00O000OO0O00O00O )],na =False )].copy ()#line:3902
            OO0OOO0OOOO0OO0OO ["报表类型"]="ori_dfx_deepview"#line:3903
            TABLE_tree_Level_2 (OO0OOO0OOOO0OO0OO ,0 ,OO0OOO0OOOO0OO0OO )#line:3904
            return 0 #line:3905
        if "dfx_zhenghao"in O00O0OOO00O0O0OO0 ["报表类型"]:#line:3909
            OO0OOO0OOOO0OO0OO =O00OO0O00000OO00O [(O00OO0O00000OO00O ["注册证编号/曾用注册证编号"]==O00O0OOO00O0O0OO0 ["注册证编号/曾用注册证编号"])].copy ()#line:3910
            OO0OOO0OOOO0OO0OO ["报表类型"]="ori_dfx_zhenghao"#line:3911
            TABLE_tree_Level_2 (OO0OOO0OOOO0OO0OO ,0 ,OO0OOO0OOOO0OO0OO )#line:3912
            return 0 #line:3913
        if ("dfx_pihao"in O00O0OOO00O0O0OO0 ["报表类型"]or "dfx_findrisk"in O00O0OOO00O0O0OO0 ["报表类型"]or "dfx_xinghao"in O00O0OOO00O0O0OO0 ["报表类型"]or "dfx_guige"in O00O0OOO00O0O0OO0 ["报表类型"])and O0O00O0O0O0OOOOO0 ==1 :#line:3917
            OOO000OO00000O00O ="CLT"#line:3918
            if "pihao"in O00O0OOO00O0O0OO0 ["报表类型"]or "产品批号"in O00O0OOO00O0O0OO0 ["报表类型"]:#line:3919
                OOO000OO00000O00O ="产品批号"#line:3920
            if "xinghao"in O00O0OOO00O0O0OO0 ["报表类型"]or "型号"in O00O0OOO00O0O0OO0 ["报表类型"]:#line:3921
                OOO000OO00000O00O ="型号"#line:3922
            if "guige"in O00O0OOO00O0O0OO0 ["报表类型"]or "规格"in O00O0OOO00O0O0OO0 ["报表类型"]:#line:3923
                OOO000OO00000O00O ="规格"#line:3924
            if "事件发生季度"in O00O0OOO00O0O0OO0 ["报表类型"]:#line:3925
                OOO000OO00000O00O ="事件发生季度"#line:3926
            if "事件发生月份"in O00O0OOO00O0O0OO0 ["报表类型"]:#line:3927
                OOO000OO00000O00O ="事件发生月份"#line:3928
            if "性别"in O00O0OOO00O0O0OO0 ["报表类型"]:#line:3929
                OOO000OO00000O00O ="性别"#line:3930
            if "年龄段"in O00O0OOO00O0O0OO0 ["报表类型"]:#line:3931
                OOO000OO00000O00O ="年龄段"#line:3932
            OO0OOO0OOOO0OO0OO =O00OO0O00000OO00O [(O00OO0O00000OO00O ["注册证编号/曾用注册证编号"]==O00O0OOO00O0O0OO0 ["注册证编号/曾用注册证编号"])&(O00OO0O00000OO00O [OOO000OO00000O00O ]==O00O0OOO00O0O0OO0 [OOO000OO00000O00O ])].copy ()#line:3933
            OO0OOO0OOOO0OO0OO ["报表类型"]="ori_pihao"#line:3934
            TABLE_tree_Level_2 (OO0OOO0OOOO0OO0OO ,0 ,OO0OOO0OOOO0OO0OO )#line:3935
            return 0 #line:3936
        if ("findrisk"in O00O0OOO00O0O0OO0 ["报表类型"]or "dfx_pihao"in O00O0OOO00O0O0OO0 ["报表类型"]or "dfx_xinghao"in O00O0OOO00O0O0OO0 ["报表类型"]or "dfx_guige"in O00O0OOO00O0O0OO0 ["报表类型"])and O0O00O0O0O0OOOOO0 !=1 :#line:3940
            OO0OOO0OOOO0OO0OO =OO0OO0OOO0O0OOO00 [(OO0OO0OOO0O0OOO00 ["注册证编号/曾用注册证编号"]==O00O0OOO00O0O0OO0 ["注册证编号/曾用注册证编号"])].copy ()#line:3941
            OO0OOO0OOOO0OO0OO ["报表类型"]=O00O0OOO00O0O0OO0 ["报表类型"]+"1"#line:3942
            TABLE_tree_Level_2 (OO0OOO0OOOO0OO0OO ,1 ,O00OO0O00000OO00O )#line:3943
            return 0 #line:3945
        if "dfx_org监测机构"in O00O0OOO00O0O0OO0 ["报表类型"]:#line:3948
            OO0OOO0OOOO0OO0OO =O00OO0O00000OO00O [(O00OO0O00000OO00O ["监测机构"]==O00O0OOO00O0O0OO0 ["监测机构"])].copy ()#line:3949
            OO0OOO0OOOO0OO0OO ["报表类型"]="ori_dfx_org"#line:3950
            TABLE_tree_Level_2 (OO0OOO0OOOO0OO0OO ,0 ,OO0OOO0OOOO0OO0OO )#line:3951
            return 0 #line:3952
        if "dfx_org市级监测机构"in O00O0OOO00O0O0OO0 ["报表类型"]:#line:3954
            OO0OOO0OOOO0OO0OO =O00OO0O00000OO00O [(O00OO0O00000OO00O ["市级监测机构"]==O00O0OOO00O0O0OO0 ["市级监测机构"])].copy ()#line:3955
            OO0OOO0OOOO0OO0OO ["报表类型"]="ori_dfx_org"#line:3956
            TABLE_tree_Level_2 (OO0OOO0OOOO0OO0OO ,0 ,OO0OOO0OOOO0OO0OO )#line:3957
            return 0 #line:3958
        if "dfx_user"in O00O0OOO00O0O0OO0 ["报表类型"]:#line:3961
            OO0OOO0OOOO0OO0OO =O00OO0O00000OO00O [(O00OO0O00000OO00O ["单位名称"]==O00O0OOO00O0O0OO0 ["单位名称"])].copy ()#line:3962
            OO0OOO0OOOO0OO0OO ["报表类型"]="ori_dfx_user"#line:3963
            TABLE_tree_Level_2 (OO0OOO0OOOO0OO0OO ,0 ,OO0OOO0OOOO0OO0OO )#line:3964
            return 0 #line:3965
        if "dfx_chiyouren"in O00O0OOO00O0O0OO0 ["报表类型"]:#line:3969
            OO0OOO0OOOO0OO0OO =O00OO0O00000OO00O [(O00OO0O00000OO00O ["上市许可持有人名称"]==O00O0OOO00O0O0OO0 ["上市许可持有人名称"])].copy ()#line:3970
            OO0OOO0OOOO0OO0OO ["报表类型"]="ori_dfx_chiyouren"#line:3971
            TABLE_tree_Level_2 (OO0OOO0OOOO0OO0OO ,0 ,OO0OOO0OOOO0OO0OO )#line:3972
            return 0 #line:3973
        if "dfx_chanpin"in O00O0OOO00O0O0OO0 ["报表类型"]:#line:3975
            OO0OOO0OOOO0OO0OO =O00OO0O00000OO00O [(O00OO0O00000OO00O ["产品名称"]==O00O0OOO00O0O0OO0 ["产品名称"])].copy ()#line:3976
            OO0OOO0OOOO0OO0OO ["报表类型"]="ori_dfx_chanpin"#line:3977
            TABLE_tree_Level_2 (OO0OOO0OOOO0OO0OO ,0 ,OO0OOO0OOOO0OO0OO )#line:3978
            return 0 #line:3979
        if "dfx_findrisk事件发生季度1"in O00O0OOO00O0O0OO0 ["报表类型"]:#line:3984
            OO0OOO0OOOO0OO0OO =O00OO0O00000OO00O [(O00OO0O00000OO00O ["注册证编号/曾用注册证编号"]==O00O0OOO00O0O0OO0 ["注册证编号/曾用注册证编号"])&(O00OO0O00000OO00O ["事件发生季度"]==O00O0OOO00O0O0OO0 ["事件发生季度"])].copy ()#line:3985
            OO0OOO0OOOO0OO0OO ["报表类型"]="ori_dfx_findrisk事件发生季度"#line:3986
            TABLE_tree_Level_2 (OO0OOO0OOOO0OO0OO ,0 ,OO0OOO0OOOO0OO0OO )#line:3987
            return 0 #line:3988
        if "dfx_findrisk事件发生月份1"in O00O0OOO00O0O0OO0 ["报表类型"]:#line:3991
            OO0OOO0OOOO0OO0OO =O00OO0O00000OO00O [(O00OO0O00000OO00O ["注册证编号/曾用注册证编号"]==O00O0OOO00O0O0OO0 ["注册证编号/曾用注册证编号"])&(O00OO0O00000OO00O ["事件发生月份"]==O00O0OOO00O0O0OO0 ["事件发生月份"])].copy ()#line:3992
            OO0OOO0OOOO0OO0OO ["报表类型"]="ori_dfx_findrisk事件发生月份"#line:3993
            TABLE_tree_Level_2 (OO0OOO0OOOO0OO0OO ,0 ,OO0OOO0OOOO0OO0OO )#line:3994
            return 0 #line:3995
        if ("keyword_findrisk"in O00O0OOO00O0O0OO0 ["报表类型"])and O0O00O0O0O0OOOOO0 ==1 :#line:3998
            OOO000OO00000O00O ="CLT"#line:3999
            if "批号"in O00O0OOO00O0O0OO0 ["报表类型"]:#line:4000
                OOO000OO00000O00O ="产品批号"#line:4001
            if "事件发生季度"in O00O0OOO00O0O0OO0 ["报表类型"]:#line:4002
                OOO000OO00000O00O ="事件发生季度"#line:4003
            if "事件发生月份"in O00O0OOO00O0O0OO0 ["报表类型"]:#line:4004
                OOO000OO00000O00O ="事件发生月份"#line:4005
            if "性别"in O00O0OOO00O0O0OO0 ["报表类型"]:#line:4006
                OOO000OO00000O00O ="性别"#line:4007
            if "年龄段"in O00O0OOO00O0O0OO0 ["报表类型"]:#line:4008
                OOO000OO00000O00O ="年龄段"#line:4009
            OO0OOO0OOOO0OO0OO =O00OO0O00000OO00O [(O00OO0O00000OO00O ["注册证编号/曾用注册证编号"]==O00O0OOO00O0O0OO0 ["注册证编号/曾用注册证编号"])&(O00OO0O00000OO00O [OOO000OO00000O00O ]==O00O0OOO00O0O0OO0 [OOO000OO00000O00O ])].copy ()#line:4010
            OO0OOO0OOOO0OO0OO ["关键字查找列"]=""#line:4011
            for OO0O000000OO0OO0O in TOOLS_get_list (O00O0OOO00O0O0OO0 ["关键字查找列"]):#line:4012
                OO0OOO0OOOO0OO0OO ["关键字查找列"]=OO0OOO0OOOO0OO0OO ["关键字查找列"]+OO0OOO0OOOO0OO0OO [OO0O000000OO0OO0O ].astype ("str")#line:4013
            OO0OOO0OOOO0OO0OO =OO0OOO0OOOO0OO0OO [(OO0OOO0OOOO0OO0OO ["关键字查找列"].str .contains (O00O0OOO00O0O0OO0 ["关键字组合"],na =False ))]#line:4014
            if str (O00O0OOO00O0O0OO0 ["排除值"])!="nan":#line:4016
                OO0OOO0OOOO0OO0OO =OO0OOO0OOOO0OO0OO .loc [~OO0OOO0OOOO0OO0OO ["关键字查找列"].str .contains (O00O0OOO00O0O0OO0 ["排除值"],na =False )]#line:4017
            OO0OOO0OOOO0OO0OO ["报表类型"]="ori_"+O00O0OOO00O0O0OO0 ["报表类型"]#line:4019
            TABLE_tree_Level_2 (OO0OOO0OOOO0OO0OO ,0 ,OO0OOO0OOOO0OO0OO )#line:4020
            return 0 #line:4021
        if ("PSUR"in O00O0OOO00O0O0OO0 ["报表类型"]):#line:4026
            OO0OOO0OOOO0OO0OO =O00OO0O00000OO00O .copy ()#line:4027
            if ini ["模式"]=="器械":#line:4028
                OO0OOO0OOOO0OO0OO ["关键字查找列"]=OO0OOO0OOOO0OO0OO ["器械故障表现"].astype (str )+OO0OOO0OOOO0OO0OO ["伤害表现"].astype (str )+OO0OOO0OOOO0OO0OO ["使用过程"].astype (str )+OO0OOO0OOOO0OO0OO ["事件原因分析描述"].astype (str )+OO0OOO0OOOO0OO0OO ["初步处置情况"].astype (str )#line:4029
            else :#line:4030
                OO0OOO0OOOO0OO0OO ["关键字查找列"]=OO0OOO0OOOO0OO0OO ["器械故障表现"]#line:4031
            if "-其他关键字-"in str (O00O0OOO00O0O0OO0 ["关键字标记"]):#line:4033
                OO0OOO0OOOO0OO0OO =OO0OOO0OOOO0OO0OO .loc [~OO0OOO0OOOO0OO0OO ["关键字查找列"].str .contains (O00O0OOO00O0O0OO0 ["关键字标记"],na =False )].copy ()#line:4034
                TABLE_tree_Level_2 (OO0OOO0OOOO0OO0OO ,0 ,OO0OOO0OOOO0OO0OO )#line:4035
                return 0 #line:4036
            OO0OOO0OOOO0OO0OO =OO0OOO0OOOO0OO0OO [(OO0OOO0OOOO0OO0OO ["关键字查找列"].str .contains (O00O0OOO00O0O0OO0 ["关键字标记"],na =False ))]#line:4039
            if str (O00O0OOO00O0O0OO0 ["排除值"])!="没有排除值":#line:4040
                OO0OOO0OOOO0OO0OO =OO0OOO0OOOO0OO0OO .loc [~OO0OOO0OOOO0OO0OO ["关键字查找列"].str .contains (O00O0OOO00O0O0OO0 ["排除值"],na =False )]#line:4041
            TABLE_tree_Level_2 (OO0OOO0OOOO0OO0OO ,0 ,OO0OOO0OOOO0OO0OO )#line:4045
            return 0 #line:4046
        if ("ROR"in O00O0OOO00O0O0OO0 ["报表类型"]):#line:4049
            OO0O0OOO0OO0O0O0O ={'nan':"-未定义-"}#line:4050
            OOOO0OOOO000O0O00 =eval (O00O0OOO00O0O0OO0 ["报表定位"],OO0O0OOO0OO0O0O0O )#line:4051
            OO0OOO0OOOO0OO0OO =O00OO0O00000OO00O .copy ()#line:4052
            for O0OO000OOO000O0O0 ,OOOOOO0O0O0O000O0 in OOOO0OOOO000O0O00 .items ():#line:4054
                if O0OO000OOO000O0O0 =="合并列"and OOOOOO0O0O0O000O0 !={}:#line:4056
                    for O0OO0000OOOOO0OO0 ,OO00OO0OOO0000000 in OOOOOO0O0O0O000O0 .items ():#line:4057
                        if OO00OO0OOO0000000 !="-未定义-":#line:4058
                            OO0O0O0OOOO000O00 =TOOLS_get_list (OO00OO0OOO0000000 )#line:4059
                            OO0OOO0OOOO0OO0OO [O0OO0000OOOOO0OO0 ]=""#line:4060
                            for O00OOOO000OO00000 in OO0O0O0OOOO000O00 :#line:4061
                                OO0OOO0OOOO0OO0OO [O0OO0000OOOOO0OO0 ]=OO0OOO0OOOO0OO0OO [O0OO0000OOOOO0OO0 ]+OO0OOO0OOOO0OO0OO [O00OOOO000OO00000 ].astype ("str")#line:4062
                if O0OO000OOO000O0O0 =="等于"and OOOOOO0O0O0O000O0 !={}:#line:4064
                    for O0OO0000OOOOO0OO0 ,OO00OO0OOO0000000 in OOOOOO0O0O0O000O0 .items ():#line:4065
                        OO0OOO0OOOO0OO0OO =OO0OOO0OOOO0OO0OO [(OO0OOO0OOOO0OO0OO [O0OO0000OOOOO0OO0 ]==OO00OO0OOO0000000 )]#line:4066
                if O0OO000OOO000O0O0 =="不等于"and OOOOOO0O0O0O000O0 !={}:#line:4068
                    for O0OO0000OOOOO0OO0 ,OO00OO0OOO0000000 in OOOOOO0O0O0O000O0 .items ():#line:4069
                        if OO00OO0OOO0000000 !="-未定义-":#line:4070
                            OO0OOO0OOOO0OO0OO =OO0OOO0OOOO0OO0OO [(OO0OOO0OOOO0OO0OO [O0OO0000OOOOO0OO0 ]!=OO00OO0OOO0000000 )]#line:4071
                if O0OO000OOO000O0O0 =="包含"and OOOOOO0O0O0O000O0 !={}:#line:4073
                    for O0OO0000OOOOO0OO0 ,OO00OO0OOO0000000 in OOOOOO0O0O0O000O0 .items ():#line:4074
                        if OO00OO0OOO0000000 !="-未定义-":#line:4075
                            OO0OOO0OOOO0OO0OO =OO0OOO0OOOO0OO0OO .loc [OO0OOO0OOOO0OO0OO [O0OO0000OOOOO0OO0 ].str .contains (OO00OO0OOO0000000 ,na =False )]#line:4076
                if O0OO000OOO000O0O0 =="不包含"and OOOOOO0O0O0O000O0 !={}:#line:4078
                    for O0OO0000OOOOO0OO0 ,OO00OO0OOO0000000 in OOOOOO0O0O0O000O0 .items ():#line:4079
                        if OO00OO0OOO0000000 !="-未定义-":#line:4080
                            OO0OOO0OOOO0OO0OO =OO0OOO0OOOO0OO0OO .loc [~OO0OOO0OOOO0OO0OO [O0OO0000OOOOO0OO0 ].str .contains (OO00OO0OOO0000000 ,na =False )]#line:4081
            TABLE_tree_Level_2 (OO0OOO0OOOO0OO0OO ,0 ,OO0OOO0OOOO0OO0OO )#line:4083
            return 0 #line:4084
    if ("关键字标记"in OOOOOO000O0OO0000 ["values"])and ("不良事件名称1"in OOOOOO000O0OO0000 ["values"]):#line:4087
            def O000O000OO0OOO00O (event =None ):#line:4088
                for O0O00OOOOOOOOO0O0 in O0O00O0OOOO00O0OO .selection ():#line:4089
                    OOOO0OO00OO000000 =O0O00O0OOOO00O0OO .item (O0O00OOOOOOOOO0O0 ,"values")#line:4090
                O0000O0O0OO0O0OOO =dict (zip (OO000000O0OOOO00O ,OOOO0OO00OO000000 ))#line:4091
                O0O0O0O0OO0OOOO00 =O0O00OOOOOOO0OO00 .copy ()#line:4092
                if ini ["模式"]=="器械":#line:4093
                    O0O0O0O0OO0OOOO00 ["关键字查找列"]=O0O0O0O0OO0OOOO00 ["器械故障表现"].astype (str )+O0O0O0O0OO0OOOO00 ["伤害表现"].astype (str )+O0O0O0O0OO0OOOO00 ["使用过程"].astype (str )+O0O0O0O0OO0OOOO00 ["事件原因分析描述"].astype (str )+O0O0O0O0OO0OOOO00 ["初步处置情况"].astype (str )#line:4094
                else :#line:4095
                    O0O0O0O0OO0OOOO00 ["关键字查找列"]=O0O0O0O0OO0OOOO00 ["器械故障表现"]#line:4096
                if "-其他关键字-"in str (O0000O0O0OO0O0OOO ["关键字标记"]):#line:4097
                    O0O0O0O0OO0OOOO00 =O0O0O0O0OO0OOOO00 .loc [~O0O0O0O0OO0OOOO00 ["关键字查找列"].str .contains (O0000O0O0OO0O0OOO ["关键字标记"],na =False )].copy ()#line:4098
                O0O0O0O0OO0OOOO00 =O0O0O0O0OO0OOOO00 [(O0O0O0O0OO0OOOO00 ["关键字查找列"].str .contains (O0000O0O0OO0O0OOO ["关键字标记"],na =False ))]#line:4100
                if str (O0000O0O0OO0O0OOO ["排除值"])!="没有排除值":#line:4101
                    O0O0O0O0OO0OOOO00 =O0O0O0O0OO0OOOO00 .loc [~O0O0O0O0OO0OOOO00 ["关键字查找列"].str .contains (O0000O0O0OO0O0OOO ["排除值"],na =False )]#line:4102
                OO0O0OOO00OO0OOOO =TOOLS_count_elements (O0O0O0O0OO0OOOO00 ,O0000O0O0OO0O0OOO ["关键字标记"],"关键字查找列")#line:4103
                TABLE_tree_Level_2 (OO0O0OOO00OO0OOOO ,1 ,O0O0O0O0OO0OOOO00 )#line:4104
            O00000OO0O0OO00O0 =Menu (O0OO0O000O0O0O00O ,tearoff =False ,)#line:4105
            O00000OO0O0OO00O0 .add_command (label ="表现具体细项",command =O000O000OO0OOO00O )#line:4106
            def O00000OOO00O0OO00 (O0OO0OOOOOO0OO000 ):#line:4107
                O00000OO0O0OO00O0 .post (O0OO0OOOOOO0OO000 .x_root ,O0OO0OOOOOO0OO000 .y_root )#line:4108
            O0OO0O000O0O0O00O .bind ("<Button-3>",O00000OOO00O0OO00 )#line:4109
    try :#line:4113
        if OO0000OO00OOO0O00 [1 ]=="dfx_zhenghao":#line:4114
            O000O0O00OO00OOO0 ="dfx_zhenghao"#line:4115
            O00OOO0000O00OO0O =""#line:4116
    except :#line:4117
            O000O0O00OO00OOO0 =""#line:4118
            O00OOO0000O00OO0O ="近一年"#line:4119
    if (("总体评分"in OOOOOO000O0OO0000 ["values"])and ("高峰批号均值"in OOOOOO000O0OO0000 ["values"])and ("月份均值"in OOOOOO000O0OO0000 ["values"]))or O000O0O00OO00OOO0 =="dfx_zhenghao":#line:4121
            def OO00OO00000O00O0O (event =None ):#line:4124
                for O000O000OO0000OOO in O0O00O0OOOO00O0OO .selection ():#line:4125
                    O0000O000O0O00OO0 =O0O00O0OOOO00O0OO .item (O000O000OO0000OOO ,"values")#line:4126
                O0OOO0O0O0O0O0O00 =dict (zip (OO000000O0OOOO00O ,O0000O000O0O00OO0 ))#line:4127
                O00OOO0OOOO00OOOO =O0O00OOOOOOO0OO00 [(O0O00OOOOOOO0OO00 ["注册证编号/曾用注册证编号"]==O0OOO0O0O0O0O0O00 ["注册证编号/曾用注册证编号"])].copy ()#line:4128
                O00OOO0OOOO00OOOO ["报表类型"]=O0OOO0O0O0O0O0O00 ["报表类型"]+"1"#line:4129
                TABLE_tree_Level_2 (O00OOO0OOOO00OOOO ,1 ,O0O00OOOOOOO0OO00 )#line:4130
            def O0O0O0OO00OOO0OO0 (event =None ):#line:4131
                for O0OOO00O0OO0OOOO0 in O0O00O0OOOO00O0OO .selection ():#line:4132
                    O0OOOOOO00O00OOO0 =O0O00O0OOOO00O0OO .item (O0OOO00O0OO0OOOO0 ,"values")#line:4133
                O0O0O0OO00O0OO0O0 =dict (zip (OO000000O0OOOO00O ,O0OOOOOO00O00OOO0 ))#line:4134
                O0O00O0O0O000OO0O =OO0000OO00OOO0O00 [0 ][(OO0000OO00OOO0O00 [0 ]["注册证编号/曾用注册证编号"]==O0O0O0OO00O0OO0O0 ["注册证编号/曾用注册证编号"])].copy ()#line:4135
                O0O00O0O0O000OO0O ["报表类型"]=O0O0O0OO00O0OO0O0 ["报表类型"]+"1"#line:4136
                TABLE_tree_Level_2 (O0O00O0O0O000OO0O ,1 ,OO0000OO00OOO0O00 [0 ])#line:4137
            def OO0000OOO0OOO0O0O (O0O000O0OO0O0O0OO ):#line:4138
                for O0O000OO0000O00OO in O0O00O0OOOO00O0OO .selection ():#line:4139
                    O0000O0OO0000O00O =O0O00O0OOOO00O0OO .item (O0O000OO0000O00OO ,"values")#line:4140
                O0O0O00O0O00OO000 =dict (zip (OO000000O0OOOO00O ,O0000O0OO0000O00O ))#line:4141
                O0O0O0000OOO00000 =O0O00OOOOOOO0OO00 [(O0O00OOOOOOO0OO00 ["注册证编号/曾用注册证编号"]==O0O0O00O0O00OO000 ["注册证编号/曾用注册证编号"])].copy ()#line:4144
                O0O0O0000OOO00000 ["报表类型"]=O0O0O00O0O00OO000 ["报表类型"]+"1"#line:4145
                OOOO0O0O00OOOO0O0 =Countall (O0O0O0000OOO00000 ).df_psur (O0O000O0OO0O0O0OO ,O0O0O00O0O00OO000 ["规整后品类"])[["关键字标记","总数量","严重比"]]#line:4146
                OOOO0O0O00OOOO0O0 =OOOO0O0O00OOOO0O0 .rename (columns ={"总数量":"最近30天总数量"})#line:4147
                OOOO0O0O00OOOO0O0 =OOOO0O0O00OOOO0O0 .rename (columns ={"严重比":"最近30天严重比"})#line:4148
                O0O0O0000OOO00000 =OO0000OO00OOO0O00 [0 ][(OO0000OO00OOO0O00 [0 ]["注册证编号/曾用注册证编号"]==O0O0O00O0O00OO000 ["注册证编号/曾用注册证编号"])].copy ()#line:4150
                O0O0O0000OOO00000 ["报表类型"]=O0O0O00O0O00OO000 ["报表类型"]+"1"#line:4151
                O0OOO0000O000O000 =Countall (O0O0O0000OOO00000 ).df_psur (O0O000O0OO0O0O0OO ,O0O0O00O0O00OO000 ["规整后品类"])#line:4152
                OOO000OO0000OOOOO =pd .merge (O0OOO0000O000O000 ,OOOO0O0O00OOOO0O0 ,on ="关键字标记",how ="left")#line:4154
                del OOO000OO0000OOOOO ["报表类型"]#line:4155
                OOO000OO0000OOOOO ["报表类型"]="PSUR"#line:4156
                TABLE_tree_Level_2 (OOO000OO0000OOOOO ,1 ,O0O0O0000OOO00000 )#line:4158
            def O0O0000O0OOO0O00O (OO0OO00O00OOO00O0 ):#line:4161
                for O0000OOOO0OO000OO in O0O00O0OOOO00O0OO .selection ():#line:4162
                    OO0OOO0O0O0OO0O00 =O0O00O0OOOO00O0OO .item (O0000OOOO0OO000OO ,"values")#line:4163
                O00O0O0O0O000OOO0 =dict (zip (OO000000O0OOOO00O ,OO0OOO0O0O0OO0O00 ))#line:4164
                O00OOO0OO0000O000 =OO0000OO00OOO0O00 [0 ]#line:4165
                if O00O0O0O0O000OOO0 ["规整后品类"]=="N":#line:4166
                    if OO0OO00O00OOO00O0 =="特定品种":#line:4167
                        showinfo (title ="关于",message ="未能适配该品种规则，可能未制定或者数据规整不完善。")#line:4168
                        return 0 #line:4169
                    O00OOO0OO0000O000 =O00OOO0OO0000O000 .loc [O00OOO0OO0000O000 ["产品名称"].str .contains (O00O0O0O0O000OOO0 ["产品名称"],na =False )].copy ()#line:4170
                else :#line:4171
                    O00OOO0OO0000O000 =O00OOO0OO0000O000 .loc [O00OOO0OO0000O000 ["规整后品类"].str .contains (O00O0O0O0O000OOO0 ["规整后品类"],na =False )].copy ()#line:4172
                O00OOO0OO0000O000 =O00OOO0OO0000O000 .loc [O00OOO0OO0000O000 ["产品类别"].str .contains (O00O0O0O0O000OOO0 ["产品类别"],na =False )].copy ()#line:4173
                O00OOO0OO0000O000 ["报表类型"]=O00O0O0O0O000OOO0 ["报表类型"]+"1"#line:4175
                if OO0OO00O00OOO00O0 =="特定品种":#line:4176
                    TABLE_tree_Level_2 (Countall (O00OOO0OO0000O000 ).df_ror (["产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号"],O00O0O0O0O000OOO0 ["规整后品类"],O00O0O0O0O000OOO0 ["注册证编号/曾用注册证编号"]),1 ,O00OOO0OO0000O000 )#line:4177
                else :#line:4178
                    TABLE_tree_Level_2 (Countall (O00OOO0OO0000O000 ).df_ror (["产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号"],OO0OO00O00OOO00O0 ,O00O0O0O0O000OOO0 ["注册证编号/曾用注册证编号"]),1 ,O00OOO0OO0000O000 )#line:4179
            def O0O00OOO0O0OO0O00 (event =None ):#line:4181
                for OOOO00OOO0OOO00O0 in O0O00O0OOOO00O0OO .selection ():#line:4182
                    OOO0O000O00OOO000 =O0O00O0OOOO00O0OO .item (OOOO00OOO0OOO00O0 ,"values")#line:4183
                OOO0O0O0O000OOO00 =dict (zip (OO000000O0OOOO00O ,OOO0O000O00OOO000 ))#line:4184
                OO00O00O00OO0000O =OO0000OO00OOO0O00 [0 ][(OO0000OO00OOO0O00 [0 ]["注册证编号/曾用注册证编号"]==OOO0O0O0O000OOO00 ["注册证编号/曾用注册证编号"])].copy ()#line:4185
                OO00O00O00OO0000O ["报表类型"]=OOO0O0O0O000OOO00 ["报表类型"]+"1"#line:4186
                TABLE_tree_Level_2 (Countall (OO00O00O00OO0000O ).df_pihao (),1 ,OO00O00O00OO0000O ,)#line:4191
            def OOOO0000OOO00OO00 (event =None ):#line:4193
                for OO0O00OOO0OOOO00O in O0O00O0OOOO00O0OO .selection ():#line:4194
                    O000OO0OO00O0O0O0 =O0O00O0OOOO00O0OO .item (OO0O00OOO0OOOO00O ,"values")#line:4195
                O0O0OO00O0OO00O00 =dict (zip (OO000000O0OOOO00O ,O000OO0OO00O0O0O0 ))#line:4196
                OOO0O00OOO0OOO0OO =OO0000OO00OOO0O00 [0 ][(OO0000OO00OOO0O00 [0 ]["注册证编号/曾用注册证编号"]==O0O0OO00O0OO00O00 ["注册证编号/曾用注册证编号"])].copy ()#line:4197
                OOO0O00OOO0OOO0OO ["报表类型"]=O0O0OO00O0OO00O00 ["报表类型"]+"1"#line:4198
                TABLE_tree_Level_2 (Countall (OOO0O00OOO0OOO0OO ).df_xinghao (),1 ,OOO0O00OOO0OOO0OO ,)#line:4203
            def OO0000O0OO0OOOOOO (event =None ):#line:4205
                for O00OOOO0O0000OO0O in O0O00O0OOOO00O0OO .selection ():#line:4206
                    OO0O0OO000OOO0000 =O0O00O0OOOO00O0OO .item (O00OOOO0O0000OO0O ,"values")#line:4207
                O0OO000O00OO0000O =dict (zip (OO000000O0OOOO00O ,OO0O0OO000OOO0000 ))#line:4208
                O0000OO000OOOOO0O =OO0000OO00OOO0O00 [0 ][(OO0000OO00OOO0O00 [0 ]["注册证编号/曾用注册证编号"]==O0OO000O00OO0000O ["注册证编号/曾用注册证编号"])].copy ()#line:4209
                O0000OO000OOOOO0O ["报表类型"]=O0OO000O00OO0000O ["报表类型"]+"1"#line:4210
                TABLE_tree_Level_2 (Countall (O0000OO000OOOOO0O ).df_user (),1 ,O0000OO000OOOOO0O ,)#line:4215
            def OOOOOOOO00000O0OO (event =None ):#line:4217
                for OO00000O0O00O0O0O in O0O00O0OOOO00O0OO .selection ():#line:4219
                    O0O0OO00O0O00O0O0 =O0O00O0OOOO00O0OO .item (OO00000O0O00O0O0O ,"values")#line:4220
                O0OOO000O000OOO00 =dict (zip (OO000000O0OOOO00O ,O0O0OO00O0O00O0O0 ))#line:4221
                OOOO0000O0000OOOO =OO0000OO00OOO0O00 [0 ][(OO0000OO00OOO0O00 [0 ]["注册证编号/曾用注册证编号"]==O0OOO000O000OOO00 ["注册证编号/曾用注册证编号"])].copy ()#line:4222
                OOOO0000O0000OOOO ["报表类型"]=O0OOO000O000OOO00 ["报表类型"]+"1"#line:4223
                OOO00O0OO00O0O000 =pd .read_excel (peizhidir +"0（范例）预警参数.xlsx",header =0 ,sheet_name =0 ).reset_index (drop =True )#line:4224
                if ini ["模式"]=="药品":#line:4225
                    OOO00O0OO00O0O000 =pd .read_excel (peizhidir +"0（范例）预警参数.xlsx",header =0 ,sheet_name ="药品").reset_index (drop =True )#line:4226
                if ini ["模式"]=="器械":#line:4227
                    OOO00O0OO00O0O000 =pd .read_excel (peizhidir +"0（范例）预警参数.xlsx",header =0 ,sheet_name ="器械").reset_index (drop =True )#line:4228
                if ini ["模式"]=="化妆品":#line:4229
                    OOO00O0OO00O0O000 =pd .read_excel (peizhidir +"0（范例）预警参数.xlsx",header =0 ,sheet_name ="化妆品").reset_index (drop =True )#line:4230
                O0OO0OOOOOOO0O0O0 =OOO00O0OO00O0O000 ["值"][3 ]+"|"+OOO00O0OO00O0O000 ["值"][4 ]#line:4231
                if ini ["模式"]=="器械":#line:4232
                    OOOO0000O0000OOOO ["关键字查找列"]=OOOO0000O0000OOOO ["器械故障表现"].astype (str )+OOOO0000O0000OOOO ["伤害表现"].astype (str )+OOOO0000O0000OOOO ["使用过程"].astype (str )+OOOO0000O0000OOOO ["事件原因分析描述"].astype (str )+OOOO0000O0000OOOO ["初步处置情况"].astype (str )#line:4233
                else :#line:4234
                    OOOO0000O0000OOOO ["关键字查找列"]=OOOO0000O0000OOOO ["器械故障表现"].astype (str )#line:4235
                OOOO0000O0000OOOO =OOOO0000O0000OOOO .loc [OOOO0000O0000OOOO ["关键字查找列"].str .contains (O0OO0OOOOOOO0O0O0 ,na =False )].copy ().reset_index (drop =True )#line:4236
                TABLE_tree_Level_2 (OOOO0000O0000OOOO ,0 ,OOOO0000O0000OOOO ,)#line:4242
            def O00O0OOOO0OOO0O00 (event =None ):#line:4245
                for OO0OOOOO00O00OO00 in O0O00O0OOOO00O0OO .selection ():#line:4246
                    OOOOOO0O0O000OO00 =O0O00O0OOOO00O0OO .item (OO0OOOOO00O00OO00 ,"values")#line:4247
                O00O00000O00000O0 =dict (zip (OO000000O0OOOO00O ,OOOOOO0O0O000OO00 ))#line:4248
                OO000000OO000O0O0 =OO0000OO00OOO0O00 [0 ][(OO0000OO00OOO0O00 [0 ]["注册证编号/曾用注册证编号"]==O00O00000O00000O0 ["注册证编号/曾用注册证编号"])].copy ()#line:4249
                OO000000OO000O0O0 ["报表类型"]=O00O00000O00000O0 ["报表类型"]+"1"#line:4250
                TOOLS_time (OO000000OO000O0O0 ,"事件发生日期",0 )#line:4251
            def OO00OOOOOOO000OOO (OOOO000O00OOOOOOO ,OOO000O00O00O0OO0 ):#line:4253
                for O00O000O00O00O00O in O0O00O0OOOO00O0OO .selection ():#line:4255
                    O000O0O0O0OOO000O =O0O00O0OOOO00O0OO .item (O00O000O00O00O00O ,"values")#line:4256
                O000O000O0OO0OO00 =dict (zip (OO000000O0OOOO00O ,O000O0O0O0OOO000O ))#line:4257
                OOO000000OO00OOOO =OO0000OO00OOO0O00 [0 ]#line:4258
                if O000O000O0OO0OO00 ["规整后品类"]=="N":#line:4259
                    if OOOO000O00OOOOOOO =="特定品种":#line:4260
                        showinfo (title ="关于",message ="未能适配该品种规则，可能未制定或者数据规整不完善。")#line:4261
                        return 0 #line:4262
                OOO000000OO00OOOO =OOO000000OO00OOOO .loc [OOO000000OO00OOOO ["注册证编号/曾用注册证编号"].str .contains (O000O000O0OO0OO00 ["注册证编号/曾用注册证编号"],na =False )].copy ()#line:4263
                OOO000000OO00OOOO ["报表类型"]=O000O000O0OO0OO00 ["报表类型"]+"1"#line:4264
                if OOOO000O00OOOOOOO =="特定品种":#line:4265
                    TABLE_tree_Level_2 (Countall (OOO000000OO00OOOO ).df_find_all_keword_risk (OOO000O00O00O0OO0 ,O000O000O0OO0OO00 ["规整后品类"]),1 ,OOO000000OO00OOOO )#line:4266
                else :#line:4267
                    TABLE_tree_Level_2 (Countall (OOO000000OO00OOOO ).df_find_all_keword_risk (OOO000O00O00O0OO0 ,OOOO000O00OOOOOOO ),1 ,OOO000000OO00OOOO )#line:4268
            O00000OO0O0OO00O0 =Menu (O0OO0O000O0O0O00O ,tearoff =False ,)#line:4272
            O00000OO0O0OO00O0 .add_command (label =O00OOO0000O00OO0O +"故障表现分类（无源）",command =lambda :OO0000OOO0OOO0O0O ("通用无源"))#line:4273
            O00000OO0O0OO00O0 .add_command (label =O00OOO0000O00OO0O +"故障表现分类（有源）",command =lambda :OO0000OOO0OOO0O0O ("通用有源"))#line:4274
            O00000OO0O0OO00O0 .add_command (label =O00OOO0000O00OO0O +"故障表现分类（特定品种）",command =lambda :OO0000OOO0OOO0O0O ("特定品种"))#line:4275
            O00000OO0O0OO00O0 .add_separator ()#line:4277
            if O000O0O00OO00OOO0 =="":#line:4278
                O00000OO0O0OO00O0 .add_command (label =O00OOO0000O00OO0O +"同类比较(ROR-无源)",command =lambda :O0O0000O0OOO0O00O ("无源"))#line:4279
                O00000OO0O0OO00O0 .add_command (label =O00OOO0000O00OO0O +"同类比较(ROR-有源)",command =lambda :O0O0000O0OOO0O00O ("有源"))#line:4280
                O00000OO0O0OO00O0 .add_command (label =O00OOO0000O00OO0O +"同类比较(ROR-特定品种)",command =lambda :O0O0000O0OOO0O00O ("特定品种"))#line:4281
            O00000OO0O0OO00O0 .add_separator ()#line:4283
            O00000OO0O0OO00O0 .add_command (label =O00OOO0000O00OO0O +"关键字趋势(批号-无源)",command =lambda :OO00OOOOOOO000OOO ("无源","产品批号"))#line:4284
            O00000OO0O0OO00O0 .add_command (label =O00OOO0000O00OO0O +"关键字趋势(批号-特定品种)",command =lambda :OO00OOOOOOO000OOO ("特定品种","产品批号"))#line:4285
            O00000OO0O0OO00O0 .add_command (label =O00OOO0000O00OO0O +"关键字趋势(月份-无源)",command =lambda :OO00OOOOOOO000OOO ("无源","事件发生月份"))#line:4286
            O00000OO0O0OO00O0 .add_command (label =O00OOO0000O00OO0O +"关键字趋势(月份-有源)",command =lambda :OO00OOOOOOO000OOO ("有源","事件发生月份"))#line:4287
            O00000OO0O0OO00O0 .add_command (label =O00OOO0000O00OO0O +"关键字趋势(月份-特定品种)",command =lambda :OO00OOOOOOO000OOO ("特定品种","事件发生月份"))#line:4288
            O00000OO0O0OO00O0 .add_command (label =O00OOO0000O00OO0O +"关键字趋势(季度-无源)",command =lambda :OO00OOOOOOO000OOO ("无源","事件发生季度"))#line:4289
            O00000OO0O0OO00O0 .add_command (label =O00OOO0000O00OO0O +"关键字趋势(季度-有源)",command =lambda :OO00OOOOOOO000OOO ("有源","事件发生季度"))#line:4290
            O00000OO0O0OO00O0 .add_command (label =O00OOO0000O00OO0O +"关键字趋势(季度-特定品种)",command =lambda :OO00OOOOOOO000OOO ("特定品种","事件发生季度"))#line:4291
            O00000OO0O0OO00O0 .add_separator ()#line:4293
            O00000OO0O0OO00O0 .add_command (label =O00OOO0000O00OO0O +"各批号报送情况",command =O0O00OOO0O0OO0O00 )#line:4294
            O00000OO0O0OO00O0 .add_command (label =O00OOO0000O00OO0O +"各型号报送情况",command =OOOO0000OOO00OO00 )#line:4295
            O00000OO0O0OO00O0 .add_command (label =O00OOO0000O00OO0O +"报告单位情况",command =OO0000O0OO0OOOOOO )#line:4296
            O00000OO0O0OO00O0 .add_command (label =O00OOO0000O00OO0O +"事件发生时间曲线",command =O00O0OOOO0OOO0O00 )#line:4297
            O00000OO0O0OO00O0 .add_separator ()#line:4298
            O00000OO0O0OO00O0 .add_command (label =O00OOO0000O00OO0O +"原始数据",command =O0O0O0OO00OOO0OO0 )#line:4299
            if O000O0O00OO00OOO0 =="":#line:4300
                O00000OO0O0OO00O0 .add_command (label ="近30天原始数据",command =OO00OO00000O00O0O )#line:4301
            O00000OO0O0OO00O0 .add_command (label =O00OOO0000O00OO0O +"高度关注(一级和二级)",command =OOOOOOOO00000O0OO )#line:4302
            def O00000OOO00O0OO00 (OO00O0O0OOOO0OOO0 ):#line:4304
                O00000OO0O0OO00O0 .post (OO00O0O0OOOO0OOO0 .x_root ,OO00O0O0OOOO0OOO0 .y_root )#line:4305
            O0OO0O000O0O0O00O .bind ("<Button-3>",O00000OOO00O0OO00 )#line:4306
    if OO0OOOOO0O00OO0OO ==0 or "规整编码"in OO0OO0OOO0O0OOO00 .columns :#line:4309
        O0O00O0OOOO00O0OO .bind ("<Double-1>",lambda OO0O0O000O0OOO0O0 :O000O0O0OO00OOOOO (OO0O0O000O0OOO0O0 ,OO0OO0OOO0O0OOO00 ))#line:4310
    if OO0OOOOO0O00OO0OO ==1 and "规整编码"not in OO0OO0OOO0O0OOO00 .columns :#line:4311
        O0O00O0OOOO00O0OO .bind ("<Double-1>",lambda O00O000OOOOOO00O0 :OO0O0O00O0OOO0OOO (O00O000OOOOOO00O0 ,OO000000O0OOOO00O ,O0O00OOOOOOO0OO00 ))#line:4312
    def OO000O00OOO0000OO (O00OO0OOOOOOO0OOO ,OOOOO0OOO00O00000 ,O0O0OO00OO0OOOO00 ):#line:4315
        O000OOOO0OOOOOO00 =[(O00OO0OOOOOOO0OOO .set (O00O00O0O0O0O00OO ,OOOOO0OOO00O00000 ),O00O00O0O0O0O00OO )for O00O00O0O0O0O00OO in O00OO0OOOOOOO0OOO .get_children ("")]#line:4316
        O000OOOO0OOOOOO00 .sort (reverse =O0O0OO00OO0OOOO00 )#line:4317
        for O0O00O000OOO00OOO ,(OOO00OO0OOOOOOO00 ,O000OO00O0O000O0O )in enumerate (O000OOOO0OOOOOO00 ):#line:4319
            O00OO0OOOOOOO0OOO .move (O000OO00O0O000O0O ,"",O0O00O000OOO00OOO )#line:4320
        O00OO0OOOOOOO0OOO .heading (OOOOO0OOO00O00000 ,command =lambda :OO000O00OOO0000OO (O00OO0OOOOOOO0OOO ,OOOOO0OOO00O00000 ,not O0O0OO00OO0OOOO00 ))#line:4323
    for O0O0OO0OO00OOOO00 in OO000000O0OOOO00O :#line:4325
        O0O00O0OOOO00O0OO .heading (O0O0OO0OO00OOOO00 ,text =O0O0OO0OO00OOOO00 ,command =lambda _col =O0O0OO0OO00OOOO00 :OO000O00OOO0000OO (O0O00O0OOOO00O0OO ,_col ,False ),)#line:4330
    def O000O0O0OO00OOOOO (O0000OO000OOOO000 ,OO0OO000O00O000OO ):#line:4334
        if "规整编码"in OO0OO000O00O000OO .columns :#line:4336
            OO0OO000O00O000OO =OO0OO000O00O000OO .rename (columns ={"规整编码":"报告编码"})#line:4337
        for OO00OOOOOOO0O0000 in O0O00O0OOOO00O0OO .selection ():#line:4339
            O0OOO0O0000OOOO0O =O0O00O0OOOO00O0OO .item (OO00OOOOOOO0O0000 ,"values")#line:4340
            OOO0000OO0OOO0OO0 =Toplevel ()#line:4343
            O0OOO0O0OO0O00O00 =OOO0000OO0OOO0OO0 .winfo_screenwidth ()#line:4345
            O0000O0O0O0OOOO00 =OOO0000OO0OOO0OO0 .winfo_screenheight ()#line:4347
            O0O0000000O00OO00 =800 #line:4349
            OO0O0O0O000O0O0O0 =600 #line:4350
            OOO000O0OO0O00OO0 =(O0OOO0O0OO0O00O00 -O0O0000000O00OO00 )/2 #line:4352
            O000000O0OO000O0O =(O0000O0O0O0OOOO00 -OO0O0O0O000O0O0O0 )/2 #line:4353
            OOO0000OO0OOO0OO0 .geometry ("%dx%d+%d+%d"%(O0O0000000O00OO00 ,OO0O0O0O000O0O0O0 ,OOO000O0OO0O00OO0 ,O000000O0OO000O0O ))#line:4354
            O0OO0OO0O0O0OO0OO =ScrolledText (OOO0000OO0OOO0OO0 ,height =1100 ,width =1100 ,bg ="#FFFFFF")#line:4358
            O0OO0OO0O0O0OO0OO .pack (padx =10 ,pady =10 )#line:4359
            def O0OOO000O0OOOOO0O (event =None ):#line:4360
                O0OO0OO0O0O0OO0OO .event_generate ('<<Copy>>')#line:4361
            def OO00OO00O0O00O00O (OO000000OO00OOOO0 ,O00000O0O0O0O0OOO ):#line:4362
                TOOLS_savetxt (OO000000OO00OOOO0 ,O00000O0O0O0O0OOO ,1 )#line:4363
            OO0000000OOO0000O =Menu (O0OO0OO0O0O0OO0OO ,tearoff =False ,)#line:4364
            OO0000000OOO0000O .add_command (label ="复制",command =O0OOO000O0OOOOO0O )#line:4365
            OO0000000OOO0000O .add_command (label ="导出",command =lambda :PROGRAM_thread_it (OO00OO00O0O00O00O ,O0OO0OO0O0O0OO0OO .get (1.0 ,'end'),filedialog .asksaveasfilename (title =u"保存文件",initialfile =OO0OO000O00O000OO .iloc [0 ,0 ],defaultextension ="txt",filetypes =[("txt","*.txt")])))#line:4366
            def OO00O0000OO0O0O0O (OO0O00O00OOO000O0 ):#line:4368
                OO0000000OOO0000O .post (OO0O00O00OOO000O0 .x_root ,OO0O00O00OOO000O0 .y_root )#line:4369
            O0OO0OO0O0O0OO0OO .bind ("<Button-3>",OO00O0000OO0O0O0O )#line:4370
            try :#line:4372
                OOO0000OO0OOO0OO0 .title (str (O0OOO0O0000OOOO0O [0 ]))#line:4373
                OO0OO000O00O000OO ["报告编码"]=OO0OO000O00O000OO ["报告编码"].astype ("str")#line:4374
                OOOOOO0OOO000000O =OO0OO000O00O000OO [(OO0OO000O00O000OO ["报告编码"]==str (O0OOO0O0000OOOO0O [0 ]))]#line:4375
            except :#line:4376
                pass #line:4377
            OOOO0000OOOO0OO00 =OO0OO000O00O000OO .columns .values .tolist ()#line:4379
            for OO0000OOO000OO0O0 in range (len (OOOO0000OOOO0OO00 )):#line:4380
                try :#line:4382
                    if OOOO0000OOOO0OO00 [OO0000OOO000OO0O0 ]=="报告编码.1":#line:4383
                        O0OO0OO0O0O0OO0OO .insert (END ,"\n\n")#line:4384
                    if OOOO0000OOOO0OO00 [OO0000OOO000OO0O0 ]=="产品名称":#line:4385
                        O0OO0OO0O0O0OO0OO .insert (END ,"\n\n")#line:4386
                    if OOOO0000OOOO0OO00 [OO0000OOO000OO0O0 ]=="事件发生日期":#line:4387
                        O0OO0OO0O0O0OO0OO .insert (END ,"\n\n")#line:4388
                    if OOOO0000OOOO0OO00 [OO0000OOO000OO0O0 ]=="是否开展了调查":#line:4389
                        O0OO0OO0O0O0OO0OO .insert (END ,"\n\n")#line:4390
                    if OOOO0000OOOO0OO00 [OO0000OOO000OO0O0 ]=="市级监测机构":#line:4391
                        O0OO0OO0O0O0OO0OO .insert (END ,"\n\n")#line:4392
                    if OOOO0000OOOO0OO00 [OO0000OOO000OO0O0 ]=="上报机构描述":#line:4393
                        O0OO0OO0O0O0OO0OO .insert (END ,"\n\n")#line:4394
                    if OOOO0000OOOO0OO00 [OO0000OOO000OO0O0 ]=="持有人处理描述":#line:4395
                        O0OO0OO0O0O0OO0OO .insert (END ,"\n\n")#line:4396
                    if OO0000OOO000OO0O0 >1 and OOOO0000OOOO0OO00 [OO0000OOO000OO0O0 -1 ]=="持有人处理描述":#line:4397
                        O0OO0OO0O0O0OO0OO .insert (END ,"\n\n")#line:4398
                except :#line:4400
                    pass #line:4401
                try :#line:4402
                    if OOOO0000OOOO0OO00 [OO0000OOO000OO0O0 ]in ["单位名称","产品名称ori","上报机构描述","持有人处理描述","产品名称","注册证编号/曾用注册证编号","型号","规格","产品批号","上市许可持有人名称ori","上市许可持有人名称","伤害","伤害表现","器械故障表现","使用过程","事件原因分析描述","初步处置情况","调查情况","关联性评价","事件原因分析.1","具体控制措施"]:#line:4403
                        O0OO0OO0O0O0OO0OO .insert (END ,"●")#line:4404
                except :#line:4405
                    pass #line:4406
                O0OO0OO0O0O0OO0OO .insert (END ,OOOO0000OOOO0OO00 [OO0000OOO000OO0O0 ])#line:4407
                O0OO0OO0O0O0OO0OO .insert (END ,"：")#line:4408
                try :#line:4409
                    O0OO0OO0O0O0OO0OO .insert (END ,OOOOOO0OOO000000O .iloc [0 ,OO0000OOO000OO0O0 ])#line:4410
                except :#line:4411
                    O0OO0OO0O0O0OO0OO .insert (END ,O0OOO0O0000OOOO0O [OO0000OOO000OO0O0 ])#line:4412
                O0OO0OO0O0O0OO0OO .insert (END ,"\n")#line:4413
            O0OO0OO0O0O0OO0OO .config (state =DISABLED )#line:4414
    O0O00O0OOOO00O0OO .pack ()#line:4416
def TOOLS_get_guize2 (O0OOO0000000OO00O ):#line:4419
	""#line:4420
	O0OOO0OOOOO0O00O0 =peizhidir +"0（范例）比例失衡关键字库.xls"#line:4421
	OOO0O0OOO0O000OOO =pd .read_excel (O0OOO0OOOOO0O00O0 ,header =0 ,sheet_name ="器械")#line:4422
	O000O0OO0O0000O0O =OOO0O0OOO0O000OOO [["适用范围列","适用范围"]].drop_duplicates ("适用范围")#line:4423
	text .insert (END ,O000O0OO0O0000O0O )#line:4424
	text .see (END )#line:4425
	O0OOO00OO00000O0O =Toplevel ()#line:4426
	O0OOO00OO00000O0O .title ('切换通用规则')#line:4427
	OOO00O00O0O000O0O =O0OOO00OO00000O0O .winfo_screenwidth ()#line:4428
	OO0OOOO00OOOO0O0O =O0OOO00OO00000O0O .winfo_screenheight ()#line:4430
	OOO0O00O0OOO0O0OO =450 #line:4432
	O0O00OOOO00O00000 =100 #line:4433
	OOOO0OOOOO0OOO0O0 =(OOO00O00O0O000O0O -OOO0O00O0OOO0O0OO )/2 #line:4435
	O00O0000O000OOO0O =(OO0OOOO00OOOO0O0O -O0O00OOOO00O00000 )/2 #line:4436
	O0OOO00OO00000O0O .geometry ("%dx%d+%d+%d"%(OOO0O00O0OOO0O0OO ,O0O00OOOO00O00000 ,OOOO0OOOOO0OOO0O0 ,O00O0000O000OOO0O ))#line:4437
	OOOO0OOOOOOO0OO0O =Label (O0OOO00OO00000O0O ,text ="查找位置：器械故障表现+伤害表现+使用过程+事件原因分析描述+初步处置情况")#line:4438
	OOOO0OOOOOOO0OO0O .pack ()#line:4439
	OOO0OO00O0O00OOOO =Label (O0OOO00OO00000O0O ,text ="请选择您所需要的通用规则关键字：")#line:4440
	OOO0OO00O0O00OOOO .pack ()#line:4441
	def O0OO0OOO000OOOO0O (*O0000000O00000O00 ):#line:4442
		O0OO0OOO000O0OOOO .set (O000OO0O0OO00O0O0 .get ())#line:4443
	O0OO0OOO000O0OOOO =StringVar ()#line:4444
	O000OO0O0OO00O0O0 =ttk .Combobox (O0OOO00OO00000O0O ,width =14 ,height =30 ,state ="readonly",textvariable =O0OO0OOO000O0OOOO )#line:4445
	O000OO0O0OO00O0O0 ["values"]=O000O0OO0O0000O0O ["适用范围"].to_list ()#line:4446
	O000OO0O0OO00O0O0 .current (0 )#line:4447
	O000OO0O0OO00O0O0 .bind ("<<ComboboxSelected>>",O0OO0OOO000OOOO0O )#line:4448
	O000OO0O0OO00O0O0 .pack ()#line:4449
	O000O0000O0OO0OOO =LabelFrame (O0OOO00OO00000O0O )#line:4452
	O0O0OO0OOO0O0OOOO =Button (O000O0000O0OO0OOO ,text ="确定",width =10 ,command =lambda :OOOOOOO00OO00OO00 (OOO0O0OOO0O000OOO ,O0OO0OOO000O0OOOO .get ()))#line:4453
	O0O0OO0OOO0O0OOOO .pack (side =LEFT ,padx =1 ,pady =1 )#line:4454
	O000O0000O0OO0OOO .pack ()#line:4455
	def OOOOOOO00OO00OO00 (OOOO0O0O0OO00O0OO ,OO000000OOOO0O0O0 ):#line:4457
		OOO0OOOOO000OO0O0 =OOOO0O0O0OO00O0OO .loc [OOOO0O0O0OO00O0OO ["适用范围"].str .contains (OO000000OOOO0O0O0 ,na =False )].copy ().reset_index (drop =True )#line:4458
		TABLE_tree_Level_2 (Countall (O0OOO0000000OO00O ).df_psur ("特定品种作为通用关键字",OOO0OOOOO000OO0O0 ),1 ,O0OOO0000000OO00O )#line:4459
def TOOLS_findin (OOOOOOO0O000OOOOO ,OOO0O000OO000OO0O ):#line:4460
	""#line:4461
	O000OO0OOO00OO000 =Toplevel ()#line:4462
	O000OO0OOO00OO000 .title ('高级查找')#line:4463
	O000O0000O00O0OOO =O000OO0OOO00OO000 .winfo_screenwidth ()#line:4464
	OO0OOO000O0OO00O0 =O000OO0OOO00OO000 .winfo_screenheight ()#line:4466
	O000O0O0000000OOO =400 #line:4468
	OOO0000OOO0OO00OO =120 #line:4469
	OOOO000O00OOO0O0O =(O000O0000O00O0OOO -O000O0O0000000OOO )/2 #line:4471
	OO0OO00O000000O00 =(OO0OOO000O0OO00O0 -OOO0000OOO0OO00OO )/2 #line:4472
	O000OO0OOO00OO000 .geometry ("%dx%d+%d+%d"%(O000O0O0000000OOO ,OOO0000OOO0OO00OO ,OOOO000O00OOO0O0O ,OO0OO00O000000O00 ))#line:4473
	OO0OO00O00O00000O =Label (O000OO0OOO00OO000 ,text ="需要查找的关键字（用|隔开）：")#line:4474
	OO0OO00O00O00000O .pack ()#line:4475
	OOO0O00O000000OO0 =Label (O000OO0OOO00OO000 ,text ="在哪些列查找（用|隔开）：")#line:4476
	O0OO000000O0O0O00 =Entry (O000OO0OOO00OO000 ,width =80 )#line:4478
	O0OO000000O0O0O00 .insert (0 ,"破裂|断裂")#line:4479
	OO0O0OOO00000O000 =Entry (O000OO0OOO00OO000 ,width =80 )#line:4480
	OO0O0OOO00000O000 .insert (0 ,"器械故障表现|伤害表现")#line:4481
	O0OO000000O0O0O00 .pack ()#line:4482
	OOO0O00O000000OO0 .pack ()#line:4483
	OO0O0OOO00000O000 .pack ()#line:4484
	O0O00OOOO0O00OO0O =LabelFrame (O000OO0OOO00OO000 )#line:4485
	OOO0O000OO00OOO0O =Button (O0O00OOOO0O00OO0O ,text ="确定",width =10 ,command =lambda :PROGRAM_thread_it (TABLE_tree_Level_2 ,OO00O00O0O00000OO (O0OO000000O0O0O00 .get (),OO0O0OOO00000O000 .get (),OOOOOOO0O000OOOOO ),1 ,OOO0O000OO000OO0O ))#line:4486
	OOO0O000OO00OOO0O .pack (side =LEFT ,padx =1 ,pady =1 )#line:4487
	O0O00OOOO0O00OO0O .pack ()#line:4488
	def OO00O00O0O00000OO (OO0OO00O0OO0000OO ,OOO0OO0O00O0000O0 ,O0OOO0000OOO000O0 ):#line:4491
		O0OOO0000OOO000O0 ["关键字查找列10"]="######"#line:4492
		for O0OOO00OO0O00000O in TOOLS_get_list (OOO0OO0O00O0000O0 ):#line:4493
			O0OOO0000OOO000O0 ["关键字查找列10"]=O0OOO0000OOO000O0 ["关键字查找列10"].astype (str )+O0OOO0000OOO000O0 [O0OOO00OO0O00000O ].astype (str )#line:4494
		O0OOO0000OOO000O0 =O0OOO0000OOO000O0 .loc [O0OOO0000OOO000O0 ["关键字查找列10"].str .contains (OO0OO00O0OO0000OO ,na =False )]#line:4495
		del O0OOO0000OOO000O0 ["关键字查找列10"]#line:4496
		return O0OOO0000OOO000O0 #line:4497
def PROGRAM_about ():#line:4499
    ""#line:4500
    OOOO00OO0OO0OO00O =" 佛山市食品药品检验检测中心 \n(佛山市药品不良反应监测中心)\n蔡权周（QQ或微信411703730）\n仅供政府设立的不良反应监测机构使用。"#line:4501
    showinfo (title ="关于",message =OOOO00OO0OO0OO00O )#line:4502
def PROGRAM_thread_it (OOOO0OO0OO0OO0OOO ,*OOOOO000O0O0OO000 ):#line:4505
    ""#line:4506
    O0OO00OO0000O00O0 =threading .Thread (target =OOOO0OO0OO0OO0OOO ,args =OOOOO000O0O0OO000 )#line:4508
    O0OO00OO0000O00O0 .setDaemon (True )#line:4510
    O0OO00OO0000O00O0 .start ()#line:4512
def PROGRAM_Menubar (OOO0O000O00O0OO00 ,O0O0OOO0O00OO0O00 ,OO0000O0000OO000O ,OOO00OO0OOO00OOO0 ):#line:4513
	""#line:4514
	if ini ["模式"]=="其他":#line:4515
		return 0 #line:4516
	O0O00O00OO000O00O =Menu (OOO0O000O00O0OO00 )#line:4517
	OOO0O000O00O0OO00 .config (menu =O0O00O00OO000O00O )#line:4519
	O0000000OO0OO00OO =Menu (O0O00O00OO000O00O ,tearoff =0 )#line:4523
	O0O00O00OO000O00O .add_cascade (label ="信号检测",menu =O0000000OO0OO00OO )#line:4524
	O0000000OO0OO00OO .add_command (label ="数量比例失衡监测-证号内批号",command =lambda :TABLE_tree_Level_2 (Countall (O0O0OOO0O00OO0O00 ).df_findrisk ("产品批号"),1 ,OOO00OO0OOO00OOO0 ))#line:4527
	O0000000OO0OO00OO .add_command (label ="数量比例失衡监测-证号内季度",command =lambda :TABLE_tree_Level_2 (Countall (O0O0OOO0O00OO0O00 ).df_findrisk ("事件发生季度"),1 ,OOO00OO0OOO00OOO0 ))#line:4529
	O0000000OO0OO00OO .add_command (label ="数量比例失衡监测-证号内月份",command =lambda :TABLE_tree_Level_2 (Countall (O0O0OOO0O00OO0O00 ).df_findrisk ("事件发生月份"),1 ,OOO00OO0OOO00OOO0 ))#line:4531
	O0000000OO0OO00OO .add_command (label ="数量比例失衡监测-证号内性别",command =lambda :TABLE_tree_Level_2 (Countall (O0O0OOO0O00OO0O00 ).df_findrisk ("性别"),1 ,OOO00OO0OOO00OOO0 ))#line:4533
	O0000000OO0OO00OO .add_command (label ="数量比例失衡监测-证号内年龄段",command =lambda :TABLE_tree_Level_2 (Countall (O0O0OOO0O00OO0O00 ).df_findrisk ("年龄段"),1 ,OOO00OO0OOO00OOO0 ))#line:4535
	O0000000OO0OO00OO .add_separator ()#line:4537
	O0000000OO0OO00OO .add_command (label ="关键字检测（同证号内不同批号比对）",command =lambda :TABLE_tree_Level_2 (Countall (O0O0OOO0O00OO0O00 ).df_find_all_keword_risk ("产品批号"),1 ,OOO00OO0OOO00OOO0 ))#line:4539
	O0000000OO0OO00OO .add_command (label ="关键字检测（同证号内不同月份比对）",command =lambda :TABLE_tree_Level_2 (Countall (O0O0OOO0O00OO0O00 ).df_find_all_keword_risk ("事件发生月份"),1 ,OOO00OO0OOO00OOO0 ))#line:4541
	O0000000OO0OO00OO .add_command (label ="关键字检测（同证号内不同季度比对）",command =lambda :TABLE_tree_Level_2 (Countall (O0O0OOO0O00OO0O00 ).df_find_all_keword_risk ("事件发生季度"),1 ,OOO00OO0OOO00OOO0 ))#line:4543
	O0000000OO0OO00OO .add_command (label ="关键字检测（同证号内不同性别比对）",command =lambda :TABLE_tree_Level_2 (Countall (O0O0OOO0O00OO0O00 ).df_find_all_keword_risk ("性别"),1 ,OOO00OO0OOO00OOO0 ))#line:4545
	O0000000OO0OO00OO .add_command (label ="关键字检测（同证号内不同年龄段比对）",command =lambda :TABLE_tree_Level_2 (Countall (O0O0OOO0O00OO0O00 ).df_find_all_keword_risk ("年龄段"),1 ,OOO00OO0OOO00OOO0 ))#line:4547
	O0000000OO0OO00OO .add_separator ()#line:4549
	O0000000OO0OO00OO .add_command (label ="关键字ROR-页面内同证号的批号间比对",command =lambda :TABLE_tree_Level_2 (Countall (O0O0OOO0O00OO0O00 ).df_ror (["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号","产品批号"]),1 ,OOO00OO0OOO00OOO0 ))#line:4551
	O0000000OO0OO00OO .add_command (label ="关键字ROR-页面内同证号的月份间比对",command =lambda :TABLE_tree_Level_2 (Countall (O0O0OOO0O00OO0O00 ).df_ror (["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号","事件发生月份"]),1 ,OOO00OO0OOO00OOO0 ))#line:4553
	O0000000OO0OO00OO .add_command (label ="关键字ROR-页面内同证号的季度间比对",command =lambda :TABLE_tree_Level_2 (Countall (O0O0OOO0O00OO0O00 ).df_ror (["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号","事件发生季度"]),1 ,OOO00OO0OOO00OOO0 ))#line:4555
	O0000000OO0OO00OO .add_command (label ="关键字ROR-页面内同证号的年龄段间比对",command =lambda :TABLE_tree_Level_2 (Countall (O0O0OOO0O00OO0O00 ).df_ror (["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号","年龄段"]),1 ,OOO00OO0OOO00OOO0 ))#line:4557
	O0000000OO0OO00OO .add_command (label ="关键字ROR-页面内同证号的性别间比对",command =lambda :TABLE_tree_Level_2 (Countall (O0O0OOO0O00OO0O00 ).df_ror (["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号","性别"]),1 ,OOO00OO0OOO00OOO0 ))#line:4559
	O0000000OO0OO00OO .add_separator ()#line:4561
	O0000000OO0OO00OO .add_command (label ="关键字ROR-页面内同品名的证号间比对",command =lambda :TABLE_tree_Level_2 (Countall (O0O0OOO0O00OO0O00 ).df_ror (["产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号"]),1 ,OOO00OO0OOO00OOO0 ))#line:4563
	O0000000OO0OO00OO .add_command (label ="关键字ROR-页面内同品名的年龄段间比对",command =lambda :TABLE_tree_Level_2 (Countall (O0O0OOO0O00OO0O00 ).df_ror (["产品类别","规整后品类","产品名称","年龄段"]),1 ,OOO00OO0OOO00OOO0 ))#line:4565
	O0000000OO0OO00OO .add_command (label ="关键字ROR-页面内同品名的性别间比对",command =lambda :TABLE_tree_Level_2 (Countall (O0O0OOO0O00OO0O00 ).df_ror (["产品类别","规整后品类","产品名称","性别"]),1 ,OOO00OO0OOO00OOO0 ))#line:4567
	O0000000OO0OO00OO .add_separator ()#line:4569
	O0000000OO0OO00OO .add_command (label ="关键字ROR-页面内同类别的名称间比对",command =lambda :TABLE_tree_Level_2 (Countall (O0O0OOO0O00OO0O00 ).df_ror (["产品类别","产品名称"]),1 ,OOO00OO0OOO00OOO0 ))#line:4571
	O0000000OO0OO00OO .add_command (label ="关键字ROR-页面内同类别的年龄段间比对",command =lambda :TABLE_tree_Level_2 (Countall (O0O0OOO0O00OO0O00 ).df_ror (["产品类别","年龄段"]),1 ,OOO00OO0OOO00OOO0 ))#line:4573
	O0000000OO0OO00OO .add_command (label ="关键字ROR-页面内同类别的性别间比对",command =lambda :TABLE_tree_Level_2 (Countall (O0O0OOO0O00OO0O00 ).df_ror (["产品类别","性别"]),1 ,OOO00OO0OOO00OOO0 ))#line:4575
	O0000000OO0OO00OO .add_separator ()#line:4586
	if ini ["模式"]=="药品":#line:4587
		O0000000OO0OO00OO .add_command (label ="新的不良反应检测(证号)",command =lambda :PROGRAM_thread_it (TOOLS_get_new ,OOO00OO0OOO00OOO0 ,"证号"))#line:4590
		O0000000OO0OO00OO .add_command (label ="新的不良反应检测(品种)",command =lambda :PROGRAM_thread_it (TOOLS_get_new ,OOO00OO0OOO00OOO0 ,"品种"))#line:4593
	OOOO00O0OOO0000OO =Menu (O0O00O00OO000O00O ,tearoff =0 )#line:4596
	O0O00O00OO000O00O .add_cascade (label ="简报制作",menu =OOOO00O0OOO0000OO )#line:4597
	OOOO00O0OOO0000OO .add_command (label ="药品简报",command =lambda :TOOLS_autocount (O0O0OOO0O00OO0O00 ,"药品"))#line:4600
	OOOO00O0OOO0000OO .add_command (label ="器械简报",command =lambda :TOOLS_autocount (O0O0OOO0O00OO0O00 ,"器械"))#line:4602
	OOOO00O0OOO0000OO .add_command (label ="化妆品简报",command =lambda :TOOLS_autocount (O0O0OOO0O00OO0O00 ,"化妆品"))#line:4604
	OOO00OO0O0OO0O00O =Menu (O0O00O00OO000O00O ,tearoff =0 )#line:4608
	O0O00O00OO000O00O .add_cascade (label ="品种评价",menu =OOO00OO0O0OO0O00O )#line:4609
	OOO00OO0O0OO0O00O .add_command (label ="报告年份",command =lambda :STAT_pinzhong (O0O0OOO0O00OO0O00 ,"报告年份",-1 ))#line:4611
	OOO00OO0O0OO0O00O .add_command (label ="发生年份",command =lambda :STAT_pinzhong (O0O0OOO0O00OO0O00 ,"事件发生年份",-1 ))#line:4613
	OOO00OO0O0OO0O00O .add_separator ()#line:4614
	OOO00OO0O0OO0O00O .add_command (label ="怀疑/并用",command =lambda :STAT_pinzhong (O0O0OOO0O00OO0O00 ,"怀疑/并用",1 ))#line:4616
	OOO00OO0O0OO0O00O .add_command (label ="涉及企业",command =lambda :STAT_pinzhong (O0O0OOO0O00OO0O00 ,"上市许可持有人名称",1 ))#line:4618
	OOO00OO0O0OO0O00O .add_command (label ="产品名称",command =lambda :STAT_pinzhong (O0O0OOO0O00OO0O00 ,"产品名称",1 ))#line:4620
	OOO00OO0O0OO0O00O .add_command (label ="注册证号",command =lambda :TABLE_tree_Level_2 (Countall (O0O0OOO0O00OO0O00 ).df_zhenghao (),1 ,OOO00OO0OOO00OOO0 ))#line:4622
	OOO00OO0O0OO0O00O .add_separator ()#line:4623
	OOO00OO0O0OO0O00O .add_command (label ="年龄段分布",command =lambda :STAT_pinzhong (O0O0OOO0O00OO0O00 ,"年龄段",1 ))#line:4625
	OOO00OO0O0OO0O00O .add_command (label ="性别分布",command =lambda :STAT_pinzhong (O0O0OOO0O00OO0O00 ,"性别",1 ))#line:4627
	OOO00OO0O0OO0O00O .add_command (label ="年龄性别分布",command =lambda :TABLE_tree_Level_2 (Countall (O0O0OOO0O00OO0O00 ).df_age (),1 ,OOO00OO0OOO00OOO0 ,))#line:4629
	OOO00OO0O0OO0O00O .add_separator ()#line:4630
	OOO00OO0O0OO0O00O .add_command (label ="不良反应发生时间",command =lambda :STAT_pinzhong (O0O0OOO0O00OO0O00 ,"时隔",1 ))#line:4632
	OOO00OO0O0OO0O00O .add_command (label ="报告类型-严重程度",command =lambda :STAT_pinzhong (O0O0OOO0O00OO0O00 ,"报告类型-严重程度",1 ))#line:4635
	OOO00OO0O0OO0O00O .add_command (label ="停药减药后反应是否减轻或消失",command =lambda :STAT_pinzhong (O0O0OOO0O00OO0O00 ,"停药减药后反应是否减轻或消失",1 ))#line:4637
	OOO00OO0O0OO0O00O .add_command (label ="再次使用可疑药是否出现同样反应",command =lambda :STAT_pinzhong (O0O0OOO0O00OO0O00 ,"再次使用可疑药是否出现同样反应",1 ))#line:4639
	OOO00OO0O0OO0O00O .add_command (label ="对原患疾病影响",command =lambda :STAT_pinzhong (O0O0OOO0O00OO0O00 ,"对原患疾病影响",1 ))#line:4641
	OOO00OO0O0OO0O00O .add_command (label ="不良反应结果",command =lambda :STAT_pinzhong (O0O0OOO0O00OO0O00 ,"不良反应结果",1 ))#line:4643
	OOO00OO0O0OO0O00O .add_command (label ="报告单位关联性评价",command =lambda :STAT_pinzhong (O0O0OOO0O00OO0O00 ,"关联性评价",1 ))#line:4645
	OOO00OO0O0OO0O00O .add_separator ()#line:4646
	OOO00OO0O0OO0O00O .add_command (label ="不良反应转归情况",command =lambda :STAT_pinzhong (O0O0OOO0O00OO0O00 ,"不良反应结果2",4 ))#line:4648
	OOO00OO0O0OO0O00O .add_command (label ="关联性评价汇总",command =lambda :STAT_pinzhong (O0O0OOO0O00OO0O00 ,"关联性评价汇总",5 ))#line:4650
	OOO00OO0O0OO0O00O .add_separator ()#line:4654
	OOO00OO0O0OO0O00O .add_command (label ="不良反应-术语",command =lambda :STAT_pinzhong (O0O0OOO0O00OO0O00 ,"器械故障表现",0 ))#line:4656
	OOO00OO0O0OO0O00O .add_command (label ="不良反应器官系统-术语",command =lambda :TABLE_tree_Level_2 (Countall (O0O0OOO0O00OO0O00 ).df_psur (),1 ,OOO00OO0OOO00OOO0 ))#line:4658
	OOO00OO0O0OO0O00O .add_command (label ="不良反应-由code转化",command =lambda :STAT_pinzhong (O0O0OOO0O00OO0O00 ,"不良反应-code",2 ))#line:4660
	OOO00OO0O0OO0O00O .add_command (label ="不良反应器官系统-由code转化",command =lambda :STAT_pinzhong (O0O0OOO0O00OO0O00 ,"不良反应-code",3 ))#line:4662
	OOO00OO0O0OO0O00O .add_command (label ="故障细项目（器械专用）",command =lambda :STAT_pinzhong (O0O0OOO0O00OO0O00 ,"器械故障表现",0 ))#line:4664
	OOO00OO0O0OO0O00O .add_separator ()#line:4666
	OOO00OO0O0OO0O00O .add_command (label ="疾病名称-术语",command =lambda :STAT_pinzhong (O0O0OOO0O00OO0O00 ,"相关疾病信息[疾病名称]-术语",0 ))#line:4668
	OOO00OO0O0OO0O00O .add_command (label ="疾病名称-由code转化",command =lambda :STAT_pinzhong (O0O0OOO0O00OO0O00 ,"相关疾病信息[疾病名称]-code",2 ))#line:4670
	OOO00OO0O0OO0O00O .add_command (label ="疾病器官系统-由code转化",command =lambda :STAT_pinzhong (O0O0OOO0O00OO0O00 ,"相关疾病信息[疾病名称]-code",3 ))#line:4672
	OOO00OO0O0OO0O00O .add_separator ()#line:4673
	OOO00OO0O0OO0O00O .add_command (label ="适应症-术语",command =lambda :STAT_pinzhong (O0O0OOO0O00OO0O00 ,"治疗适应症-术语",0 ))#line:4675
	OOO00OO0O0OO0O00O .add_command (label ="适应症-由code转化",command =lambda :STAT_pinzhong (O0O0OOO0O00OO0O00 ,"治疗适应症-code",2 ))#line:4677
	OOO00OO0O0OO0O00O .add_command (label ="适应症器官系统-由code转化",command =lambda :STAT_pinzhong (O0O0OOO0O00OO0O00 ,"治疗适应症-code",3 ))#line:4679
	O0O00OO0000OOOOOO =Menu (O0O00O00OO000O00O ,tearoff =0 )#line:4681
	O0O00O00OO000O00O .add_cascade (label ="基础研究",menu =O0O00OO0000OOOOOO )#line:4682
	O0O00OO0000OOOOOO .add_command (label ="基础信息批量操作（品名）",command =lambda :TOOLS_ror_mode1 (O0O0OOO0O00OO0O00 ,"产品名称"))#line:4684
	O0O00OO0000OOOOOO .add_command (label ="器官系统分类批量操作（品名）",command =lambda :TOOLS_ror_mode4 (O0O0OOO0O00OO0O00 ,"产品名称"))#line:4686
	O0O00OO0000OOOOOO .add_command (label ="器官系统ROR批量操作（品名）",command =lambda :TOOLS_ror_mode2 (O0O0OOO0O00OO0O00 ,"产品名称"))#line:4688
	O0O00OO0000OOOOOO .add_command (label ="ADR-ROR批量操作（品名）",command =lambda :TOOLS_ror_mode3 (O0O0OOO0O00OO0O00 ,"产品名称"))#line:4690
	O0O00OO0000OOOOOO .add_separator ()#line:4691
	O0O00OO0000OOOOOO .add_command (label ="基础信息批量操作（注册证号）",command =lambda :TOOLS_ror_mode1 (O0O0OOO0O00OO0O00 ,"注册证编号/曾用注册证编号"))#line:4693
	O0O00OO0000OOOOOO .add_command (label ="器官系统分类批量操作（注册证号）",command =lambda :TOOLS_ror_mode4 (O0O0OOO0O00OO0O00 ,"注册证编号/曾用注册证编号"))#line:4695
	O0O00OO0000OOOOOO .add_command (label ="器官系统ROR批量操作（注册证号）",command =lambda :TOOLS_ror_mode2 (O0O0OOO0O00OO0O00 ,"注册证编号/曾用注册证编号"))#line:4697
	O0O00OO0000OOOOOO .add_command (label ="ADR-ROR批量操作（注册证号）",command =lambda :TOOLS_ror_mode3 (O0O0OOO0O00OO0O00 ,"注册证编号/曾用注册证编号"))#line:4699
	OOOO00O00000OOO00 =Menu (O0O00O00OO000O00O ,tearoff =0 )#line:4701
	O0O00O00OO000O00O .add_cascade (label ="风险预警",menu =OOOO00O00000OOO00 )#line:4702
	OOOO00O00000OOO00 .add_command (label ="预警（单日）",command =lambda :TOOLS_keti (O0O0OOO0O00OO0O00 ))#line:4704
	OOOO00O00000OOO00 .add_command (label ="事件分布（器械）",command =lambda :TOOLS_get_guize2 (O0O0OOO0O00OO0O00 ))#line:4707
	OOO0O00OOOO0O000O =Menu (O0O00O00OO000O00O ,tearoff =0 )#line:4714
	O0O00O00OO000O00O .add_cascade (label ="实用工具",menu =OOO0O00OOOO0O000O )#line:4715
	OOO0O00OOOO0O000O .add_command (label ="数据规整（报告单位）",command =lambda :TOOL_guizheng (O0O0OOO0O00OO0O00 ,2 ,False ))#line:4719
	OOO0O00OOOO0O000O .add_command (label ="数据规整（产品名称）",command =lambda :TOOL_guizheng (O0O0OOO0O00OO0O00 ,3 ,False ))#line:4721
	OOO0O00OOOO0O000O .add_command (label ="数据规整（自定义）",command =lambda :TOOL_guizheng (O0O0OOO0O00OO0O00 ,0 ,False ))#line:4723
	OOO0O00OOOO0O000O .add_separator ()#line:4725
	OOO0O00OOOO0O000O .add_command (label ="原始导入",command =TOOLS_fileopen )#line:4727
	OOO0O00OOOO0O000O .add_command (label ="脱敏保存",command =lambda :TOOLS_data_masking (O0O0OOO0O00OO0O00 ))#line:4729
	OOO0O00OOOO0O000O .add_separator ()#line:4730
	OOO0O00OOOO0O000O .add_command (label ="批量筛选（默认）",command =lambda :TOOLS_xuanze (O0O0OOO0O00OO0O00 ,1 ))#line:4732
	OOO0O00OOOO0O000O .add_command (label ="批量筛选（自定义）",command =lambda :TOOLS_xuanze (O0O0OOO0O00OO0O00 ,0 ))#line:4734
	OOO0O00OOOO0O000O .add_separator ()#line:4735
	OOO0O00OOOO0O000O .add_command (label ="评价人员（广东化妆品）",command =lambda :TOOL_person (O0O0OOO0O00OO0O00 ))#line:4737
	OOO0O00OOOO0O000O .add_separator ()#line:4738
	OOO0O00OOOO0O000O .add_command (label ="意见反馈",command =lambda :PROGRAM_helper (["","  药械妆不良反应报表统计分析工作站","  开发者：蔡权周","  邮箱：411703730@qq.com","  微信号：sysucai","  手机号：18575757461"]))#line:4742
	OOO0O00OOOO0O000O .add_command (label ="更改用户组",command =lambda :PROGRAM_thread_it (display_random_number ))#line:4744
def PROGRAM_helper (OO000O00OO0O0OO00 ):#line:4748
    ""#line:4749
    OOOOO0OO00OO0000O =Toplevel ()#line:4750
    OOOOO0OO00OO0000O .title ("信息查看")#line:4751
    OOOOO0OO00OO0000O .geometry ("700x500")#line:4752
    OOO00O0OO000O00O0 =Scrollbar (OOOOO0OO00OO0000O )#line:4754
    O0OO0O000OOO0O00O =Text (OOOOO0OO00OO0000O ,height =80 ,width =150 ,bg ="#FFFFFF",font ="微软雅黑")#line:4755
    OOO00O0OO000O00O0 .pack (side =RIGHT ,fill =Y )#line:4756
    O0OO0O000OOO0O00O .pack ()#line:4757
    OOO00O0OO000O00O0 .config (command =O0OO0O000OOO0O00O .yview )#line:4758
    O0OO0O000OOO0O00O .config (yscrollcommand =OOO00O0OO000O00O0 .set )#line:4759
    for O0O0OOO0OOO00O00O in OO000O00OO0O0OO00 :#line:4761
        O0OO0O000OOO0O00O .insert (END ,O0O0OOO0OOO00O00O )#line:4762
        O0OO0O000OOO0O00O .insert (END ,"\n")#line:4763
    def O0O0O00O0OO00O0OO (event =None ):#line:4766
        O0OO0O000OOO0O00O .event_generate ('<<Copy>>')#line:4767
    O000000O0O0O00O0O =Menu (O0OO0O000OOO0O00O ,tearoff =False ,)#line:4770
    O000000O0O0O00O0O .add_command (label ="复制",command =O0O0O00O0OO00O0OO )#line:4771
    def OO00OOOOOOO00O0O0 (O0OO00000O0O00OO0 ):#line:4772
         O000000O0O0O00O0O .post (O0OO00000O0O00OO0 .x_root ,O0OO00000O0O00OO0 .y_root )#line:4773
    O0OO0O000OOO0O00O .bind ("<Button-3>",OO00OOOOOOO00O0O0 )#line:4774
    O0OO0O000OOO0O00O .config (state =DISABLED )#line:4776
def PROGRAM_change_schedule (OOOO0O000O00OO00O ,O0O0OOOOOO0000O0O ):#line:4778
    ""#line:4779
    canvas .coords (fill_rec ,(5 ,5 ,(OOOO0O000O00OO00O /O0O0OOOOOO0000O0O )*680 ,25 ))#line:4781
    root .update ()#line:4782
    x .set (str (round (OOOO0O000O00OO00O /O0O0OOOOOO0000O0O *100 ,2 ))+"%")#line:4783
    if round (OOOO0O000O00OO00O /O0O0OOOOOO0000O0O *100 ,2 )==100.00 :#line:4784
        x .set ("完成")#line:4785
def PROGRAM_showWelcome ():#line:4788
    ""#line:4789
    O0O0000OO0OO0OOO0 =roox .winfo_screenwidth ()#line:4790
    O00OOOOO000O0OO00 =roox .winfo_screenheight ()#line:4792
    roox .overrideredirect (True )#line:4794
    roox .attributes ("-alpha",1 )#line:4795
    O0O0OO0O0O0OOO0OO =(O0O0000OO0OO0OOO0 -475 )/2 #line:4796
    OO0O0O00OO000O00O =(O00OOOOO000O0OO00 -200 )/2 #line:4797
    roox .geometry ("675x130+%d+%d"%(O0O0OO0O0O0OOO0OO ,OO0O0O00OO000O00O ))#line:4799
    roox ["bg"]="green"#line:4800
    OOO000O0000OO00O0 =Label (roox ,text =title_all2 ,fg ="white",bg ="green",font =("微软雅黑",20 ))#line:4803
    OOO000O0000OO00O0 .place (x =0 ,y =15 ,width =675 ,height =90 )#line:4804
    OOOOO0O000OOO000O =Label (roox ,text ="仅供监测机构使用 ",fg ="white",bg ="black",font =("微软雅黑",15 ))#line:4807
    OOOOO0O000OOO000O .place (x =0 ,y =90 ,width =675 ,height =40 )#line:4808
def PROGRAM_closeWelcome ():#line:4811
    ""#line:4812
    for OO000O0OO00O0OOO0 in range (2 ):#line:4813
        root .attributes ("-alpha",0 )#line:4814
        time .sleep (1 )#line:4815
    root .attributes ("-alpha",1 )#line:4816
    roox .destroy ()#line:4817
class Countall ():#line:4832
	""#line:4833
	def __init__ (OOOOO0000000O0000 ,OO0O0OOO000O0O000 ):#line:4834
		""#line:4835
		OOOOO0000000O0000 .df =OO0O0OOO000O0O000 #line:4836
		OOOOO0000000O0000 .mode =ini ["模式"]#line:4837
	def df_org (O0OOO000OOO00OOO0 ,O0OO0O00O00000000 ):#line:4839
		""#line:4840
		OO0OOOOOO00OOOOO0 =O0OOO000OOO00OOO0 .df .drop_duplicates (["报告编码"]).groupby ([O0OO0O00O00000000 ]).agg (报告数量 =("注册证编号/曾用注册证编号","count"),审核通过数 =("有效报告","sum"),严重伤害数 =("伤害",lambda O000O000000O0O0O0 :STAT_countpx (O000O000000O0O0O0 .values ,"严重伤害")),死亡数量 =("伤害",lambda OOO000O0O00OOO000 :STAT_countpx (OOO000O0O00OOO000 .values ,"死亡")),超时报告数 =("超时标记",lambda OOOOO00OOOOOO0OO0 :STAT_countpx (OOOOO00OOOOOO0OO0 .values ,1 )),有源 =("产品类别",lambda OO0O0O0OO0OO0O0OO :STAT_countpx (OO0O0O0OO0OO0O0OO .values ,"有源")),无源 =("产品类别",lambda OOO00OOOO000OO0OO :STAT_countpx (OOO00OOOO000OO0OO .values ,"无源")),体外诊断试剂 =("产品类别",lambda O000O0O00OOO0OOOO :STAT_countpx (O000O0O00OOO0OOOO .values ,"体外诊断试剂")),三类数量 =("管理类别",lambda O0O0O000O0OO000O0 :STAT_countpx (O0O0O000O0OO000O0 .values ,"Ⅲ类")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),报告季度 =("报告季度",STAT_countx ),报告月份 =("报告月份",STAT_countx ),).sort_values (by ="报告数量",ascending =[False ],na_position ="last").reset_index ()#line:4855
		OO0OO0000O0O0000O =["报告数量","审核通过数","严重伤害数","死亡数量","超时报告数","有源","无源","体外诊断试剂","三类数量","单位个数"]#line:4857
		OO0OOOOOO00OOOOO0 .loc ["合计"]=OO0OOOOOO00OOOOO0 [OO0OO0000O0O0000O ].apply (lambda O000000OO0O00O0O0 :O000000OO0O00O0O0 .sum ())#line:4858
		OO0OOOOOO00OOOOO0 [OO0OO0000O0O0000O ]=OO0OOOOOO00OOOOO0 [OO0OO0000O0O0000O ].apply (lambda O000O0O00O0OO000O :O000O0O00O0OO000O .astype (int ))#line:4859
		OO0OOOOOO00OOOOO0 .iloc [-1 ,0 ]="合计"#line:4860
		OO0OOOOOO00OOOOO0 ["严重比"]=round ((OO0OOOOOO00OOOOO0 ["严重伤害数"]+OO0OOOOOO00OOOOO0 ["死亡数量"])/OO0OOOOOO00OOOOO0 ["报告数量"]*100 ,2 )#line:4862
		OO0OOOOOO00OOOOO0 ["Ⅲ类比"]=round ((OO0OOOOOO00OOOOO0 ["三类数量"])/OO0OOOOOO00OOOOO0 ["报告数量"]*100 ,2 )#line:4863
		OO0OOOOOO00OOOOO0 ["超时比"]=round ((OO0OOOOOO00OOOOO0 ["超时报告数"])/OO0OOOOOO00OOOOO0 ["报告数量"]*100 ,2 )#line:4864
		OO0OOOOOO00OOOOO0 ["报表类型"]="dfx_org"+O0OO0O00O00000000 #line:4865
		if ini ["模式"]=="药品":#line:4868
			del OO0OOOOOO00OOOOO0 ["有源"]#line:4870
			del OO0OOOOOO00OOOOO0 ["无源"]#line:4871
			del OO0OOOOOO00OOOOO0 ["体外诊断试剂"]#line:4872
			OO0OOOOOO00OOOOO0 =OO0OOOOOO00OOOOO0 .rename (columns ={"三类数量":"新的和严重的数量"})#line:4873
			OO0OOOOOO00OOOOO0 =OO0OOOOOO00OOOOO0 .rename (columns ={"Ⅲ类比":"新严比"})#line:4874
		return OO0OOOOOO00OOOOO0 #line:4876
	def df_user (OO0OO0O00O000000O ):#line:4880
		""#line:4881
		OO0OO0O00O000000O .df ["医疗机构类别"]=OO0OO0O00O000000O .df ["医疗机构类别"].fillna ("未填写")#line:4882
		O0O0O0O0O000O0000 =OO0OO0O00O000000O .df .drop_duplicates (["报告编码"]).groupby (["监测机构","单位名称","医疗机构类别"]).agg (报告数量 =("注册证编号/曾用注册证编号","count"),审核通过数 =("有效报告","sum"),严重伤害数 =("伤害",lambda O0000000000000O0O :STAT_countpx (O0000000000000O0O .values ,"严重伤害")),死亡数量 =("伤害",lambda OO00O0OOOO000OO00 :STAT_countpx (OO00O0OOOO000OO00 .values ,"死亡")),超时报告数 =("超时标记",lambda O00OOOOOOOO0OOO00 :STAT_countpx (O00OOOOOOOO0OOO00 .values ,1 )),有源 =("产品类别",lambda O0O0O0OOO0000OOOO :STAT_countpx (O0O0O0OOO0000OOOO .values ,"有源")),无源 =("产品类别",lambda O0000OO0O00OO0O0O :STAT_countpx (O0000OO0O00OO0O0O .values ,"无源")),体外诊断试剂 =("产品类别",lambda O0OO0O0OO0O0OOO0O :STAT_countpx (O0OO0O0OO0O0OOO0O .values ,"体外诊断试剂")),三类数量 =("管理类别",lambda OO0OO0O0OO000O0O0 :STAT_countpx (OO0OO0O0OO000O0O0 .values ,"Ⅲ类")),产品数量 =("产品名称","nunique"),产品清单 =("产品名称",STAT_countx ),报告季度 =("报告季度",STAT_countx ),报告月份 =("报告月份",STAT_countx ),).sort_values (by ="报告数量",ascending =[False ],na_position ="last").reset_index ()#line:4897
		OOO000000OO0OOO00 =["报告数量","审核通过数","严重伤害数","死亡数量","超时报告数","有源","无源","体外诊断试剂","三类数量"]#line:4900
		O0O0O0O0O000O0000 .loc ["合计"]=O0O0O0O0O000O0000 [OOO000000OO0OOO00 ].apply (lambda O0O0O0O00000OO00O :O0O0O0O00000OO00O .sum ())#line:4901
		O0O0O0O0O000O0000 [OOO000000OO0OOO00 ]=O0O0O0O0O000O0000 [OOO000000OO0OOO00 ].apply (lambda OO00O0000O0O00O0O :OO00O0000O0O00O0O .astype (int ))#line:4902
		O0O0O0O0O000O0000 .iloc [-1 ,0 ]="合计"#line:4903
		O0O0O0O0O000O0000 ["严重比"]=round ((O0O0O0O0O000O0000 ["严重伤害数"]+O0O0O0O0O000O0000 ["死亡数量"])/O0O0O0O0O000O0000 ["报告数量"]*100 ,2 )#line:4905
		O0O0O0O0O000O0000 ["Ⅲ类比"]=round ((O0O0O0O0O000O0000 ["三类数量"])/O0O0O0O0O000O0000 ["报告数量"]*100 ,2 )#line:4906
		O0O0O0O0O000O0000 ["超时比"]=round ((O0O0O0O0O000O0000 ["超时报告数"])/O0O0O0O0O000O0000 ["报告数量"]*100 ,2 )#line:4907
		O0O0O0O0O000O0000 ["报表类型"]="dfx_user"#line:4908
		if ini ["模式"]=="药品":#line:4910
			del O0O0O0O0O000O0000 ["有源"]#line:4912
			del O0O0O0O0O000O0000 ["无源"]#line:4913
			del O0O0O0O0O000O0000 ["体外诊断试剂"]#line:4914
			O0O0O0O0O000O0000 =O0O0O0O0O000O0000 .rename (columns ={"三类数量":"新的和严重的数量"})#line:4915
			O0O0O0O0O000O0000 =O0O0O0O0O000O0000 .rename (columns ={"Ⅲ类比":"新严比"})#line:4916
		return O0O0O0O0O000O0000 #line:4918
	def df_zhenghao (O0OOOOOOOO0OOO0OO ):#line:4923
		""#line:4924
		OO0O000OO0OOOOO0O =O0OOOOOOOO0OOO0OO .df .groupby (["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号"]).agg (证号计数 =("报告编码","nunique"),批号个数 =("产品批号","nunique"),批号列表 =("产品批号",STAT_countx ),型号个数 =("型号","nunique"),型号列表 =("型号",STAT_countx ),规格个数 =("规格","nunique"),规格列表 =("规格",STAT_countx ),).sort_values (by ="证号计数",ascending =[False ],na_position ="last").reset_index ()#line:4934
		OO0O0O0OO00OOOOO0 =O0OOOOOOOO0OOO0OO .df .drop_duplicates (["报告编码"]).groupby (["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号"]).agg (严重伤害数 =("伤害",lambda OOO000O0O00OOO0OO :STAT_countpx (OOO000O0O00OOO0OO .values ,"严重伤害")),死亡数量 =("伤害",lambda OO00OOOO000O00OO0 :STAT_countpx (OO00OOOO000O00OO0 .values ,"死亡")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),待评价数 =("持有人报告状态",lambda OOOOO0O0OOO000OOO :STAT_countpx (OOOOO0O0OOO000OOO .values ,"待评价")),严重伤害待评价数 =("伤害与评价",lambda O0O0000000OO00O0O :STAT_countpx (O0O0000000OO00O0O .values ,"严重伤害待评价")),).reset_index ()#line:4943
		O0O0O00OOOO0OOOO0 =pd .merge (OO0O000OO0OOOOO0O ,OO0O0O0OO00OOOOO0 ,on =["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号"],how ="left")#line:4945
		O0O0O00OOOO0OOOO0 =STAT_basic_risk (O0O0O00OOOO0OOOO0 ,"证号计数","严重伤害数","死亡数量","单位个数")#line:4946
		O0O0O00OOOO0OOOO0 =pd .merge (O0O0O00OOOO0OOOO0 ,STAT_recent30 (O0OOOOOOOO0OOO0OO .df ,["注册证编号/曾用注册证编号"]),on =["注册证编号/曾用注册证编号"],how ="left")#line:4948
		O0O0O00OOOO0OOOO0 ["最近30天报告数"]=O0O0O00OOOO0OOOO0 ["最近30天报告数"].fillna (0 ).astype (int )#line:4949
		O0O0O00OOOO0OOOO0 ["最近30天报告严重伤害数"]=O0O0O00OOOO0OOOO0 ["最近30天报告严重伤害数"].fillna (0 ).astype (int )#line:4950
		O0O0O00OOOO0OOOO0 ["最近30天报告死亡数量"]=O0O0O00OOOO0OOOO0 ["最近30天报告死亡数量"].fillna (0 ).astype (int )#line:4951
		O0O0O00OOOO0OOOO0 ["最近30天报告单位个数"]=O0O0O00OOOO0OOOO0 ["最近30天报告单位个数"].fillna (0 ).astype (int )#line:4952
		O0O0O00OOOO0OOOO0 ["最近30天风险评分"]=O0O0O00OOOO0OOOO0 ["最近30天风险评分"].fillna (0 ).astype (int )#line:4953
		O0O0O00OOOO0OOOO0 ["报表类型"]="dfx_zhenghao"#line:4955
		if ini ["模式"]=="药品":#line:4957
			O0O0O00OOOO0OOOO0 =O0O0O00OOOO0OOOO0 .rename (columns ={"待评价数":"新的数量"})#line:4958
			O0O0O00OOOO0OOOO0 =O0O0O00OOOO0OOOO0 .rename (columns ={"严重伤害待评价数":"新的严重的数量"})#line:4959
		return O0O0O00OOOO0OOOO0 #line:4961
	def df_pihao (O00OOO00OOO0O00OO ):#line:4963
		""#line:4964
		O00OOO00O0000O000 =O00OOO00OOO0O00OO .df .groupby (["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","产品批号"]).agg (批号计数 =("报告编码","nunique"),型号个数 =("型号","nunique"),型号列表 =("型号",STAT_countx ),规格个数 =("规格","nunique"),规格列表 =("规格",STAT_countx ),).sort_values (by ="批号计数",ascending =[False ],na_position ="last").reset_index ()#line:4971
		O000OOOO0OO000000 =O00OOO00OOO0O00OO .df .drop_duplicates (["报告编码"]).groupby (["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","产品批号"]).agg (严重伤害数 =("伤害",lambda OO0000O0OOOO0O0OO :STAT_countpx (OO0000O0OOOO0O0OO .values ,"严重伤害")),死亡数量 =("伤害",lambda O00O000O0000000OO :STAT_countpx (O00O000O0000000OO .values ,"死亡")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),待评价数 =("持有人报告状态",lambda OO00000000O0000O0 :STAT_countpx (OO00000000O0000O0 .values ,"待评价")),严重伤害待评价数 =("伤害与评价",lambda OO00O0O000OO00O00 :STAT_countpx (OO00O0O000OO00O00 .values ,"严重伤害待评价")),).reset_index ()#line:4980
		OO0OOOOO0O00O00O0 =pd .merge (O00OOO00O0000O000 ,O000OOOO0OO000000 ,on =["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","产品批号"],how ="left")#line:4982
		OO0OOOOO0O00O00O0 =STAT_basic_risk (OO0OOOOO0O00O00O0 ,"批号计数","严重伤害数","死亡数量","单位个数")#line:4984
		OO0OOOOO0O00O00O0 =pd .merge (OO0OOOOO0O00O00O0 ,STAT_recent30 (O00OOO00OOO0O00OO .df ,["注册证编号/曾用注册证编号","产品批号"]),on =["注册证编号/曾用注册证编号","产品批号"],how ="left")#line:4986
		OO0OOOOO0O00O00O0 ["最近30天报告数"]=OO0OOOOO0O00O00O0 ["最近30天报告数"].fillna (0 ).astype (int )#line:4987
		OO0OOOOO0O00O00O0 ["最近30天报告严重伤害数"]=OO0OOOOO0O00O00O0 ["最近30天报告严重伤害数"].fillna (0 ).astype (int )#line:4988
		OO0OOOOO0O00O00O0 ["最近30天报告死亡数量"]=OO0OOOOO0O00O00O0 ["最近30天报告死亡数量"].fillna (0 ).astype (int )#line:4989
		OO0OOOOO0O00O00O0 ["最近30天报告单位个数"]=OO0OOOOO0O00O00O0 ["最近30天报告单位个数"].fillna (0 ).astype (int )#line:4990
		OO0OOOOO0O00O00O0 ["最近30天风险评分"]=OO0OOOOO0O00O00O0 ["最近30天风险评分"].fillna (0 ).astype (int )#line:4991
		OO0OOOOO0O00O00O0 ["报表类型"]="dfx_pihao"#line:4993
		if ini ["模式"]=="药品":#line:4994
			OO0OOOOO0O00O00O0 =OO0OOOOO0O00O00O0 .rename (columns ={"待评价数":"新的数量"})#line:4995
			OO0OOOOO0O00O00O0 =OO0OOOOO0O00O00O0 .rename (columns ={"严重伤害待评价数":"新的严重的数量"})#line:4996
		return OO0OOOOO0O00O00O0 #line:4997
	def df_xinghao (O0O00O00OO000000O ):#line:4999
		""#line:5000
		O0O000O0OO0000000 =O0O00O00OO000000O .df .groupby (["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","型号"]).agg (型号计数 =("报告编码","nunique"),批号个数 =("产品批号","nunique"),批号列表 =("产品批号",STAT_countx ),规格个数 =("规格","nunique"),规格列表 =("规格",STAT_countx ),).sort_values (by ="型号计数",ascending =[False ],na_position ="last").reset_index ()#line:5007
		OO00O0OOO0OO0OO0O =O0O00O00OO000000O .df .drop_duplicates (["报告编码"]).groupby (["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","型号"]).agg (严重伤害数 =("伤害",lambda O00OOO000O0000O0O :STAT_countpx (O00OOO000O0000O0O .values ,"严重伤害")),死亡数量 =("伤害",lambda OO0OOOOOO0OO00O00 :STAT_countpx (OO0OOOOOO0OO00O00 .values ,"死亡")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),待评价数 =("持有人报告状态",lambda OOO0OO00O0OO0O00O :STAT_countpx (OOO0OO00O0OO0O00O .values ,"待评价")),严重伤害待评价数 =("伤害与评价",lambda O00OOOOOO0O00O0OO :STAT_countpx (O00OOOOOO0O00O0OO .values ,"严重伤害待评价")),).reset_index ()#line:5016
		OO0000O0O00O0OO0O =pd .merge (O0O000O0OO0000000 ,OO00O0OOO0OO0OO0O ,on =["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","型号"],how ="left")#line:5018
		OO0000O0O00O0OO0O ["报表类型"]="dfx_xinghao"#line:5021
		if ini ["模式"]=="药品":#line:5022
			OO0000O0O00O0OO0O =OO0000O0O00O0OO0O .rename (columns ={"待评价数":"新的数量"})#line:5023
			OO0000O0O00O0OO0O =OO0000O0O00O0OO0O .rename (columns ={"严重伤害待评价数":"新的严重的数量"})#line:5024
		return OO0000O0O00O0OO0O #line:5026
	def df_guige (O00000O00OOO00O00 ):#line:5028
		""#line:5029
		OO0OO0OOO00O0O00O =O00000O00OOO00O00 .df .groupby (["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","规格"]).agg (规格计数 =("报告编码","nunique"),批号个数 =("产品批号","nunique"),批号列表 =("产品批号",STAT_countx ),型号个数 =("型号","nunique"),型号列表 =("型号",STAT_countx ),).sort_values (by ="规格计数",ascending =[False ],na_position ="last").reset_index ()#line:5036
		OO0O0O0O0O000OO00 =O00000O00OOO00O00 .df .drop_duplicates (["报告编码"]).groupby (["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","规格"]).agg (严重伤害数 =("伤害",lambda OO00OO0O0000O0000 :STAT_countpx (OO00OO0O0000O0000 .values ,"严重伤害")),死亡数量 =("伤害",lambda O0O00OO00OO0O0O0O :STAT_countpx (O0O00OO00OO0O0O0O .values ,"死亡")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),待评价数 =("持有人报告状态",lambda O0OOO0OO00O00OO00 :STAT_countpx (O0OOO0OO00O00OO00 .values ,"待评价")),严重伤害待评价数 =("伤害与评价",lambda O0O0OOOOOO0O0O00O :STAT_countpx (O0O0OOOOOO0O0O00O .values ,"严重伤害待评价")),).reset_index ()#line:5045
		OOO0OO0O0O0000O0O =pd .merge (OO0OO0OOO00O0O00O ,OO0O0O0O0O000OO00 ,on =["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","规格"],how ="left")#line:5047
		OOO0OO0O0O0000O0O ["报表类型"]="dfx_guige"#line:5049
		if ini ["模式"]=="药品":#line:5050
			OOO0OO0O0O0000O0O =OOO0OO0O0O0000O0O .rename (columns ={"待评价数":"新的数量"})#line:5051
			OOO0OO0O0O0000O0O =OOO0OO0O0O0000O0O .rename (columns ={"严重伤害待评价数":"新的严重的数量"})#line:5052
		return OOO0OO0O0O0000O0O #line:5054
	def df_findrisk (OO0O0OO0OO0000000 ,O0O0OOOO0OOO0OO0O ):#line:5056
		""#line:5057
		if O0O0OOOO0OOO0OO0O =="产品批号":#line:5058
			return STAT_find_risk (OO0O0OO0OO0000000 .df [(OO0O0OO0OO0000000 .df ["产品类别"]!="有源")],["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号"],"注册证编号/曾用注册证编号",O0O0OOOO0OOO0OO0O )#line:5059
		else :#line:5060
			return STAT_find_risk (OO0O0OO0OO0000000 .df ,["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号"],"注册证编号/曾用注册证编号",O0O0OOOO0OOO0OO0O )#line:5061
	def df_find_all_keword_risk (O00OO0O00O00O00O0 ,O0OO00000O0OO000O ,*O0O0OOO0O0O00000O ):#line:5063
		""#line:5064
		OOO00OOOOO0O00O0O =O00OO0O00O00O00O0 .df .copy ()#line:5066
		OOO00OOOOO0O00O0O =OOO00OOOOO0O00O0O .drop_duplicates (["报告编码"]).reset_index (drop =True )#line:5067
		O00OOO0O0000OO000 =time .time ()#line:5068
		O00O00OOOOO0O00O0 =peizhidir +"0（范例）比例失衡关键字库.xls"#line:5069
		if "报告类型-新的"in OOO00OOOOO0O00O0O .columns :#line:5070
			OO000O00OO00OOO00 ="药品"#line:5071
		else :#line:5072
			OO000O00OO00OOO00 ="器械"#line:5073
		O0000O00O000000OO =pd .read_excel (O00O00OOOOO0O00O0 ,header =0 ,sheet_name =OO000O00OO00OOO00 ).reset_index (drop =True )#line:5074
		try :#line:5077
			if len (O0O0OOO0O0O00000O [0 ])>0 :#line:5078
				O0000O00O000000OO =O0000O00O000000OO .loc [O0000O00O000000OO ["适用范围"].str .contains (O0O0OOO0O0O00000O [0 ],na =False )].copy ().reset_index (drop =True )#line:5079
		except :#line:5080
			pass #line:5081
		O0000O0O000O00OO0 =["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号"]#line:5083
		OOOO000000O000O00 =O0000O0O000O00OO0 [-1 ]#line:5084
		O0O0O00O0OO0O0OOO =OOO00OOOOO0O00O0O .groupby (O0000O0O000O00OO0 ).agg (总数量 =(OOOO000000O000O00 ,"count"),严重伤害数 =("伤害",lambda O00OO000OOOOOO00O :STAT_countpx (O00OO000OOOOOO00O .values ,"严重伤害")),死亡数量 =("伤害",lambda O0OO0O0O00O0O00OO :STAT_countpx (O0OO0O0O00O0O00OO .values ,"死亡")),)#line:5089
		OOOO000000O000O00 =O0000O0O000O00OO0 [-1 ]#line:5090
		OO0O0000OOO0O000O =O0000O0O000O00OO0 .copy ()#line:5092
		OO0O0000OOO0O000O .append (O0OO00000O0OO000O )#line:5093
		OO00O0OOO0O0O0OO0 =OOO00OOOOO0O00O0O .groupby (OO0O0000OOO0O000O ).agg (该元素总数量 =(OOOO000000O000O00 ,"count"),).reset_index ()#line:5096
		O0O0O00O0OO0O0OOO =O0O0O00O0OO0O0OOO [(O0O0O00O0OO0O0OOO ["总数量"]>=3 )].reset_index ()#line:5099
		O0OO00OO0000OOOOO =[]#line:5100
		OOOOOOOO000OOOOOO =0 #line:5104
		O0O00000O0000O000 =int (len (O0O0O00O0OO0O0OOO ))#line:5105
		for O0OO000O0O000OO00 ,OOO0OO00OOOOO0O0O ,O0OOOO00O0O0OOO0O ,OOOO0O0O00000O0OO in zip (O0O0O00O0OO0O0OOO ["产品名称"].values ,O0O0O00O0OO0O0OOO ["产品类别"].values ,O0O0O00O0OO0O0OOO [OOOO000000O000O00 ].values ,O0O0O00O0OO0O0OOO ["总数量"].values ):#line:5106
			OOOOOOOO000OOOOOO +=1 #line:5107
			if (time .time ()-O00OOO0O0000OO000 )>3 :#line:5109
				root .attributes ("-topmost",True )#line:5110
				PROGRAM_change_schedule (OOOOOOOO000OOOOOO ,O0O00000O0000O000 )#line:5111
				root .attributes ("-topmost",False )#line:5112
			O00000OO00OOO0OO0 =OOO00OOOOO0O00O0O [(OOO00OOOOO0O00O0O [OOOO000000O000O00 ]==O0OOOO00O0O0OOO0O )].copy ()#line:5113
			O0000O00O000000OO ["SELECT"]=O0000O00O000000OO .apply (lambda O00O00O0O0OOOO00O :(O00O00O0O0OOOO00O ["适用范围"]in O0OO000O0O000OO00 )or (O00O00O0O0OOOO00O ["适用范围"]in OOO0OO00OOOOO0O0O )or (O00O00O0O0OOOO00O ["适用范围"]=="通用"),axis =1 )#line:5114
			O0O0OOO0O0OOOOOOO =O0000O00O000000OO [(O0000O00O000000OO ["SELECT"]==True )].reset_index ()#line:5115
			if len (O0O0OOO0O0OOOOOOO )>0 :#line:5116
				for O0OO0O000O0OO0000 ,OO0O000O0O00O00OO ,O0OO0O0O000OOO00O in zip (O0O0OOO0O0OOOOOOO ["值"].values ,O0O0OOO0O0OOOOOOO ["查找位置"].values ,O0O0OOO0O0OOOOOOO ["排除值"].values ):#line:5118
					O0OO0000000OO0000 =O00000OO00OOO0OO0 .copy ()#line:5119
					O000OOOO0OOO0O00O =TOOLS_get_list (O0OO0O000O0OO0000 )[0 ]#line:5120
					O0OO0000000OO0000 ["关键字查找列"]=""#line:5122
					for O0O0O00OOOO0O0OO0 in TOOLS_get_list (OO0O000O0O00O00OO ):#line:5123
						O0OO0000000OO0000 ["关键字查找列"]=O0OO0000000OO0000 ["关键字查找列"]+O0OO0000000OO0000 [O0O0O00OOOO0O0OO0 ].astype ("str")#line:5124
					O0OO0000000OO0000 .loc [O0OO0000000OO0000 ["关键字查找列"].str .contains (O0OO0O000O0OO0000 ,na =False ),"关键字"]=O000OOOO0OOO0O00O #line:5126
					if str (O0OO0O0O000OOO00O )!="nan":#line:5129
						O0OO0000000OO0000 =O0OO0000000OO0000 .loc [~O0OO0000000OO0000 ["关键字查找列"].str .contains (O0OO0O0O000OOO00O ,na =False )].copy ()#line:5130
					if (len (O0OO0000000OO0000 ))<1 :#line:5132
						continue #line:5133
					O0O0O0OO0OOOOOO00 =STAT_find_keyword_risk (O0OO0000000OO0000 ,["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","关键字"],"关键字",O0OO00000O0OO000O ,int (OOOO0O0O00000O0OO ))#line:5135
					if len (O0O0O0OO0OOOOOO00 )>0 :#line:5136
						O0O0O0OO0OOOOOO00 ["关键字组合"]=O0OO0O000O0OO0000 #line:5137
						O0O0O0OO0OOOOOO00 ["排除值"]=O0OO0O0O000OOO00O #line:5138
						O0O0O0OO0OOOOOO00 ["关键字查找列"]=OO0O000O0O00O00OO #line:5139
						O0OO00OO0000OOOOO .append (O0O0O0OO0OOOOOO00 )#line:5140
		OO0OOOOOO0OOOO0O0 =pd .concat (O0OO00OO0000OOOOO )#line:5144
		OO0OOOOOO0OOOO0O0 =pd .merge (OO0OOOOOO0OOOO0O0 ,OO00O0OOO0O0O0OO0 ,on =OO0O0000OOO0O000O ,how ="left")#line:5147
		OO0OOOOOO0OOOO0O0 ["关键字数量比例"]=round (OO0OOOOOO0OOOO0O0 ["计数"]/OO0OOOOOO0OOOO0O0 ["该元素总数量"],2 )#line:5148
		OO0OOOOOO0OOOO0O0 =OO0OOOOOO0OOOO0O0 .reset_index (drop =True )#line:5150
		if len (OO0OOOOOO0OOOO0O0 )>0 :#line:5151
			OO0OOOOOO0OOOO0O0 ["风险评分"]=0 #line:5152
			OO0OOOOOO0OOOO0O0 ["报表类型"]="keyword_findrisk"+O0OO00000O0OO000O #line:5153
			OO0OOOOOO0OOOO0O0 .loc [(OO0OOOOOO0OOOO0O0 ["计数"]>=3 ),"风险评分"]=OO0OOOOOO0OOOO0O0 ["风险评分"]+3 #line:5154
			OO0OOOOOO0OOOO0O0 .loc [(OO0OOOOOO0OOOO0O0 ["计数"]>=(OO0OOOOOO0OOOO0O0 ["数量均值"]+OO0OOOOOO0OOOO0O0 ["数量标准差"])),"风险评分"]=OO0OOOOOO0OOOO0O0 ["风险评分"]+1 #line:5155
			OO0OOOOOO0OOOO0O0 .loc [(OO0OOOOOO0OOOO0O0 ["计数"]>=OO0OOOOOO0OOOO0O0 ["数量CI"]),"风险评分"]=OO0OOOOOO0OOOO0O0 ["风险评分"]+1 #line:5156
			OO0OOOOOO0OOOO0O0 .loc [(OO0OOOOOO0OOOO0O0 ["关键字数量比例"]>0.5 )&(OO0OOOOOO0OOOO0O0 ["计数"]>=3 ),"风险评分"]=OO0OOOOOO0OOOO0O0 ["风险评分"]+1 #line:5157
			OO0OOOOOO0OOOO0O0 .loc [(OO0OOOOOO0OOOO0O0 ["严重伤害数"]>=3 ),"风险评分"]=OO0OOOOOO0OOOO0O0 ["风险评分"]+1 #line:5158
			OO0OOOOOO0OOOO0O0 .loc [(OO0OOOOOO0OOOO0O0 ["单位个数"]>=3 ),"风险评分"]=OO0OOOOOO0OOOO0O0 ["风险评分"]+1 #line:5159
			OO0OOOOOO0OOOO0O0 .loc [(OO0OOOOOO0OOOO0O0 ["死亡数量"]>=1 ),"风险评分"]=OO0OOOOOO0OOOO0O0 ["风险评分"]+10 #line:5160
			OO0OOOOOO0OOOO0O0 ["风险评分"]=OO0OOOOOO0OOOO0O0 ["风险评分"]+OO0OOOOOO0OOOO0O0 ["单位个数"]/100 #line:5161
			OO0OOOOOO0OOOO0O0 =OO0OOOOOO0OOOO0O0 .sort_values (by ="风险评分",ascending =[False ],na_position ="last").reset_index (drop =True )#line:5162
		print ("耗时：",(time .time ()-O00OOO0O0000OO000 ))#line:5168
		return OO0OOOOOO0OOOO0O0 #line:5169
	def df_ror (O0OO00O0O0O0OO000 ,O0OOOO0O00OO0OOO0 ,*OO0000OOO00O0000O ):#line:5172
		""#line:5173
		OOO00OO0000O0000O =O0OO00O0O0O0OO000 .df .copy ()#line:5175
		O000000O000OOO000 =time .time ()#line:5176
		O000O0O00OOO0O000 =peizhidir +"0（范例）比例失衡关键字库.xls"#line:5177
		if "报告类型-新的"in OOO00OO0000O0000O .columns :#line:5178
			O0O00O0O0OO0O0O00 ="药品"#line:5179
		else :#line:5181
			O0O00O0O0OO0O0O00 ="器械"#line:5182
		O0OO0O0O0O0OO0OOO =pd .read_excel (O000O0O00OOO0O000 ,header =0 ,sheet_name =O0O00O0O0OO0O0O00 ).reset_index (drop =True )#line:5183
		if "css"in OOO00OO0000O0000O .columns :#line:5186
			OOO00O000O0O0OO0O =OOO00OO0000O0000O .copy ()#line:5187
			OOO00O000O0O0OO0O ["器械故障表现"]=OOO00O000O0O0OO0O ["器械故障表现"].fillna ("未填写")#line:5188
			OOO00O000O0O0OO0O ["器械故障表现"]=OOO00O000O0O0OO0O ["器械故障表现"].str .replace ("*","",regex =False )#line:5189
			OOOOOOOO0O000OO0O ="use("+str ("器械故障表现")+").file"#line:5190
			OOOO0000O000OO0OO =str (Counter (TOOLS_get_list0 (OOOOOOOO0O000OO0O ,OOO00O000O0O0OO0O ,1000 ))).replace ("Counter({","{")#line:5191
			OOOO0000O000OO0OO =OOOO0000O000OO0OO .replace ("})","}")#line:5192
			OOOO0000O000OO0OO =ast .literal_eval (OOOO0000O000OO0OO )#line:5193
			O0OO0O0O0O0OO0OOO =pd .DataFrame .from_dict (OOOO0000O000OO0OO ,orient ="index",columns =["计数"]).reset_index ()#line:5194
			O0OO0O0O0O0OO0OOO ["适用范围列"]="产品类别"#line:5195
			O0OO0O0O0O0OO0OOO ["适用范围"]="无源"#line:5196
			O0OO0O0O0O0OO0OOO ["查找位置"]="伤害表现"#line:5197
			O0OO0O0O0O0OO0OOO ["值"]=O0OO0O0O0O0OO0OOO ["index"]#line:5198
			O0OO0O0O0O0OO0OOO ["排除值"]="-没有排除值-"#line:5199
			del O0OO0O0O0O0OO0OOO ["index"]#line:5200
		OOO0OOO0O000OO000 =O0OOOO0O00OO0OOO0 [-2 ]#line:5203
		O0OOOO0O0OOOOO0OO =O0OOOO0O00OO0OOO0 [-1 ]#line:5204
		OOOOOOOOOO00OOOOO =O0OOOO0O00OO0OOO0 [:-1 ]#line:5205
		try :#line:5208
			if len (OO0000OOO00O0000O [0 ])>0 :#line:5209
				OOO0OOO0O000OO000 =O0OOOO0O00OO0OOO0 [-3 ]#line:5210
				O0OO0O0O0O0OO0OOO =O0OO0O0O0O0OO0OOO .loc [O0OO0O0O0O0OO0OOO ["适用范围"].str .contains (OO0000OOO00O0000O [0 ],na =False )].copy ().reset_index (drop =True )#line:5211
				OO0OOO0O00000O00O =OOO00OO0000O0000O .groupby (["产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号"]).agg (该元素总数量 =(O0OOOO0O0OOOOO0OO ,"count"),该元素严重伤害数 =("伤害",lambda O0O000OO0000OO000 :STAT_countpx (O0O000OO0000OO000 .values ,"严重伤害")),该元素死亡数量 =("伤害",lambda OO00OO0O0O00O00OO :STAT_countpx (OO00OO0O0O00O00OO .values ,"死亡")),该元素单位个数 =("单位名称","nunique"),该元素单位列表 =("单位名称",STAT_countx ),).reset_index ()#line:5218
				OOO0O0OO0O00OOO00 =OOO00OO0000O0000O .groupby (["产品类别","规整后品类"]).agg (所有元素总数量 =(OOO0OOO0O000OO000 ,"count"),所有元素严重伤害数 =("伤害",lambda O00O00OO0O00O00OO :STAT_countpx (O00O00OO0O00O00OO .values ,"严重伤害")),所有元素死亡数量 =("伤害",lambda O0O0O00OO00OO00O0 :STAT_countpx (O0O0O00OO00OO00O0 .values ,"死亡")),)#line:5223
				if len (OOO0O0OO0O00OOO00 )>1 :#line:5224
					text .insert (END ,"注意，产品类别有两种，产品名称规整疑似不正确！")#line:5225
				OO0OOO0O00000O00O =pd .merge (OO0OOO0O00000O00O ,OOO0O0OO0O00OOO00 ,on =["产品类别","规整后品类"],how ="left").reset_index ()#line:5227
		except :#line:5229
			text .insert (END ,"\n目前结果为未进行名称规整的结果！\n")#line:5230
			OO0OOO0O00000O00O =OOO00OO0000O0000O .groupby (O0OOOO0O00OO0OOO0 ).agg (该元素总数量 =(O0OOOO0O0OOOOO0OO ,"count"),该元素严重伤害数 =("伤害",lambda O00O000OOOO0OOO0O :STAT_countpx (O00O000OOOO0OOO0O .values ,"严重伤害")),该元素死亡数量 =("伤害",lambda OO0OO0O0OOO00OO00 :STAT_countpx (OO0OO0O0OOO00OO00 .values ,"死亡")),该元素单位个数 =("单位名称","nunique"),该元素单位列表 =("单位名称",STAT_countx ),).reset_index ()#line:5237
			OOO0O0OO0O00OOO00 =OOO00OO0000O0000O .groupby (OOOOOOOOOO00OOOOO ).agg (所有元素总数量 =(OOO0OOO0O000OO000 ,"count"),所有元素严重伤害数 =("伤害",lambda OOOOO0OOOOO0OO000 :STAT_countpx (OOOOO0OOOOO0OO000 .values ,"严重伤害")),所有元素死亡数量 =("伤害",lambda O00O0OO0000OO00OO :STAT_countpx (O00O0OO0000OO00OO .values ,"死亡")),)#line:5243
			OO0OOO0O00000O00O =pd .merge (OO0OOO0O00000O00O ,OOO0O0OO0O00OOO00 ,on =OOOOOOOOOO00OOOOO ,how ="left").reset_index ()#line:5247
		OOO0O0OO0O00OOO00 =OOO0O0OO0O00OOO00 [(OOO0O0OO0O00OOO00 ["所有元素总数量"]>=3 )].reset_index ()#line:5249
		OOO0O000O000O0O00 =[]#line:5250
		if ("产品名称"not in OOO0O0OO0O00OOO00 .columns )and ("规整后品类"not in OOO0O0OO0O00OOO00 .columns ):#line:5252
			OOO0O0OO0O00OOO00 ["产品名称"]=OOO0O0OO0O00OOO00 ["产品类别"]#line:5253
		if "规整后品类"not in OOO0O0OO0O00OOO00 .columns :#line:5259
			OOO0O0OO0O00OOO00 ["规整后品类"]="不适用"#line:5260
		O0O00OOO0O0OO0O0O =0 #line:5263
		O00000O000O0OOO0O =int (len (OOO0O0OO0O00OOO00 ))#line:5264
		for OO0O00O0OOO00000O ,OO0OO00O0000OO0OO ,OOOOOO0O0O0000O00 ,OO0O0O0O00OO0OO0O in zip (OOO0O0OO0O00OOO00 ["规整后品类"],OOO0O0OO0O00OOO00 ["产品类别"],OOO0O0OO0O00OOO00 [OOO0OOO0O000OO000 ],OOO0O0OO0O00OOO00 ["所有元素总数量"]):#line:5265
			O0O00OOO0O0OO0O0O +=1 #line:5266
			if (time .time ()-O000000O000OOO000 )>3 :#line:5267
				root .attributes ("-topmost",True )#line:5268
				PROGRAM_change_schedule (O0O00OOO0O0OO0O0O ,O00000O000O0OOO0O )#line:5269
				root .attributes ("-topmost",False )#line:5270
			OOOOOOO0OOOO0OOOO =OOO00OO0000O0000O [(OOO00OO0000O0000O [OOO0OOO0O000OO000 ]==OOOOOO0O0O0000O00 )].copy ()#line:5271
			O0OO0O0O0O0OO0OOO ["SELECT"]=O0OO0O0O0O0OO0OOO .apply (lambda O0OO0OOOO00OOO0OO :((OO0O00O0OOO00000O in O0OO0OOOO00OOO0OO ["适用范围"])or (O0OO0OOOO00OOO0OO ["适用范围"]in OO0OO00O0000OO0OO )),axis =1 )#line:5272
			O0O0OOOO0000OOOOO =O0OO0O0O0O0OO0OOO [(O0OO0O0O0O0OO0OOO ["SELECT"]==True )].reset_index ()#line:5273
			if len (O0O0OOOO0000OOOOO )>0 :#line:5274
				for O00O0O0OO0OOOO000 ,OOO0OOO0O0OOOO0O0 ,O000O00O0000000OO in zip (O0O0OOOO0000OOOOO ["值"].values ,O0O0OOOO0000OOOOO ["查找位置"].values ,O0O0OOOO0000OOOOO ["排除值"].values ):#line:5276
					OOOOOOOOO00OOOOOO =OOOOOOO0OOOO0OOOO .copy ()#line:5277
					OO0O0O00O0OOO00O0 =TOOLS_get_list (O00O0O0OO0OOOO000 )[0 ]#line:5278
					OO0O0OO000O0O00O0 ="关键字查找列"#line:5279
					OOOOOOOOO00OOOOOO [OO0O0OO000O0O00O0 ]=""#line:5280
					for OOO0000OO0000O0OO in TOOLS_get_list (OOO0OOO0O0OOOO0O0 ):#line:5281
						OOOOOOOOO00OOOOOO [OO0O0OO000O0O00O0 ]=OOOOOOOOO00OOOOOO [OO0O0OO000O0O00O0 ]+OOOOOOOOO00OOOOOO [OOO0000OO0000O0OO ].astype ("str")#line:5282
					OOOOOOOOO00OOOOOO .loc [OOOOOOOOO00OOOOOO [OO0O0OO000O0O00O0 ].str .contains (O00O0O0OO0OOOO000 ,na =False ),"关键字"]=OO0O0O00O0OOO00O0 #line:5284
					if str (O000O00O0000000OO )!="nan":#line:5287
						OOOOOOOOO00OOOOOO =OOOOOOOOO00OOOOOO .loc [~OOOOOOOOO00OOOOOO ["关键字查找列"].str .contains (O000O00O0000000OO ,na =False )].copy ()#line:5288
					if (len (OOOOOOOOO00OOOOOO ))<1 :#line:5291
						continue #line:5292
					for O000O00OOO0O000OO in zip (OOOOOOOOO00OOOOOO [O0OOOO0O0OOOOO0OO ].drop_duplicates ()):#line:5294
						try :#line:5297
							if O000O00OOO0O000OO [0 ]!=OO0000OOO00O0000O [1 ]:#line:5298
								continue #line:5299
						except :#line:5300
							pass #line:5301
						OO00O0OOOO0OOOOOO ={"合并列":{OO0O0OO000O0O00O0 :OOO0OOO0O0OOOO0O0 },"等于":{OOO0OOO0O000OO000 :OOOOOO0O0O0000O00 ,O0OOOO0O0OOOOO0OO :O000O00OOO0O000OO [0 ]},"不等于":{},"包含":{OO0O0OO000O0O00O0 :O00O0O0OO0OOOO000 },"不包含":{OO0O0OO000O0O00O0 :O000O00O0000000OO }}#line:5309
						O0OO0OO0OO0OOO0O0 =STAT_PPR_ROR_1 (O0OOOO0O0OOOOO0OO ,str (O000O00OOO0O000OO [0 ]),"关键字查找列",O00O0O0OO0OOOO000 ,OOOOOOOOO00OOOOOO )+(O00O0O0OO0OOOO000 ,O000O00O0000000OO ,OOO0OOO0O0OOOO0O0 ,OOOOOO0O0O0000O00 ,O000O00OOO0O000OO [0 ],str (OO00O0OOOO0OOOOOO ))#line:5311
						if O0OO0OO0OO0OOO0O0 [1 ]>0 :#line:5313
							O0O0O0OO000O000O0 =pd .DataFrame (columns =["特定关键字","出现频次","占比","ROR值","ROR值的95%CI下限","PRR值","PRR值的95%CI下限","卡方值","四分表","关键字组合","排除值","关键字查找列",OOO0OOO0O000OO000 ,O0OOOO0O0OOOOO0OO ,"报表定位"])#line:5315
							O0O0O0OO000O000O0 .loc [0 ]=O0OO0OO0OO0OOO0O0 #line:5316
							OOO0O000O000O0O00 .append (O0O0O0OO000O000O0 )#line:5317
		OO0O0OOOO0000000O =pd .concat (OOO0O000O000O0O00 )#line:5321
		OO0O0OOOO0000000O =pd .merge (OO0OOO0O00000O00O ,OO0O0OOOO0000000O ,on =[OOO0OOO0O000OO000 ,O0OOOO0O0OOOOO0OO ],how ="right")#line:5325
		OO0O0OOOO0000000O =OO0O0OOOO0000000O .reset_index (drop =True )#line:5326
		del OO0O0OOOO0000000O ["index"]#line:5327
		if len (OO0O0OOOO0000000O )>0 :#line:5328
			OO0O0OOOO0000000O ["风险评分"]=0 #line:5329
			OO0O0OOOO0000000O ["报表类型"]="ROR"#line:5330
			OO0O0OOOO0000000O .loc [(OO0O0OOOO0000000O ["出现频次"]>=3 ),"风险评分"]=OO0O0OOOO0000000O ["风险评分"]+3 #line:5331
			OO0O0OOOO0000000O .loc [(OO0O0OOOO0000000O ["ROR值的95%CI下限"]>1 ),"风险评分"]=OO0O0OOOO0000000O ["风险评分"]+1 #line:5332
			OO0O0OOOO0000000O .loc [(OO0O0OOOO0000000O ["PRR值的95%CI下限"]>1 ),"风险评分"]=OO0O0OOOO0000000O ["风险评分"]+1 #line:5333
			OO0O0OOOO0000000O ["风险评分"]=OO0O0OOOO0000000O ["风险评分"]+OO0O0OOOO0000000O ["该元素单位个数"]/100 #line:5334
			OO0O0OOOO0000000O =OO0O0OOOO0000000O .sort_values (by ="风险评分",ascending =[False ],na_position ="last").reset_index (drop =True )#line:5335
		print ("耗时：",(time .time ()-O000000O000OOO000 ))#line:5341
		return OO0O0OOOO0000000O #line:5342
	def df_chiyouren (OOOO0OO0O0OO0000O ):#line:5348
		""#line:5349
		OO00000000O00OO0O =OOOO0OO0O0OO0000O .df .copy ().reset_index (drop =True )#line:5350
		OO00000000O00OO0O ["总报告数"]=data ["报告编码"].copy ()#line:5351
		OO00000000O00OO0O .loc [(OO00000000O00OO0O ["持有人报告状态"]=="待评价"),"总待评价数量"]=data ["报告编码"]#line:5352
		OO00000000O00OO0O .loc [(OO00000000O00OO0O ["伤害"]=="严重伤害"),"严重伤害报告数"]=data ["报告编码"]#line:5353
		OO00000000O00OO0O .loc [(OO00000000O00OO0O ["持有人报告状态"]=="待评价")&(OO00000000O00OO0O ["伤害"]=="严重伤害"),"严重伤害待评价数量"]=data ["报告编码"]#line:5354
		OO00000000O00OO0O .loc [(OO00000000O00OO0O ["持有人报告状态"]=="待评价")&(OO00000000O00OO0O ["伤害"]=="其他"),"其他待评价数量"]=data ["报告编码"]#line:5355
		OOOOOO00OO0O0OO00 =OO00000000O00OO0O .groupby (["上市许可持有人名称"]).aggregate ({"总报告数":"nunique","总待评价数量":"nunique","严重伤害报告数":"nunique","严重伤害待评价数量":"nunique","其他待评价数量":"nunique"})#line:5358
		OOOOOO00OO0O0OO00 ["严重伤害待评价比例"]=round (OOOOOO00OO0O0OO00 ["严重伤害待评价数量"]/OOOOOO00OO0O0OO00 ["严重伤害报告数"]*100 ,2 )#line:5363
		OOOOOO00OO0O0OO00 ["总待评价比例"]=round (OOOOOO00OO0O0OO00 ["总待评价数量"]/OOOOOO00OO0O0OO00 ["总报告数"]*100 ,2 )#line:5366
		OOOOOO00OO0O0OO00 ["总报告数"]=OOOOOO00OO0O0OO00 ["总报告数"].fillna (0 )#line:5367
		OOOOOO00OO0O0OO00 ["总待评价比例"]=OOOOOO00OO0O0OO00 ["总待评价比例"].fillna (0 )#line:5368
		OOOOOO00OO0O0OO00 ["严重伤害报告数"]=OOOOOO00OO0O0OO00 ["严重伤害报告数"].fillna (0 )#line:5369
		OOOOOO00OO0O0OO00 ["严重伤害待评价比例"]=OOOOOO00OO0O0OO00 ["严重伤害待评价比例"].fillna (0 )#line:5370
		OOOOOO00OO0O0OO00 ["总报告数"]=OOOOOO00OO0O0OO00 ["总报告数"].astype (int )#line:5371
		OOOOOO00OO0O0OO00 ["总待评价比例"]=OOOOOO00OO0O0OO00 ["总待评价比例"].astype (int )#line:5372
		OOOOOO00OO0O0OO00 ["严重伤害报告数"]=OOOOOO00OO0O0OO00 ["严重伤害报告数"].astype (int )#line:5373
		OOOOOO00OO0O0OO00 ["严重伤害待评价比例"]=OOOOOO00OO0O0OO00 ["严重伤害待评价比例"].astype (int )#line:5374
		OOOOOO00OO0O0OO00 =OOOOOO00OO0O0OO00 .sort_values (by =["总报告数","总待评价比例"],ascending =[False ,False ],na_position ="last")#line:5377
		if "场所名称"in OO00000000O00OO0O .columns :#line:5379
			OO00000000O00OO0O .loc [(OO00000000O00OO0O ["审核日期"]=="未填写"),"审核日期"]=3000 -12 -12 #line:5380
			OO00000000O00OO0O ["报告时限"]=pd .Timestamp .today ()-pd .to_datetime (OO00000000O00OO0O ["审核日期"])#line:5381
			OO00000000O00OO0O ["报告时限2"]=45 -(pd .Timestamp .today ()-pd .to_datetime (OO00000000O00OO0O ["审核日期"])).dt .days #line:5382
			OO00000000O00OO0O ["报告时限"]=OO00000000O00OO0O ["报告时限"].dt .days #line:5383
			OO00000000O00OO0O .loc [(OO00000000O00OO0O ["报告时限"]>45 )&(OO00000000O00OO0O ["伤害"]=="严重伤害")&(OO00000000O00OO0O ["持有人报告状态"]=="待评价"),"待评价且超出当前日期45天（严重）"]=1 #line:5384
			OO00000000O00OO0O .loc [(OO00000000O00OO0O ["报告时限"]>45 )&(OO00000000O00OO0O ["伤害"]=="其他")&(OO00000000O00OO0O ["持有人报告状态"]=="待评价"),"待评价且超出当前日期45天（其他）"]=1 #line:5385
			OO00000000O00OO0O .loc [(OO00000000O00OO0O ["报告时限"]>30 )&(OO00000000O00OO0O ["伤害"]=="死亡")&(OO00000000O00OO0O ["持有人报告状态"]=="待评价"),"待评价且超出当前日期30天（死亡）"]=1 #line:5386
			OO00000000O00OO0O .loc [(OO00000000O00OO0O ["报告时限2"]<=1 )&(OO00000000O00OO0O ["伤害"]=="严重伤害")&(OO00000000O00OO0O ["报告时限2"]>0 )&(OO00000000O00OO0O ["持有人报告状态"]=="待评价"),"严重待评价且只剩1天"]=1 #line:5388
			OO00000000O00OO0O .loc [(OO00000000O00OO0O ["报告时限2"]>1 )&(OO00000000O00OO0O ["报告时限2"]<=3 )&(OO00000000O00OO0O ["伤害"]=="严重伤害")&(OO00000000O00OO0O ["持有人报告状态"]=="待评价"),"严重待评价且只剩1-3天"]=1 #line:5389
			OO00000000O00OO0O .loc [(OO00000000O00OO0O ["报告时限2"]>3 )&(OO00000000O00OO0O ["报告时限2"]<=5 )&(OO00000000O00OO0O ["伤害"]=="严重伤害")&(OO00000000O00OO0O ["持有人报告状态"]=="待评价"),"严重待评价且只剩3-5天"]=1 #line:5390
			OO00000000O00OO0O .loc [(OO00000000O00OO0O ["报告时限2"]>5 )&(OO00000000O00OO0O ["报告时限2"]<=10 )&(OO00000000O00OO0O ["伤害"]=="严重伤害")&(OO00000000O00OO0O ["持有人报告状态"]=="待评价"),"严重待评价且只剩5-10天"]=1 #line:5391
			OO00000000O00OO0O .loc [(OO00000000O00OO0O ["报告时限2"]>10 )&(OO00000000O00OO0O ["报告时限2"]<=20 )&(OO00000000O00OO0O ["伤害"]=="严重伤害")&(OO00000000O00OO0O ["持有人报告状态"]=="待评价"),"严重待评价且只剩10-20天"]=1 #line:5392
			OO00000000O00OO0O .loc [(OO00000000O00OO0O ["报告时限2"]>20 )&(OO00000000O00OO0O ["报告时限2"]<=30 )&(OO00000000O00OO0O ["伤害"]=="严重伤害")&(OO00000000O00OO0O ["持有人报告状态"]=="待评价"),"严重待评价且只剩20-30天"]=1 #line:5393
			OO00000000O00OO0O .loc [(OO00000000O00OO0O ["报告时限2"]>30 )&(OO00000000O00OO0O ["报告时限2"]<=45 )&(OO00000000O00OO0O ["伤害"]=="严重伤害")&(OO00000000O00OO0O ["持有人报告状态"]=="待评价"),"严重待评价且只剩30-45天"]=1 #line:5394
			del OO00000000O00OO0O ["报告时限2"]#line:5395
			O0000OOOO000OOO00 =(OO00000000O00OO0O .groupby (["上市许可持有人名称"]).aggregate ({"待评价且超出当前日期45天（严重）":"sum","待评价且超出当前日期45天（其他）":"sum","待评价且超出当前日期30天（死亡）":"sum","严重待评价且只剩1天":"sum","严重待评价且只剩1-3天":"sum","严重待评价且只剩3-5天":"sum","严重待评价且只剩5-10天":"sum","严重待评价且只剩10-20天":"sum","严重待评价且只剩20-30天":"sum","严重待评价且只剩30-45天":"sum"}).reset_index ())#line:5397
			OOOOOO00OO0O0OO00 =pd .merge (OOOOOO00OO0O0OO00 ,O0000OOOO000OOO00 ,on =["上市许可持有人名称"],how ="outer",)#line:5398
			OOOOOO00OO0O0OO00 ["待评价且超出当前日期45天（严重）"]=OOOOOO00OO0O0OO00 ["待评价且超出当前日期45天（严重）"].fillna (0 )#line:5399
			OOOOOO00OO0O0OO00 ["待评价且超出当前日期45天（严重）"]=OOOOOO00OO0O0OO00 ["待评价且超出当前日期45天（严重）"].astype (int )#line:5400
			OOOOOO00OO0O0OO00 ["待评价且超出当前日期45天（其他）"]=OOOOOO00OO0O0OO00 ["待评价且超出当前日期45天（其他）"].fillna (0 )#line:5401
			OOOOOO00OO0O0OO00 ["待评价且超出当前日期45天（其他）"]=OOOOOO00OO0O0OO00 ["待评价且超出当前日期45天（其他）"].astype (int )#line:5402
			OOOOOO00OO0O0OO00 ["待评价且超出当前日期30天（死亡）"]=OOOOOO00OO0O0OO00 ["待评价且超出当前日期30天（死亡）"].fillna (0 )#line:5403
			OOOOOO00OO0O0OO00 ["待评价且超出当前日期30天（死亡）"]=OOOOOO00OO0O0OO00 ["待评价且超出当前日期30天（死亡）"].astype (int )#line:5404
			OOOOOO00OO0O0OO00 ["严重待评价且只剩1天"]=OOOOOO00OO0O0OO00 ["严重待评价且只剩1天"].fillna (0 )#line:5406
			OOOOOO00OO0O0OO00 ["严重待评价且只剩1天"]=OOOOOO00OO0O0OO00 ["严重待评价且只剩1天"].astype (int )#line:5407
			OOOOOO00OO0O0OO00 ["严重待评价且只剩1-3天"]=OOOOOO00OO0O0OO00 ["严重待评价且只剩1-3天"].fillna (0 )#line:5408
			OOOOOO00OO0O0OO00 ["严重待评价且只剩1-3天"]=OOOOOO00OO0O0OO00 ["严重待评价且只剩1-3天"].astype (int )#line:5409
			OOOOOO00OO0O0OO00 ["严重待评价且只剩3-5天"]=OOOOOO00OO0O0OO00 ["严重待评价且只剩3-5天"].fillna (0 )#line:5410
			OOOOOO00OO0O0OO00 ["严重待评价且只剩3-5天"]=OOOOOO00OO0O0OO00 ["严重待评价且只剩3-5天"].astype (int )#line:5411
			OOOOOO00OO0O0OO00 ["严重待评价且只剩5-10天"]=OOOOOO00OO0O0OO00 ["严重待评价且只剩5-10天"].fillna (0 )#line:5412
			OOOOOO00OO0O0OO00 ["严重待评价且只剩5-10天"]=OOOOOO00OO0O0OO00 ["严重待评价且只剩5-10天"].astype (int )#line:5413
			OOOOOO00OO0O0OO00 ["严重待评价且只剩10-20天"]=OOOOOO00OO0O0OO00 ["严重待评价且只剩10-20天"].fillna (0 )#line:5414
			OOOOOO00OO0O0OO00 ["严重待评价且只剩10-20天"]=OOOOOO00OO0O0OO00 ["严重待评价且只剩10-20天"].astype (int )#line:5415
			OOOOOO00OO0O0OO00 ["严重待评价且只剩20-30天"]=OOOOOO00OO0O0OO00 ["严重待评价且只剩20-30天"].fillna (0 )#line:5416
			OOOOOO00OO0O0OO00 ["严重待评价且只剩20-30天"]=OOOOOO00OO0O0OO00 ["严重待评价且只剩20-30天"].astype (int )#line:5417
			OOOOOO00OO0O0OO00 ["严重待评价且只剩30-45天"]=OOOOOO00OO0O0OO00 ["严重待评价且只剩30-45天"].fillna (0 )#line:5418
			OOOOOO00OO0O0OO00 ["严重待评价且只剩30-45天"]=OOOOOO00OO0O0OO00 ["严重待评价且只剩30-45天"].astype (int )#line:5419
		OOOOOO00OO0O0OO00 ["总待评价数量"]=OOOOOO00OO0O0OO00 ["总待评价数量"].fillna (0 )#line:5421
		OOOOOO00OO0O0OO00 ["总待评价数量"]=OOOOOO00OO0O0OO00 ["总待评价数量"].astype (int )#line:5422
		OOOOOO00OO0O0OO00 ["严重伤害待评价数量"]=OOOOOO00OO0O0OO00 ["严重伤害待评价数量"].fillna (0 )#line:5423
		OOOOOO00OO0O0OO00 ["严重伤害待评价数量"]=OOOOOO00OO0O0OO00 ["严重伤害待评价数量"].astype (int )#line:5424
		OOOOOO00OO0O0OO00 ["其他待评价数量"]=OOOOOO00OO0O0OO00 ["其他待评价数量"].fillna (0 )#line:5425
		OOOOOO00OO0O0OO00 ["其他待评价数量"]=OOOOOO00OO0O0OO00 ["其他待评价数量"].astype (int )#line:5426
		O0000OOOO00000O0O =["总报告数","总待评价数量","严重伤害报告数","严重伤害待评价数量","其他待评价数量"]#line:5429
		OOOOOO00OO0O0OO00 .loc ["合计"]=OOOOOO00OO0O0OO00 [O0000OOOO00000O0O ].apply (lambda OO0O00O0O00O00OOO :OO0O00O0O00O00OOO .sum ())#line:5430
		OOOOOO00OO0O0OO00 [O0000OOOO00000O0O ]=OOOOOO00OO0O0OO00 [O0000OOOO00000O0O ].apply (lambda O0OO00OOOOOO00O0O :O0OO00OOOOOO00O0O .astype (int ))#line:5431
		OOOOOO00OO0O0OO00 .iloc [-1 ,0 ]="合计"#line:5432
		if "场所名称"in OO00000000O00OO0O .columns :#line:5434
			OOOOOO00OO0O0OO00 =OOOOOO00OO0O0OO00 .reset_index (drop =True )#line:5435
		else :#line:5436
			OOOOOO00OO0O0OO00 =OOOOOO00OO0O0OO00 .reset_index ()#line:5437
		if ini ["模式"]=="药品":#line:5439
			OOOOOO00OO0O0OO00 =OOOOOO00OO0O0OO00 .rename (columns ={"总待评价数量":"新的数量"})#line:5440
			OOOOOO00OO0O0OO00 =OOOOOO00OO0O0OO00 .rename (columns ={"严重伤害待评价数量":"新的严重的数量"})#line:5441
			OOOOOO00OO0O0OO00 =OOOOOO00OO0O0OO00 .rename (columns ={"严重伤害待评价比例":"新的严重的比例"})#line:5442
			OOOOOO00OO0O0OO00 =OOOOOO00OO0O0OO00 .rename (columns ={"总待评价比例":"新的比例"})#line:5443
			del OOOOOO00OO0O0OO00 ["其他待评价数量"]#line:5445
		OOOOOO00OO0O0OO00 ["报表类型"]="dfx_chiyouren"#line:5446
		return OOOOOO00OO0O0OO00 #line:5447
	def df_age (O000OOO0000OO00OO ):#line:5449
		""#line:5450
		O00O00O0O000OO0OO =O000OOO0000OO00OO .df .copy ()#line:5451
		O00O00O0O000OO0OO =O00O00O0O000OO0OO .drop_duplicates ("报告编码").copy ()#line:5452
		O0OO000000000OOOO =pd .pivot_table (O00O00O0O000OO0OO .drop_duplicates ("报告编码"),values =["报告编码"],index ="年龄段",columns ="性别",aggfunc ={"报告编码":"nunique"},fill_value ="0",margins =True ,dropna =False ,).rename (columns ={"报告编码":"数量"}).reset_index ()#line:5453
		O0OO000000000OOOO .columns =O0OO000000000OOOO .columns .droplevel (0 )#line:5454
		O0OO000000000OOOO ["构成比(%)"]=round (100 *O0OO000000000OOOO ["All"]/len (O00O00O0O000OO0OO ),2 )#line:5455
		O0OO000000000OOOO ["累计构成比(%)"]=O0OO000000000OOOO ["构成比(%)"].cumsum ()#line:5456
		O0OO000000000OOOO ["报表类型"]="年龄性别表"#line:5457
		return O0OO000000000OOOO #line:5458
	def df_psur (OO0OOO00OOOO000OO ,*OO0O0O0OO0OO0OOOO ):#line:5460
		""#line:5461
		O000O00O0O0O00O0O =OO0OOO00OOOO000OO .df .copy ()#line:5462
		O00O0OOO0O00O000O =peizhidir +"0（范例）比例失衡关键字库.xls"#line:5463
		OO00OOOO000OO0000 =len (O000O00O0O0O00O0O .drop_duplicates ("报告编码"))#line:5464
		if "报告类型-新的"in O000O00O0O0O00O0O .columns :#line:5468
			OOO00O000O00000OO ="药品"#line:5469
		elif "皮损形态"in O000O00O0O0O00O0O .columns :#line:5470
			OOO00O000O00000OO ="化妆品"#line:5471
		else :#line:5472
			OOO00O000O00000OO ="器械"#line:5473
		O0O00OOO000O00OOO =pd .read_excel (O00O0OOO0O00O000O ,header =0 ,sheet_name =OOO00O000O00000OO )#line:5476
		O0O0OOOO00O00OO00 =(O0O00OOO000O00OOO .loc [O0O00OOO000O00OOO ["适用范围"].str .contains ("通用监测关键字|无源|有源",na =False )].copy ().reset_index (drop =True ))#line:5479
		try :#line:5482
			if OO0O0O0OO0OO0OOOO [0 ]in ["特定品种","通用无源","通用有源"]:#line:5483
				OO0000OOO0O0OO000 =""#line:5484
				if OO0O0O0OO0OO0OOOO [0 ]=="特定品种":#line:5485
					OO0000OOO0O0OO000 =O0O00OOO000O00OOO .loc [O0O00OOO000O00OOO ["适用范围"].str .contains (OO0O0O0OO0OO0OOOO [1 ],na =False )].copy ().reset_index (drop =True )#line:5486
				if OO0O0O0OO0OO0OOOO [0 ]=="通用无源":#line:5488
					OO0000OOO0O0OO000 =O0O00OOO000O00OOO .loc [O0O00OOO000O00OOO ["适用范围"].str .contains ("通用监测关键字|无源",na =False )].copy ().reset_index (drop =True )#line:5489
				if OO0O0O0OO0OO0OOOO [0 ]=="通用有源":#line:5490
					OO0000OOO0O0OO000 =O0O00OOO000O00OOO .loc [O0O00OOO000O00OOO ["适用范围"].str .contains ("通用监测关键字|有源",na =False )].copy ().reset_index (drop =True )#line:5491
				if OO0O0O0OO0OO0OOOO [0 ]=="体外诊断试剂":#line:5492
					OO0000OOO0O0OO000 =O0O00OOO000O00OOO .loc [O0O00OOO000O00OOO ["适用范围"].str .contains ("体外诊断试剂",na =False )].copy ().reset_index (drop =True )#line:5493
				if len (OO0000OOO0O0OO000 )<1 :#line:5494
					showinfo (title ="提示",message ="未找到相应的自定义规则，任务结束。")#line:5495
					return 0 #line:5496
				else :#line:5497
					O0O0OOOO00O00OO00 =OO0000OOO0O0OO000 #line:5498
		except :#line:5500
			pass #line:5501
		try :#line:5505
			if OOO00O000O00000OO =="器械"and OO0O0O0OO0OO0OOOO [0 ]=="特定品种作为通用关键字":#line:5506
				O0O0OOOO00O00OO00 =OO0O0O0OO0OO0OOOO [1 ]#line:5507
		except dddd :#line:5509
			pass #line:5510
		O0O000OOOOO0OOO00 =""#line:5513
		O0OO000OOOO0O00OO ="-其他关键字-不含："#line:5514
		for OO0O0O0OO0O000OOO ,O0OOOOOOO0000OO0O in O0O0OOOO00O00OO00 .iterrows ():#line:5515
			O0OO000OOOO0O00OO =O0OO000OOOO0O00OO +"|"+str (O0OOOOOOO0000OO0O ["值"])#line:5516
			O0OOOOO00OO0O000O =O0OOOOOOO0000OO0O #line:5517
		O0OOOOO00OO0O000O [2 ]="通用监测关键字"#line:5518
		O0OOOOO00OO0O000O [4 ]=O0OO000OOOO0O00OO #line:5519
		O0O0OOOO00O00OO00 .loc [len (O0O0OOOO00O00OO00 )]=O0OOOOO00OO0O000O #line:5520
		O0O0OOOO00O00OO00 =O0O0OOOO00O00OO00 .reset_index (drop =True )#line:5521
		if ini ["模式"]=="器械":#line:5525
			O000O00O0O0O00O0O ["关键字查找列"]=O000O00O0O0O00O0O ["器械故障表现"].astype (str )+O000O00O0O0O00O0O ["伤害表现"].astype (str )+O000O00O0O0O00O0O ["使用过程"].astype (str )+O000O00O0O0O00O0O ["事件原因分析描述"].astype (str )+O000O00O0O0O00O0O ["初步处置情况"].astype (str )#line:5526
		else :#line:5527
			O000O00O0O0O00O0O ["关键字查找列"]=O000O00O0O0O00O0O ["器械故障表现"]#line:5528
		text .insert (END ,"\n药品查找列默认为不良反应表现,药品规则默认为通用规则。\n器械默认查找列为器械故障表现+伤害表现+使用过程+事件原因分析描述+初步处置情况，器械默认规则为无源通用规则+有源通用规则。\n")#line:5529
		O0OOOOO0OO0000OO0 =[]#line:5531
		for OO0O0O0OO0O000OOO ,O0OOOOOOO0000OO0O in O0O0OOOO00O00OO00 .iterrows ():#line:5533
			OOO00000000000OOO =O0OOOOOOO0000OO0O ["值"]#line:5534
			if "-其他关键字-"not in OOO00000000000OOO :#line:5536
				OO000O00O0OO00000 =O000O00O0O0O00O0O .loc [O000O00O0O0O00O0O ["关键字查找列"].str .contains (OOO00000000000OOO ,na =False )].copy ()#line:5539
				if str (O0OOOOOOO0000OO0O ["排除值"])!="nan":#line:5540
					OO000O00O0OO00000 =OO000O00O0OO00000 .loc [~OO000O00O0OO00000 ["关键字查找列"].str .contains (str (O0OOOOOOO0000OO0O ["排除值"]),na =False )].copy ()#line:5542
			else :#line:5544
				OO000O00O0OO00000 =O000O00O0O0O00O0O .loc [~O000O00O0O0O00O0O ["关键字查找列"].str .contains (OOO00000000000OOO ,na =False )].copy ()#line:5547
			OO000O00O0OO00000 ["关键字标记"]=str (OOO00000000000OOO )#line:5548
			OO000O00O0OO00000 ["关键字计数"]=1 #line:5549
			if len (OO000O00O0OO00000 )>0 :#line:5555
				try :#line:5556
					OO000OO0000O0O000 =pd .pivot_table (OO000O00O0OO00000 .drop_duplicates ("报告编码"),values =["关键字计数"],index ="关键字标记",columns ="伤害PSUR",aggfunc ={"关键字计数":"count"},fill_value ="0",margins =True ,dropna =False ,)#line:5566
				except :#line:5568
					OO000OO0000O0O000 =pd .pivot_table (OO000O00O0OO00000 .drop_duplicates ("报告编码"),values =["关键字计数"],index ="关键字标记",columns ="伤害",aggfunc ={"关键字计数":"count"},fill_value ="0",margins =True ,dropna =False ,)#line:5578
				OO000OO0000O0O000 =OO000OO0000O0O000 [:-1 ]#line:5579
				OO000OO0000O0O000 .columns =OO000OO0000O0O000 .columns .droplevel (0 )#line:5580
				OO000OO0000O0O000 =OO000OO0000O0O000 .reset_index ()#line:5581
				if len (OO000OO0000O0O000 )>0 :#line:5584
					O00OOO0OO00O00O0O =str (Counter (TOOLS_get_list0 ("use(器械故障表现).file",OO000O00O0OO00000 ,1000 ))).replace ("Counter({","{")#line:5585
					O00OOO0OO00O00O0O =O00OOO0OO00O00O0O .replace ("})","}")#line:5586
					O00OOO0OO00O00O0O =ast .literal_eval (O00OOO0OO00O00O0O )#line:5587
					OO000OO0000O0O000 .loc [0 ,"事件分类"]=str (TOOLS_get_list (OO000OO0000O0O000 .loc [0 ,"关键字标记"])[0 ])#line:5589
					OO000OO0000O0O000 .loc [0 ,"不良事件名称1"]=str ({O0OOO0OOO000O00O0 :O0O0000OOO0O0OO0O for O0OOO0OOO000O00O0 ,O0O0000OOO0O0OO0O in O00OOO0OO00O00O0O .items ()if STAT_judge_x (str (O0OOO0OOO000O00O0 ),TOOLS_get_list (OOO00000000000OOO ))==1 })#line:5590
					OO000OO0000O0O000 .loc [0 ,"不良事件名称2"]=str ({O000OO00OO0O000OO :OO00O0OO00OO00OOO for O000OO00OO0O000OO ,OO00O0OO00OO00OOO in O00OOO0OO00O00O0O .items ()if STAT_judge_x (str (O000OO00OO0O000OO ),TOOLS_get_list (OOO00000000000OOO ))!=1 })#line:5591
					if ini ["模式"]=="药品":#line:5602
						for OO00OOOOOO00OO0O0 in ["SOC","HLGT","HLT","PT"]:#line:5603
							OO000OO0000O0O000 [OO00OOOOOO00OO0O0 ]=O0OOOOOOO0000OO0O [OO00OOOOOO00OO0O0 ]#line:5604
					if ini ["模式"]=="器械":#line:5605
						for OO00OOOOOO00OO0O0 in ["国家故障术语集（大类）","国家故障术语集（小类）","IMDRF有关术语（故障）","国家伤害术语集（大类）","国家伤害术语集（小类）","IMDRF有关术语（伤害）"]:#line:5606
							OO000OO0000O0O000 [OO00OOOOOO00OO0O0 ]=O0OOOOOOO0000OO0O [OO00OOOOOO00OO0O0 ]#line:5607
					O0OOOOO0OO0000OO0 .append (OO000OO0000O0O000 )#line:5610
		O0O000OOOOO0OOO00 =pd .concat (O0OOOOO0OO0000OO0 )#line:5611
		O0O000OOOOO0OOO00 =O0O000OOOOO0OOO00 .sort_values (by =["All"],ascending =[False ],na_position ="last")#line:5616
		O0O000OOOOO0OOO00 =O0O000OOOOO0OOO00 .reset_index ()#line:5617
		O0O000OOOOO0OOO00 ["All占比"]=round (O0O000OOOOO0OOO00 ["All"]/OO00OOOO000OO0000 *100 ,2 )#line:5619
		O0O000OOOOO0OOO00 =O0O000OOOOO0OOO00 .rename (columns ={"All":"总数量","All占比":"总数量占比"})#line:5620
		try :#line:5621
			O0O000OOOOO0OOO00 =O0O000OOOOO0OOO00 .rename (columns ={"其他":"一般"})#line:5622
		except :#line:5623
			pass #line:5624
		try :#line:5626
			O0O000OOOOO0OOO00 =O0O000OOOOO0OOO00 .rename (columns ={" 一般":"一般"})#line:5627
		except :#line:5628
			pass #line:5629
		try :#line:5630
			O0O000OOOOO0OOO00 =O0O000OOOOO0OOO00 .rename (columns ={" 严重":"严重"})#line:5631
		except :#line:5632
			pass #line:5633
		try :#line:5634
			O0O000OOOOO0OOO00 =O0O000OOOOO0OOO00 .rename (columns ={"严重伤害":"严重"})#line:5635
		except :#line:5636
			pass #line:5637
		try :#line:5638
			O0O000OOOOO0OOO00 =O0O000OOOOO0OOO00 .rename (columns ={"死亡":"死亡(仅支持器械)"})#line:5639
		except :#line:5640
			pass #line:5641
		for O00O000O0OOOOO0O0 in ["一般","新的一般","严重","新的严重"]:#line:5644
			if O00O000O0OOOOO0O0 not in O0O000OOOOO0OOO00 .columns :#line:5645
				O0O000OOOOO0OOO00 [O00O000O0OOOOO0O0 ]=0 #line:5646
		try :#line:5648
			O0O000OOOOO0OOO00 ["严重比"]=round ((O0O000OOOOO0OOO00 ["严重"].fillna (0 )+O0O000OOOOO0OOO00 ["死亡(仅支持器械)"].fillna (0 ))/O0O000OOOOO0OOO00 ["总数量"]*100 ,2 )#line:5649
		except :#line:5650
			O0O000OOOOO0OOO00 ["严重比"]=round ((O0O000OOOOO0OOO00 ["严重"].fillna (0 )+O0O000OOOOO0OOO00 ["新的严重"].fillna (0 ))/O0O000OOOOO0OOO00 ["总数量"]*100 ,2 )#line:5651
		O0O000OOOOO0OOO00 ["构成比"]=round ((O0O000OOOOO0OOO00 ["总数量"].fillna (0 ))/O0O000OOOOO0OOO00 ["总数量"].sum ()*100 ,2 )#line:5653
		if ini ["模式"]=="药品":#line:5655
			try :#line:5656
				O0O000OOOOO0OOO00 =O0O000OOOOO0OOO00 [["关键字标记","一般","新的一般","严重","新的严重","总数量","总数量占比","构成比","严重比","事件分类","不良事件名称1","不良事件名称2","死亡(仅支持器械)","SOC","HLGT","HLT","PT"]]#line:5657
			except :#line:5658
				O0O000OOOOO0OOO00 =O0O000OOOOO0OOO00 [["关键字标记","一般","新的一般","严重","新的严重","总数量","总数量占比","构成比","严重比","事件分类","不良事件名称1","不良事件名称2","SOC","HLGT","HLT","PT"]]#line:5659
		elif ini ["模式"]=="器械":#line:5660
			try :#line:5661
				O0O000OOOOO0OOO00 =O0O000OOOOO0OOO00 [["关键字标记","一般","新的一般","严重","新的严重","总数量","总数量占比","构成比","严重比","事件分类","不良事件名称1","不良事件名称2","死亡(仅支持器械)","国家故障术语集（大类）","国家故障术语集（小类）","IMDRF有关术语（故障）","国家伤害术语集（大类）","国家伤害术语集（小类）","IMDRF有关术语（伤害）"]]#line:5662
			except :#line:5663
				O0O000OOOOO0OOO00 =O0O000OOOOO0OOO00 [["关键字标记","一般","新的一般","严重","新的严重","总数量","总数量占比","构成比","严重比","事件分类","不良事件名称1","不良事件名称2","国家故障术语集（大类）","国家故障术语集（小类）","IMDRF有关术语（故障）","国家伤害术语集（大类）","国家伤害术语集（小类）","IMDRF有关术语（伤害）"]]#line:5664
		else :#line:5666
			try :#line:5667
				O0O000OOOOO0OOO00 =O0O000OOOOO0OOO00 [["关键字标记","一般","新的一般","严重","新的严重","总数量","总数量占比","构成比","严重比","事件分类","不良事件名称1","不良事件名称2","死亡(仅支持器械)"]]#line:5668
			except :#line:5669
				O0O000OOOOO0OOO00 =O0O000OOOOO0OOO00 [["关键字标记","一般","新的一般","严重","新的严重","总数量","总数量占比","构成比","严重比","事件分类","不良事件名称1","不良事件名称2"]]#line:5670
		for OO00OO0O000O00OOO ,O0O0OOOO0O0000000 in O0O0OOOO00O00OO00 .iterrows ():#line:5672
			O0O000OOOOO0OOO00 .loc [(O0O000OOOOO0OOO00 ["关键字标记"].astype (str )==str (O0O0OOOO0O0000000 ["值"])),"排除值"]=O0O0OOOO0O0000000 ["排除值"]#line:5673
		O0O000OOOOO0OOO00 ["排除值"]=O0O000OOOOO0OOO00 ["排除值"].fillna ("没有排除值")#line:5675
		for OOO00O0OOOOO00O0O in ["一般","新的一般","严重","新的严重","总数量","总数量占比","严重比"]:#line:5679
			O0O000OOOOO0OOO00 [OOO00O0OOOOO00O0O ]=O0O000OOOOO0OOO00 [OOO00O0OOOOO00O0O ].fillna (0 )#line:5680
		for OOO00O0OOOOO00O0O in ["一般","新的一般","严重","新的严重","总数量"]:#line:5682
			O0O000OOOOO0OOO00 [OOO00O0OOOOO00O0O ]=O0O000OOOOO0OOO00 [OOO00O0OOOOO00O0O ].astype (int )#line:5683
		O0O000OOOOO0OOO00 ["RPN"]="未定义"#line:5686
		O0O000OOOOO0OOO00 ["故障原因"]="未定义"#line:5687
		O0O000OOOOO0OOO00 ["可造成的伤害"]="未定义"#line:5688
		O0O000OOOOO0OOO00 ["应采取的措施"]="未定义"#line:5689
		O0O000OOOOO0OOO00 ["发生率"]="未定义"#line:5690
		O0O000OOOOO0OOO00 ["报表类型"]="PSUR"#line:5692
		return O0O000OOOOO0OOO00 #line:5693
	def df_psur2 (O0OOO0OOOO00O00OO ,OO00OO000OO0OOOO0 ,O0O0OO00000O00OO0 ):#line:5696
		""#line:5697
		OO0OOOOOOOOOO00O0 =O0OOO0OOOO00O00OO .df .copy ()#line:5699
		OO00OO0000O0O0OO0 =len (OO0OOOOOOOOOO00O0 )#line:5700
		if OO00OO000OO0OOOO0 :#line:5704
			OOOO0OO00OOOOO0OO =OO00OO000OO0OOOO0 #line:5705
		else :#line:5706
			OOOO0OO00OOOOO0OO ="透视列"#line:5707
			OO0OOOOOOOOOO00O0 [OOOO0OO00OOOOO0OO ]="未正确设置"#line:5708
		OO0OOOOOOOOOO00O0 ["关键字查找列"]=OO0OOOOOOOOOO00O0 [O0O0OO00000O00OO0 ]#line:5712
		OOOO0O00O0O000O00 =[]#line:5714
		OO0OOOOOOOOOO00O0 [O0O0OO00000O00OO0 ]=OO0OOOOOOOOOO00O0 [O0O0OO00000O00OO0 ].fillna ("未填写")#line:5715
		OO0OOOOOOOOOO00O0 [O0O0OO00000O00OO0 ]=OO0OOOOOOOOOO00O0 [O0O0OO00000O00OO0 ].str .replace ("*","",regex =False )#line:5716
		OO00OO0O0O0O0OO0O ="use("+str (O0O0OO00000O00OO0 )+").file"#line:5717
		OOO0O000O000000OO =str (Counter (TOOLS_get_list0 (OO00OO0O0O0O0OO0O ,OO0OOOOOOOOOO00O0 ,1000 ))).replace ("Counter({","{")#line:5718
		OOO0O000O000000OO =OOO0O000O000000OO .replace ("})","}")#line:5719
		OOO0O000O000000OO =ast .literal_eval (OOO0O000O000000OO )#line:5720
		O0OOOO00OO0O00O00 =pd .DataFrame .from_dict (OOO0O000O000000OO ,orient ="index",columns =["计数"]).reset_index ()#line:5721
		for OO00O000O00O00O00 ,O0O0O0OOOO00O0O0O in O0OOOO00OO0O00O00 .iterrows ():#line:5723
			O0O00000OO00OOOOO =O0O0O0OOOO00O0O0O ["index"]#line:5724
			OOOO0O000O0O0OOOO =OO0OOOOOOOOOO00O0 .loc [OO0OOOOOOOOOO00O0 ["关键字查找列"].str .contains (O0O00000OO00OOOOO ,na =False )].copy ()#line:5725
			OOOO0O000O0O0OOOO ["关键字标记"]=str (O0O00000OO00OOOOO )#line:5727
			OOOO0O000O0O0OOOO ["关键字计数"]=1 #line:5728
			if len (OOOO0O000O0O0OOOO )>0 :#line:5730
				O0O0O00000OO0O0O0 =pd .pivot_table (OOOO0O000O0O0OOOO ,values =["关键字计数"],index ="关键字标记",columns =OO00OO000OO0OOOO0 ,aggfunc ={"关键字计数":"count"},fill_value ="0",margins =True ,dropna =False ,)#line:5740
				O0O0O00000OO0O0O0 =O0O0O00000OO0O0O0 [:-1 ]#line:5741
				O0O0O00000OO0O0O0 .columns =O0O0O00000OO0O0O0 .columns .droplevel (0 )#line:5742
				O0O0O00000OO0O0O0 =O0O0O00000OO0O0O0 .reset_index ()#line:5743
				if len (O0O0O00000OO0O0O0 )>0 :#line:5746
					OOOO0O00O0O000O00 .append (O0O0O00000OO0O0O0 )#line:5747
		O00OOOOOOOO00O00O =pd .concat (OOOO0O00O0O000O00 )#line:5748
		O00OOOOOOOO00O00O =O00OOOOOOOO00O00O .sort_values (by =["All"],ascending =[False ],na_position ="last")#line:5753
		O00OOOOOOOO00O00O =O00OOOOOOOO00O00O .reset_index ()#line:5754
		O00OOOOOOOO00O00O ["All占比"]=round (O00OOOOOOOO00O00O ["All"]/OO00OO0000O0O0OO0 *100 ,2 )#line:5756
		O00OOOOOOOO00O00O =O00OOOOOOOO00O00O .rename (columns ={"All":"总数量","All占比":"总数量占比"})#line:5757
		O00OOOOOOOO00O00O ["报表类型"]="DSUR"#line:5762
		del O00OOOOOOOO00O00O ["index"]#line:5763
		try :#line:5764
			del O00OOOOOOOO00O00O ["未正确设置"]#line:5765
		except :#line:5766
			pass #line:5767
		return O00OOOOOOOO00O00O #line:5768
def A0000_Main ():#line:5777
	print ("")#line:5778
if __name__ =='__main__':#line:5780
	root =Tk .Tk ()#line:5783
	root .title (title_all )#line:5784
	try :#line:5785
		root .iconphoto (True ,PhotoImage (file =peizhidir +"0（范例）ico.png"))#line:5786
	except :#line:5787
		pass #line:5788
	sw_root =root .winfo_screenwidth ()#line:5789
	sh_root =root .winfo_screenheight ()#line:5791
	ww_root =700 #line:5793
	wh_root =620 #line:5794
	x_root =(sw_root -ww_root )/2 #line:5796
	y_root =(sh_root -wh_root )/2 #line:5797
	root .geometry ("%dx%d+%d+%d"%(ww_root ,wh_root ,x_root ,y_root ))#line:5798
	framecanvas =Frame (root )#line:5803
	canvas =Canvas (framecanvas ,width =680 ,height =30 )#line:5804
	canvas .pack ()#line:5805
	x =StringVar ()#line:5806
	out_rec =canvas .create_rectangle (5 ,5 ,680 ,25 ,outline ="silver",width =1 )#line:5807
	fill_rec =canvas .create_rectangle (5 ,5 ,5 ,25 ,outline ="",width =0 ,fill ="silver")#line:5808
	canvas .create_text (350 ,15 ,text ="总执行进度")#line:5809
	framecanvas .pack ()#line:5810
	try :#line:5817
		frame0 =ttk .Frame (root ,width =90 ,height =20 )#line:5818
		frame0 .pack (side =LEFT )#line:5819
		B_open_files1 =Button (frame0 ,text ="导入数据",bg ="white",height =2 ,width =12 ,font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =TOOLS_allfileopen ,)#line:5830
		B_open_files1 .pack ()#line:5831
		B_open_files3 =Button (frame0 ,text ="数据查看",bg ="white",height =2 ,width =12 ,font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (ori ,0 ,ori ),)#line:5846
		B_open_files3 .pack ()#line:5847
	except KEY :#line:5850
		pass #line:5851
	text =ScrolledText (root ,height =400 ,width =400 ,bg ="#FFFFFF")#line:5855
	text .pack (padx =5 ,pady =5 )#line:5856
	text .insert (END ,"\n 本程序适用于整理和分析国家医疗器械不良事件信息系统、国家药品不良反应监测系统和国家化妆品不良反应监测系统中导出的监测数据。如您有改进建议，请点击实用工具-意见反馈。\n")#line:5859
	text .insert (END ,"\n\n")#line:5860
	setting_cfg =read_setting_cfg ()#line:5863
	generate_random_file ()#line:5864
	setting_cfg =open_setting_cfg ()#line:5865
	if setting_cfg ["settingdir"]==0 :#line:5866
		showinfo (title ="提示",message ="未发现默认配置文件夹，请选择一个。如该配置文件夹中并无配置文件，将生成默认配置文件。")#line:5867
		filepathu =filedialog .askdirectory ()#line:5868
		path =get_directory_path (filepathu )#line:5869
		update_setting_cfg ("settingdir",path )#line:5870
	setting_cfg =open_setting_cfg ()#line:5871
	random_number =int (setting_cfg ["sidori"])#line:5872
	input_number =int (str (setting_cfg ["sidfinal"])[0 :6 ])#line:5873
	day_end =convert_and_compare_dates (str (setting_cfg ["sidfinal"])[6 :14 ])#line:5874
	sid =random_number *2 +183576 #line:5875
	if input_number ==sid and day_end =="未过期":#line:5876
		usergroup ="用户组=1"#line:5877
		text .insert (END ,usergroup +"   有效期至：")#line:5878
		text .insert (END ,datetime .strptime (str (int (int (str (setting_cfg ["sidfinal"])[6 :14 ])/4 )),"%Y%m%d"))#line:5879
	else :#line:5880
		text .insert (END ,usergroup )#line:5881
	text .insert (END ,"\n配置文件路径："+setting_cfg ["settingdir"]+"\n")#line:5882
	peizhidir =str (setting_cfg ["settingdir"])+csdir .split ("pinggutools")[0 ][-1 ]#line:5883
	roox =Toplevel ()#line:5887
	tMain =threading .Thread (target =PROGRAM_showWelcome )#line:5888
	tMain .start ()#line:5889
	t1 =threading .Thread (target =PROGRAM_closeWelcome )#line:5890
	t1 .start ()#line:5891
	root .lift ()#line:5893
	root .attributes ("-topmost",True )#line:5894
	root .attributes ("-topmost",False )#line:5895
	root .mainloop ()#line:5899
	print ("done.")#line:5900
