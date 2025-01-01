import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(String[][] clothes) {
        HashMap<String, Integer> hm = new HashMap<String, Integer>(clothes.length);
        for (int i=0; i<clothes.length; i++) {
            hm.put(clothes[i][1], hm.getOrDefault(clothes[i][1], 0) + 1);
        }
        
        int answer = 1;
        for (Map.Entry<String, Integer> entry : hm.entrySet()) {
            answer = answer * (entry.getValue() + 1);
        }
        return answer - 1;
    }
}