.mode column
.headers off

----problem 1g
select prod from (select a.row_num as a_row, b.col_num as b_row, sum(a.value*b.value) as prod from a,b where a.col_num=b.row_num group by a.row_num, b.col_num) where a_row=2 and b_row=3;


