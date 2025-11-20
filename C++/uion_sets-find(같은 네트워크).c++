#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

int find(vector<int> &parent, int x) {
    if (parent[x] != x) {
        parent[x] = find(parent, parent[x]);
    }
    return parent[x];
}

void union_sets(vector<int> &parent, int a, int b) {
    a = find(parent, a);
    b = find(parent, b);
    
    if (a < b)
        parent[b] = a;
    else
        parent[a] = b;
}

int solution(int n, vector<vector<int>> computers) {
    vector<int> parent(n);  // 0-based 인덱스 사용
    
    // 각 노드는 자기 자신을 부모로 초기화
    for (int i = 0; i < n; ++i) {
        parent[i] = i;
    }
    
    // 연결된 노드끼리 union 수행
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (computers[i][j] == 1 && i != j) {
                union_sets(parent, i, j); // i와 j를 연결
            }
        }
    }
    
    // 부모 배열에서 서로 다른 부모를 찾는 방법
    unordered_map<int, int> counter;
    for (int i = 0; i < n; ++i) {
        counter[find(parent, i)]++;  // 각 연결된 그룹의 부모 찾기
    }
    
    return counter.size();  // 서로 다른 부모가 연결된 네트워크 수
}