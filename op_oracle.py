import cx_Oracle,os,uuid,datetime

db_string = 'hr/112510@39.104.235.35:49161/xe'

def wr_jdsf_zhuzhai(location,status,num):
    try:
        os.environ['NLS_LANG'] = "SIMPLIFIED CHINESE_CHINA.AL32UTF8" #设置Oracle语言编码变量，非常重要
        db = cx_Oracle.connect(db_string)
        cursor = db.cursor()
        param={'UUID':str(uuid.uuid1()),
               'LOCATION':location,
               'STATUS':status,
               'NUM':num,
               'UPDATE_TIME':datetime.datetime.now()}
        sql="""insert into HR."JDSF_ZHUZHAI" values(:UUID,:LOCATION,:STATUS,:NUM,:UPDATE_TIME)"""
        cursor.execute(sql,param)
        db.commit()
        cursor.close()
        db.close()
    except Exception as e:
        raise e
