import java.util.HashMap;
import java.util.Map;
/**
    Key : Value 가 필요하겠다. Value는 Boolean인 줄 알았으나, 동명이인 조건에 의해 Integer로 변경
    배열을 그대로 HashMap으로 변환하는 메서드는 없을까?
*/

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> map = new HashMap<String, Integer>(participant.length);
        for (String part : participant) {
            map.put(part, map.getOrDefault(part, 0) + 1);
        }
        for (String comp : completion) {
            map.put(comp, map.getOrDefault(comp, 0) - 1);
        }
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            if (entry.getValue() != 0)
                return entry.getKey();
        }
        return "";
    }
}