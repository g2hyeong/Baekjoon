import java.util.HashMap;

/**
    key : val 형식의 자료구조가 필요.
    key의 개수와 N/2 간의 대수 비교.
    key >= N/2 : ans == N/2
    else : ans == key
    
    hm.put("파인애플", hm.getOrDefault("파인애플",0)+1);
    
    1. HashMap을 사용하려면 Import java.util.HashMap 해야한다.
    2. HashMap 선언 시 사용되는 타입에 제약이 있나?
    3. HashMap과 관련해서 배워야 할 주요 메서드와 기술이 있는 것 같다.
    4. HashMap을 사용하면서 성능적인 개선을 이룰 수 있는 추가적인 준비 장치들이 있다.
*/

class Solution {
    public int solution(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>(nums.length);
        for(int elem : nums) {
            map.put(elem, map.getOrDefault(elem, 0)+1);
        }
        if(map.size() >= nums.length/2)
            return nums.length/2;
        else
            return map.size();
    }
}