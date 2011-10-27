import java.util.*;

public class chemiLogik
{
    private static int cnt=0;
    //Проверка завершения игры
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
                                if(etalon[i][j]>0 && etalon[i][j]!=mas[r+i][c+j])
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

    //Вывод массива
    public static void out(int out[][])
    {
        int i,j;
        for(i=0;i<out.length;i++)
        {
            for(j=0;j<out[0].length;j++)
                System.out.print(out[i][j]);
            System.out.print("\n");
        }
        System.out.print("\n");
    }

    //Получение индекса позиции куда ещё можно доехать чтоб упереться
    //0-вправо, 1-влево, 2-вверх,3-вниз
    public static int getStepCount(int curRow,int curCol,int direction, int mas[][])
    {
        int i=0;
        int colCount=mas[0].length;
        int rowCount=mas.length;
        if(direction==0 && curCol!=(colCount-1))//вправо и фокус стоит не справа скраю
        {
            //движение горизонтальное по колонкам вправо
            for(i=curCol+1;i<colCount;i++)
                if(mas[curRow][i]!=0)
                    return i-1;
        }
        if(direction==1 && curCol!=0)//влево
        {
            //движение горизонтальное по колонкам вправо
            for(i=curCol-1;i>=0;i--)
                if(mas[curRow][i]!=0)
                    return i+1;
        }
        if(direction==2 && curRow!=0)//вверх
        {
            //движение вертикальное по строкам вниз
            for(i=curRow-1;i>=0;i--)
                if(mas[i][curCol]!=0)
                    return i+1;

        }
        if(direction==3 && (curRow!=rowCount-1))//вниз
        {
            //движение вертикальное по строкам вниз
            for(i=curRow+1;i<rowCount;i++)
                if(mas[i][curCol]!=0)
                    return i-1;
        }
        return 0;
    }

    //Перемещение указанного элемента (по фокусу)
    public static int makeStep(int curRow,int curCol,int stepPosRow, int spepPosCol, int mas[][])
    {
        int karman=mas[curRow][curCol];
        mas[curRow][curCol]=mas[stepPosRow][spepPosCol];
        mas[stepPosRow][spepPosCol]=karman;
        return 0;
    }

    public static void main(String[] pars)
    {
        int [][] mas={      { 0, 0, 0, 0, 0},//2ка это припятствие
                            {-1, 0, 0, 0, 0},
                            { 0, 0, 0, 0, 1},
                            { 2, 0, 0, 0, 3},
                            { 1, 0, 0, 0, 4}
                        };
        int [][] etalon={   {0,1},
                            {2,3},
                            {0,4},
                        };

        //нажатие вправо
        //0-вправо, 1-влево, 2-вверх,3-вниз
        out(mas);
        if(isFinished(mas,etalon))
            System.out.println("ok");
        else
            System.out.println("error");
        //0-вправо, 1-влево, 2-вверх,3-вниз
        makeStep(3,0,3,getStepCount(3,0,0, mas),mas);
        out(mas);

        if(isFinished(mas,etalon))
            System.out.println("ok");
        else
            System.out.println("error");

//        //Потоки 1й способ создания
//        //Создание потока путем наследования класса Thread
//        class thrd extends Thread
//        {
//            thrd(){}
//            @Override
//            public void run()
//            {
//                try
//                {
//                    for(int i=0;i<5;i++)
//                    {
//                        sleep(1000);
//                        System.out.print(cnt);
//                        cnt++;
//                    }
//                }
//                catch (InterruptedException e) { return; }
//                System.out.print("\n");
//            }
//        }
//
//        thrd c=new thrd();
//        c.start();
//        //Остановить основной (вызывающий) поток и ждать пока не завершиться вызванный поток
//        try
//        {
//            c.join();
//        }
//        catch(InterruptedException e)
//        {
//            System.out.println("catch p.t.join()");
//        }
    }
}
