# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 07:31:11 2017

@author: Atul
"""

########################################################
#######         NullChkCase Function   #################
######################################################## 
def NullChkCase(NullChk, errcol, FtrRule):
    # defining NULL case statament
    if NullChk=='N':
        return -1
    else:
        fil_cond = '1=1' if len(FtrRule)==0 else FtrRule
        return 'case ('+errcol+' is null and '+errcol+" = '') and "+fil_cond+" When True Then 1 Else 0 end"

########################################################
########         LenChkCase Function   #################
########################################################
def LenChkCase(LenChk, errcol, LenFtrRule, MinLen, MaxLen):
    # defining Len case statament
    if LenChk=='N':
        return -1
    else:
        fil_cond = '1=1' if len(LenFtrRule)==0 else LenFtrRule
        return "case (length("+errcol+") < "+MinLen+" or length("+errcol+") > "+MaxLen+") and "+fil_cond+" When True Then 1 Else 0 end"
    

########################################################
##############         Main Function   #################
########################################################

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
    
        
        detail_query = "select '{chk_id}', '{pknames}' pknames, {pk1} pk1, {pk2} pk2, {pk3} pk3, {pk4} pk4, {pk5} pk5,{pk6} pk6, {pk7} pk7, {pk8} pk8, {errcol} errcol,  {NullChkStmt} NullChkResult, {LenChkStmt} LenChkResult from {table} where ({errcol} is null and {errcol} = '')"\
                    .format(chk_id=ChkId, pknames=pknames, pk1=pk1, pk2=pk2, pk3=pk3, pk4=pk4, pk5=pk5, pk6=pk6, pk7=pk7, pk8=pk8, errcol=errcol, table=SrcTab,  NullChkStmt=NullChkCase(NullChk, errcol, FtrRule), LenChkStmt=LenChkCase(LenChk, errcol, LenFtrRule, MinLen, MaxLen) );
        detail_query1 = detail_query+"\n";
        detail_sqls.append(detail_query1)
        
 
       
    # Writing data into Files
    detail = open(outfile, 'w')
    detail.writelines(detail_sqls);
    detail.close()
    
    
    conf.close()
    

##############################################################################
######################## Calling Main ######################################## 
##############################################################################

# Setting File
config = "AllChkConfig.csv"
outfile = 'Queries_out.sql'

# Calling Main
if __name__== "__main__":
    main(config, outfile)