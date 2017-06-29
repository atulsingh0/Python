# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 07:31:11 2017
@author: Atul
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
        
 
def NullChkCase(NullChk, errcol, FtrRule):
    # defining NULL CASE statament
    if NullChk=='N':
        return -1
    else:
        fil_cond = '1=1' if len(FtrRule)==0 else FtrRule
        CaseStmt = "CASE WHEN (({errcol} is null or {errcol} = '') and {fil_cond}) THEN 1 ELSE 0 END"\
                    .format(errcol=errcol, fil_cond=fil_cond)
        return CaseStmt
        #return 'CASE ('+errcol+' is null and '+errcol+" = '') and "+fil_cond+" When True Then 1 Else 0 END"


def LenChkCase(LenChk, errcol, LenFtrRule, MinLen, MaxLen):
    # defining Length CASE statament
    if LenChk=='N':
        return -1
    else:
        fil_cond = '1=1' if len(LenFtrRule)==0 else LenFtrRule
        CaseStmt = "CASE WHEN ((length({errcol}) < {MinLen} or length({errcol}) > {MaxLen}) and {fil_cond}) THEN 1 ELSE 0 END"\
                    .format(errcol=errcol, fil_cond=fil_cond, MinLen=MinLen, MaxLen=MaxLen)
        return CaseStmt  
        #return "CASE (length("+errcol+") < "+MinLen+" or length("+errcol+") > "+MaxLen+") and "+fil_cond+" When True Then 1 Else 0 END"
    

def LovChkCase(LovChk, errcol, LovFtrRule):
    # defining Love CASE statament
    if LovChk=='N' or len(LovFtrRule)==0:
        return -1
    else:
        CaseStmt = "CASE WHEN ({errcol} not in {LovFtrRule}) THEN 1 ELSE 0 END"\
                    .format(errcol=errcol, LovFtrRule=LovFtrRule)
        return CaseStmt  
        #return "CASE "+errcol+" not in "+LovFtrRule+" When True Then 1 Else 0 END"


def DataChkCase(DataChk, errcol, DataFtrRule, table, SrcCol):
    # defining DataType CASE statament
    if DataChk=='N':
        return -1
    else:    
        CaseStmt = "CASE WHEN (Not ({table}.{SrcCol} is null or {table}.{SrcCol} = '') and ({table}.{SrcCol} like {DataFtrRule})) THEN 1 ELSE 0 END"\
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


def RefChkCase(RefChk,RefFtrRule, ChkId, PK1, PK2, PK3, PK4, PK5,  SrcTab, SrcCol, errcol, LkpTblNm, LkpTblKeyCustSQL, LkpCustSQL, LkpTblSchema, CustSQLTblNm, CustSQLTblNmCustSqlKey, Cust_Sql):
    # defining Reference CASE statament
	if RefChk=='N':
		return -1
	else:
		#print("if LkpCustSQL=Y ",LkpCustSQL)
		#print(LkpTblNm, LkpTblKeyCustSQL)
		#print("if LkpCustSQL=N ",LkpCustSQL)
		#print(CustSQLTblNm,CustSQLTblNmCustSqlKey)
		#print("if LkpCustSQL=Y ",LkpCustSQL)
		#print(LkpTblSchema,LkpTblNm, SrcTab, SrcCol, LkpTblNm, LkpTblKeyCustSQL)
		#print("if LkpCustSQL=Y ",LkpCustSQL)
		#print(Cust_Sql,SrcTab,SrcCol,CustSQLTblNm,CustSQLTblNmCustSqlKey)
		pk1, pk2, pk3, pk4, pk5 = genPK(PK1,PK2,PK3,PK4,PK5,SrcTab)
		ref_Case =  'CASE WHEN (('+LkpTblNm+"."+LkpTblKeyCustSQL+' IS NULL OR '+LkpTblNm+"."+LkpTblKeyCustSQL+"='' ) and (1=1)) THEN 1 ELSE 0 END" if LkpCustSQL=='Y' else 'CASE WHEN (( '+CustSQLTblNm+"."+CustSQLTblNmCustSqlKey+' IS NULL OR '+CustSQLTblNm+"."+CustSQLTblNmCustSqlKey+"='' ) and (1=1)) THEN 1 ELSE 0 END"
		leftTable = 'LEFT OUTER JOIN '+ LkpTblSchema+"."+LkpTblNm+' on ( '+ SrcTab+"."+SrcCol+'='+LkpTblNm+"."+LkpTblKeyCustSQL+')' if LkpCustSQL=='Y' else 'LEFT OUTER JOIN '+ Cust_Sql + ' on ( '+ SrcTab+"."+SrcCol+'='+CustSQLTblNm+"."+CustSQLTblNmCustSqlKey+")"
		#print(ref_Case)
		#print(leftTable)
		ref_Case = str.rstrip(ref_Case)
		leftTable=str.rstrip(leftTable)
		Ref_detail_query = "select {pk1}, {pk2}, {pk3}, {pk4}, {pk5}, {ref_Case} ref_Case from {SrcTab} {leftTable}"\
                    .format( pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, SrcTab=SrcTab, LkpTblNm=LkpTblNm,LkpTblKeyCustSQL=LkpTblKeyCustSQL, leftTable=leftTable, ref_Case=ref_Case);
		
		
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
		NullChk = cols[11]                          
		FtrRule = cols[12]                          
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
			pk12, pk22, pk32, pk42, pk52 = genPK(PK1,PK2,PK3,PK4,PK5,SrcTab,'C')
			
			dup_table = DupChkCase(DupChk, DupFtrRule, ChkId, PK1, PK2, PK3, PK4, PK5 , SrcTab, SrcCol, errcol)
			ref_table = RefChkCase(RefChk,RefFtrRule, ChkId, PK1, PK2, PK3, PK4, PK5,   SrcTab, SrcCol, errcol, LkpTblNm, LkpTblKeyCustSQL, LkpCustSQL, LkpTblSchema, CustSQLTblNm, CustSQLTblNmCustSqlKey, Cust_Sql)
			
			detail_query = "select '{chk_id}', '{pknames}' pknames, {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5, {errcol} errcol, \
{NullChkStmt} NullChkResult, {LenChkStmt} LenChkResult, {LovChkStmt} LovChkResult, {DataChkStmt} DataChkResult, CASE WHEN B.CNT THEN 1 ELSE 0 END DupChkResult, \
CASE WHEN C.ref_Case THEN 1 ELSE 0 END RefChkResult  from {SrcTab} A LEFT OUTER JOIN ({dup_table}) B LEFT OUTER JOIN ({ref_table}) C \
on {pk1}={pk11} and {pk2}={pk21} and {pk3}={pk31} and {pk4}={pk41} and {pk5}={pk51} and \
{pk1}={pk12} and {pk2}={pk22} and {pk3}={pk32} and {pk4}={pk42} and {pk5}={pk52} \
where ({errcol} is not null and {errcol} != '')"\
                    .format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5,  errcol=errcol, SrcTab=SrcTab,   \
                            pk11=pk11, pk21=pk21, pk31=pk31, pk41=pk41, pk51=pk51, \
                            pk12=pk12, pk22=pk22, pk32=pk32, pk42=pk42, pk52=pk52,  \
                            NullChkStmt=NullChkCase(NullChk, errcol, FtrRule), LenChkStmt=LenChkCase(LenChk, errcol, LenFtrRule, MinLen, MaxLen), \
                            LovChkStmt=LovChkCase(LovChk, errcol, LovFtrRule), DataChkStmt=DataChkCase(DataChk, errcol, DataFtrRule, SrcTab, SrcCol),ref_table=ref_table, dup_table=dup_table );

        # Generating SQL WHEN Duplicate is ENABLE but Referecne Check      
		elif DupChk=='Y' and RefChk=='N':
			pknames = genPKnames(PK1,PK2,PK3,PK4,PK5,SrcTab)
			pk1, pk2, pk3, pk4, pk5 = genPK(PK1,PK2,PK3,PK4,PK5,SrcTab,'A')
			errcol = 'A.'+SrcCol
			pk11, pk21, pk31, pk41, pk51 = genPK(PK1,PK2,PK3,PK4,PK5,SrcTab,'B')
			
			dup_table = DupChkCase(DupChk, DupFtrRule, ChkId, PK1, PK2, PK3, PK4, PK5,  SrcTab, SrcCol, errcol)
			detail_query = "select '{chk_id}', '{pknames}' pknames, {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5,{errcol} errcol, \
{NullChkStmt} NullChkResult, {LenChkStmt} LenChkResult, {LovChkStmt} LovChkResult, {DataChkStmt} DataChkResult, CASE WHEN B.CNT THEN 1 ELSE 0 END DupChkResult \
from {SrcTab} A LEFT OUTER JOIN ({dup_table}) B on {pk1}={pk11} and {pk2}={pk21} and {pk3}={pk31} and {pk4}={pk41} and {pk5}={pk51} \
where ({errcol} is not null and {errcol} != '')"\
					.format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5,  errcol=errcol, SrcTab=SrcTab,   \
							pk11=pk11, pk21=pk21, pk31=pk31, pk41=pk41, pk51=pk51, \
							NullChkStmt=NullChkCase(NullChk, errcol, FtrRule), LenChkStmt=LenChkCase(LenChk, errcol, LenFtrRule, MinLen, MaxLen), \
							LovChkStmt=LovChkCase(LovChk, errcol, LovFtrRule), DataChkStmt=DataChkCase(DataChk, errcol, DataFtrRule, SrcTab, SrcCol),dup_table=dup_table );
                            
        # Generating SQL WHEN Referecne is ENABLE but Duplicate Check
		elif DupChk=='N' and RefChk=='Y':
			pknames = genPKnames(PK1,PK2,PK3,PK4,PK5,SrcTab)
			pk1, pk2, pk3, pk4, pk5 = genPK(PK1,PK2,PK3,PK4,PK5,SrcTab,'A')
			errcol = 'A.'+SrcCol
			pk11, pk21, pk31, pk41, pk51 = genPK(PK1,PK2,PK3,PK4,PK5,SrcTab,'C')
			
			ref_table = RefChkCase(RefChk,RefFtrRule, ChkId, PK1, PK2, PK3, PK4, PK5,  SrcTab, SrcCol, errcol, LkpTblNm, LkpTblKeyCustSQL, LkpCustSQL, LkpTblSchema, CustSQLTblNm, CustSQLTblNmCustSqlKey, Cust_Sql)
			detail_query = "select '{chk_id}', '{pknames}' pknames, {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5,{errcol} errcol, \
{NullChkStmt} NullChkResult, {LenChkStmt} LenChkResult, {LovChkStmt} LovChkResult, {DataChkStmt} DataChkResult, CASE WHEN C.ref_Case THEN 1 ELSE 0 END RefChkResult \
from {SrcTab} A LEFT OUTER JOIN ({ref_table}) C on {pk1}={pk11} and {pk2}={pk21} and {pk3}={pk31} and {pk4}={pk41} and {pk5}={pk51} \
where ({errcol} is not null and {errcol} != '')"\
					.format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, errcol=errcol, SrcTab=SrcTab,   \
							pk11=pk11, pk21=pk21, pk31=pk31, pk41=pk41, pk51=pk51,  \
							NullChkStmt=NullChkCase(NullChk, errcol, FtrRule), LenChkStmt=LenChkCase(LenChk, errcol, LenFtrRule, MinLen, MaxLen), \
							LovChkStmt=LovChkCase(LovChk, errcol, LovFtrRule), DataChkStmt=DataChkCase(DataChk, errcol, DataFtrRule, SrcTab, SrcCol),ref_table=ref_table );

        # Generating SQL WHEN Referecne and Duplicate Checks are not ENABLE    
		else:
			pknames = genPKnames(PK1,PK2,PK3,PK4,PK5,SrcTab)
			pk1, pk2, pk3, pk4, pk5 = genPK(PK1,PK2,PK3,PK4,PK5,SrcTab)
			errcol = SrcTab+'.'+SrcCol
		
		
			detail_query = "select '{chk_id}', '{pknames}' pknames, {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5, {errcol} errcol, \
{NullChkStmt} NullChkResult, {LenChkStmt} LenChkResult, {LovChkStmt} LovChkResult, {DataChkStmt} DataChkResult, -1  DupChkResult, -1  RefChkResult from {SrcTab} \
where ({errcol} is not null and {errcol} != '')"\
					.format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, errcol=errcol, SrcTab=SrcTab,   \
						NullChkStmt=NullChkCase(NullChk, errcol, FtrRule), LenChkStmt=LenChkCase(LenChk, errcol, LenFtrRule, MinLen, MaxLen), LovChkStmt=LovChkCase(LovChk, errcol, LovFtrRule), DataChkStmt=DataChkCase(DataChk, errcol, DataFtrRule, SrcTab, SrcCol) );
		

		#detail_query1 = detail_query+";\n";
		detail_query1 = detail_query.replace("and '-'='-'", ' ')+";\n";
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
config = "AllChkConfig1.csv"
outfile = 'Queries_out.sql'

# Calling Main
if __name__== "__main__":
    main(config, outfile)


