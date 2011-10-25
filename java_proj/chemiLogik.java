public class chemiLogik
{
    public static void main(String[] pars)
    {
        int [][] mas={      {0,0,0,1,0},
                            {0,0,1,1,0},
                            {0,0,0,1,0},
                            {0,0,0,0,0},
                            {0,0,0,0,0}
                        };
        int [][] etalon={   {0,1,0},
                            {1,1,0},
                            {0,1,0},
                        };



        int i,j,r,c;
        //Перебор игровой матрицы
        for(r=0;r<mas.length;r++)
        {
            for(c=0;c<mas[r].length;c++)
            {
                //Нашли вхождение и снего проверить соответствует ли матрица подматрице
                //подбор шаблона по игровой матрице
                if(r<(mas.length-etalon.length) && c<(mas[0].length-etalon[0].length))
                {
                    for(i=0;i<etalon.length;i++)
                    {
                        for(j=0;j<etalon[i].length;j++)
                        {


                            if(etalon[i][j]==1 && etalon[i][j]==mas[r+i][c+j])
                        }
                    }
                }
            }
        }
        System.out.println(etalon.length);
    }
}
