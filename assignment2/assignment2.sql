.mode column
.headers off
----problem 1a
--select count(*) from (select docid from Frequency
--where docid='10398_txt_earn')
--x;

----problem 1b
--select count(*) from (select term from Frequency
--where (docid='10398_txt_earn' and count='1'))
--x;

----problem 1c
--select count(*) 
--from 
--(
--select * from 
--(
--select term from Frequency where (docid='10398_txt_earn' and count='1')
--union
--select term from Frequency where (docid='925_txt_trade' and count='1')
--)
--)
--x;

----problem 1d
--select count(*) 
--from 
--(
--select term from Frequency where term='parliament'
--)
--x;

--problem 1e
select count(*) 
from 
(
select term from Frequency where term='parliament'
)
x;
