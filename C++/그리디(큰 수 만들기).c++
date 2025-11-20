// https://school.programmers.co.kr/learn/courses/30/lessons/42883?language=cpp

#include <string>
#include <vector>
#include <deque>
#include <iostream>

using namespace std;

string solution(string number, int k) {
    deque<char> q;  // 큐 대신 덱 사용

    for (char v : number) {
        while (!q.empty() && v > q.back() && k > 0) {
            q.pop_back();
            k--;
        }
        q.push_back(v);
    }

    // ✅ 만약 k가 남아 있으면 뒤에서 추가 제거
    while (k > 0) {
        q.pop_back();
        k--;
    }

    // ✅ 정답 문자열 구성
    string answer = "";
    while (!q.empty()) {
        answer += q.front();
        q.pop_front();
    }

    return answer;
}
