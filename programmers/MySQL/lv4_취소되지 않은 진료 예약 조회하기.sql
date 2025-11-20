-- https://school.programmers.co.kr/learn/courses/30/lessons/132204

-- 코드를 입력하세요

# 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시 항목
# '2022-04-13' '취소되지 않은' '흉부외과 CS' '진료예약일시 기준 오름차순'

SELECT APNT_NO, PT_NAME, P.PT_NO, A.MCDP_CD, D.DR_NAME, APNT_YMD
FROM PATIENT P
    JOIN APPOINTMENT A
    ON P.PT_NO = A.PT_NO
    JOIN DOCTOR D
    ON A.MDDR_ID = D.DR_ID
WHERE APNT_YMD like '2022-04-13%' AND APNT_CNCL_YN = 'N' AND A.MCDP_CD = 'CS'
ORDER BY APNT_YMD ASC