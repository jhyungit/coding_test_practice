// https://school.programmers.co.kr/learn/courses/30/lessons/12978

#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <unordered_map>

using namespace std;

int solution(int N, vector<vector<int>> road, int K) {
    int answer = 0;
    
    // 각 마을까지의 최단 거리 (INF로 초기화)
    vector<int> dist(N + 1, INT_MAX);
    dist[1] = 0;  // 시작점인 1번 마을은 거리가 0
    
    // 그래프 초기화 (양방향 도로)
    unordered_map<int, vector<pair<int, int>>> graph;
    for (const auto& r : road) {
        int s_node = r[0], e_node = r[1], length = r[2];
        graph[s_node].push_back({e_node, length});
        graph[e_node].push_back({s_node, length});
    }
    
    // 우선순위 큐 (최소 힙)
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, 1});  // (거리, 노드)
    
    // 다익스트라 알고리즘 수행
    while (!pq.empty()) {
        int cur_dist = pq.top().first;
        int cur_node = pq.top().second;
        pq.pop();
        
        // 이미 더 짧은 경로가 발견되면 건너뛰기
        if (cur_dist > dist[cur_node]) continue;

        // 연결된 노드 탐색
        for (const auto& next : graph[cur_node]) {
            int next_node = next.first;
            int edge_weight = next.second;
            
            // 최단 거리 갱신
            if (dist[next_node] > cur_dist + edge_weight) {
                dist[next_node] = cur_dist + edge_weight;
                pq.push({dist[next_node], next_node});
            }
        }
    }

    // 최단 거리가 K 이하인 마을의 수를 세기
    for (int i = 1; i <= N; ++i) {
        if (dist[i] <= K) {
            answer++;
        }
    }
    
    return answer;
}