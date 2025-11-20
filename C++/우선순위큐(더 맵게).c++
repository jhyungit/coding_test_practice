// https://school.programmers.co.kr/learn/courses/30/lessons/42626

#include <string>
#include <vector>
#include <iostream>
#include <queue> // 우선 순위 큐
#include <functional> // for std::greater 최소 큐 구현

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int,vector<int>,greater<int>> pq (scoville.begin(),scoville.end());
    
    if(pq.top() >= K)
        return answer;
    
    while(pq.size()>=2){
        int food1 = pq.top();
        pq.pop();
        int food2 = pq.top();
        pq.pop();
        int next_score = food1 + (food2*2);
        pq.push(next_score);
        ++answer;
        if (pq.top() >= K)
            return answer;
    }
    return -1;
}