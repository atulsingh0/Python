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
    # defining Love case statament
    if LovChk=='N' or len(LovFtrRule)==0:
        return -1
    else:
        CaseStmt = "case ({errcol} not in {LovFtrRule}) When True Then 1 Else 0 end"\
                    .format(errcol=errcol, LovFtrRule=LovFtrRule)
        return CaseStmt  
        #return "case "+errcol+" not in "+LovFtrRule+" When True Then 1 Else 0 end"


def DataChkCase(DataChk, errcol, DataFtrRule, table, SrcCol):
    # defining DataType case statament
    if DataChk=='N':
        return -1
    else:    
        CaseStmt = "case (Not ({table}.{SrcCol} is null or {table}.{SrcCol} = '') and ({table}.{SrcCol} like {DataFtrRule})) When True Then 1 Else 0 end"\
                    .format(errcol=errcol, table=table, SrcCol=SrcCol,  DataFtrRule=DataFtrRule)
        return CaseStmt  


def DupChkCase(DupChk, DupFtrRule, ChkId, PK1, PK2, PK3, PK4, PK5, PK6, PK7, PK8,  SrcTab, SrcCol, errcol):
    # defining Duplicate case statament
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
        
        pk1, pk2, pk3, pk4, pk5, pk6, pk7, pk8 = genPK(PK1,PK2,PK3,PK4,PK5,PK6,PK7,PK8,SrcTab)
        
        Dup_detail_query = "select {pk1}, {pk2}, {pk3}, {pk4}, {pk5},{pk6}, {pk7}, {pk8}, 1 CNT from {SrcTab} where {Dup_fil_cond} GROUP BY {PartitionByKey} HAVING COUNT(1)>1"\
                    .format(pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, pk6=pk6, pk7=pk7, pk8=pk8, SrcTab=SrcTab,Dup_fil_cond=Dup_fil_cond,PartitionByKey=PartitionByKey );   
        return Dup_detail_query


def RefChkCase(RefChk,DupFtrRule, ChkId, PK1, PK2, PK3, PK4, PK5, PK6, PK7, PK8,  SrcTab, SrcCol, errcol, LkpTblNm, LkpTblKeyCustSQL, LkpCustSQL, LkpTblSchema, CustSQLTblNm, CustSQLTblNmCustSqlKey, Cust_Sql):
    # defining Reference case statament
	if RefChk=='N':
		return -1
	else:
		
		pk1, pk2, pk3, pk4, pk5, pk6, pk7, pk8 = genPK(PK1,PK2,PK3,PK4,PK5,PK6,PK7,PK8,SrcTab)
		ref_Case =  'case when (('+LkpTblNm+"."+LkpTblKeyCustSQL+' IS NULL OR '+LkpTblNm+"."+LkpTblKeyCustSQL+"='' ) and (1=1)) then 1 else 0 end" if LkpCustSQL=='Y' else 'case when (( '+CustSQLTblNm+"."+CustSQLTblNmCustSqlKey+' IS NULL OR '+CustSQLTblNm+"."+CustSQLTblNmCustSqlKey+"='' ) and (1=1)) then 1 else 0 end"
		leftTable = 'LEFT OUTER JOIN '+ LkpTblSchema+"."+LkpTblNm+' on ( '+ SrcTab+"."+SrcCol+'='+LkpTblNm+"."+LkpTblKeyCustSQL+')' if LkpCustSQL=='Y' else 'LEFT OUTER JOIN '+ Cust_Sql + 'on ( '+ SrcTab+"."+SrcCol+'='+CustSQLTblNm+"."+CustSQLTblNmCustSqlKey+")"
		ref_Case = str.rstrip(ref_Case)
		leftTable=str.rstrip(leftTable)
		Ref_detail_query = "select {pk1}, {pk2}, {pk3}, {pk4}, {pk5},{pk6}, {pk7}, {pk8}, {ref_Case} ref_Case from {SrcTab} {leftTable}"\
                    .format( pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, pk6=pk6, pk7=pk7, pk8=pk8,  SrcTab=SrcTab, LkpTblNm=LkpTblNm,LkpTblKeyCustSQL=LkpTblKeyCustSQL, leftTable=leftTable, ref_Case=ref_Case);
		
		
		return Ref_detail_query



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
    
        
        # Generating SQL when Duplicate and Referecne Checks are ENABLE
        if DupChk=='Y' and RefChk=='Y':
            pknames = genPKnames(PK1,PK2,PK3,PK4,PK5,PK6,PK7,PK8,SrcTab)
            pk1, pk2, pk3, pk4, pk5, pk6, pk7, pk8 = genPK(PK1,PK2,PK3,PK4,PK5,PK6,PK7,PK8,SrcTab,'A')
            errcol = 'A.'+SrcCol
            pk11, pk21, pk31, pk41, pk51, pk61, pk71, pk81 = genPK(PK1,PK2,PK3,PK4,PK5,PK6,PK7,PK8,SrcTab,'B')
            pk12, pk22, pk32, pk42, pk52, pk62, pk72, pk82 = genPK(PK1,PK2,PK3,PK4,PK5,PK6,PK7,PK8,SrcTab,'C')
            
            dup_table = DupChkCase(DupChk, DupFtrRule, ChkId, PK1, PK2, PK3, PK4, PK5, PK6, PK7, PK8,  SrcTab, SrcCol, errcol)
            ref_table = RefChkCase(RefChk,DupFtrRule, ChkId, PK1, PK2, PK3, PK4, PK5, PK6, PK7, PK8,  SrcTab, SrcCol, errcol, LkpTblNm, LkpTblKeyCustSQL, LkpCustSQL, LkpTblSchema, CustSQLTblNm, CustSQLTblNmCustSqlKey, Cust_Sql)
            
            detail_query = "select '{chk_id}', '{pknames}' pknames, {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5,{pk6} pk6, {pk7} pk7, {pk8} pk8, {errcol} errcol, \
        {NullChkStmt} NullChkResult, {LenChkStmt} LenChkResult, {LovChkStmt} LovChkResult, {DataChkStmt} DataChkResult, case B.CNT=1 then 1 else 0 end DupChkResult, \
        case C.ref_Case=1 then 1 else 0 end RefChkResult  from {SrcTab} A LEFT OUTER JOIN ({dup_table}) B LEFT OUTER JOIN ({ref_table}) C \
        on {pk1}={pk11} and {pk2}={pk21} and {pk3}={pk31} and {pk4}={pk41} and {pk5}={pk51} and {pk6}={pk61} and {pk7}={pk71} and {pk8}={pk81} \
        {pk1}={pk12} and {pk2}={pk22} and {pk3}={pk32} and {pk4}={pk42} and {pk5}={pk52} and {pk6}={pk62} and {pk7}={pk72} and {pk8}={pk82} \
        where ({errcol} is not null and {errcol} != '')"   \
                    .format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, pk6=pk6, pk7=pk7, pk8=pk8, errcol=errcol, SrcTab=SrcTab,   \
                            pk11=pk11, pk21=pk21, pk31=pk31, pk41=pk41, pk51=pk51, pk61=pk61, pk71=pk71, pk81=pk81, \
                            pk12=pk12, pk22=pk22, pk32=pk32, pk42=pk42, pk52=pk52, pk62=pk62, pk72=pk72, pk82=pk82, \
                            NullChkStmt=NullChkCase(NullChk, errcol, FtrRule), LenChkStmt=LenChkCase(LenChk, errcol, LenFtrRule, MinLen, MaxLen), \
                            LovChkStmt=LovChkCase(LovChk, errcol, LovFtrRule), DataChkStmt=DataChkCase(DataChk, errcol, DataFtrRule, SrcTab, SrcCol),ref_table=ref_table, dup_table=dup_table );

        # Generating SQL when Duplicate is ENABLE but Referecne Check      
        elif DupChk=='Y' and RefChk=='N':
            pknames = genPKnames(PK1,PK2,PK3,PK4,PK5,PK6,PK7,PK8,SrcTab)
            pk1, pk2, pk3, pk4, pk5, pk6, pk7, pk8 = genPK(PK1,PK2,PK3,PK4,PK5,PK6,PK7,PK8,SrcTab,'A')
            errcol = 'A.'+SrcCol
            pk11, pk21, pk31, pk41, pk51, pk61, pk71, pk81 = genPK(PK1,PK2,PK3,PK4,PK5,PK6,PK7,PK8,SrcTab,'B')
            
            dup_table = DupChkCase(DupChk, DupFtrRule, ChkId, PK1, PK2, PK3, PK4, PK5, PK6, PK7, PK8,  SrcTab, SrcCol, errcol)
            detail_query = "select '{chk_id}', '{pknames}' pknames, {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5,{pk6} pk6, {pk7} pk7, {pk8} pk8, {errcol} errcol, \
        {NullChkStmt} NullChkResult, {LenChkStmt} LenChkResult, {LovChkStmt} LovChkResult, {DataChkStmt} DataChkResult, case B.CNT=1 then 1 else 0 end DupChkResult  from {SrcTab} A LEFT OUTER JOIN ({dup_table}) B\
        on {pk1}={pk11} and {pk2}={pk21} and {pk3}={pk31} and {pk4}={pk41} and {pk5}={pk51} and {pk6}={pk61} and {pk7}={pk71} and {pk8}={pk81} \
        where ({errcol} is not null and {errcol} != '')"   \
                    .format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, pk6=pk6, pk7=pk7, pk8=pk8, errcol=errcol, SrcTab=SrcTab,   \
                            pk11=pk11, pk21=pk21, pk31=pk31, pk41=pk41, pk51=pk51, pk61=pk61, pk71=pk71, pk81=pk81, \
                            NullChkStmt=NullChkCase(NullChk, errcol, FtrRule), LenChkStmt=LenChkCase(LenChk, errcol, LenFtrRule, MinLen, MaxLen), \
                            LovChkStmt=LovChkCase(LovChk, errcol, LovFtrRule), DataChkStmt=DataChkCase(DataChk, errcol, DataFtrRule, SrcTab, SrcCol),dup_table=dup_table );
                            
        # Generating SQL when Referecne is ENABLE but Duplicate Check
        elif DupChk=='N' and RefChk=='Y':
            pknames = genPKnames(PK1,PK2,PK3,PK4,PK5,PK6,PK7,PK8,SrcTab)
            pk1, pk2, pk3, pk4, pk5, pk6, pk7, pk8 = genPK(PK1,PK2,PK3,PK4,PK5,PK6,PK7,PK8,SrcTab,'A')
            errcol = 'A.'+SrcCol
            pk11, pk21, pk31, pk41, pk51, pk61, pk71, pk81 = genPK(PK1,PK2,PK3,PK4,PK5,PK6,PK7,PK8,SrcTab,'C')
            
            ref_table = RefChkCase(RefChk,DupFtrRule, ChkId, PK1, PK2, PK3, PK4, PK5, PK6, PK7, PK8,  SrcTab, SrcCol, errcol, LkpTblNm, LkpTblKeyCustSQL, LkpCustSQL, LkpTblSchema, CustSQLTblNm, CustSQLTblNmCustSqlKey, Cust_Sql)
            detail_query = "select '{chk_id}', '{pknames}' pknames, {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5,{pk6} pk6, {pk7} pk7, {pk8} pk8, {errcol} errcol, \
        {NullChkStmt} NullChkResult, {LenChkStmt} LenChkResult, {LovChkStmt} LovChkResult, {DataChkStmt} DataChkResult, case B.CNT=1 then 1 else 0 end RefChkResult  from {SrcTab} A LEFT OUTER JOIN ({ref_table}) C\
        on {pk1}={pk11} and {pk2}={pk21} and {pk3}={pk31} and {pk4}={pk41} and {pk5}={pk51} and {pk6}={pk61} and {pk7}={pk71} and {pk8}={pk81} \
        where ({errcol} is not null and {errcol} != '')"   \
                    .format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, pk6=pk6, pk7=pk7, pk8=pk8, errcol=errcol, SrcTab=SrcTab,   \
                            pk11=pk11, pk21=pk21, pk31=pk31, pk41=pk41, pk51=pk51, pk61=pk61, pk71=pk71, pk81=pk81, \
                            NullChkStmt=NullChkCase(NullChk, errcol, FtrRule), LenChkStmt=LenChkCase(LenChk, errcol, LenFtrRule, MinLen, MaxLen), \
                            LovChkStmt=LovChkCase(LovChk, errcol, LovFtrRule), DataChkStmt=DataChkCase(DataChk, errcol, DataFtrRule, SrcTab, SrcCol),ref_table=ref_table );

        # Generating SQL when Referecne and Duplicate Checks are not ENABLE    
        else:
            pknames = genPKnames(PK1,PK2,PK3,PK4,PK5,PK6,PK7,PK8,SrcTab)
            pk1, pk2, pk3, pk4, pk5, pk6, pk7, pk8 = genPK(PK1,PK2,PK3,PK4,PK5,PK6,PK7,PK8,SrcTab)
            errcol = SrcTab+'.'+SrcCol

        
            detail_query = "select '{chk_id}', '{pknames}' pknames, {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5, {pk6} pk6, {pk7} pk7, {pk8} pk8, {errcol} errcol, \
        {NullChkStmt} NullChkResult, {LenChkStmt} LenChkResult, {LovChkStmt} LovChkResult, {DataChkStmt} DataChkResult, -1  DupChkResult, -1  RefChkResult from {SrcTab} \
        where ({errcol} is not null and {errcol} != '')"   \
                    .format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, pk6=pk6, pk7=pk7, pk8=pk8, errcol=errcol, SrcTab=SrcTab,   \
                    	NullChkStmt=NullChkCase(NullChk, errcol, FtrRule), LenChkStmt=LenChkCase(LenChk, errcol, LenFtrRule, MinLen, MaxLen), LovChkStmt=LovChkCase(LovChk, errcol, LovFtrRule), DataChkStmt=DataChkCase(DataChk, errcol, DataFtrRule, SrcTab, SrcCol) );


        detail_query1 = detail_query+"\n";
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
#config = "AllChkConfig.csv"
config = "AllChkConfig_sfurty.csv"
outfile = 'Queries_out.sql'

# Calling Main
if __name__== "__main__":
    main(config, outfile)
