
-- create table EMPLOYEE
CREATE TABLE  "EMPLOYEE"    (	"EMPNO" NUMBER(4,0) NOT NULL ENABLE, 	"ENAME" VARCHAR2(10), 	"JOB" VARCHAR2(9), 	"MGR" NUMBER(4,0), 	"HIREDATE" DATE, 	"SAL" NUMBER(7,2), 	"COMM" NUMBER(7,2), 	"DEPTNO" NUMBER(2,0)   ) ;

-- insert data into EMPLOYEE
insert into EMPLOYEE values ("7839","KING","PRESIDENT","","11/17/1981","5000","","10") ;
insert into EMPLOYEE values ("7698","BLAKE","MANAGER","7839","05/01/1981","2850","","30") ;
insert into EMPLOYEE values ("7782","","MANAGER","7839","06/09/1981","2450","","10") ;
insert into EMPLOYEE values ("756","JONES","MANAGER","7839","04/02/1981","2975","","20") ;
insert into EMPLOYEE values ("7788","SCOTT","ANALYST","7566","12/09/1982","3000","","20") ;
insert into EMPLOYEE values ("7788","FORD","ANALYST","7566","12/03/1981","3000","","10") ;
insert into EMPLOYEE values ("7369","SMITH","CLERK","7902","12/17/1980","800","","") ;
insert into EMPLOYEE values ("7499","ALLEN","SALESMAN","7698","02/20/1981","1600","300","3") ;


-- create table DEPT
CREATE TABLE  "DEPT"    (	"DEPTNO" NUMBER(2,0), 	"DNAME" VARCHAR2(14), 	"LOC" VARCHAR2(13), 	 PRIMARY KEY ("DEPTNO") ENABLE   ) ;

-- insert data into DEPT
insert into DEPT values ("10","ACCOUNTING","NEW YORK") ;
insert into DEPT values ("20","RESEARCH","DALLAS") ;
insert into DEPT values ("30","SALES","CHICAGO") ;
insert into DEPT values ("40","OPERATIONS","BOSTON") ;

