/**
    HashMap 속 HashMap
    1. HashMap<String, Integer>
    2. HashMap<String, HashMap<Integer, Integer>>
    
    부족한 점
    1. HashMap 속 HashMap에 익숙치 않음
    2. HashMap의 정렬 관련 로직
    3. EntrySet, KeySet 같은 기능 공부
    4. ArrayList 메서드 까먹음
*/

import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        ArrayList<Integer> answer = new ArrayList<>();
        int length = genres.length;
        HashMap<String, Integer> hm_order = new HashMap<String, Integer>(length);
        HashMap<String, HashMap<Integer, Integer>> hm_index = new HashMap<String, HashMap<Integer, Integer>>(length); // 컴파일 오류 나는지 확인
        
        for (int i=0; i<length; i++) {
            hm_order.put(genres[i], hm_order.getOrDefault(genres[i], 0) + plays[i]);
            HashMap<Integer, Integer> tmp = hm_index.getOrDefault(genres[i], new HashMap<Integer, Integer>());
            tmp.put(i, plays[i]);
            hm_index.put(genres[i], tmp);
            //System.out.println(hm_index.get(genres[i]));
        }
        
        
        // HashMap value 기준 sort
        List<String> keySet = new ArrayList<>(hm_order.keySet());
        keySet.sort((o1, o2) -> hm_order.get(o2).compareTo(hm_order.get(o1)));
        
        for (String key : keySet) {
            HashMap<Integer, Integer> tmp = hm_index.get(key);
            List<Integer> rst = new ArrayList<>(tmp.keySet());
            rst.sort((o1, o2) -> tmp.get(o2).compareTo(tmp.get(o1)));
            answer.add(rst.get(0));
            if(rst.size() > 1)
                answer.add(rst.get(1));
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }
}