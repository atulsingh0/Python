CONF = "ConfigLen.txt"
LenDetailQuery = 'Len_Detail_Query.sql'
#NullInsertQuery = 'Null_Insert_Query.sql'
#NullHiveQuery = 'Null_Hive_Query.sql'

conf = open(CONF, 'r');
null_detail_sqls=[]
null_insert_sqls=[]
null_hive_sqls=[]

for line in conf:
    cols = line.strip().split('~')

    Name = cols[0]
    SrcName = cols[1]
    ChkId = cols[2]
    Desp = cols[3]
    SrcTab = cols[4]
    SrcCol = cols[5]
    PK1 = cols[6]
    PK2 = cols[7]
    PK3 = cols[8]
    PK4 = cols[9]
    PK5 = cols[10]
    PK6 = cols[11]
    PK7 = cols[12]
    PK8 = cols[13]
    FtrRule = cols[14]
    ChkType = cols[15]
    MinLen = cols[16]
    MaxLen = cols[17]
    ThrePer = cols[18]
    Dt = cols[19]
	
    
    


    pknames=('\'-\'' if len(PK1)==0 else SrcTab+'.'+PK1)  + \
            ('' if len(PK2)==0 else  ', '+SrcTab+'.'+ PK2) + \
            ('' if len(PK3)==0 else  ', '+SrcTab+'.'+ PK3 ) + \
            ('' if len(PK4)==0 else  ', '+SrcTab+'.'+ PK4 ) + \
            ('' if len(PK5)==0 else  ', '+SrcTab+'.'+ PK5 ) + \
            ('' if len(PK6)==0 else  ', '+SrcTab+'.'+ PK6 ) + \
            ('' if len(PK7)==0 else  ', '+SrcTab+'.'+ PK7 ) + \
            ('' if len(PK8)==0 else  ', '+SrcTab+'.'+ PK8 )

    pk1 =  '\'-\'' if len(PK1)==0 else SrcTab+'.'+PK1
    pk2 =  '\'-\'' if len(PK2)==0 else SrcTab+'.'+PK2
    pk3 =  '\'-\''  if len(PK3)==0 else SrcTab+'.'+PK3
    pk4 =  '\'-\''  if len(PK4)==0 else SrcTab+'.'+PK4
    pk5 =  '\'-\''  if len(PK5)==0 else SrcTab+'.'+PK5
    pk6 =  '\'-\''  if len(PK6)==0 else SrcTab+'.'+PK6
    pk7 =  '\'-\''  if len(PK7)==0 else SrcTab+'.'+PK7
    pk8 =  '\'-\''  if len(PK8)==0 else SrcTab+'.'+PK8
    errcol = SrcTab+'.'+SrcCol
    fil_cond = '1=1' if len(FtrRule)==0 else FtrRule
	
	# select 'DQ_LEN_AMC_CUST_ACCOUNT_2','AMC_CUST_ACCOUNT.ETL_FILEID ,AMC_CUST_ACCOUNT.ETL_BATCHID ,AMC_CUST_ACCOUNT.EAP_AS_OF_DT ,AMC_CUST_ACCOUNT.IMSNUMBER' pknames ,AMC_CUST_ACCOUNT.ETL_FILEID pk1,AMC_CUST_ACCOUNT.ETL_BATCHID PK2,AMC_CUST_ACCOUNT.EAP_AS_OF_DT pk3,AMC_CUST_ACCOUNT.IMSNUMBER pk4,'-' pk5,'-' pk6,'-' pk7,'-' pk8,AMC_CUST_ACCOUNT.TAXID errcol   from AMC_CUST_ACCOUNT where (AMC_CUST_ACCOUNT.TAXID is  not null or AMC_CUST_ACCOUNT.TAXID != '') and (length(AMC_CUST_ACCOUNT.TAXID) < 0 OR length(AMC_CUST_ACCOUNT.TAXID) > 20)  


    # generating NULL Detailed Query
    Len_detail_query = "select '{chk_id}', '{pknames}' pknames, {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5,{pk6} pk6, {pk7} pk7, {pk8} pk8, {errcol} errcol from {table} where ({errcol} is not null or {errcol} != '') and (length({errcol}) < {MinLen} OR length({errcol}) > {MaxLen})"\
                  .format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, pk6=pk6, pk7=pk7, pk8=pk8, errcol=errcol, table=SrcTab,MinLen=MinLen,MaxLen=MaxLen );
    null_detail_query1 = Len_detail_query+"\n";
    null_detail_sqls.append(null_detail_query1)


    # generating Insert Query for Oracle DQ_CHECK_MASTER
    # null_insert_query = "insert into dq_check_master (DQ_APP_NAME,DQ_CHECK_ID,DQ_CHECK_DESC,DQ_SRC_SCHEMA,,DQ_SRC_TBL,DQ_SRC_COL,DQ_THRESHOLD_PER,DQ_DETL_SQL,DQ_CHK_TYPE,dq_chk_created_dt) values('{Name}', '{ChkId}', '{Desp}', '{SrcName}', '{SrcTab}', '{SrcCol}', '{ThrePer}', '{null_detail_query}', '{ChkType}', '{Dt}') \n"\
                        # .format(SrcTab=SrcTab, Desp=Desp, ChkId=ChkId, SrcCol=SrcCol, Name=Name, SrcName=SrcName, ThrePer=ThrePer, null_detail_query=null_detail_query, ChkType=ChkType, Dt=Dt)
    # null_insert_sqls.append(null_insert_query)


    # generating HIVE DQ_CHECK_MASTER
    # null_hive_query = "{Name}~{ChkId}~{Desp}~{SrcName}~{SrcTab}~{SrcCol}~{ThrePer}~{null_detail_query}~{ChkType}~{Dt}\n"\
                        # .format(Name=Name, ChkId=ChkId, Desp=Desp, SrcName=SrcName, SrcTab=SrcTab, SrcCol=SrcCol, ThrePer=ThrePer, null_detail_query=null_detail_query, ChkType=ChkType, Dt=Dt)
    # null_hive_sqls.append(null_hive_query)


# Writing data into Files
nulldetail = open(LenDetailQuery, 'w')
nulldetail.writelines(null_detail_sqls);
nulldetail.close()

#nullinsert = open(NullInsertQuery, 'w')
#nullinsert.writelines(null_insert_sqls);
#nullinsert.close()

#nullhive = open(NullHiveQuery, 'w')
#nullhive.writelines(null_hive_sqls);
#nullhive.close()

conf.close()

