import java.util.*;

public class LinearSearch{
  public boolean isPresent(List<Integer> items,int find){
      for(int x : items){
        if(x == find){
          return true;
       }
    }
    return false;
  }
}
