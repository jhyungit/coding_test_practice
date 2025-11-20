#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(string a, string b){
    return a+b > b+a;
}

string solution(vector<int> numbers) {
    string answer = "";
    vector <string> vec;
    
    for (int num : numbers){
        vec.push_back(to_string(num));
    }
    
    sort(vec.begin(),vec.end(),compare);
    
    for(string v : vec)
        answer += v;
    if (answer[0] == '0')
        return "0";
    
    return answer;
}