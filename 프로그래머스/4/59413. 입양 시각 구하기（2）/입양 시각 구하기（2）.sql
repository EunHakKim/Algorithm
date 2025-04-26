select HOUR, max(COUNT) COUNT from
    (
        (select 0 HOUR, 0 COUNT) UNION 
        (select 1, 0) UNION 
        (select 2, 0) UNION 
        (select 3, 0) UNION 
        (select 4, 0) UNION 
        (select 5, 0) UNION 
        (select 6, 0) UNION 
        (select 7, 0) UNION 
        (select 8, 0) UNION 
        (select 9, 0) UNION 
        (select 10, 0) UNION 
        (select 11, 0) UNION 
        (select 12, 0) UNION 
        (select 13, 0) UNION 
        (select 14, 0) UNION 
        (select 15, 0) UNION 
        (select 16, 0) UNION 
        (select 17, 0) UNION 
        (select 18, 0) UNION 
        (select 19, 0) UNION 
        (select 20, 0) UNION 
        (select 21, 0) UNION 
        (select 22, 0) UNION 
        (select 23, 0) UNION 
        (select hour(datetime) HOUR, count(*) COUNT from animal_outs group by 1)
    ) TMP
group by 1 
order by 1 asc