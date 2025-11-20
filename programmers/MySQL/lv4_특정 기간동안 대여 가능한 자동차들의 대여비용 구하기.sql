-- https://school.programmers.co.kr/learn/courses/30/lessons/157339

-- 코드를 입력하세요
select car_id, c.car_type, round((daily_fee * ((100-discount_rate)/100) * 30), 0) as `fee`
from CAR_RENTAL_COMPANY_CAR as c
join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as p
on c.car_type = p.car_type
where car_id in (
    select car_id
    from CAR_RENTAL_COMPANY_CAR
    where car_type in ('세단', 'SUV')
) and
car_id not in (
    select car_id
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where START_DATE <= '2022-11-30' and END_DATE >= '2022-11-1'
) and
duration_type = '30일 이상'
having fee between 500000 and 2000000
order by FEE desc, car_type asc, car_id desc