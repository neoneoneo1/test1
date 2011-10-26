public class chemiLogik
{
    public static boolean isFinished(int mas[][],int etalon[][])
    {
        int i,j,r,c;
        int iterCount=0;
        boolean bFind=false;
        int colCnt=etalon[0].length;
        int rowCnt=etalon.length;
        //Перебор игровой матрицы
        for(r=0;r<mas.length;r++)
        {
            for(c=0;c<mas[r].length;c++)
            {
                bFind=false;
                //Нашли вхождение и снего проверить соответствует ли матрица подматрице
                //подбор шаблона по игровой матрице
                if(r<=(mas[0].length-rowCnt) && c<=(mas.length-colCnt))
                {
                    Outr:
                    {
                        bFind=true;
                        for(i=0;i<rowCnt;i++)
                        {
                            for(j=0;j<colCnt;j++)
                            {
                                if(etalon[i][j]==1 && etalon[i][j]!=mas[r+i][c+j])
                                {
                                    bFind=false;
                                    break Outr;
                                }
                            }
                        }
                    }
                }
                if(bFind)
                {
                    //System.out.println("ok iterCount="+iterCount);
                    return true;
                }
                iterCount++;
            }
        }
        //System.out.println("ok iterCount="+iterCount);
        return false;
    }

    public static void out(int out[][])
    {
        int i,j;
        for(i=0;i<out.length;i++)
        {
            for(j=0;j<out[0].length;j++)
                System.out.print(out[i][j]);
            System.out.print("\n");
        }
    }

    public static void main(String[] pars)
    {
        int [][] mas={      {1,0,0,0,0},
                            {0,0,0,0,0},
                            {0,0,0,0,1},
                            {0,0,0,0,1},
                            {0,0,0,0,1}
                        };
        int [][] etalon={   {0,1},
                            {1,1},
                            {0,1},
                        };


        out(mas);
        out(etalon);
        //нажатие вправо

        //0-вправо, 1-влево, 2-вверх,3-вниз
        int direction=0;
        if(isFinished(mas,etalon))
            System.out.println("ok");
        else
            System.out.println("error");


    }


//дальше просто вывод
//        //Нашли вхождение и снего проверить соответствует ли матрица подматрице
//        //подбор шаблона по игровой матрице
//        for(i=0;i<etalon.length;i++)
//        {
//            for(j=0;j<etalon[i].length;j++)
//            {
//                System.out.print(etalon[i][j]);
//            }
//            System.out.print("\n");
//        }
//
//
//        //Перебор игровой матрицы
//        for(r=0;r<mas.length;r++)
//        {
//            for(c=0;c<mas[r].length;c++)
//            {
////                //Нашли вхождение и снего проверить соответствует ли матрица подматрице
////                //подбор шаблона по игровой матрице
////                if(r<(mas.length-etalon.length) && c<(mas[0].length-etalon[0].length))
////                {
////                    boolean bFind=true;
////                    Outr:
////                    {
////                        for(i=0;i<etalon.length;i++)
////                        {
////                            for(j=0;j<etalon[i].length;j++)
////                            {
////                                if(!(etalon[i][j]==1 && etalon[i][j]==mas[r+i][c+j]))
////                                {
////                                    bFind=false;
////                                    break Outr;
////                                }
////                            }
////                        }
////                    }
////                    if(bFind)
////                        System.out.println("ok");
////                }
//                System.out.print(mas[r][c]);
//            }
//            System.out.print("\n");
//        }
//    }
}
