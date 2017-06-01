CONF = "AllChkConfig.csv"
QueryFile = 'Queries.sql'
#NullInsertQuery = 'Null_Insert_Query.sql'
#NullHiveQuery = 'Null_Hive_Query.sql'

conf = open(CONF, 'r');
detail_sqls=[]


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
    NullChk = cols[14]
    NullFtrRule = cols[15]
    NullChkCrtDt = cols[16]
    NullChkThrePer = cols[17]
    LenChk = cols[18]
    LenFtrRule = cols[19]
    MinLen = cols[20]
    MaxLen = cols[21]
    LenChkThrePer = cols[22]
    LenChkDt = cols[23]
    LovChk = cols[24]
    LovFtrRule = cols[25]
    LovChkDt = cols[26]
    LovChkThrePer = cols[27]
    RefChk = cols[28]
    RefFtrRule = cols[29]
    LkpCustSQL= cols[30]
    LkpTblSchema = cols[31]
    LkpTblNm = cols[32]
    LkpTblKeyCustSQL = cols[33]
    Cust_Sql= cols[34]
    CustSQLTblNm = cols[35]
    CustSQLTblNmCustSqlKey = cols[36]
    RefChkThrePer = cols[37]
    RefChkDt = cols[38]
    DupChk = cols[39]
    DupFtrRule = cols[40]
    DupChkDt = cols[41]
    DupChkThrePer = cols[42]
    DataChk = cols[43]
    DataFtrRule = cols[44]
    DataChkDt = cols[45]
    DataChkThrePer = cols[46]




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

        
    # If Null CHK Exist, Generate the NULL Query
    if (NullChk=='Y'):
        ChkType='NULL CHK'
        Null_fil_cond = '1=1' if len(NullFtrRule)==0 else NullFtrRule
        
        null_detail_query = "select '{chk_id}', '{pknames}' pknames, {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5,{pk6} pk6, {pk7} pk7, {pk8} pk8, {errcol} errcol from {table} where ({errcol} is null and {errcol} = '') and {Null_fil_cond}"\
                  .format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, pk6=pk6, pk7=pk7, pk8=pk8, errcol=errcol, table=SrcTab, Null_fil_cond=Null_fil_cond);
        null_detail_query1 = null_detail_query+"\n";
        detail_sqls.append(null_detail_query1)

    # If LEN CHK Exist, Generate the LEN Query
    if (LenChk=='Y'):
        ChkType='LEN CHK'
        Lov_fil_cond = '1=1' if len(LovFtrRule)==0 else LovFtrRule
        Len_detail_query = "select '{chk_id}', '{pknames}' pknames, {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5,{pk6} pk6, {pk7} pk7, {pk8} pk8, {errcol} errcol from {table} where ({errcol} is not null or {errcol} != '') and (length({errcol}) < {MinLen} OR length({errcol}) > {MaxLen})"\
                  .format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, pk6=pk6, pk7=pk7, pk8=pk8, errcol=errcol, table=SrcTab,MinLen=MinLen,MaxLen=MaxLen );
        Len_detail_query1 = Len_detail_query+"\n";
        detail_sqls.append(Len_detail_query1)


    # If LOV CHK Exist, Generate the LOV Query
    if (LovChk=='Y'):
        ChkType='LOV CHK'
        Lov_detail_query = "select '{chk_id}', '{pknames}' pknames, {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5,{pk6} pk6, {pk7} pk7, {pk8} pk8, {errcol} errcol from {table} where ({errcol} is not null or {errcol} != '') and {errcol} not in ({LovFtrRule})"\
                  .format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, pk6=pk6, pk7=pk7, pk8=pk8, errcol=errcol, table=SrcTab, LovFtrRule=LovFtrRule );
        Lov_detail_query1 = Lov_detail_query+"\n";
        detail_sqls.append(Lov_detail_query1)


    # If REF CHK Exist, Generate the REF Query
    if (RefChk=='Y'):
        ChkType='REF CHK'
        ref_Case =  'case when (('+LkpTblNm+"."+LkpTblKeyCustSQL+' IS NULL OR '+LkpTblNm+"."+LkpTblKeyCustSQL+"='' ) and (1=1)) then 1 else 0 end " if LkpCustSQL=='Y' else 'case when (( '+CustSQLTblNm+"."+CustSQLTblNmCustSqlKey+' IS NULL OR + '+CustSQLTblNm+"."+CustSQLTblNmCustSqlKey+"='' ) and (1=1)) then 1 else 0 end "
        leftTable = 'LEFT OUTER JOIN '+ LkpTblSchema+"."+LkpTblNm+' on ( '+ SrcTab+"."+SrcCol+'='+LkpTblNm+"."+LkpTblKeyCustSQL+')' if LkpCustSQL=='Y' else 'LEFT OUTER JOIN '+ Cust_Sql + 'on ( '+ SrcTab+"."+SrcCol+'='+CustSQLTblNm+"."+CustSQLTblNmCustSqlKey+")"

        Ref_detail_query = "select '{pknames}' pknames,{pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5,{pk6} pk6, {pk7} pk7, {pk8} pk8, {errcol} errcol, {ref_Case} ref_Case from {SrcTab} {leftTable}"\
                  .format( pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, pk6=pk6, pk7=pk7, pk8=pk8, errcol=errcol, SrcTab=SrcTab, LkpTblNm=LkpTblNm,LkpTblKeyCustSQL=LkpTblKeyCustSQL, leftTable=leftTable, ref_Case=ref_Case);
        Ref_detail_query1 = Ref_detail_query+"\n";
        detail_sqls.append(Ref_detail_query1)


    # If DUP CHK Exist, Generate the DUP Query
    if (DupChk=='Y'):
        ChkType='DUP CHK'
        Dup_fil_cond = '1=1' if len(DupFtrRule)==0 else DupFtrRule
        PartitionByKey=('\'-\'' if len(PK1)==0 else PK1) + \
                   ('' if len(PK2)==0 else   ',' + PK2) + \
               ('' if len(PK3)==0 else   ',' + PK3 ) + \
                   ('' if len(PK4)==0 else   ',' + PK4 ) + \
                   ('' if len(PK5)==0 else   ',' + PK5 ) + \
                   ('' if len(PK6)==0 else   ',' + PK6 ) + \
                   ('' if len(PK7)==0 else   ',' + PK7 ) + \
                   ('' if len(PK8)==0 else   ',' + PK8 )


        Dup_detail_query = "select '{chk_id}', '{pknames}' pknames, {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5,{pk6} pk6, {pk7} pk7, {pk8} pk8,count(*) errcol from {table} where {Dup_fil_cond} GROUP BY {PartitionByKey} HAVING COUNT(1)>1"\
                  .format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, pk6=pk6, pk7=pk7, pk8=pk8, errcol=errcol, table=SrcTab,Dup_fil_cond=Dup_fil_cond,PartitionByKey=PartitionByKey );
        Dup_detail_query1 = Dup_detail_query+"\n";
        detail_sqls.append(Dup_detail_query1)



    # generating DATA TYPE CHK Detailed Query
    if (DataChk=='Y'):
        ChkType='Data CHK'
        DataType_detail_query = "select '{chk_id}', '{pknames}' pknames, {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5,{pk6} pk6, {pk7} pk7, {pk8} pk8,{errcol} errcol from {table} where Not ({table}.{SrcCol} is null or {table}.{SrcCol} = '') and ({SrcCol} like {DataFtrRule})"\
                  .format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, pk6=pk6, pk7=pk7, pk8=pk8, errcol=errcol, table=SrcTab,SrcCol=SrcCol,DataFtrRule=DataFtrRule );
        DataType_detail_query1 = DataType_detail_query+"\n";
        detail_sqls.append(DataType_detail_query1)



# Writing data into Files
detail = open(QueryFile, 'w')
detail.writelines(detail_sqls);
detail.close()


conf.close()