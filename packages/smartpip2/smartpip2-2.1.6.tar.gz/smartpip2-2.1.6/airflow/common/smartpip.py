import os #line:2
import requests #line:3
import time #line:4
import json #line:5
import re #line:6
import subprocess #line:7
import logging #line:8
try :#line:10
    from kafka import KafkaConsumer ,TopicPartition #line:11
except :#line:12
    logging .warning ('you need pip install kafka-python')#line:13
os .environ ['NLS_LANG']='SIMPLIFIED CHINESE_CHINA.UTF8'#line:15
requests .packages .urllib3 .disable_warnings ()#line:16
from airflow .settings import ETL_FILE_PATH ,KETTLE_HOME ,HIVE_HOME ,P_URL ,DATASET_TOKEN ,REFRESH_TOKEN #line:18
from airflow .utils .email import fun_email ,list_email #line:19
from airflow .common .datax import datax_cmdStr #line:20
_O0000O000000OO00O =f'{P_URL}/echart/dataset_api/?token={DATASET_TOKEN}&visitor=Airflow&type='#line:23
_OO0OO0OOOOO00OO00 =f'{P_URL}/echart/refresh_ds/?token={REFRESH_TOKEN}&type='#line:24
class SmartPipError (Exception ):#line:27
    def __init__ (O0OO00000OO0O00OO ,err ='SmartPip Error'):#line:28
        Exception .__init__ (O0OO00000OO0O00OO ,err )#line:29
def smart_upload (O00O00OO000O00OO0 ):#line:33
    OO00O0000OOO0OOOO ,OOOOOOOO000OO0000 =os .path .split (O00O00OO000O00OO0 )#line:34
    OOOOOOOO000OO0000 =OOOOOOOO000OO0000 .split ('.')[0 ]#line:35
    O00O0OOO0O0000OO0 ={"title":OOOOOOOO000OO0000 ,"token":DATASET_TOKEN ,"visitor":"Airflow"}#line:40
    OO0O0OO0OO0000OOO ={'file':open (O00O00OO000O00OO0 ,'rb')}#line:41
    O000OOOOO00OOOOOO =f'''{P_URL}/echart/dataset_api/?type=506&visitor=Airflow&token={DATASET_TOKEN}&param={{"uptime":"{time.time()}","filename":"{OOOOOOOO000OO0000}"}}'''#line:42
    O000O000OO00O00O0 =60 #line:43
    OO0OOO0O0O00OOO00 =requests .post (f'{P_URL}/etl/api/upload_file_api/',files =OO0O0OO0OO0000OOO ,data =O00O0OOO0O0000OO0 )#line:45
    print (OO0OOO0O0O00OOO00 .status_code )#line:46
    if OO0OOO0O0O00OOO00 .status_code ==200 :#line:47
        OO0OOO0O0O00OOO00 =OO0OOO0O0O00OOO00 .json ()#line:48
    elif OO0OOO0O0O00OOO00 .status_code ==504 :#line:49
        print ('timeout, try waiting...')#line:50
        OO0OOO0O0O00OOO00 ={"result":"error","data":"time out"}#line:51
        for O0OO0O0O000O0O0OO in range (20 ):#line:52
            O0OO000OO0OOOOOOO =requests .get (O000OOOOO00OOOOOO ).json ()#line:53
            print (O0OO000OO0OOOOOOO )#line:54
            O00O0OOO0O0000OO0 =O0OO000OO0OOOOOOO ['data']#line:55
            if len (O00O0OOO0O0000OO0 )>1 :#line:56
                OO0OOO0O0O00OOO00 ={"result":"success","data":"uploaded"}#line:57
                break #line:58
            time .sleep (O000O000OO00O00O0 )#line:59
    else :#line:60
        OO0OOO0O0O00OOO00 ={"result":"error","data":"some thing wrong"}#line:61
    print (OO0OOO0O0O00OOO00 )#line:62
    if OO0OOO0O0O00OOO00 ['result']=='error':#line:63
        raise SmartPipError ('Upload Error')#line:64
def get_dataset (O00OOOO0O0OO0OO0O ):#line:67
    ""#line:72
    O00000000OOOOOO00 =requests .get (_O0000O000000OO00O +str (O00OOOO0O0OO0OO0O ),verify =False )#line:73
    O00000000OOOOOO00 =O00000000OOOOOO00 .json ()#line:74
    return O00000000OOOOOO00 #line:75
def dataset (O0000O0OOOOO00000 ,OO0OO0OO00OOO0O0O ,O00OOOO000000OO0O ,tolist =None ):#line:78
    ""#line:85
    O000O0OO00OOO000O =60 *15 #line:86
    OOO000O0OOOO000OO =3600 *2 #line:87
    OOOO0O0OOO0OOOO0O =''#line:88
    try :#line:89
        while True :#line:90
            O0OO0OO00OOO00O0O =requests .get (_O0000O000000OO00O +OO0OO0OO00OOO0O0O ,verify =False )#line:91
            O0OO0OO00OOO00O0O =O0OO0OO00OOO00O0O .json ()#line:92
            O00O000O0O0000000 =O0OO0OO00OOO00O0O ['result']#line:93
            O0OO0OO00OOO00O0O =O0OO0OO00OOO00O0O ['data']#line:94
            if O00O000O0O0000000 =='error':#line:95
                raise Exception (f'{O0OO0OO00OOO00O0O}')#line:96
            OOOO0O0OOO0OOOO0O =',\n'.join ([str (OO0OO00O0OOOOO000 )for OO0OO00O0OOOOO000 in O0OO0OO00OOO00O0O ])#line:97
            print (f'Dataset: {OOOO0O0OOO0OOOO0O} ')#line:98
            if O00OOOO000000OO0O =='e3':#line:99
                if len (O0OO0OO00OOO00O0O )<2 :#line:100
                    if OOO000O0OOOO000OO <=0 :#line:101
                        raise Exception ('超时且数据为空')#line:102
                    else :#line:103
                        time .sleep (O000O0OO00OOO000O )#line:104
                        OOO000O0OOOO000OO =OOO000O0OOOO000OO -O000O0OO00OOO000O #line:105
                else :#line:106
                    break #line:107
            else :#line:108
                if len (O0OO0OO00OOO00O0O )>1 :#line:109
                    if O00OOOO000000OO0O =='e1':#line:110
                        raise Exception ('有异常数据')#line:111
                    elif O00OOOO000000OO0O =='e2':#line:112
                        list_email (f'Info_{O0000O0OOOOO00000}',f'{O0000O0OOOOO00000}-Dataset Status',O0OO0OO00OOO00O0O ,to_list =tolist )#line:113
                else :#line:114
                    if O00OOOO000000OO0O not in ['info','e1']:#line:115
                        OOOO0O0OOO0OOOO0O ='数据为空'#line:116
                        raise Exception (OOOO0O0OOO0OOOO0O )#line:117
                break #line:118
    except Exception as O000O00O000000000 :#line:119
        fun_email (f'{O0000O0OOOOO00000}-执行Dataset校验出错',OOOO0O0OOO0OOOO0O ,to_list =tolist )#line:120
        raise SmartPipError (str (O000O00O000000000 .args ))#line:121
def refresh_dash (OO0OOO000000O0OO0 ,OO0O0O0O00O0000O0 ):#line:124
    ""#line:127
    try :#line:128
        OO00O00O00O0OO000 =requests .get (f'{_OO0OO0OOOOO00OO00}{OO0O0O0O00O0000O0}',verify =False )#line:129
        OO00O00O00O0OO000 =OO00O00O00O0OO000 .json ()#line:130
        print (OO00O00O00O0OO000 )#line:131
        OO00000OO00O0O0O0 =OO00O00O00O0OO000 ['status']#line:132
        if OO00000OO00O0O0O0 !=200 :#line:133
            raise SmartPipError ('refresh_dash')#line:134
    except Exception as OOOO00OOO0O0O0O00 :#line:135
        fun_email (f'{OO0OOO000000O0OO0}-执行re出错',str (OOOO00OOO0O0O0O00 .args ))#line:136
        raise SmartPipError (str (OOOO00OOO0O0O0O00 .args ))#line:137
def run_bash (OOOO000OO0OOO0O0O ):#line:141
    O00O0000O0OO00O0O =''#line:142
    OO0O0O0OOO0O00000 =subprocess .Popen (OOOO000OO0OOO0O0O ,stdout =subprocess .PIPE ,stderr =subprocess .STDOUT ,shell =True ,cwd =ETL_FILE_PATH )#line:143
    print ('PID:',OO0O0O0OOO0O00000 .pid )#line:144
    for O00O0OO0O0O0OO0OO in iter (OO0O0O0OOO0O00000 .stdout .readline ,b''):#line:145
        if OO0O0O0OOO0O00000 .poll ()and O00O0OO0O0O0OO0OO ==b'':#line:146
            break #line:147
        O00O0OO0O0O0OO0OO =O00O0OO0O0O0OO0OO .decode (encoding ='utf8')#line:148
        print (O00O0OO0O0O0OO0OO .rstrip ())#line:149
        O00O0000O0OO00O0O =O00O0000O0OO00O0O +O00O0OO0O0O0OO0OO #line:150
    OO0O0O0OOO0O00000 .stdout .close ()#line:151
    OO0000O00O0000O0O =OO0O0O0OOO0O00000 .wait ()#line:152
    print ('result code: ',OO0000O00O0000O0O )#line:153
    return O00O0000O0OO00O0O ,OO0000O00O0000O0O #line:154
def run_python (OO0O000O00000O0OO ,OOOO0O0OOOO0OO0O0 ,dev =''):#line:157
    OO000OOO000O0O0OO =OO0O000O00000O0OO .split ('/')#line:158
    _O000OOOO00OO000O0 ,OO000OO0OO0OO000O =run_bash ('python %s %s'%(OO0O000O00000O0OO ,OOOO0O0OOOO0OO0O0 ))#line:159
    if OO000OO0OO0OO000O !=0 :#line:160
        fun_email (f'{OO000OOO000O0O0OO[-2]}/{OO000OOO000O0O0OO[-1]}出错','python error')#line:161
        raise Exception ('error')#line:162
def run_dataxx (OOO0OO0O00OO00000 ,OOOO0OO000OO00000 ,dev =''):#line:166
    OOOO0O0O0O0O0OO0O =OOO0OO0O00OO00000 .split ('/')#line:167
    if OOOO0OO000OO00000 :#line:168
        O0OOO00000OO0O000 =[f'-D{OO0000O00000OOO00}:{O00OOOOO0O0O0OOO0}'for OO0000O00000OOO00 ,O00OOOOO0O0O0OOO0 in OOOO0OO000OO00000 .items ()]#line:169
        O0O00OO0OO0O000O0 =' '.join (O0OOO00000OO0O000 )#line:170
        OO0O00OO00O0O000O =[f'-p"{O0O00OO0OO0O000O0}"',OOO0OO0O00OO00000 ]#line:171
    else :#line:172
        OO0O00OO00O0O000O =[OOO0OO0O00OO00000 ]#line:173
    O00OO0O00O0OO00O0 =datax_cmdStr (OO0O00OO00O0O000O )#line:174
    _OO000O0O000O00000 ,O0OO000O00000OOOO =run_bash (O00OO0O00O0OO00O0 )#line:175
    if O0OO000O00000OOOO !=0 :#line:176
        fun_email (f'{OOOO0O0O0O0O0OO0O[-2]}/{OOOO0O0O0O0O0OO0O[-1]}出错','datax error')#line:177
        raise Exception ('error')#line:178
def run_datax (OO00OOOO00OOOOOO0 ,O000OO0O00O0O000O ,O0OO0O000000O00OO ,OOO00OOOOO00O0O0O ,dev =''):#line:181
    with open (OO00OOOO00OOOOOO0 ,'r',encoding ='utf8')as O000000OO0OO0O00O :#line:182
        O0OO00O00O0O00O0O =readSqlstr (O000000OO0OO0O00O .read ().strip (),para_dict =OOO00OOOOO00O0O0O )#line:183
    O0OO00O00O0O00O0O =O0OO00O00O0O00O0O .split ('##')#line:184
    O0O00O000OOO0O0OO ={}#line:185
    for O0OO0OOOO00O0OO0O in O0OO00O00O0O00O0O :#line:186
        O0OOO0O0OO00O0000 =O0OO0OOOO00O0OO0O .find ('=')#line:187
        if O0OOO0O0OO00O0000 >0 :#line:188
            O0O00O000OOO0O0OO [O0OO0OOOO00O0OO0O [:O0OOO0O0OO00O0000 ].strip ()]=O0OO0OOOO00O0OO0O [O0OOO0O0OO00O0000 +1 :].replace ('\n',' ').strip ()#line:189
    OOO000O00O0O0OOOO =O0O00O000OOO0O0OO .keys ()#line:190
    O000O0O0OOOOO00OO =O0O00O000OOO0O0OO .pop ('template')if 'template'in OOO000O00O0O0OOOO else 'default'#line:191
    OOOO0000O000OOOO0 =O0O00O000OOO0O0OO .get ('targetColumn')#line:192
    OOOO00OOO00O00O00 =None #line:193
    if O000O0O0OOOOO00OO .endswith ('hdfs'):#line:194
        OOOO00OOO00O00O00 =O0O00O000OOO0O0OO .pop ('hiveSql')if 'hiveSql'in OOO000O00O0O0OOOO else None #line:196
        if not OOOO00OOO00O00O00 :#line:197
            OOOO00OOO00O00O00 =O0O00O000OOO0O0OO .pop ('postSql')if 'postSql'in OOO000O00O0O0OOOO else None #line:198
        if OOOO0000O000OOOO0 :#line:200
            OOOO0000O000OOOO0 =OOOO0000O000OOOO0 .split (',')#line:201
            OO0O0O00OOOOO0O0O =[]#line:202
            for O0OO0OOOO00O0OO0O in OOOO0000O000OOOO0 :#line:203
                if ':'in O0OO0OOOO00O0OO0O :#line:204
                    O0OO0OOOO00O0OO0O =O0OO0OOOO00O0OO0O .split (':')#line:205
                    OO0O0O00OOOOO0O0O .append ({"name":O0OO0OOOO00O0OO0O [0 ].strip (),"type":O0OO0OOOO00O0OO0O [1 ].strip ()})#line:206
                else :#line:207
                    OO0O0O00OOOOO0O0O .append ({"name":O0OO0OOOO00O0OO0O .strip (),"type":"STRING"})#line:208
            O0O00O000OOO0O0OO ['targetColumn']=json .dumps (OO0O0O00OOOOO0O0O )#line:209
    else :#line:210
        if OOOO0000O000OOOO0 :#line:211
            OOOO0000O000OOOO0 =[O000O0OO0O00O000O .strip ()for O000O0OO0O00O000O in OOOO0000O000OOOO0 .split (',')]#line:212
            O0O00O000OOO0O0OO ['targetColumn']=json .dumps (OOOO0000O000OOOO0 )#line:213
        else :#line:214
            O0O00O000OOO0O0OO ['targetColumn']='["*"]'#line:215
        if O000O0O0OOOOO00OO .endswith ('starrocks'):#line:217
            if '.'in O0O00O000OOO0O0OO ['targetTable']:#line:218
                O0O00O000OOO0O0OO ['targetDB'],O0O00O000OOO0O0OO ['targetTable']=O0O00O000OOO0O0OO ['targetTable'].split ('.')#line:219
            else :#line:220
                O0O00O000OOO0O0OO ['targetDB']='Test'#line:221
    if 'preSql'in OOO000O00O0O0OOOO :#line:223
        O0O00O000OOO0O0OO ['preSql']=json .dumps (O0O00O000OOO0O0OO ['preSql'].strip ().split (';'))#line:224
    else :#line:225
        O0O00O000OOO0O0OO ['preSql']=''#line:226
    if 'postSql'in OOO000O00O0O0OOOO :#line:227
        O0O00O000OOO0O0OO ['postSql']=json .dumps (O0O00O000OOO0O0OO ['postSql'].strip ().split (';'))#line:228
    else :#line:229
        O0O00O000OOO0O0OO ['postSql']=''#line:230
    O00OOO0OOOO00O0OO =OO00OOOO00OOOOOO0 .split ('/')#line:231
    O00O000OO0O00OOO0 =O00OOO0OOOO00O0OO [-1 ].split ('.')[0 ]#line:232
    with open (os .path .join (O0OO0O000000O00OO ,'datax','templates',O000O0O0OOOOO00OO ),'r')as O000000OO0OO0O00O :#line:233
        OO0000OO0000OO0OO =O000000OO0OO0O00O .read ()#line:234
    OO00OOOO00OOOOOO0 =os .path .join (O0OO0O000000O00OO ,'datax',O00O000OO0O00OOO0 +'.json')#line:235
    with open (OO00OOOO00OOOOOO0 ,'w',encoding ='utf8')as O000000OO0OO0O00O :#line:236
        O000000OO0OO0O00O .write (readSqlstr (OO0000OO0000OO0OO ,O0O00O000OOO0O0OO ))#line:237
    O0O000OOOOO0O00OO =datax_cmdStr ([OO00OOOO00OOOOOO0 ])#line:238
    _O0O000O0O00OOOOO0 ,OOOOOO0OOO0O000O0 =run_bash (O0O000OOOOO0O00OO )#line:239
    if OOOOOO0OOO0O000O0 !=0 :#line:240
        fun_email (f'{O00OOO0OOOO00O0OO[-2]}/{O00OOO0OOOO00O0OO[-1]}出错','datax error')#line:241
        raise Exception ('error')#line:242
    if OOOO00OOO00O00O00 :#line:243
        print (_OOOO0OO0OO0O0OOOO (OOOO00OOO00O00O00 .split (';'),O000OO0O00O0O000O ,db_connect ='hive',dev =dev ))#line:244
def readSqlFile (OO00OO0OO00OO0000 ,para_dict =None ):#line:248
    if OO00OO0OO00OO0000 .find ('.sql')<0 :#line:249
        return 'file type error'#line:250
    with open (OO00OO0OO00OO0000 ,'r',encoding ='utf-8')as O0O0000O0O0OO0OOO :#line:251
        OO00OOO0OO0O00OOO =O0O0000O0O0OO0OOO .read ()#line:252
    OOO0O0O0O0OO0O00O =readSqlstr (OO00OOO0OO0O00OOO ,para_dict )#line:253
    return OOO0O0O0O0OO0O00O #line:254
def readSqoopFile (OOOO00OOOO00O0O00 ,para_dict =None ):#line:257
    if not OOOO00OOOO00O0O00 .endswith ('.sql'):#line:258
        return 'file type error'#line:259
    with open (OOOO00OOOO00O0O00 ,'r',encoding ='utf8')as O0OO0OO0O00O0OO00 :#line:260
        OO00OOOO00OOO0OOO =O0OO0OO0O00O0OO00 .read ().strip ()#line:261
    O0OO00O00O000O00O =re .match (r"/\*(.*?)\*/(.+)",OO00OOOO00OOO0OOO ,re .M |re .S )#line:262
    OO00O0O0O0O00OO00 =readSqlstr (O0OO00O00O000O00O .group (1 ).strip (),para_dict )#line:263
    OOO0O0O0O0O00O00O =O0OO00O00O000O00O .group (2 ).strip ()#line:264
    return OO00O0O0O0O00OO00 ,OOO0O0O0O0O00O00O #line:265
def readSqlstr (O00OO0OO00O00OO00 ,para_dict =None ):#line:268
    O0OOO0O00000OO0O0 =re .sub (r"(\/\*(.|\n)*?\*\/)|--.*",'',O00OO0OO00O00OO00 .strip ())#line:269
    if para_dict :#line:270
        for OOOO0000O0OOO0O0O ,OOO000O0000O0O00O in para_dict .items ():#line:271
            O0OOO0O00000OO0O0 =O0OOO0O00000OO0O0 .replace ('$'+OOOO0000O0OOO0O0O ,str (OOO000O0000O0O00O ))#line:272
    return O0OOO0O00000OO0O0 #line:273
def run_sql_file (OO0O000O0OO0OO00O ,OO0O0OO0OOOOO0000 ,db_connect ='starrocks',para_dict =None ,dev =''):#line:276
    O00O0OO00O000OO0O =OO0O000O0OO0OO00O .split ('/')#line:277
    try :#line:278
        O00O0OO00O000O0OO =readSqlFile (OO0O000O0OO0OO00O ,para_dict ).split (';')#line:279
        O0OO00O0O0OO00OOO =OO0O0OO0OOOOO0000 .get (db_connect )#line:280
        if dev :#line:281
            if f'{db_connect}{dev}'in OO0O0OO0OOOOO0000 .keys ():#line:282
                O0OO00O0O0OO00OOO =OO0O0OO0OOOOO0000 .get (f'{db_connect}{dev}')#line:283
        O0000O0OO0OOO0O00 =connect_db_execute ().execute_sql_list (O00O0OO00O000O0OO ,db_connect ,connect_dict =O0OO00O0O0OO00OOO )#line:284
        return O0000O0OO0OOO0O00 #line:285
    except Exception as OOOO0OOOOO0000O0O :#line:286
        fun_email ('{}/{}执行出错'.format (O00O0OO00O000OO0O [-2 ],O00O0OO00O000OO0O [-1 ]),str (OOOO0OOOOO0000O0O .args ))#line:287
        print (OOOO0OOOOO0000O0O .args )#line:288
        raise SmartPipError ('Run SQL Error')#line:289
def _OOOO0OO0OO0O0OOOO (O0OOOO0O0O0O0O0O0 ,O000OO00OOO0OOO0O ,db_connect ='starrocks',para_dict =None ,dev =''):#line:292
    try :#line:293
        if isinstance (O0OOOO0O0O0O0O0O0 ,str ):#line:294
            O0OOOO0O0O0O0O0O0 =readSqlstr (O0OOOO0O0O0O0O0O0 ,para_dict ).split (';')#line:295
        OO0O00OOO000000O0 =O000OO00OOO0OOO0O .get (db_connect )#line:296
        if dev :#line:297
            if f'{db_connect}{dev}'in O000OO00OOO0OOO0O .keys ():#line:298
                OO0O00OOO000000O0 =O000OO00OOO0OOO0O .get (f'{db_connect}{dev}')#line:299
        O000OO00OOOO00OOO =connect_db_execute ().execute_sql_list (O0OOOO0O0O0O0O0O0 ,db_connect ,connect_dict =OO0O00OOO000000O0 )#line:300
        return O000OO00OOOO00OOO #line:301
    except Exception as O0OO0O00OO0OO0O00 :#line:302
        fun_email ('SQL执行出错',f'{O0OOOO0O0O0O0O0O0}{O0OO0O00OO0OO0O00.args}')#line:303
        print (O0OO0O00OO0OO0O00 .args )#line:304
        raise SmartPipError ('Run SQL Error')#line:305
def run_kettle (O0O000OOOOOO0OO0O ,para_str ='',dev =False ):#line:309
    ""#line:316
    O0OOO000OO0OO0O00 =O0O000OOOOOO0OO0O .split ('/')#line:317
    print ('kettle job start')#line:318
    if '.ktr'in O0O000OOOOOO0OO0O :#line:320
        O00OO0000O00OOOO0 =f'{KETTLE_HOME}/pan.sh -level=Basic -file={O0O000OOOOOO0OO0O}{para_str}'#line:321
    else :#line:322
        O00OO0000O00OOOO0 =f'{KETTLE_HOME}/kitchen.sh -level=Basic -file={O0O000OOOOOO0OO0O}{para_str}'#line:323
    print (O00OO0000O00OOOO0 )#line:324
    O0O0O0OOOOO0O00O0 ,O00O0O000O00O000O =run_bash (O00OO0000O00OOOO0 )#line:328
    if O00O0O000O00O000O ==0 :#line:329
        print ('{} 完成数据抽取'.format (str (O0O000OOOOOO0OO0O )))#line:330
    else :#line:331
        print ('{} 执行错误'.format (O0O000OOOOOO0OO0O ))#line:332
        fun_email ('{}/{}出错'.format (O0OOO000OO0OO0O00 [-2 ],O0OOO000OO0OO0O00 [-1 ]),str (O0O0O0OOOOO0O00O0 ))#line:333
        raise SmartPipError ('Run Kettle Error')#line:334
def hdfsStarrocks (O00OO0OOOOOOO0O00 ,O0OO00OOO00O00O00 ,para_dict =None ):#line:338
    ""#line:342
    O0OO0O000O0OOOO00 =O00OO0OOOOOOO0O00 .split ('/')#line:343
    print ('strocks load job start')#line:344
    O0O000000O00OOOO0 ,OO00O0OO0OOO00O0O =readSqoopFile (O00OO0OOOOOOO0O00 ,para_dict =para_dict )#line:345
    O0O000000O00OOOO0 =O0O000000O00OOOO0 .split ('\n')#line:346
    OOO0O0OOO0OO00O0O ={}#line:347
    OOO0O0OOO0OO00O0O ['LABEL']=f'{O0OO0O000O0OOOO00[-2]}{O0OO0O000O0OOOO00[-1][:-4]}{int(time.time())}'#line:348
    OOO0O0OOO0OO00O0O ['HDFS']=HIVE_HOME #line:349
    for OOO00OOOO0O0000O0 in O0O000000O00OOOO0 :#line:350
        OOOO0OOOOOOO0OO00 =OOO00OOOO0O0000O0 .find ('=')#line:351
        if OOOO0OOOOOOO0OO00 >0 :#line:352
            OOO0O0OOO0OO00O0O [OOO00OOOO0O0000O0 [:OOOO0OOOOOOO0OO00 ].strip ()]=OOO00OOOO0O0000O0 [OOOO0OOOOOOO0OO00 +1 :].strip ()#line:353
    OOO000O0O0O00O00O =OOO0O0OOO0OO00O0O .get ('sleepTime')#line:355
    if OOO000O0O0O00O00O :#line:356
        OOO000O0O0O00O00O =int (OOO000O0O0O00O00O )#line:357
        if OOO000O0O0O00O00O <30 :#line:358
            OOO000O0O0O00O00O =30 #line:359
    else :#line:360
        OOO000O0O0O00O00O =30 #line:361
    O0O000O00OOOO000O =OOO0O0OOO0OO00O0O .get ('maxTime')#line:363
    if O0O000O00OOOO000O :#line:364
        O0O000O00OOOO000O =int (O0O000O00OOOO000O )#line:365
        if O0O000O00OOOO000O >3600 :#line:366
            O0O000O00OOOO000O =3600 #line:367
    else :#line:368
        O0O000O00OOOO000O =600 #line:369
    _OOOO0OO0OO0O0OOOO (OO00O0OO0OOO00O0O ,O0OO00OOO00O00O00 ,db_connect ='starrocks',para_dict =OOO0O0OOO0OO00O0O )#line:371
    time .sleep (OOO000O0O0O00O00O )#line:372
    OO00O000OO000OOOO =f'''show load from {OOO0O0OOO0OO00O0O.get('targetDB')} where label = '{OOO0O0OOO0OO00O0O['LABEL']}' order by CreateTime desc limit 1 '''#line:373
    OOOO000O00O000O0O ='start to check label'#line:374
    try :#line:375
        while True :#line:376
            OOOO000O00O000O0O =_OOOO0OO0OO0O0OOOO ([OO00O000OO000OOOO ],O0OO00OOO00O00O00 ,db_connect ='starrocks')#line:377
            print (OOOO000O00O000O0O )#line:378
            O0OO0OOO000O0OO00 =OOOO000O00O000O0O [1 ][2 ]#line:379
            if O0OO0OOO000O0OO00 =='CANCELLED':#line:380
                raise Exception (f'Starrocks:{O0OO0OOO000O0OO00}')#line:381
            elif O0OO0OOO000O0OO00 =='FINISHED':#line:382
                print ('Load completed')#line:383
                break #line:384
            if O0O000O00OOOO000O <=0 :#line:385
                raise Exception ('超时未完成')#line:386
            else :#line:387
                time .sleep (OOO000O0O0O00O00O )#line:388
                O0O000O00OOOO000O =O0O000O00OOOO000O -OOO000O0O0O00O00O #line:389
    except Exception as OO00OO0O0O0OO0O00 :#line:390
        print ('{} 执行错误'.format (O00OO0OOOOOOO0O00 ))#line:391
        fun_email ('{}/{}执行出错'.format (O0OO0O000O0OOOO00 [-2 ],O0OO0O000O0OOOO00 [-1 ]),str (OOOO000O00O000O0O ))#line:392
        raise SmartPipError (str (OO00OO0O0O0OO0O00 .args ))#line:393
def kafkaStarrocks (OOOOO0OO00OO0O00O ,O0O0OOO0OO00O0OO0 ,O0OOO00OO0OOO000O ,O000OOOOO000OO000 ,O0OOOOO00O0000OOO ,dev =''):#line:396
    with open (OOOOO0OO00OO0O00O ,'r',encoding ='utf8')as OO0O0OOO00000000O :#line:397
        O00OO0O0000O00O00 =readSqlstr (OO0O0OOO00000000O .read ().strip (),para_dict =O0OOOOO00O0000OOO )#line:398
    O00OO0O0000O00O00 =O00OO0O0000O00O00 .split ('##')#line:399
    O00O00O00OO00O0OO ={}#line:400
    for OO00O0O00O00OOOO0 in O00OO0O0000O00O00 :#line:401
        OOOOO0OO00OOO0OO0 =OO00O0O00O00OOOO0 .find ('=')#line:402
        if OOOOO0OO00OOO0OO0 >0 :#line:403
            OOO0O000OOO00O000 =OO00O0O00O00OOOO0 [OOOOO0OO00OOO0OO0 +1 :].replace ('\n',' ').strip ()#line:404
            if OOO0O000OOO00O000 :#line:405
                O00O00O00OO00O0OO [OO00O0O00O00OOOO0 [:OOOOO0OO00OOO0OO0 ].strip ()]=OOO0O000OOO00O000 #line:406
    OO0O0O0OO0OO000OO =O00O00O00OO00O0OO .pop ('topic')#line:407
    O000O0O00000O0OOO =O00O00O00OO00O0OO .pop ('table')#line:408
    OOO00000OO00O0OO0 =O00O00O00OO00O0OO .keys ()#line:409
    if 'skipError'in OOO00000OO00O0OO0 :#line:410
        skipError =O00O00O00OO00O0OO .pop ('skipError')#line:411
    else :#line:412
        skipError =None #line:413
    if 'kafkaConn'in OOO00000OO00O0OO0 :#line:414
        O0OOO0O0O00O00OO0 =O00O00O00OO00O0OO .pop ('kafkaConn')#line:415
    else :#line:416
        O0OOO0O0O00O00OO0 ='default'#line:417
    if 'json_root'in OOO00000OO00O0OO0 :#line:418
        OO0OO0O00OOO00000 =O00O00O00OO00O0OO .pop ('json_root')#line:419
    else :#line:420
        OO0OO0O00OOO00000 =None #line:421
    if 'jsonpaths'in OOO00000OO00O0OO0 :#line:422
        O0000000OOO00OOOO =O00O00O00OO00O0OO .get ('jsonpaths')#line:423
        if not O0000000OOO00OOOO .startswith ('['):#line:424
            O0000000OOO00OOOO =O0000000OOO00OOOO .split (',')#line:425
            O0000000OOO00OOOO =json .dumps (['$.'+OO000O0OO0OOOO0OO .strip ()for OO000O0OO0OOOO0OO in O0000000OOO00OOOO ])#line:426
            O00O00O00OO00O0OO ['jsonpaths']=O0000000OOO00OOOO #line:427
    OO0O0O0OOO0OOOOOO =_O0O0OO0000O00O0O0 (OO0O0O0OO0OO000OO ,O0O0OOO0OO00O0OO0 [O0OOO0O0O00O00OO0 ],O000OOOOO000OO000 )#line:428
    def O0OO0O0OO00000OO0 (O0OO0OO0O0O0O0O00 ):#line:430
        OO0O0000O0OOOOOOO =b''#line:431
        OO0OO0000OOO000OO =None #line:432
        if 'format'in OOO00000OO00O0OO0 :#line:433
            for OO0OO0000OOO000OO in O0OO0OO0O0O0O0O00 :#line:434
                OOO0O0OO000OOOO00 =OO0OO0000OOO000OO .value #line:435
                if OO0OO0O00OOO00000 :#line:436
                    OOO0O0OO000OOOO00 =json .loads (OOO0O0OO000OOOO00 .decode ('utf8'))#line:437
                    OOO0O0OO000OOOO00 =json .dumps (OOO0O0OO000OOOO00 [OO0OO0O00OOO00000 ]).encode ('utf8')#line:438
                if OOO0O0OO000OOOO00 .startswith (b'['):#line:439
                    OO0O0000O0OOOOOOO =OO0O0000O0OOOOOOO +b','+OOO0O0OO000OOOO00 [1 :-1 ]#line:440
                else :#line:441
                    OO0O0000O0OOOOOOO =OO0O0000O0OOOOOOO +b','+OOO0O0OO000OOOO00 #line:442
                if len (OO0O0000O0OOOOOOO )>94857600 :#line:443
                    streamStarrocks (O000O0O00000O0OOO ,O0OOO00OO0OOO000O ,O00O00O00OO00O0OO ,OO0O0000O0OOOOOOO ,skipError )#line:444
                    OO0O0O0OOO0OOOOOO .write_offset (OO0OO0000OOO000OO .partition ,OO0OO0000OOO000OO .offset +1 )#line:445
                    OO0O0000O0OOOOOOO =b''#line:446
                if OO0OO0000OOO000OO .offset ==OO0O0O0OOO0OOOOOO .end_offset -1 :#line:447
                    break #line:448
        else :#line:449
            for OO0OO0000OOO000OO in O0OO0OO0O0O0O0O00 :#line:450
                OOO0O0OO000OOOO00 =OO0OO0000OOO000OO .value #line:451
                if OO0OO0O00OOO00000 :#line:452
                    OOO0O0OO000OOOO00 =json .loads (OOO0O0OO000OOOO00 .decode ('utf8'))#line:453
                    OOO0O0OO000OOOO00 =json .dumps (OOO0O0OO000OOOO00 [OO0OO0O00OOO00000 ]).encode ('utf8')#line:454
                OO0O0000O0OOOOOOO =OO0O0000O0OOOOOOO +b'\n'+OOO0O0OO000OOOO00 #line:455
                if len (OO0O0000O0OOOOOOO )>94857600 :#line:456
                    streamStarrocks (O000O0O00000O0OOO ,O0OOO00OO0OOO000O ,O00O00O00OO00O0OO ,OO0O0000O0OOOOOOO ,skipError )#line:457
                    OO0O0O0OOO0OOOOOO .write_offset (OO0OO0000OOO000OO .partition ,OO0OO0000OOO000OO .offset +1 )#line:458
                    OO0O0000O0OOOOOOO =b''#line:459
                if OO0OO0000OOO000OO .offset ==OO0O0O0OOO0OOOOOO .end_offset -1 :#line:460
                    break #line:461
        print (OO0O0000O0OOOOOOO [1 :1000 ])#line:462
        if OO0O0000O0OOOOOOO :#line:463
            streamStarrocks (O000O0O00000O0OOO ,O0OOO00OO0OOO000O ,O00O00O00OO00O0OO ,OO0O0000O0OOOOOOO ,skipError )#line:464
        return OO0OO0000OOO000OO #line:465
    OO0O0O0OOO0OOOOOO .consumer_topic (O0OO0O0OO00000OO0 )#line:467
def streamStarrocks (OO0OOO00OO000OO0O ,O0000O0O000OO000O ,O00O0OO0O000O0OO0 ,OOOO00OO0O00OOO00 ,skipError =False ):#line:470
    import base64 ,uuid #line:471
    O00O0O0OO0OO0000O ,OO0OOO00OO000OO0O =OO0OOO00OO000OO0O .split ('.')#line:472
    OO0O0OOOO00O00O00 =str (base64 .b64encode (f'{O0000O0O000OO000O["user"]}:{O0000O0O000OO000O["password"]}'.encode ('utf-8')),'utf-8')#line:473
    OOOO00OO0O00OOO00 =OOOO00OO0O00OOO00 .strip ()#line:474
    if OOOO00OO0O00OOO00 .startswith (b','):#line:475
        O00O0OO0O000O0OO0 ['strip_outer_array']='true'#line:476
        OOOO00OO0O00OOO00 =b'['+OOOO00OO0O00OOO00 [1 :]+b']'#line:477
    OO00OO000000O00OO ={'Content-Type':'application/json','Authorization':f'Basic {OO0O0OOOO00O00O00}','label':f'{OO0OOO00OO000OO0O}{uuid.uuid4()}',**O00O0OO0O000O0OO0 }#line:483
    OO0OO0OO0OOOOOOO0 =f"{O0000O0O000OO000O['url']}/api/{O00O0O0OO0OO0000O}/{OO0OOO00OO000OO0O}/_stream_load"#line:484
    print ('start loading to starrocks....')#line:485
    O0O0000OOO0O00O0O =requests .put (OO0OO0OO0OOOOOOO0 ,headers =OO00OO000000O00OO ,data =OOOO00OO0O00OOO00 ).json ()#line:486
    print (O0O0000OOO0O00O0O )#line:487
    if O0O0000OOO0O00O0O ['Status']=='Fail':#line:488
        if skipError :#line:489
            print (f'Starrocks Load Error, Skip this offset')#line:490
        else :#line:491
            raise Exception ('Starrocks Load Error')#line:492
def routineStarrocks (OO000OOOOOO0OOOOO ,O000OO0OOOOO00O0O ,flag =''):#line:494
    O000O000O0OO0O0OO =_OOOO0OO0OO0O0OOOO ([f'SHOW ROUTINE LOAD FOR {O000OO0OOOOO00O0O}'],OO000OOOOOO0OOOOO ,db_connect ='starrocks')#line:495
    O000O000O0OO0O0OO =dict (zip (O000O000O0OO0O0OO [0 ],O000O000O0OO0O0OO [1 ]))#line:496
    print ('状态:',O000O000O0OO0O0OO ['State'])#line:497
    print ('统计:',O000O000O0OO0O0OO ['Statistic'])#line:498
    print ('进度:',O000O000O0OO0O0OO ['Progress'])#line:499
    if O000O000O0OO0O0OO ['State']!='RUNNING':#line:500
        print ('ERROR: ',O000O000O0OO0O0OO ['ReasonOfStateChanged'])#line:501
        if not flag :#line:502
            raise Exception ('Starrocks Routin Load')#line:503
def point_test (O0O0OOOO0O00OO0O0 ,OO0O0000OO0000O00 ,sleeptime ='',maxtime =''):#line:510
    ""#line:517
    import pymysql #line:518
    if sleeptime :#line:519
        sleeptime =int (sleeptime )#line:520
        sleeptime =sleeptime if sleeptime >60 else 60 #line:521
    if maxtime :#line:522
        maxtime =int (maxtime )#line:523
        maxtime =maxtime if maxtime <60 *60 *2 else 60 *60 *2 #line:524
    else :#line:525
        maxtime =0 #line:526
    O0OOOO0OOOO0O0O0O =OO0O0000OO0000O00 ['airflow']#line:527
    OO0OO0OOOOO0OOOOO =pymysql .connect (user =O0OOOO0OOOO0O0O0O ['user'],password =O0OOOO0OOOO0O0O0O ['password'],host =O0OOOO0OOOO0O0O0O ['host'],port =O0OOOO0OOOO0O0O0O ['port'],database =O0OOOO0OOOO0O0O0O ['db'],autocommit =True )#line:535
    try :#line:536
        OOO00O00OO00O0000 =OO0OO0OOOOO0OOOOO .cursor ()#line:537
        O0000OOOOOOOO0OOO =f"select start_date,state from dag_run where dag_id ='{O0O0OOOO0O00OO0O0}' ORDER BY id desc LIMIT 1"#line:538
        while True :#line:539
            OOO00O00OO00O0000 .execute (O0000OOOOOOOO0OOO )#line:540
            O00OO00OO0OOOOOO0 =OOO00O00OO00O0000 .fetchall ()#line:541
            if O00OO00OO0OOOOOO0 [0 ][1 ]!='success':#line:542
                if maxtime >0 and O00OO00OO0OOOOOO0 [0 ][1 ]!='failed':#line:543
                    print ('waiting...'+O00OO00OO0OOOOOO0 [0 ][1 ])#line:544
                    time .sleep (sleeptime )#line:545
                    maxtime =maxtime -sleeptime #line:546
                else :#line:547
                    O0O000O0OO000O000 =O00OO00OO0OOOOOO0 [0 ][0 ].strftime ("%Y-%m-%d %H:%M:%S")#line:548
                    O0OOO0O000OO0O00O ='所依赖的dag:'+O0O0OOOO0O00OO0O0 +',状态为'+O00OO00OO0OOOOOO0 [0 ][1 ]+'.其最新的执行时间为'+O0O000O0OO000O000 #line:549
                    fun_email (O0OOO0O000OO0O00O ,'前置DAG任务未成功')#line:550
                    print (O0OOO0O000OO0O00O )#line:551
                    raise SmartPipError ('Run DAG validate Error')#line:552
            else :#line:553
                print ('success...')#line:554
                break #line:555
    except Exception as O00O0OO0OOO000000 :#line:556
        print (O00O0OO0OOO000000 .args )#line:557
        raise SmartPipError ('DAG validate Error')#line:558
    finally :#line:559
        OO0OO0OOOOO0OOOOO .close ()#line:560
class connect_db_execute ():#line:565
    def __init__ (OO0O0O0O0O00OO000 ,dev =False ,db =''):#line:566
        OO0O0O0O0O00OO000 .dev =dev #line:567
    def insert_contents (O000OOO0OOO00O00O ,O0O0OOO00OO000000 ,O0O000O0OO0OOO000 ,per_in =1000 ,connect_dict =None ):#line:569
        O000OOO0000OOOO00 =time .time ()#line:570
        logging .info ('starting to execute insert contents...')#line:571
        if isinstance (connect_dict ,dict ):#line:572
            OOOOOO000O000000O =connect_dict ['dbtype']#line:573
        else :#line:574
            if connect_dict =='':#line:575
                OOOOOO000O000000O ='oracle'#line:576
            else :#line:577
                OOOOOO000O000000O =connect_dict #line:578
            connect_dict =None #line:579
        OO0000O0OO0O0OOOO =getattr (O000OOO0OOO00O00O ,'insert_contents_'+OOOOOO000O000000O )#line:580
        O0OO00O0OOOOOO00O =OO0000O0OO0O0OOOO (O0O0OOO00OO000000 ,O0O000O0OO0OOO000 ,per_in ,connect_dict )#line:581
        logging .info ('execute insert contents time : {}ms'.format (time .time ()-O000OOO0000OOOO00 ))#line:582
        return O0OO00O0OOOOOO00O #line:583
    def impala (OOOO00O0000OOOO0O ,O0O000O0OO0O0O000 ,connect_dict =None ):#line:585
        ""#line:586
        from impala .dbapi import connect as impala #line:587
        OO000O0000O000O00 =impala (user =connect_dict ['user'],password =connect_dict ['password'],host =connect_dict ['host'],port =int (connect_dict ['port']),auth_mechanism ='PLAIN')#line:594
        OOO0O0OO0O00OO00O =OO000O0000O000O00 .cursor ()#line:595
        OOO00OOO0OOO0O0OO =r'^insert\s|^update\s|^truncate\s|^delete\s|^load\s|^refresh\s|^upsert\s'#line:596
        OOOO000OOO0000OOO =None #line:597
        for OO000OO0O0O00O0OO in O0O000O0OO0O0O000 :#line:598
            print (OO000OO0O0O00O0OO )#line:599
            OO000OO0O0O00O0OO =OO000OO0O0O00O0OO .strip ()#line:600
            if not OO000OO0O0O00O0OO :#line:601
                continue #line:602
            if re .search (OOO00OOO0OOO0O0OO ,OO000OO0O0O00O0OO ,re .I |re .IGNORECASE ):#line:603
                OOO0O0OO0O00OO00O .execute (OO000OO0O0O00O0OO )#line:604
            else :#line:605
                OOO0O0OO0O00OO00O .execute (OO000OO0O0O00O0OO )#line:606
                try :#line:607
                    OOOO000OOO0000OOO =OOO0O0OO0O00OO00O .fetchall ()#line:608
                except Exception as OO0000O000000O000 :#line:609
                    print (OO0000O000000O000 .args )#line:610
        OO000O0000O000O00 .close ()#line:611
        return OOOO000OOO0000OOO #line:612
    def hive (O0OO00OO0O000OOOO ,OO0O00000OO00000O ,connect_dict =None ):#line:614
        ""#line:615
        from impala .dbapi import connect as impala #line:616
        OOOOOOO00O0OO0OOO =impala (user =connect_dict ['user'],password =connect_dict ['password'],host =connect_dict ['host'],port =int (connect_dict ['port']),auth_mechanism ='PLAIN')#line:623
        O00OO00000OO000O0 =OOOOOOO00O0OO0OOO .cursor ()#line:624
        O0O0O0O00OO00O000 =r'^insert\s|^update\s|^truncate\s|^delete\s|^load\s'#line:625
        O0OOOOO0O00O0OOOO =None #line:626
        for O00O0OO000O00O0OO in OO0O00000OO00000O :#line:627
            O00O0OO000O00O0OO =O00O0OO000O00O0OO .strip ()#line:628
            if not O00O0OO000O00O0OO :#line:629
                continue #line:630
            print (O00O0OO000O00O0OO )#line:631
            if O00O0OO000O00O0OO .startswith ('refresh'):#line:632
                connect_dict ['port']=21050 #line:633
                O0OO00OO0O000OOOO .impala ([O00O0OO000O00O0OO ],connect_dict =connect_dict )#line:634
            else :#line:635
                if re .search (O0O0O0O00OO00O000 ,O00O0OO000O00O0OO ,re .I |re .IGNORECASE ):#line:636
                    O00OO00000OO000O0 .execute (O00O0OO000O00O0OO )#line:637
                else :#line:638
                    O00OO00000OO000O0 .execute (O00O0OO000O00O0OO )#line:639
                    try :#line:640
                        O0OOOOO0O00O0OOOO =O00OO00000OO000O0 .fetchall ()#line:641
                    except Exception as O000O0000O0O0O0O0 :#line:642
                        print (O000O0000O0O0O0O0 .args )#line:643
        OOOOOOO00O0OO0OOO .close ()#line:644
        return O0OOOOO0O00O0OOOO #line:645
    def mysql (O0OO0O0O000OOOO0O ,OOOO00O00O000OO0O ,connect_dict =None ):#line:647
        import pymysql #line:648
        O0O0OOO0OOO0O00OO =pymysql .connect (user =connect_dict ['user'],password =connect_dict ['password'],host =connect_dict ['host'],port =connect_dict ['port'],database =connect_dict ['db'])#line:655
        try :#line:656
            O0000000OO000O0OO =O0O0OOO0OOO0O00OO .cursor ()#line:657
            OOOO000O0000000OO =r'^insert\s|^update\s|^truncate\s|^delete\s|^load\s'#line:658
            for OO00O0OOO0O0O00O0 in OOOO00O00O000OO0O :#line:659
                OO00O0OOO0O0O00O0 =OO00O0OOO0O0O00O0 .strip ()#line:660
                if not OO00O0OOO0O0O00O0 :#line:661
                    continue #line:662
                print (OO00O0OOO0O0O00O0 )#line:663
                if re .search (OOOO000O0000000OO ,OO00O0OOO0O0O00O0 ,re .I |re .IGNORECASE ):#line:664
                    try :#line:665
                        O0000000OO000O0OO .execute (OO00O0OOO0O0O00O0 )#line:666
                        O0O0OOO0OOO0O00OO .commit ()#line:667
                    except Exception as O0OO00O000000OOO0 :#line:668
                        O0O0OOO0OOO0O00OO .rollback ()#line:669
                        raise O0OO00O000000OOO0 #line:670
                else :#line:671
                    O0000000OO000O0OO .execute (OO00O0OOO0O0O00O0 )#line:672
                    O0O0OO0OOO0OO0OOO =O0000000OO000O0OO .fetchall ()#line:673
                    O0O0OO0OOO0OO0OOO =[[OO0OOOO0O00O0O000 [0 ]for OO0OOOO0O00O0O000 in O0000000OO000O0OO .description ]]+list (O0O0OO0OOO0OO0OOO )#line:674
                    return O0O0OO0OOO0OO0OOO #line:675
        except Exception as OOOO000O0OOO00O00 :#line:676
            raise OOOO000O0OOO00O00 #line:677
        finally :#line:678
            O0O0OOO0OOO0O00OO .close ()#line:679
    def starrocks (OOO00OOO000OO000O ,O0O0OO0O0OOO0O0OO ,connect_dict =None ):#line:681
        return OOO00OOO000OO000O .mysql (O0O0OO0O0OOO0O0OO ,connect_dict )#line:682
    def oracle (OOOO0O00OO0OOO0O0 ,OO0OOO0OO00000OO0 ,connect_dict =None ):#line:684
        import cx_Oracle #line:685
        OO0O00OOOO0O0OO0O ='{}/{}@{}/{}'.format (connect_dict ['user'],connect_dict ['password'],connect_dict ['host'],connect_dict ['db'])#line:690
        O0O000OOOO0000O0O =cx_Oracle .connect (OO0O00OOOO0O0OO0O )#line:691
        try :#line:692
            O00000O0000O0OOO0 =O0O000OOOO0000O0O .cursor ()#line:693
            O0O0O0OO0O0O00O00 =r'^insert\s|^update\s|^truncate\s|^delete\s|^comment\s'#line:694
            for OO0O00O000O000OOO in OO0OOO0OO00000OO0 :#line:695
                OO0O00O000O000OOO =OO0O00O000O000OOO .strip ()#line:696
                if not OO0O00O000O000OOO :#line:697
                    continue #line:698
                if re .search (O0O0O0OO0O0O00O00 ,OO0O00O000O000OOO ,re .I ):#line:699
                    try :#line:700
                        O00000O0000O0OOO0 .execute (OO0O00O000O000OOO )#line:701
                        O0O000OOOO0000O0O .commit ()#line:702
                    except Exception as O0OOO0O0O00O0000O :#line:703
                        if OO0O00O000O000OOO .startswith ('comment'):#line:704
                            print ('err:',OO0O00O000O000OOO )#line:705
                            continue #line:706
                        O0O000OOOO0000O0O .rollback ()#line:707
                        raise O0OOO0O0O00O0000O #line:708
                else :#line:709
                    O00000O0000O0OOO0 .execute (OO0O00O000O000OOO )#line:710
                    OOOO0O0OOO000OOO0 =O00000O0000O0OOO0 .fetchall ()#line:711
                    OOOO0O0OOO000OOO0 =[[O0OOO0OO00000OOOO [0 ]for O0OOO0OO00000OOOO in O00000O0000O0OOO0 .description ]]+list (OOOO0O0OOO000OOO0 )#line:712
                    return OOOO0O0OOO000OOO0 #line:713
        except Exception as O0O00O0O0OOO0O0OO :#line:714
            raise O0O00O0O0OOO0O0OO #line:715
        finally :#line:716
            O0O000OOOO0000O0O .close ()#line:717
    def gp (OO0O0O00O0O0OO0O0 ,O0OO00000O0OO0000 ,connect_dict =None ):#line:719
        import psycopg2 #line:720
        OO0000OOOO0OOO0O0 =psycopg2 .connect (user =connect_dict ['user'],password =connect_dict ['password'],host =connect_dict ['host'],port =connect_dict ['port'],database =connect_dict ['db'])#line:727
        try :#line:728
            OOOOO00O0O0OO0000 =OO0000OOOO0OOO0O0 .cursor ()#line:729
            OO0000O000O0O000O =r'^insert\s|^update\s|^truncate\s|^delete\s'#line:730
            for OO0OO0O00OO0O0OOO in O0OO00000O0OO0000 :#line:731
                OO0OO0O00OO0O0OOO =OO0OO0O00OO0O0OOO .strip ()#line:732
                if not OO0OO0O00OO0O0OOO :#line:733
                    continue #line:734
                if re .search (OO0000O000O0O000O ,OO0OO0O00OO0O0OOO ,re .I |re .IGNORECASE ):#line:735
                    try :#line:736
                        OOOOO00O0O0OO0000 .execute (OO0OO0O00OO0O0OOO )#line:737
                        OO0000OOOO0OOO0O0 .commit ()#line:738
                    except Exception as OO00O0OOOOO0O0O00 :#line:739
                        OO0000OOOO0OOO0O0 .rollback ()#line:740
                        raise OO00O0OOOOO0O0O00 #line:741
                else :#line:742
                    OOOOO00O0O0OO0000 .execute (OO0OO0O00OO0O0OOO )#line:743
                    O0000O0O0OO0000O0 =OOOOO00O0O0OO0000 .fetchall ()#line:744
                    O0000O0O0OO0000O0 =[[O00O0O0OO0OO00O0O [0 ]for O00O0O0OO0OO00O0O in OOOOO00O0O0OO0000 .description ]]+list (O0000O0O0OO0000O0 )#line:745
                    return O0000O0O0OO0000O0 #line:746
        except Exception as O0O0OO0OOO00OO0OO :#line:747
            raise O0O0OO0OOO00OO0OO #line:748
        finally :#line:749
            OO0000OOOO0OOO0O0 .close ()#line:750
    def mssql (OO0O000000OO0OOO0 ,O00OOOO0OO00OO0O0 ,connect_dict =None ):#line:751
        import pymssql #line:752
        if connect_dict ['port']:#line:753
            O000OOOOO0OO00O0O =pymssql .connect (user =connect_dict ['user'],password =connect_dict ['password'],host =connect_dict ['host'],port =int (connect_dict ['port']),database =connect_dict ['db'],charset ="utf8",)#line:761
        else :#line:762
            O000OOOOO0OO00O0O =pymssql .connect (user =connect_dict ['user'],password =connect_dict ['password'],host =connect_dict ['host'],database =connect_dict ['db'],charset ="utf8",)#line:769
        try :#line:770
            OOOOO00O0OO0OO00O =O000OOOOO0OO00O0O .cursor ()#line:771
            O0O00O000OO0OO000 =r'^insert\s|^update\s|^truncate\s|^delete\s'#line:772
            for O0000OO0000OO0OO0 in O00OOOO0OO00OO0O0 :#line:773
                O0000OO0000OO0OO0 =O0000OO0000OO0OO0 .strip ()#line:774
                if not O0000OO0000OO0OO0 :#line:775
                    continue #line:776
                if re .search (O0O00O000OO0OO000 ,O0000OO0000OO0OO0 ,re .I |re .IGNORECASE ):#line:777
                    try :#line:778
                        OOOOO00O0OO0OO00O .execute (O0000OO0000OO0OO0 )#line:779
                        O000OOOOO0OO00O0O .commit ()#line:780
                    except Exception as OOO0O0OO0O0OOO000 :#line:781
                        O000OOOOO0OO00O0O .rollback ()#line:782
                        raise OOO0O0OO0O0OOO000 #line:783
                else :#line:784
                    OOOOO00O0OO0OO00O .execute (O0000OO0000OO0OO0 )#line:785
                    O0000O0O0OO000000 =OOOOO00O0OO0OO00O .fetchall ()#line:786
                    O0000O0O0OO000000 =[[OO0OOO0O0OOOO0OOO [0 ]for OO0OOO0O0OOOO0OOO in OOOOO00O0OO0OO00O .description ]]+list (O0000O0O0OO000000 )#line:787
                    return O0000O0O0OO000000 #line:788
        except Exception as OO0O00O0OO0O0000O :#line:789
            raise OO0O00O0OO0O0000O #line:790
        finally :#line:791
            O000OOOOO0OO00O0O .close ()#line:792
    def execute_sql_list (OOOO00OO0O0O0OO0O ,O00O000OO0O00OOOO ,db_connect ='',connect_dict =None ):#line:794
        if db_connect =='':db_connect ='oracle'#line:795
        O00OOO0OO0OOOO0OO =getattr (OOOO00OO0O0O0OO0O ,db_connect )#line:796
        return O00OOO0OO0OOOO0OO (O00O000OO0O00OOOO ,connect_dict =connect_dict )#line:797
    def excute_proc (OO00OO0O0OOOOOO00 ,O0OO000O000OO0OOO ,O0O00O00O00OO0OOO ,proc_para =None ):#line:799
        import cx_Oracle #line:800
        OOOO0OO0OOO00000O ='{}/{}@{}/{}'.format (O0O00O00O00OO0OOO ['user'],O0O00O00O00OO0OOO ['password'],O0O00O00O00OO0OOO ['host'],O0O00O00O00OO0OOO ['db'])#line:806
        OOO0000O0O0OOOOO0 =cx_Oracle .connect (OOOO0OO0OOO00000O )#line:807
        try :#line:809
            OO0OO000OOO0000OO =OOO0000O0O0OOOOO0 .cursor ()#line:810
            print ("开始执行过程:{}  参数: {}".format (O0OO000O000OO0OOO ,proc_para ))#line:811
            if proc_para is None :#line:812
                OOO0O0000000OOOOO =OO0OO000OOO0000OO .callproc (O0OO000O000OO0OOO )#line:813
                OOO0000O0O0OOOOO0 .commit ()#line:814
            else :#line:815
                OOO0O0000000OOOOO =OO0OO000OOO0000OO .callproc (O0OO000O000OO0OOO ,proc_para )#line:817
                OOO0000O0O0OOOOO0 .commit ()#line:818
            OO0OO000OOO0000OO .close ()#line:819
            OOO0000O0O0OOOOO0 .close ()#line:820
            print (OOO0O0000000OOOOO )#line:821
        except Exception as O0O0OOOO0OOO00O00 :#line:822
            OOO0000O0O0OOOOO0 .rollback ()#line:823
            OOO0000O0O0OOOOO0 .close ()#line:824
            raise O0O0OOOO0OOO00O00 #line:826
        return True #line:827
    def insert_contents_oracle (OO00O0O0000OOO00O ,OOO0OOOO0OOOOO000 ,O00O0O0O00OOO00OO ,per_in =100 ,connect_dict =None ):#line:829
        import cx_Oracle #line:830
        O0OOO00OOO0OOOO00 ='{}/{}@{}:{}/{}'.format (connect_dict ['user'],connect_dict ['password'],connect_dict ['host'],connect_dict ['port'],connect_dict ['db'])#line:836
        OO00OO00OO00O0O00 =cx_Oracle .connect (O0OOO00OOO0OOOO00 )#line:837
        OO0000O0O0O0000OO =OO00OO00OO00O0O00 .cursor ()#line:838
        O000O0000O0O0OOOO =' into {} values {}'#line:839
        OO000O0OOO0OO0OOO =''#line:840
        O0O000OOOO00O0O0O =len (OOO0OOOO0OOOOO000 )#line:841
        logging .info ("total {} records need to insert table {}: ".format (O0O000OOOO00O0O0O ,O00O0O0O00OOO00OO ))#line:842
        try :#line:843
            for OOO0O0OOO00O000OO in range (O0O000OOOO00O0O0O ):#line:844
                OO000O0OOO0OO0OOO =OO000O0OOO0OO0OOO +O000O0000O0O0OOOO .format (O00O0O0O00OOO00OO ,tuple (OOO0OOOO0OOOOO000 [OOO0O0OOO00O000OO ]))+'\n'#line:845
                if (OOO0O0OOO00O000OO +1 )%per_in ==0 or OOO0O0OOO00O000OO ==O0O000OOOO00O0O0O -1 :#line:846
                    OO0OOO0O0O0O0OO00 ='insert all '+OO000O0OOO0OO0OOO +'select 1 from dual'#line:847
                    logging .debug (OO0OOO0O0O0O0OO00 )#line:848
                    OO0000O0O0O0000OO .execute (OO0OOO0O0O0O0OO00 )#line:849
                    OO00OO00OO00O0O00 .commit ()#line:850
                    OO000O0OOO0OO0OOO =''#line:851
            return str (O0O000OOOO00O0O0O )#line:852
        except Exception as OOOOO00O0O0OO00OO :#line:853
            try :#line:854
                OO00OO00OO00O0O00 .rollback ()#line:855
                OO0000O0O0O0000OO .execute ("delete from {} where UPLOADTIME = '{}'".format (O00O0O0O00OOO00OO ,OOO0OOOO0OOOOO000 [0 ][-1 ]))#line:856
                OO00OO00OO00O0O00 .commit ()#line:857
            except Exception :#line:858
                logging .error ('can not delete by uploadtime')#line:859
            finally :#line:860
                raise OOOOO00O0O0OO00OO #line:861
        finally :#line:862
            OO00OO00OO00O0O00 .close ()#line:863
class _O0O0OO0000O00O0O0 (object ):#line:867
    connect =None #line:868
    def __init__ (OO0OOO0000OOO0OOO ,O00OO0OOO00O0O0O0 ,OO0OO00OO0000OO0O ,OO00OO00OOOO00O0O ):#line:870
        OO0OOO0000OOO0OOO .end_offset =None #line:871
        OO0OOO0000OOO0OOO .db_err_count =0 #line:872
        OO0OOO0000OOO0OOO .topic =O00OO0OOO00O0O0O0 #line:873
        OO0OOO0000OOO0OOO .kafkaconfig =OO0OO00OO0000OO0O #line:874
        OO0OOO0000OOO0OOO .offsetDict ={}#line:875
        OO0OOO0000OOO0OOO .current_dir =OO00OO00OOOO00O0O #line:876
        try :#line:877
            OO0OOO0000OOO0OOO .consumer =OO0OOO0000OOO0OOO .connect_kafka_customer ()#line:878
        except Exception as O0OOOOOOO0O00O0OO :#line:879
            O0OOOOOOO0O00O0OO ='kafka无法连接','ErrLocation：{}\n'.format (O00OO0OOO00O0O0O0 )+str (O0OOOOOOO0O00O0OO )+',kafka消费者无法创建'#line:880
            raise O0OOOOOOO0O00O0OO #line:881
    def get_toggle_or_offset (OO0O00OOOO00OOO0O ,OO00OO000OO000O00 ,OOO0O0OO0O0O0O0O0 ):#line:883
        ""#line:884
        O0O0000OO0OOO000O =0 #line:885
        try :#line:886
            O0000OO0O0O0OO0OO =f"{OO0O00OOOO00OOO0O.current_dir}/kafka/{OO00OO000OO000O00}_offset_{OOO0O0OO0O0O0O0O0}.txt"#line:887
            if os .path .exists (O0000OO0O0O0OO0OO ):#line:888
                OOO0OO0O0OOOOOOO0 =open (O0000OO0O0O0OO0OO ).read ()#line:889
                if OOO0OO0O0OOOOOOO0 :#line:890
                    O0O0000OO0OOO000O =int (OOO0OO0O0OOOOOOO0 )#line:891
            else :#line:892
                with open (O0000OO0O0O0OO0OO ,encoding ='utf-8',mode ='a')as O0O00OO00OO0O0O0O :#line:893
                    O0O00OO00OO0O0O0O .close ()#line:894
        except Exception as O0O0OO000OOO0O0OO :#line:895
            print (f"读取失败：{O0O0OO000OOO0O0OO}")#line:896
            raise O0O0OO000OOO0O0OO #line:897
        return O0O0000OO0OOO000O #line:898
    def write_offset (O0OO000OO0O00000O ,OOO00000000O0000O ,offset =None ):#line:900
        ""#line:903
        if O0OO000OO0O00000O .topic and offset :#line:904
            O00O00OOOO0O0OOOO =f"{O0OO000OO0O00000O.current_dir}/kafka/{O0OO000OO0O00000O.topic}_offset_{OOO00000000O0000O}.txt"#line:906
            try :#line:907
                with open (O00O00OOOO0O0OOOO ,'w')as OO0O00O0OO000OO0O :#line:908
                    OO0O00O0OO000OO0O .write (str (offset ))#line:909
                    OO0O00O0OO000OO0O .close ()#line:910
            except Exception as O0OO0O0O00000000O :#line:911
                print (f"写入offset出错：{O0OO0O0O00000000O}")#line:912
                raise O0OO0O0O00000000O #line:913
    def connect_kafka_customer (O00O0O0O0O0O0000O ):#line:915
        ""#line:916
        OO0O0O00OOOO000O0 =KafkaConsumer (**O00O0O0O0O0O0000O .kafkaconfig )#line:917
        return OO0O0O00OOOO000O0 #line:918
    def parse_data (O0O0O0O00000OO000 ,OO00O0OOO0OO00000 ):#line:920
        ""#line:925
        return dict ()#line:926
    def gen_sql (OOO0000O0OOOO0O0O ,O000O0000O0000O0O ):#line:928
        ""#line:933
        OO00OOO00OOO0O0O0 =[]#line:934
        for OO0OO0O0OO0OOOO00 in O000O0000O0000O0O :#line:935
            OO00OOO00OOO0O0O0 .append (str (tuple (OO0OO0O0OO0OOOO00 )))#line:937
        return ','.join (OO00OOO00OOO0O0O0 )#line:938
    def dispose_kafka_data (OOOO00000O00O0OOO ,O0O00OO00O0OO00O0 ):#line:940
        ""#line:945
        pass #line:946
    def get_now_time (OOO0OOOOO0OO000OO ):#line:948
        ""#line:952
        OOO0O000O00O0OOOO =int (time .time ())#line:953
        return time .strftime ('%Y-%m-%d %H:%M:%S',time .localtime (OOO0O000O00O0OOOO ))#line:954
    def tran_data (O0OO0000000OOOOOO ,O0OOO000OOOOO0OO0 ,OOO0OO00OOOO00OO0 ):#line:956
        ""#line:962
        OOOO0OO000OO000O0 =O0OOO000OOOOO0OO0 .get (OOO0OO00OOOO00OO0 ,"")#line:963
        OOOO0OO000OO000O0 =""if OOOO0OO000OO000O0 is None else OOOO0OO000OO000O0 #line:964
        return str (OOOO0OO000OO000O0 )#line:965
    def consumer_data (OO0O0O00OOO0O0000 ,O0OOOO00OOO0O00OO ,O0000OOOO00OO0OO0 ,O0OOOO0000O0000O0 ):#line:967
        ""#line:974
        if OO0O0O00OOO0O0000 .consumer :#line:975
            OO0O0O00OOO0O0000 .consumer .assign ([TopicPartition (topic =OO0O0O00OOO0O0000 .topic ,partition =O0OOOO00OOO0O00OO )])#line:976
            O0O0OOO00O000OOO0 =TopicPartition (topic =OO0O0O00OOO0O0000 .topic ,partition =O0OOOO00OOO0O00OO )#line:978
            OOO000OO0000OOOOO =OO0O0O00OOO0O0000 .consumer .beginning_offsets ([O0O0OOO00O000OOO0 ])#line:979
            O000O0O00OOOOOOO0 =OOO000OO0000OOOOO .get (O0O0OOO00O000OOO0 )#line:980
            OO00O0OOOO00OOOOO =OO0O0O00OOO0O0000 .consumer .end_offsets ([O0O0OOO00O000OOO0 ])#line:981
            OO0O0OO0O000000O0 =OO00O0OOOO00OOOOO .get (O0O0OOO00O000OOO0 )#line:982
            print (f'建立消费者, {O0OOOO00OOO0O00OO}分区, 最小offset:{O000O0O00OOOOOOO0}, 最大offset:{OO0O0OO0O000000O0}')#line:983
            if O0000OOOO00OO0OO0 <O000O0O00OOOOOOO0 :#line:984
                print (f'Warning: 消费offset：{O0000OOOO00OO0OO0} 小于最小offset:{O000O0O00OOOOOOO0}')#line:985
                O0000OOOO00OO0OO0 =O000O0O00OOOOOOO0 #line:986
            if O0000OOOO00OO0OO0 >=OO0O0OO0O000000O0 :#line:987
                print (f'消费offset：{O0000OOOO00OO0OO0} 大于最大offset:{OO0O0OO0O000000O0}, 本次不消费')#line:988
                return #line:989
            OO0O0O00OOO0O0000 .end_offset =OO0O0OO0O000000O0 #line:990
            OO0O0O00OOO0O0000 .consumer .seek (TopicPartition (topic =OO0O0O00OOO0O0000 .topic ,partition =O0OOOO00OOO0O00OO ),offset =O0000OOOO00OO0OO0 )#line:991
            print (f'消费{O0OOOO00OOO0O00OO}分区, 开始消费offset：{O0000OOOO00OO0OO0}!')#line:992
            O00000O00O0O00O0O =O0OOOO0000O0000O0 (OO0O0O00OOO0O0000 .consumer )#line:993
            O0000OOOO00OO0OO0 =O00000O00O0O00O0O .offset +1 #line:994
            OO0O0O00OOO0O0000 .offsetDict [O0OOOO00OOO0O00OO ]=O0000OOOO00OO0OO0 #line:997
            OO0O0O00OOO0O0000 .write_offset (O0OOOO00OOO0O00OO ,O0000OOOO00OO0OO0 )#line:998
            OO0O0O00OOO0O0000 .offsetDict [O0OOOO00OOO0O00OO ]=O0000OOOO00OO0OO0 #line:1001
            OO0O0O00OOO0O0000 .write_offset (O0OOOO00OOO0O00OO ,O0000OOOO00OO0OO0 )#line:1002
    def consumer_topic (O0000OOOO0O0OOOO0 ,O0O0OO000O0OOO0OO ):#line:1004
        print (f"topic: {O0000OOOO0O0OOOO0.topic}")#line:1005
        print ('开始解析。')#line:1006
        O0000OOO0O0OOO00O =O0000OOOO0O0OOOO0 .consumer .partitions_for_topic (topic =O0000OOOO0O0OOOO0 .topic )#line:1008
        for O00O00OO000O000OO in O0000OOO0O0OOO00O :#line:1009
            OO00OO0OOO000O0OO =O0000OOOO0O0OOOO0 .get_toggle_or_offset (O0000OOOO0O0OOOO0 .topic ,O00O00OO000O000OO )#line:1010
            O0O0OO000O0OO0OO0 =None if OO00OO0OOO000O0OO <0 else OO00OO0OOO000O0OO #line:1012
            O0000OOOO0O0OOOO0 .consumer_data (O00O00OO000O000OO ,O0O0OO000O0OO0OO0 ,O0O0OO000O0OOO0OO )#line:1013
    def save_all_offset (O00O0OO00OOO0O00O ):#line:1015
        for OOOO00O0OOOOOO0O0 ,OO0000OOO0O0OO0O0 in O00O0OO00OOO0O00O .offsetDict :#line:1016
            O00O0OO00OOO0O00O .write_offset (OOOO00O0OOOOOO0O0 ,OO0000OOO0O0OO0O0 )#line:1017
