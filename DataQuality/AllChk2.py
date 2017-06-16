# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 07:31:11 2017
@author: Atul
"""


def genPK(PK1,PK2,PK3,PK4,PK5,PK6,PK7,PK8,SrcTab,tabAlias=''):
	
    if len(tabAlias)>0:
        SrcTab=tabAlias
    
        
    pk1 =  '\'-\'' if len(PK1)==0 else SrcTab+'.'+PK1
    pk2 =  '\'-\'' if len(PK2)==0 else SrcTab+'.'+PK2
    pk3 =  '\'-\''  if len(PK3)==0 else SrcTab+'.'+PK3
    pk4 =  '\'-\''  if len(PK4)==0 else SrcTab+'.'+PK4
    pk5 =  '\'-\''  if len(PK5)==0 else SrcTab+'.'+PK5
    pk6 =  '\'-\''  if len(PK6)==0 else SrcTab+'.'+PK6
    pk7 =  '\'-\''  if len(PK7)==0 else SrcTab+'.'+PK7
    pk8 =  '\'-\''  if len(PK8)==0 else SrcTab+'.'+PK8
    print("Inside genPK")
    print(pk1,pk2,pk3,pk4,pk5,pk6,pk7,pk8, tabAlias)
    return pk1,pk2,pk3,pk4,pk5,pk6,pk7,pk8

    
def genPKnames(PK1,PK2,PK3,PK4,PK5,PK6,PK7,PK8,SrcTab):
    pknames=('\'-\'' if len(PK1)==0 else SrcTab+'.'+PK1)  + \
                ('' if len(PK2)==0 else  ', '+SrcTab+'.'+ PK2) + \
                ('' if len(PK3)==0 else  ', '+SrcTab+'.'+ PK3 ) + \
                ('' if len(PK4)==0 else  ', '+SrcTab+'.'+ PK4 ) + \
                ('' if len(PK5)==0 else  ', '+SrcTab+'.'+ PK5 ) + \
                ('' if len(PK6)==0 else  ', '+SrcTab+'.'+ PK6 ) + \
                ('' if len(PK7)==0 else  ', '+SrcTab+'.'+ PK7 ) + \
                ('' if len(PK8)==0 else  ', '+SrcTab+'.'+ PK8 )
    return pknames
        
 

def NullChkCase(NullChk, errcol, FtrRule):
    # defining NULL case statament
    if NullChk=='N':
        return -1
    else:
        fil_cond = '1=1' if len(FtrRule)==0 else FtrRule
        CaseStmt = "case ({errcol} is null or {errcol} = '') and {fil_cond} When True Then 1 Else 0 end"\
                    .format(errcol=errcol, fil_cond=fil_cond)
        return CaseStmt
        #return 'case ('+errcol+' is null and '+errcol+" = '') and "+fil_cond+" When True Then 1 Else 0 end"


def LenChkCase(LenChk, errcol, LenFtrRule, MinLen, MaxLen):
    # defining Length case statament
    if LenChk=='N':
        return -1
    else:
        fil_cond = '1=1' if len(LenFtrRule)==0 else LenFtrRule
        CaseStmt = "case (length({errcol}) < {MinLen} or length({errcol}) > {MaxLen}) and {fil_cond} When True Then 1 Else 0 end"\
                    .format(errcol=errcol, fil_cond=fil_cond, MinLen=MinLen, MaxLen=MaxLen)
        return CaseStmt  
        #return "case (length("+errcol+") < "+MinLen+" or length("+errcol+") > "+MaxLen+") and "+fil_cond+" When True Then 1 Else 0 end"
    

def LovChkCase(LovChk, errcol, LovFtrRule):
    # defining Length case statament
    if LovChk=='N' or len(LovFtrRule)==0:
        return -1
    else:
        CaseStmt = "case ({errcol} not in {LovFtrRule}) When True Then 1 Else 0 end"\
                    .format(errcol=errcol, LovFtrRule=LovFtrRule)
        return CaseStmt  
        #return "case "+errcol+" not in "+LovFtrRule+" When True Then 1 Else 0 end"


def DataChkCase(DataChk, errcol, DataFtrRule, table, SrcCol):
    # defining Length case statament
    if DataChk=='N':
        return -1
    else:    
        CaseStmt = "case (Not ({table}.{SrcCol} is null or {table}.{SrcCol} = '') and ({SrcCol} like {DataFtrRule})) When True Then 1 Else 0 end"\
                    .format(errcol=errcol, table=table, SrcCol=SrcCol,  DataFtrRule=DataFtrRule)
        return CaseStmt  

'''
def DupChkCase(DupChk, DupFtrRule, ChkId, PK1, PK2, PK3, PK4, PK5, PK6, PK7, PK8,  SrcTab, SrcCol, pknames, errcol):
    if DupChk=='N':
        return -1
    else:
        Dup_fil_cond = '1=1' if len(DupFtrRule)==0 else DupFtrRule
        PartitionByKey=('\'-\'' if len(PK1)==0 else PK1) + \
                ('' if len(PK2)==0 else   ',' + PK2)  + \
                ('' if len(PK3)==0 else   ',' + PK3 ) + \
                ('' if len(PK4)==0 else   ',' + PK4 ) + \
                ('' if len(PK5)==0 else   ',' + PK5 ) + \
                ('' if len(PK6)==0 else   ',' + PK6 ) + \
                ('' if len(PK7)==0 else   ',' + PK7 ) + \
                ('' if len(PK8)==0 else   ',' + PK8 )
        
        pknames = genPKnames(PK1,PK2,PK3,PK4,PK5,PK6,PK7,PK8,SrcTab)
        pk1, pk2, pk3, pk4, pk5, pk6, pk7, pk8 = genPK(PK1,PK2,PK3,PK4,PK5,PK6,PK7,PK8,SrcTab)
        errcol = SrcTab+'.'+SrcCol
        Dup_detail_query = "select '{chk_id}', '{pknames}' pknames, {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5,{pk6} pk6, {pk7} pk7, {pk8} pk8,count(*) errcol from {SrcTab} where {Dup_fil_cond} GROUP BY {PartitionByKey} HAVING COUNT(1)>1"\
                    .format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, pk6=pk6, pk7=pk7, pk8=pk8, errcol=errcol, SrcTab=SrcTab,Dup_fil_cond=Dup_fil_cond,PartitionByKey=PartitionByKey );   
        return Dup_detail_query  
'''
def DupChkCase(DupChk, DupFtrRule, ChkId, PK1, PK2, PK3, PK4, PK5, PK6, PK7, PK8,  SrcTab, SrcCol, pknames, errcol):
    if DupChk=='N':
        return -1
    else:
        
        Dup_fil_cond = '1=1' if len(DupFtrRule)==0 else DupFtrRule
        PartitionByKey=('\'-\'' if len(PK1)==0 else PK1) + \
                ('' if len(PK2)==0 else   ',' + PK2)  + \
                ('' if len(PK3)==0 else   ',' + PK3 ) + \
                ('' if len(PK4)==0 else   ',' + PK4 ) + \
                ('' if len(PK5)==0 else   ',' + PK5 ) + \
                ('' if len(PK6)==0 else   ',' + PK6 ) + \
                ('' if len(PK7)==0 else   ',' + PK7 ) + \
                ('' if len(PK8)==0 else   ',' + PK8 )
        
        pknames = genPKnames(PK1,PK2,PK3,PK4,PK5,PK6,PK7,PK8,SrcTab)
        pk1, pk2, pk3, pk4, pk5, pk6, pk7, pk8 = genPK(PK1,PK2,PK3,PK4,PK5,PK6,PK7,PK8,SrcTab)
	print("Inside DupCHK")
        print(pk1, pk2, pk3, pk4, pk5)
        errcol = SrcTab+'.'+SrcCol
        Dup_detail_query = "select {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5,{pk6} pk6, {pk7} pk7, {pk8} pk8,count(*) CNT from {SrcTab} where {Dup_fil_cond} GROUP BY {PartitionByKey} HAVING COUNT(1)>1"\
                    .format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, pk6=pk6, pk7=pk7, pk8=pk8, errcol=errcol, SrcTab=SrcTab,Dup_fil_cond=Dup_fil_cond,PartitionByKey=PartitionByKey );   
        return Dup_detail_query  

def JoinQuery(detail_query1, detail_query2):
    return detail_query1+"\n"+detail_query2+"\n";




def main(config, outfile):
    # Defining Main
    conf = open(config, 'r');
    detail_sqls=[]
    
    # Reading the config file
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
        FtrRule = cols[15]
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
    
        
    
        if DupChk=='N':
            pknames = genPKnames(PK1,PK2,PK3,PK4,PK5,PK6,PK7,PK8,SrcTab)
            pk1, pk2, pk3, pk4, pk5, pk6, pk7, pk8 = genPK(PK1,PK2,PK3,PK4,PK5,PK6,PK7,PK8,SrcTab)
            errcol = SrcTab+'.'+SrcCol

        
            detail_query = "select '{chk_id}', '{pknames}' pknames, {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5, {pk6} pk6, {pk7} pk7, {pk8} pk8, {errcol} errcol, \
        {NullChkStmt} NullChkResult, {LenChkStmt} LenChkResult, {LovChkStmt} LovChkResult, {DataChkStmt} DataChkResult, -1  DupChkResult from {SrcTab} \
        where ({errcol} is not null and {errcol} != '')"   \
                    .format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, pk6=pk6, pk7=pk7, pk8=pk8, errcol=errcol, SrcTab=SrcTab,   \
                    	NullChkStmt=NullChkCase(NullChk, errcol, FtrRule), LenChkStmt=LenChkCase(LenChk, errcol, LenFtrRule, MinLen, MaxLen), LovChkStmt=LovChkCase(LovChk, errcol, LovFtrRule), DataChkStmt=DataChkCase(DataChk, errcol, DataFtrRule, SrcTab, SrcCol) );
              
        else:
            pknames = genPKnames(PK1,PK2,PK3,PK4,PK5,PK6,PK7,PK8,SrcTab)
            pk1, pk2, pk3, pk4, pk5, pk6, pk7, pk8 = genPK(PK1,PK2,PK3,PK4,PK5,PK6,PK7,PK8,SrcTab,'A')
            errcol = 'A.'+SrcCol
            pk11, pk21, pk31, pk41, pk51, pk61, pk71, pk81 = genPK(PK1,PK2,PK3,PK4,PK5,PK6,PK7,PK8,SrcTab,'B')
            
            dup_table = DupChkCase(DupChk, DupFtrRule, ChkId, PK1, PK2, PK3, PK4, PK5, PK6, PK7, PK8,  SrcTab, SrcCol, pknames, errcol)
            detail_query = "select '{chk_id}', '{pknames}' pknames, {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5, {pk6} pk6, {pk7} pk7, {pk8} pk8, {errcol} errcol, \
        {NullChkStmt} NullChkResult, {LenChkStmt} LenChkResult, {LovChkStmt} LovChkResult, {DataChkStmt} DataChkResult, B.CNT DupChkResult  from {SrcTab} A left join ({dup_table}) B\
        on {pk1}={pk11} and {pk2}={pk21} and {pk3}={pk31} and {pk4}={pk41} and {pk5}={pk51} and {pk6}={pk61} and {pk7}={pk71} and {pk8}={pk81} \
        where ({errcol} is not null and {errcol} != '')"   \
                    .format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, pk6=pk6, pk7=pk7, pk8=pk8, errcol=errcol, SrcTab=SrcTab,   \
                            pk11=pk11, pk21=pk21, pk31=pk31, pk41=pk41, pk51=pk51, pk61=pk61, pk71=pk71, pk81=pk81, \
                            NullChkStmt=NullChkCase(NullChk, errcol, FtrRule), LenChkStmt=LenChkCase(LenChk, errcol, LenFtrRule, MinLen, MaxLen), \
                            LovChkStmt=LovChkCase(LovChk, errcol, LovFtrRule), DataChkStmt=DataChkCase(DataChk, errcol, DataFtrRule, SrcTab, SrcCol),dup_table=dup_table );
          
        detail_query1 = detail_query+"\n";
        detail_sqls.append(detail_query1)
        
        

#        tabAlias = 'B'
#        pk1 =  '\'-\'' if len(PK1)==0 else tabAlias+'.'+SrcTab+'.'+PK1
#        pk2 =  '\'-\'' if len(PK2)==0 else tabAlias+'.'+SrcTab+'.'+PK2
#        pk3 =  '\'-\''  if len(PK3)==0 else tabAlias+'.'+SrcTab+'.'+PK3
#        pk4 =  '\'-\''  if len(PK4)==0 else tabAlias+'.'+SrcTab+'.'+PK4
#        pk5 =  '\'-\''  if len(PK5)==0 else tabAlias+'.'+SrcTab+'.'+PK5
#        pk6 =  '\'-\''  if len(PK6)==0 else tabAlias+'.'+SrcTab+'.'+PK6
#        pk7 =  '\'-\''  if len(PK7)==0 else tabAlias+'.'+SrcTab+'.'+PK7
#        pk8 =  '\'-\''  if len(PK8)==0 else tabAlias+'.'+SrcTab+'.'+PK8
#        errcol = tabAlias+'.'+SrcTab+'.'+SrcCol
        
        
        #detail_query2 = DupChkCase(DupChk, DupFtrRule, pk1, pk2, pk3, pk4, pk5, pk6, pk7, pk8,  SrcTab, SrcCol, pknames, errcol)
        
        #detail_query1 = detail_query+"\n";
        #detail_sqls.append(JoinQuery(detail_query1, detail_query2))
        
        
#        # If Null CHK Exist, Generate the NULL Query
#        if (NullChk=='Y'):
#            ChkType='NULL CHK'
#            fil_cond = '1=1' if len(FtrRule)==0 else FtrRule
#            NullChkStmt= NullChkCase(errcol)
#            null_detail_query = "select '{chk_id}', '{pknames}' pknames, {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5,{pk6} pk6, {pk7} pk7, {pk8} pk8, {errcol} errcol,  {NullChkStmt} NullChkResult from {table} where {fil_cond}"\
#                    .format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, pk6=pk6, pk7=pk7, pk8=pk8, errcol=errcol, table=SrcTab, fil_cond=fil_cond, NullChkStmt=NullChkStmt);
#            null_detail_query1 = null_detail_query+"\n";
#            detail_sqls.append(null_detail_query1)
#    
#    
#        # If LOV CHK Exist, Generate the LOV Query
#        if (LovChk=='Y'):
#            ChkType='LOV CHK'
#            Lov_detail_query = "select '{chk_id}', '{pknames}' pknames, {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5,{pk6} pk6, {pk7} pk7, {pk8} pk8, {errcol} errcol from {table} where ({errcol} is not null or {errcol} != '') and {errcol} not in ({LovFtrRule})"\
#                    .format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, pk6=pk6, pk7=pk7, pk8=pk8, errcol=errcol, table=SrcTab, LovFtrRule=LovFtrRule );
#            Lov_detail_query1 = Lov_detail_query+"\n";
#            detail_sqls.append(Lov_detail_query1)
#    
#    
#        # If REF CHK Exist, Generate the REF Query
#        if (RefChk=='Y'):
#            ChkType='REF CHK'
#            ref_Case =  'case when (('+LkpTblNm+"."+LkpTblKeyCustSQL+' IS NULL OR '+LkpTblNm+"."+LkpTblKeyCustSQL+"='' ) and (1=1)) then 1 else 0 end " if LkpCustSQL=='Y' else 'case when (( '+CustSQLTblNm+"."+CustSQLTblNmCustSqlKey+' IS NULL OR + '+CustSQLTblNm+"."+CustSQLTblNmCustSqlKey+"='' ) and (1=1)) then 1 else 0 end "
#            leftTable = 'LEFT OUTER JOIN '+ LkpTblSchema+"."+LkpTblNm+' on ( '+ SrcTab+"."+SrcCol+'='+LkpTblNm+"."+LkpTblKeyCustSQL+')' if LkpCustSQL=='Y' else 'LEFT OUTER JOIN '+ Cust_Sql + 'on ( '+ SrcTab+"."+SrcCol+'='+CustSQLTblNm+"."+CustSQLTblNmCustSqlKey+")"
#    
#            Ref_detail_query = "select '{pknames}' pknames,{pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5,{pk6} pk6, {pk7} pk7, {pk8} pk8, {errcol} errcol, {ref_Case} ref_Case from {SrcTab} {leftTable}"\
#                    .format( pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, pk6=pk6, pk7=pk7, pk8=pk8, errcol=errcol, SrcTab=SrcTab, LkpTblNm=LkpTblNm,LkpTblKeyCustSQL=LkpTblKeyCustSQL, leftTable=leftTable, ref_Case=ref_Case);
#            Ref_detail_query1 = Ref_detail_query+"\n";
#            detail_sqls.append(Ref_detail_query1)
#    
#    
#        # If DUP CHK Exist, Generate the DUP Query
#        if (DupChk=='Y'):
#            ChkType='DUP CHK'
#            Dup_fil_cond = '1=1' if len(DupFtrRule)==0 else DupFtrRule
#            PartitionByKey=('\'-\'' if len(PK1)==0 else PK1) + \
#                    ('' if len(PK2)==0 else   ',' + PK2) + \
#                ('' if len(PK3)==0 else   ',' + PK3 ) + \
#                    ('' if len(PK4)==0 else   ',' + PK4 ) + \
#                    ('' if len(PK5)==0 else   ',' + PK5 ) + \
#                    ('' if len(PK6)==0 else   ',' + PK6 ) + \
#                    ('' if len(PK7)==0 else   ',' + PK7 ) + \
#                    ('' if len(PK8)==0 else   ',' + PK8 )
#    
#    
#            Dup_detail_query = "select '{chk_id}', '{pknames}' pknames, {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5,{pk6} pk6, {pk7} pk7, {pk8} pk8,count(*) errcol from {table} where {Dup_fil_cond} GROUP BY {PartitionByKey} HAVING COUNT(1)>1"\
#                    .format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, pk6=pk6, pk7=pk7, pk8=pk8, errcol=errcol, table=SrcTab,Dup_fil_cond=Dup_fil_cond,PartitionByKey=PartitionByKey );
#            Dup_detail_query1 = Dup_detail_query+"\n";
#            detail_sqls.append(Dup_detail_query1)
#    
#    
#    
#        # generating DATA TYPE CHK Detailed Query
#        if (DataChk=='Y'):
#            ChkType='Data CHK'
#            DataType_detail_query = "select '{chk_id}', '{pknames}' pknames, {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5,{pk6} pk6, {pk7} pk7, {pk8} pk8,{errcol} errcol from {table} where Not ({table}.{SrcCol} is null or {table}.{SrcCol} = '') and ({SrcCol} like {DataFtrRule})"\
#                    .format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, pk6=pk6, pk7=pk7, pk8=pk8, errcol=errcol, table=SrcTab,SrcCol=SrcCol,DataFtrRule=DataFtrRule );
#            DataType_detail_query1 = DataType_detail_query+"\n";
#            detail_sqls.append(DataType_detail_query1)
    
    
    
    # Writing data into Files
    detail = open(outfile, 'w')
    detail.writelines(detail_sqls);
    detail.close()
    
    
    conf.close()
    



# Setting File
config = "AllChkConfig.csv"
outfile = 'Queries_out.sql'

# Calling Main
if __name__== "__main__":
    main(config, outfile)
