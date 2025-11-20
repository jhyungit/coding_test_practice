// https://school.programmers.co.kr/learn/courses/30/lessons/42885

#include <string>
#include <vector>
#include <algorithm>
#include <deque>
#include <iostream>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    sort(people.begin(),people.end());
    deque <int> que (people.begin(),people.end());
    
    while (que.size()>1){
        if (que.front()+que.back() <= limit){
            que.pop_front();
            que.pop_back();
            answer++;
        }else{
            que.pop_back();
            answer++;
        }
    }
    if(!que.empty()) answer ++;
    return answer;
}