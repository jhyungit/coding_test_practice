//순열

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    vector <int> arr={1,2,3};
    
    sort(arr.begin(),arr.end());
    
    do{
        for(int num : arr){
            cout << num << " ";
        }
        cout << "\n";
    }while (next_permutation(arr.begin(),arr.end()));
    
    return 0;
}


//조합

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector <int> arr ={1,2,3,4};
    int r = 2; // 뽑아낼 조합 개수
    vector <int> mask(arr.size(),0); // mask 0으로 채움
    fill(mask.begin(),mask.begin()+r,1); //// 앞쪽 r개만 1로 설정
    
    do{for(int i = 0; i < arr.size(); i++){
        if(mask[i]) cout << arr[i] << " ";
    }cout << "\n";
    }while(next_permutation(mask.begin(),mask.end()));// 이전 조합 찾기

    return 0;
}
