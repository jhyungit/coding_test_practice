-- https://school.programmers.co.kr/learn/courses/30/lessons/59413

-- 코드를 입력하세요
with recursive time_table as (
    select 0 as hour
    union all
    select hour + 1
    from time_table
    where hour < 23
)

select t.hour, count(animal_id) as `count`
from time_table as t
left join animal_outs as a
on t.hour = hour(a.datetime)
group by hour
order by hour