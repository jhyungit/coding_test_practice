-- https://school.programmers.co.kr/learn/courses/30/lessons/131535

-- 코드를 입력하세요
SELECT count(*) as 'USERS'
FROM USER_INFO
WHERE JOINED like '%2021%' and AGE BETWEEN 20 AND 29