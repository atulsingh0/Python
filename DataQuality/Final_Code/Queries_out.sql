select 'NULL_CHK', 'employee.empno' pknames, employee.empno pk1, '-' pk2, '-' pk3, '-' pk4, '-' pk5,'employee.ename' errcol, employee.ename errcolvalue,CASE WHEN ((employee.ename is null or employee.ename = '') and 1=1) THEN 1 ELSE 0 END NullChkResult, -1 LenChkResult, -1 LovChkResult, -1 DataChkResult, -1 DupChkResult, -1 RefChkResult from employee;
select 'LEN_CHK', 'employee.empno' pknames, employee.empno pk1, '-' pk2, '-' pk3, '-' pk4, '-' pk5,'employee.empno' errcol, employee.empno errcolvalue,-1 NullChkResult, CASE WHEN ((length(employee.empno) < 4 or length(employee.empno) > 6) and 1=1) THEN 1 ELSE 0 END LenChkResult, -1 LovChkResult, -1 DataChkResult, -1 DupChkResult, -1 RefChkResult from employee;
select 'LOV_CHK', 'employee.empno' pknames, employee.empno pk1, '-' pk2, '-' pk3, '-' pk4, '-' pk5,'employee.deptno' errcol, employee.deptno errcolvalue,-1 NullChkResult, -1 LenChkResult, CASE WHEN (employee.deptno not in (10, 20)) THEN 1 ELSE 0 END LovChkResult, -1 DataChkResult, -1 DupChkResult, -1 RefChkResult from employee;
select 'DATA_CHK', 'employee.empno' pknames, employee.empno pk1, '-' pk2, '-' pk3, '-' pk4, '-' pk5,'employee.job' errcol, employee.job errcolvalue,-1 NullChkResult, -1 LenChkResult, -1 LovChkResult, CASE WHEN (employee.job like '%4%') THEN 1 ELSE 0 END DataChkResult, -1 DupChkResult, -1 RefChkResult from employee;
select 'DUP_CHK', 'employee.empno' pknames, A.empno pk1, '-' pk2, '-' pk3, '-' pk4, '-' pk5,'A.empno' errcol, A.empno errcolvalue,-1 NullChkResult, -1 LenChkResult, -1 LovChkResult, -1 DataChkResult, CASE WHEN B.CNT=1 THEN 1 ELSE 0 END DupChkResult, -1 RefChkResult from employee A LEFT OUTER JOIN (select employee.empno,     1 CNT from employee where 1=1 GROUP BY empno HAVING COUNT(1)>1) B on A.empno=B.empno  ;
select 'ALL_CHK_EXP_DATA_REF', 'employee.empno' pknames, A.empno pk1, '-' pk2, '-' pk3, '-' pk4, '-' pk5,'A.deptno' errcol, A.deptno errcolvalue,CASE WHEN ((A.deptno is null or A.deptno = '') and 1=1) THEN 1 ELSE 0 END NullChkResult, CASE WHEN ((length(A.deptno) < 2 or length(A.deptno) > 2) and 1=1) THEN 1 ELSE 0 END LenChkResult, CASE WHEN (A.deptno not in (10, 30)) THEN 1 ELSE 0 END LovChkResult, -1 DataChkResult, CASE WHEN B.CNT=1 THEN 1 ELSE 0 END DupChkResult, -1 RefChkResult from employee A LEFT OUTER JOIN (select employee.empno,     1 CNT from employee where 1=1 GROUP BY empno HAVING COUNT(1)>1) B on A.empno=B.empno  ;
select 'REF_CHK', 'employee.empno' pknames, A.empno pk1, '-' pk2, '-' pk3, '-' pk4, '-' pk5,'A.deptno' errcol, A.deptno errcolvalue,-1 NullChkResult, -1 LenChkResult, -1 LovChkResult, -1 DataChkResult, CASE WHEN B.CNT=1 THEN 1 ELSE 0 END DupChkResult, CASE WHEN ((C.deptno IS NOT NULL and length(C.deptno)>0 ) and (1=1)) THEN 1 ELSE 0 END RefChkResult from employee A LEFT OUTER JOIN (select employee.empno,     1 CNT from employee where 1=1 GROUP BY empno HAVING COUNT(1)>1) B on A.empno=B.empno   LEFT OUTER JOIN ATUL.dept C on A.deptno=C.deptno;
select 'REF_CHK2', 'employee.empno' pknames, A.empno pk1, '-' pk2, '-' pk3, '-' pk4, '-' pk5,'A.deptno' errcol, A.deptno errcolvalue,-1 NullChkResult, -1 LenChkResult, -1 LovChkResult, -1 DataChkResult, -1 DupChkResult, CASE WHEN (( C.deptno IS NULL OR C.deptno='' ) and (1=1)) THEN 1 ELSE 0 END RefChkResult from employee A LEFT OUTER JOIN (select * from dept) C on ( A.deptno=C.deptno) ;
select 'ALL_CHK_EXP_DATA', 'employee.empno' pknames, A.empno pk1, '-' pk2, '-' pk3, '-' pk4, '-' pk5,'A.deptno' errcol, A.deptno errcolvalue,CASE WHEN ((A.deptno is null or A.deptno = '') and 1=1) THEN 1 ELSE 0 END NullChkResult, CASE WHEN ((length(A.deptno) < 2 or length(A.deptno) > 2) and 1=1) THEN 1 ELSE 0 END LenChkResult, CASE WHEN (A.deptno not in (10, 30)) THEN 1 ELSE 0 END LovChkResult, -1 DataChkResult, CASE WHEN B.CNT=1 THEN 1 ELSE 0 END DupChkResult, CASE WHEN (( C.deptno IS NULL OR C.deptno='' ) and (1=1)) THEN 1 ELSE 0 END RefChkResult from employee A LEFT OUTER JOIN (select employee.empno,     1 CNT from employee where 1=1 GROUP BY empno HAVING COUNT(1)>1) B on A.empno=B.empno   LEFT OUTER JOIN (select * from dept) C on ( A.deptno=C.deptno);
select 'ALL_CHK', 'employee.empno' pknames, A.empno pk1, '-' pk2, '-' pk3, '-' pk4, '-' pk5,'A.deptno' errcol, A.deptno errcolvalue,CASE WHEN ((A.deptno is null or A.deptno = '') and 1=1) THEN 1 ELSE 0 END NullChkResult, CASE WHEN ((length(A.deptno) < 2 or length(A.deptno) > 2) and 1=1) THEN 1 ELSE 0 END LenChkResult, CASE WHEN (A.deptno not in (20, 30)) THEN 1 ELSE 0 END LovChkResult, CASE WHEN (A.deptno like '%1%') THEN 1 ELSE 0 END DataChkResult, CASE WHEN B.CNT=1 THEN 1 ELSE 0 END DupChkResult, CASE WHEN ((C.deptno IS NOT NULL and length(C.deptno)>0 ) and (1=1)) THEN 1 ELSE 0 END RefChkResult from employee A LEFT OUTER JOIN (select employee.empno,     1 CNT from employee where 1=1 GROUP BY empno HAVING COUNT(1)>1) B on A.empno=B.empno   LEFT OUTER JOIN ATUL.dept C on A.deptno=C.deptno;
select 'NULL_REF', 'employee.empno' pknames, A.empno pk1, '-' pk2, '-' pk3, '-' pk4, '-' pk5,'A.deptno' errcol, A.deptno errcolvalue,CASE WHEN ((A.deptno is null or A.deptno = '') and 1=1) THEN 1 ELSE 0 END NullChkResult, -1 LenChkResult, -1 LovChkResult, -1 DataChkResult, -1 DupChkResult, CASE WHEN ((C.deptno IS NOT NULL and length(C.deptno)>0 ) and (1=1)) THEN 1 ELSE 0 END RefChkResult from employee A LEFT OUTER JOIN ATUL.dept C on A.deptno=C.deptno ;
