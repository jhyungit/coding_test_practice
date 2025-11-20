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
    
    // 사이클 검사를 위한 변수
    bool cycle = false;

    // 연결된 컴퓨터들 검사
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (computers[i][j] == 1 && i != j) {
                if (find(parent, i) == find(parent, j)) {  // 사이클 발견
                    cycle = true;
                    break;
                } else {
                    union_sets(parent, i, j);  // 연결
                }
            }
        }
        if (cycle) break;  // 사이클이 발견되면 루프 종료
    }

    cout << cycle << endl;
    return cycle ? 1 : 0;
}
