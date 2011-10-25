import java.io.*;
import javax.swing.*;
import java.awt.*;
import java.awt.image.*;
import java.awt.event.*;
import javax.imageio.*;

public class chemi extends JFrame
{
    public int x=100,y=100;
    BufferedImage img1=null;
    public chemi()
    {
        setTitle("Simple example");
        setSize(600, 600);
        setLocationRelativeTo(null);
        try
        {
            img1 = ImageIO.read(new File("c:\\123.jpg"));
        }
        catch(Exception e)
        {

        }

        //Нажатие кнопки клавишей - можно получить код
        this.addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e)
            {
                String ss=null;
                if(e.getKeyCode()==37)
                    chemi.this.x=chemi.this.x-1;
                if(e.getKeyCode()==39)
                    chemi.this.x=chemi.this.x+1;
                if(e.getKeyCode()==38)
                    chemi.this.y=chemi.this.y-1;
                if(e.getKeyCode()==40)
                    chemi.this.y=chemi.this.y+1;
                chemi.this.update(chemi.this.getGraphics());
            }
        });
        setVisible(true);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
    }

    public void paint(Graphics g)
    {
        super.paint(g);
        Graphics2D g2 = (Graphics2D)g;
        g2.drawImage(img1, null, (int)chemi.this.x, (int)chemi.this.y);
    }

    public static void main(String[] pars)
    {
        SwingUtilities.invokeLater
        (
            new Runnable()
            {
                public void run()
                {
                    chemi ex = new chemi();
                }
            }
        );
    }
}
