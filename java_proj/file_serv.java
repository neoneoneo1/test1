//Клиент будет работать на постоянный мой адрес
//новый адрес можно присылать по почте

import java.security.PublicKey;
import java.util.*;
import java.text.*;
import java.net.*;
import java.io.*;

public class file_serv
{

    static public void main(String pars[])
    {
        myServ serv=new myServ();
        //Создать поток отдельным методом
        serv.init();
        //Остановить основной (вызывающий) поток и ждать пока не завершиться
        //вызванный поток
        try
        {
            serv.t.join();
        }
        catch(InterruptedException e)
        {
            System.out.println("catch p.t.join()");
        }
        System.out.println("main end\n");
    }
}
