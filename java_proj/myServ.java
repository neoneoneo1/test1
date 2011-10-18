import java.io.*;
import java.net.*;

class myServ implements Runnable
{
    public Thread t=null;
    myServ(){}
    public void init()
    {
        t=new Thread(this, "MyServ");
        t.setDaemon(true);//выполнение в фоне
        t.start();
    }
    public void run()
    {
        try
        {
            int i = 0; //счётчик подключений
            //привинтить сокет на локалхост, порт 3128
            //ServerSocket server = new ServerSocket(80, 0, InetAddress.getByName("localhost"));
            ServerSocket server = new ServerSocket(3128, 0, InetAddress.getByName("localhost"));
            System.out.println("server is started");
            //На каждое соединение создаётся поток который слушает клиента
            //сделать контейнер который будет хранить потоки и проверять/вычищать завершенные
            //при завершении текущего потока myServ нужно пройти по контейнеру и добить работающие потки
            //аварийное завершение
            //найти как прибивать потоки в java
            //слушаем порт
//            while(true)
//            {
//                // ждём нового подключения, после чего
//                // запускаем обработку клиента
//                // в новый вычислительный поток и
//                // увеличиваем счётчик на единичку
//                //new myConn(i, server.accept());
//                new myConn().init(i,server.accept());
//                i++;
//            }
            myConn con=new myConn();
            con.init(i,server.accept());

            try
            {
                con.t.join();
            }
            catch(InterruptedException e)
            {
                System.out.println("catch p.t.join()");
            }
            System.out.println("server end");
        }
        catch(Exception e)
        {
            System.out.println("init error: "+e);
        } // вывод исключений
    }
}
