// https://school.programmers.co.kr/learn/courses/30/lessons/1844

#include<vector>
#include<queue>
#include<iostream>

using namespace std;

// 상하좌우 방향 설정
int dx[] = {-1,1,0,0}; //상하좌우
int dy[] = {0,0,-1,1}; //상하좌우

int solution(vector<vector<int> > maps)
{
    int answer = 0;
    // 맵의 행과 열
    int row = maps.size(), col = maps[0].size();
    
    // 방문 체크
    vector <vector<int>> visited(row , vector<int>(col,0));
    
    queue<pair<int,int>> q;
    q.push({0,0}); //시작 좌표
    visited[0][0] = true; // 초기좌표 방문 처리
    
    
    while(!q.empty()){
        int x = q.front().first, y = q.front().second;
        q.pop();
        
                // 목표 위치에 도달했을 때
        if (x == row - 1 && y == col - 1) {
            return visited[x][y];  // 최단 거리 반환
        }
        
        // 상하좌우 탐색
        for (int i = 0; i < 4; ++i) {
            int nx = x + dx[i], ny = y + dy[i];
            
            // 범위 체크 및 방문 안 했고, 벽이 아닌 곳만 큐에 넣기
            if (0 <= nx && nx < row && 0 <= ny && ny < col && maps[nx][ny] == 1 && visited[nx][ny] == 0) {
                visited[nx][ny] = visited[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }   
    return -1;
}