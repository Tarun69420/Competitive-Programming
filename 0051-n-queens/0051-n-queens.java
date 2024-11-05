class Solution {
    public List<List<String>> solveNQueens(int n) {
       boolean [][] board = new boolean[n][n];
       
       
       return queens(board,0);

    }
    static List<List<String>>  queens (boolean[][] board,int row)
    {
        if (row==board.length)
        {
            return display(board);

        }
        List<List<String>> ans = new ArrayList<>();
        for (int i = 0 ; i < board[0].length;i++)
        {
            
            if (isSafe(board,row,i))
            {
            board[row][i] = true;
            ans.addAll(queens(board,row+1));
            board[row][i] = false;
            }
            
        }
        return ans;
    }
    static boolean isSafe(boolean[][] board,int row,int col)
    {
        for (int i=0;i<=row;i++)
        {
            if (board[i][col])
            {
                return false;
            }
        }
        int minleft = Math.min(row,col);
        for (int i = 1;i<=minleft;i++)
        {
            if (board[row-i][col-i])
            {
                return false;
            }
        }
        int minright = Math.min(row,board.length-col-1);
        for (int i = 1;i<=minright;i++)
        {
            if (board[row-i][col+i])
            {
                return false;
            }
        }
        return true;
    }
    static List<List<String>> display (boolean[][] board)
    {   
        List<List<String>> ans = new ArrayList<>();
        List<String> sol = new ArrayList<>();
        for (int i= 0; i < board.length; i++)
        {   String s = "";
            for (int j = 0; j<board[0].length;j++)
            {
                if (board[i][j])
                {
                    s+="Q";
                    
                }
                else
                {
                    s+=".";
                }
            }
            sol.add(s);
        }
        ans.add(sol);
        return ans;
    }
}