# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 07:31:11 2017
@author: Atul

Result:
1 = True
0 = False
-1 = Did not execute

Alias details:
A - Main Table
B - Duplicate Table
C - Alias Table
"""


def genPK(PK1,PK2,PK3,PK4,PK5,SrcTab,tabAlias=''):
    
    if len(tabAlias)>0:
        SrcTab=tabAlias
      
    pk1 =  '\'-\'' if len(PK1)==0 else SrcTab+'.'+PK1
    pk2 =  '\'-\'' if len(PK2)==0 else SrcTab+'.'+PK2
    pk3 =  '\'-\''  if len(PK3)==0 else SrcTab+'.'+PK3
    pk4 =  '\'-\''  if len(PK4)==0 else SrcTab+'.'+PK4
    pk5 =  '\'-\''  if len(PK5)==0 else SrcTab+'.'+PK5
    return pk1,pk2,pk3,pk4,pk5

    
def genPKnames(PK1,PK2,PK3,PK4,PK5,SrcTab):
    pknames=('\'-\'' if len(PK1)==0 else SrcTab+'.'+PK1)  + \
                ('' if len(PK2)==0 else  ', '+SrcTab+'.'+ PK2) + \
                ('' if len(PK3)==0 else  ', '+SrcTab+'.'+ PK3 ) + \
                ('' if len(PK4)==0 else  ', '+SrcTab+'.'+ PK4 ) + \
                ('' if len(PK5)==0 else  ', '+SrcTab+'.'+ PK5 )
    return pknames
        
 
def NullChkCase(NullChk, errcol, NullFtrRule):
    # defining NULL CASE statament
    if NullChk=='N':
        return -1
    else:
        fil_cond = '1=1' if len(NullFtrRule)==0 else NullFtrRule
        CaseStmt = "CASE WHEN (({errcol} is null or {errcol} = '') and {fil_cond}) THEN 1 ELSE 0 END"\
                    .format(errcol=errcol, fil_cond=fil_cond)
        return CaseStmt
        

def LenChkCase(LenChk, errcol, LenFtrRule, MinLen, MaxLen):
    # defining Length CASE statament
    if LenChk=='N':
        return -1
    else:
        fil_cond = '1=1' if len(LenFtrRule)==0 else LenFtrRule
        CaseStmt = "CASE WHEN ((length({errcol}) < {MinLen} or length({errcol}) > {MaxLen}) and {fil_cond}) THEN 1 ELSE 0 END"\
                    .format(errcol=errcol, fil_cond=fil_cond, MinLen=MinLen, MaxLen=MaxLen)
        return CaseStmt  
        
    
def LovChkCase(LovChk, errcol, LovFtrRule):
    # defining Love CASE statament
    if LovChk=='N' or len(LovFtrRule)==0:
        return -1
    else:
        CaseStmt = "CASE WHEN ({errcol} not in {LovFtrRule}) THEN 1 ELSE 0 END"\
                    .format(errcol=errcol, LovFtrRule=LovFtrRule)
        return CaseStmt  
        

def DataChkCase(DataChk, errcol, DataFtrRule, table, SrcCol):
    # defining DataType CASE statament
    if DataChk=='N':
        return -1
    else:    
        CaseStmt = "CASE WHEN ({errcol} like {DataFtrRule}) THEN 1 ELSE 0 END"\
                    .format(errcol=errcol, table=table, SrcCol=SrcCol,  DataFtrRule=DataFtrRule)
        return CaseStmt  


def DupChkCase(DupChk, DupFtrRule, ChkId, PK1, PK2, PK3, PK4, PK5, SrcTab, SrcCol, errcol):
    # defining Duplicate CASE statament
    if DupChk=='N':
        return -1
    else:
        Dup_fil_cond = '1=1' if len(DupFtrRule)==0 else DupFtrRule
        PartitionByKey=('\'-\'' if len(PK1)==0 else PK1) + \
                ('' if len(PK2)==0 else   ',' + PK2)  + \
                ('' if len(PK3)==0 else   ',' + PK3 ) + \
                ('' if len(PK4)==0 else   ',' + PK4 ) + \
                ('' if len(PK5)==0 else   ',' + PK5 ) 
        
        pk1, pk2, pk3, pk4, pk5 = genPK(PK1,PK2,PK3,PK4,PK5,SrcTab)
        
        Dup_detail_query = "select {pk1}, {pk2}, {pk3}, {pk4}, {pk5},  1 CNT from {SrcTab} where {Dup_fil_cond} GROUP BY {PartitionByKey} HAVING COUNT(1)>1"\
                    .format(pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, SrcTab=SrcTab,Dup_fil_cond=Dup_fil_cond,PartitionByKey=PartitionByKey );   
        return Dup_detail_query


def RefChkCase(RefChk,RefFtrRule, errcol, LkpTblNm, LkpTblKeyCustSQL, LkpCustSQL, LkpTblSchema, CustSQLTblNm, CustSQLTblNmCustSqlKey, Cust_Sql, tabAlias):
    # defining Reference CASE statament
    if RefChk=='N':
        return -1
    else:
        RefFtrRule = '1=1' if len(RefFtrRule)==0 else RefFtrRule
        ref_Case =  'CASE WHEN (('+tabAlias+"."+LkpTblKeyCustSQL+' IS NOT NULL and length('+tabAlias+"."+LkpTblKeyCustSQL+")>0 ) and ("+RefFtrRule+")) THEN 1 ELSE 0 END" if LkpCustSQL=='L' else 'CASE WHEN (( '+tabAlias+"."+CustSQLTblNmCustSqlKey+' IS NULL OR '+tabAlias+"."+CustSQLTblNmCustSqlKey+"='' ) and (1=1)) THEN 1 ELSE 0 END"
        ref_table = LkpTblSchema+"."+LkpTblNm+' '+tabAlias+' on '+ errcol+'='+tabAlias+"."+LkpTblKeyCustSQL if LkpCustSQL=='L' else ' ('+ Cust_Sql +') '+tabAlias+ ' on ( '+ errcol +'='+tabAlias+"."+CustSQLTblNmCustSqlKey+")"
        return ref_table,ref_Case



'''
###############################################################
        Defining Main 
###############################################################
'''

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
        NullChk = cols[11]                          
        NullFtrRule = cols[12]                          
        NullChkThrePer = cols[13]                   
        LenChk = cols[14]                           
        LenFtrRule = cols[15]                       
        MinLen = cols[16]                           
        MaxLen = cols[17]                           
        LenChkThrePer = cols[18]                    
        LovChk = cols[19]                           
        LovFtrRule = cols[20]                       
        LovChkThrePer = cols[21]                    
        RefChk = cols[22]                           
        RefFtrRule = cols[23]                       
        LkpCustSQL= cols[24]                        
        LkpTblSchema = cols[25]                     
        LkpTblNm = cols[26]                         
        LkpTblKeyCustSQL = cols[27]                 
        Cust_Sql= cols[28]                          
        CustSQLTblNm = cols[29]                     
        CustSQLTblNmCustSqlKey = cols[30]           
        RefChkThrePer = cols[31]                    
        DupChk = cols[32]                            
        DupFtrRule = cols[33]
        DupChkThrePer = cols[34]
        DataChk = cols[35]
        DataFtrRule = cols[36]
        DataChkThrePer = cols[37]
        ChkCreatedDate = cols[38]
    
        
        # Generating SQL WHEN Duplicate and Referecne Checks are ENABLE
        if DupChk=='Y' and RefChk=='Y':
            pknames = genPKnames(PK1,PK2,PK3,PK4,PK5,SrcTab)
            pk1, pk2, pk3, pk4, pk5 = genPK(PK1,PK2,PK3,PK4,PK5,SrcTab,'A')
            errcol = 'A.'+SrcCol
            pk11, pk21, pk31, pk41, pk51 = genPK(PK1,PK2,PK3,PK4,PK5,SrcTab,'B')
                    
            dup_table = DupChkCase(DupChk, DupFtrRule, ChkId, PK1, PK2, PK3, PK4, PK5 , SrcTab, SrcCol, errcol)
            ref_table,ref_Case = RefChkCase(RefChk,RefFtrRule, errcol, LkpTblNm, LkpTblKeyCustSQL, LkpCustSQL, LkpTblSchema, CustSQLTblNm, CustSQLTblNmCustSqlKey, Cust_Sql, 'C')
            
            detail_query = "select '{chk_id}', '{pknames}' pknames, {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5,'{errcol}' errcol, {errcol} errcolvalue,\
{NullChkStmt} NullChkResult, {LenChkStmt} LenChkResult, {LovChkStmt} LovChkResult, {DataChkStmt} DataChkResult, CASE WHEN B.CNT=1 THEN 1 ELSE 0 END DupChkResult, \
{ref_Case} RefChkResult  from {SrcTab} A LEFT OUTER JOIN ({dup_table}) B \
on {pk1}={pk11} and {pk2}={pk21} and {pk3}={pk31} and {pk4}={pk41} and {pk5}={pk51} \
LEFT OUTER JOIN {ref_table}" \
          .format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5,  errcol=errcol, SrcTab=SrcTab,   \
                            pk11=pk11, pk21=pk21, pk31=pk31, pk41=pk41, pk51=pk51, \
                            NullChkStmt=NullChkCase(NullChk, errcol, NullFtrRule), LenChkStmt=LenChkCase(LenChk, errcol, LenFtrRule, MinLen, MaxLen), \
                            LovChkStmt=LovChkCase(LovChk, errcol, LovFtrRule), DataChkStmt=DataChkCase(DataChk, errcol, DataFtrRule, SrcTab, SrcCol),ref_table=ref_table,ref_Case=ref_Case, dup_table=dup_table );

        # Generating SQL WHEN Duplicate is ENABLE but Referecne Check      
        elif DupChk=='Y' and RefChk=='N':
            pknames = genPKnames(PK1,PK2,PK3,PK4,PK5,SrcTab)
            pk1, pk2, pk3, pk4, pk5 = genPK(PK1,PK2,PK3,PK4,PK5,SrcTab,'A')
            errcol = 'A.'+SrcCol
            pk11, pk21, pk31, pk41, pk51 = genPK(PK1,PK2,PK3,PK4,PK5,SrcTab,'B')
            
            dup_table = DupChkCase(DupChk, DupFtrRule, ChkId, PK1, PK2, PK3, PK4, PK5,  SrcTab, SrcCol, errcol)
            detail_query = "select '{chk_id}', '{pknames}' pknames, {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5,'{errcol}' errcol, {errcol} errcolvalue,\
{NullChkStmt} NullChkResult, {LenChkStmt} LenChkResult, {LovChkStmt} LovChkResult, {DataChkStmt} DataChkResult, CASE WHEN B.CNT=1 THEN 1 ELSE 0 END DupChkResult, -1 RefChkResult \
from {SrcTab} A LEFT OUTER JOIN ({dup_table}) B on {pk1}={pk11} and {pk2}={pk21} and {pk3}={pk31} and {pk4}={pk41} and {pk5}={pk51}" \
                    .format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5,  errcol=errcol, SrcTab=SrcTab,   \
                            pk11=pk11, pk21=pk21, pk31=pk31, pk41=pk41, pk51=pk51, \
                            NullChkStmt=NullChkCase(NullChk, errcol, NullFtrRule), LenChkStmt=LenChkCase(LenChk, errcol, LenFtrRule, MinLen, MaxLen), \
                            LovChkStmt=LovChkCase(LovChk, errcol, LovFtrRule), DataChkStmt=DataChkCase(DataChk, errcol, DataFtrRule, SrcTab, SrcCol),dup_table=dup_table );
                            
        # Generating SQL WHEN Referecne is ENABLE but Duplicate Check
        elif DupChk=='N' and RefChk=='Y':
            pknames = genPKnames(PK1,PK2,PK3,PK4,PK5,SrcTab)
            pk1, pk2, pk3, pk4, pk5 = genPK(PK1,PK2,PK3,PK4,PK5,SrcTab,'A')
            errcol = 'A.'+SrcCol
                        
            ref_table,ref_Case = RefChkCase(RefChk,RefFtrRule, errcol, LkpTblNm, LkpTblKeyCustSQL, LkpCustSQL, LkpTblSchema, CustSQLTblNm, CustSQLTblNmCustSqlKey, Cust_Sql, 'C')
            detail_query = "select '{chk_id}', '{pknames}' pknames, {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5,'{errcol}' errcol, {errcol} errcolvalue,\
{NullChkStmt} NullChkResult, {LenChkStmt} LenChkResult, {LovChkStmt} LovChkResult, {DataChkStmt} DataChkResult, -1 DupChkResult, {ref_Case} RefChkResult \
from {SrcTab} A LEFT OUTER JOIN {ref_table} " \
                    .format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, errcol=errcol, SrcTab=SrcTab,   \
                            NullChkStmt=NullChkCase(NullChk, errcol, NullFtrRule), LenChkStmt=LenChkCase(LenChk, errcol, LenFtrRule, MinLen, MaxLen), \
                            LovChkStmt=LovChkCase(LovChk, errcol, LovFtrRule), DataChkStmt=DataChkCase(DataChk, errcol, DataFtrRule, SrcTab, SrcCol), ref_table=ref_table,ref_Case=ref_Case );

        # Generating SQL WHEN Referecne and Duplicate Checks are not ENABLE    
        else:
            pknames = genPKnames(PK1,PK2,PK3,PK4,PK5,SrcTab)
            pk1, pk2, pk3, pk4, pk5 = genPK(PK1,PK2,PK3,PK4,PK5,SrcTab)
            errcol = SrcTab+'.'+SrcCol
        
        
            detail_query = "select '{chk_id}', '{pknames}' pknames, {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5,'{errcol}' errcol, {errcol} errcolvalue,\
{NullChkStmt} NullChkResult, {LenChkStmt} LenChkResult, {LovChkStmt} LovChkResult, {DataChkStmt} DataChkResult, -1 DupChkResult, -1 RefChkResult from {SrcTab}"\
                    .format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, errcol=errcol, SrcTab=SrcTab,   \
                        NullChkStmt=NullChkCase(NullChk, errcol, NullFtrRule), LenChkStmt=LenChkCase(LenChk, errcol, LenFtrRule, MinLen, MaxLen), LovChkStmt=LovChkCase(LovChk, errcol, LovFtrRule), DataChkStmt=DataChkCase(DataChk, errcol, DataFtrRule, SrcTab, SrcCol) );
        

        
        detail_query1 = detail_query.replace("and '-'='-'", '').replace("  ", ' ').replace("'-',",'')+";\n";
        detail_sqls.append(detail_query1)
        
          
    # Writing data into Files
    detail = open(outfile, 'w')
    detail.writelines(detail_sqls);
    detail.close()
    conf.close()
    


'''
###############################################################
        Calling Main 
###############################################################
'''


# Setting File
config = "AllChkConfig_me.csv"
outfile = 'Queries_out.sql'

# Calling Main
if __name__== "__main__":
    main(config, outfile)


