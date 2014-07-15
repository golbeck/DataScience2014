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

----problem 1e
--select count(*) from (select docid, freq from (select docid, sum(count) as freq from frequency group by docid having sum(count)>300)) x;

--problem 1f
--select distinct docid from frequency group by docid having term="world" and term="transactions";
select count(*) from (
select docid, count from frequency where term="world"
intersect
select docid, count from frequency where term="transactions"
)
x;

--alternative solution to 1f using "inner join" and alias tables
select count(*) from (
(select docid, count from frequency where term="world") x
inner join
(select docid, count from frequency where term="transactions") y
on (x.docid=y.docid)
)
z;
