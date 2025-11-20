// https://school.programmers.co.kr/learn/courses/30/lessons/43238

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

long long solution(int n, vector<int> times) {
    auto it1 = min_element(times.begin(),times.end());
    long long low = *it1;
    auto it2 = max_element(times.begin(),times.end());
    long long high = n *(*it2);
    
    while (low <= high){
        long long mid = low + (high - low) / 2; // 오버플로우 방지
        long long sum = 0;
        
        for (int time : times){
            sum += mid/time;
        }
        
        if (sum < n)
            low = mid+1;
        else{
            high = mid - 1;
        }
            
    }
    
    return low;
}