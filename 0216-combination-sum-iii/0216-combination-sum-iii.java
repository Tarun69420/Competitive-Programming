class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        //int [] array = new int {1,2,3,4,5,6,7,8,9};
        List<List<Integer>> result = new ArrayList<>();
        com(k,n,result,new ArrayList<>(),1);
        return result;
    }

    static void com(int k, int n,List<List<Integer>> res, List<Integer> list,int start)
    {
        if ((n==0) & (list.size() == k))
        {
            res.add(new ArrayList<>(list));
            return;
        }
        for (int i = start;i<=9;i++)
        {
            //if (list.size()>=2 && list.get(list.size()-1)<=list.get(list.size()-2)) continue;
            if (n>=0)
            {
                list.add(i);
                com(k,n-i,res,list,i+1);
                list.remove(list.size()-1);
            }
        }
    }
}