import java.io.*;
import javax.swing.*;
import java.awt.*;
import java.awt.image.*;
import java.awt.event.*;
import javax.imageio.*;
import java.net.URL;
import java.security.PublicKey;

public class chemi extends JFrame
{
    //Координаты всех фигур
    public int x[]=new int[4];
    public int y[]=new int[4];
    public boolean moveNow=false;
    //Номер текущей фигуры
    int actRow=-1;
    int actCol=-1;
    static BufferedImage imgs[]=null;
    int [][] mas={      { 1, 0, 0, 0, 0 },//2ка это припятствие
                        { 0, 0, 0, 0, 0 },
                        { 0, 0, 0, 0, 2 },
                        { 0, 0, 0, 0, 3 },
                        { 0, 0, 0, 0, 4 }
                    };
    int [][] etalon={   {0,2},
                        {0,3},
                        {1,4},
                    };

    public int x1frm=0;
    public int y1frm=0;
    public int x2frm=0;
    public int y2frm=0;

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
            return i-1;
        }
        if(direction==1 && curCol!=0)//влево
        {
            //движение горизонтальное по колонкам вправо
            for(i=curCol-1;i>=0;i--)
                if(mas[curRow][i]!=0)
                    return i+1;
            return i+1;
        }
        if(direction==2 && curRow!=0)//вверх
        {
            //движение вертикальное по строкам вниз
            for(i=curRow-1;i>=0;i--)
                if(mas[i][curCol]!=0)
                    return i+1;
            return i+1;
        }
        if(direction==3 && (curRow!=rowCount-1))//вниз
        {
            //движение вертикальное по строкам вниз
            for(i=curRow+1;i<rowCount;i++)
                if(mas[i][curCol]!=0)
                    return i-1;
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

    //Инициализация рабочей области (левый верхний угол, правый нижний)
    public void iniFrame(int p_x1frm,int p_y1frm,int p_x2frm,int p_y2frm)
    {
        x1frm=p_x1frm;
        y1frm=p_y1frm;
        x2frm=p_x2frm;
        y2frm=p_y2frm;
    }

//    class Coords
//    {
//        public int x=0,y=0;
//        Coords(){};
//        Coords(int px,int py){x = px;y = py;};
//    }

    //Вернёт -1 если мышка попала в пустоту, или вернёт номер выбранной фигуры чтобы её подсветить
    private boolean IsShapeSelectedByCoords(int x,int y)
    {
        int xpos=x-x1frm;
        int ypos=y-y1frm;
        int numRow=0;
        int numCol=0;
        if(x>=x1frm && x<=x1frm+x2frm && y>=y1frm && y<=y1frm+y2frm)
        {
            numCol=(int)(xpos/(x2frm/mas[0].length));
            numRow=(int)(ypos/(y2frm/mas.length));
            if(mas[numRow][numCol]>0)
            {
                actRow=numRow;
                actCol=numCol;
                return true;
            }
        }
        return false;
    }



    //Потоки 1й способ создания
    //Создание потока путем наследования класса Thread
    class thrd extends Thread
    {
        thrd(){}
        @Override
        public void run()
        {
            try
            {
                for(int i=0;i<5;i++)
                {
                    sleep(1000);
                    System.out.print("ok");
                    //cnt++;
                }
            }
            catch (InterruptedException e) { return; }
            //System.out.print("\n");
        }
    }

    public chemi(){}

    public void runIt()
    {
        setTitle("Simple example");
        setSize(260, 260);
        setLocationRelativeTo(null);
        iniFrame(10,40,100,100);
        //Нажатие кнопки клавишей - можно получить код
        this.addKeyListener(new KeyAdapter()
        {
            @Override
            public void keyPressed(KeyEvent e)
            {
                int tmpRow=0,tmpCol=0;
                if(actRow>=0 && actCol>=0)
                {
                    //0-вправо, 1-влево, 2-вверх,3-вниз

//                        makeStep(0, 0, getStepCount(0,0,3,mas),0, mas);
                    //System.out.println(e.getKeyCode());
                    //влево
                    if(e.getKeyCode()==37)
                    {
                        makeStep(actRow, actCol, actRow, tmpCol=getStepCount(actRow,actCol,1,mas), mas);
                        actCol=tmpCol;
                    }
                    //вправо
                    if(e.getKeyCode()==39)
                    {
                        makeStep(actRow, actCol, actRow, tmpCol=getStepCount(actRow,actCol,0,mas), mas);
                        actCol=tmpCol;
                    }

                    //вверх
                    if(e.getKeyCode()==38)
                    {
                        makeStep(actRow, actCol, tmpRow=getStepCount(actRow,actCol,2,mas), actCol, mas);
                        actRow=tmpRow;
                    }
                    //вниз
                    if(e.getKeyCode()==40)
                    {
                        makeStep(actRow, actCol, tmpRow=getStepCount(actRow,actCol,3,mas), actCol, mas);
                        actRow=tmpRow;
                    }
                    chemi.this.update(chemi.this.getGraphics());
                    if(isFinished(mas,etalon))
                    {
                        new JOptionPane().showMessageDialog(chemi.this, "Типа выйграл","",JOptionPane.YES_OPTION);
                        System.exit(0);
                    }
                        //System.out.print("Ура!");
                    //out(mas);
                }
            }
        });

        this.addMouseListener(new MouseAdapter(){
            @Override
            public void mouseClicked(MouseEvent e)
            {
                if(IsShapeSelectedByCoords(e.getX(),e.getY()))
                    chemi.this.update(chemi.this.getGraphics());
            }
        });

//        //Запуск потока движения квадрата
//        thrd c=new thrd();
//        c.start();
//        //Остановить основной (вызывающий) поток и ждать пока не завершиться вызванный поток
//        try
//        {
//            c.join();
//        }
//        catch(InterruptedException e)
//        {
//            //System.out.println("catch p.t.join()");
//        }
        setVisible(true);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
    }

    public void paint(Graphics g)
    {
        super.paint(g);
        Graphics2D g2 = (Graphics2D)g;
        //рисуем рамку 100х100
        g2.draw3DRect(x1frm,y1frm,x2frm,y2frm,true);
        //Если есть движение активному бару даём координаты от потока
        if(moveNow)
        {

        }
        //Если нет движения рисуем всё из позиций массива mas
        else
        {
            for(int i=0;i<mas.length;i++)
                for(int j=0;j<mas[0].length;j++)
                {
                    //20 - размер картинки
                    if(mas[i][j]>0)
                        g2.drawImage(imgs[mas[i][j]-1], null, j*x2frm/mas[0].length+x1frm, i*y2frm/mas.length+y1frm);
                }
            for(int i=0;i<mas.length;i++)
                for(int j=0;j<mas[0].length;j++)
                {
                    if(j==actCol && i==actRow)
                        g2.draw3DRect(j*x2frm/mas[0].length+x1frm, i*y2frm/mas.length+y1frm,20,20,true);
                }
        }
        g2.drawImage(imgs[0], null, x1frm+x2frm+10, y1frm+80);
        g2.drawImage(imgs[1], null, x1frm+x2frm+30, y1frm+40);
        g2.drawImage(imgs[2], null, x1frm+x2frm+30, y1frm+60);
        g2.drawImage(imgs[3], null, x1frm+x2frm+30, y1frm+80);
    }

    public static void main(String[] pars)
    {
        URL resource = new chemi().getClass().getResource("/");
        String path=new File(".").getAbsolutePath();
        path=path.substring(0,path.length()-2)+"\\res\\";
        //System.out.println(ss);

        imgs=new BufferedImage[4];
        for(int i=0;i<4;i++)
        try
        {
            imgs[i] = ImageIO.read(new File(path+(i+1)+".jpg"));
        }
        catch(Exception e)
        {
            System.out.println("а нифига");
        }

        SwingUtilities.invokeLater
        (
            new Runnable()
            {
                public void run()
                {
                    chemi ex = new chemi();
                    ex.runIt();
                    //chemiRun ex=new chemiRun();
                }
            }
        );


    }
}
