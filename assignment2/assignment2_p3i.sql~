.mode column
.headers off

CREATE VIEW qview AS
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count;


select max(sumprod) from
(
select col_num, sum(prod) as sumprod from (
select x.docid as row_num, y.docid as col_num, (x.count*y.count) as prod from 
(
(select docid, term as xterm, count from qview) x
join
(select docid, term as yterm, count from qview) y
)
where xterm=yterm
)
where row_num='q' group by row_num, col_num order by sumprod asc
);

