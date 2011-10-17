import java.io.*;
import java.net.*;
class myConn implements Runnable
{
    Socket s;
    int numConn;
    public Thread t=null;
    myConn(){}
    public void init(int pnumConn,Socket ps)
    {
        System.out.println("norm");
        // копируем данные
        this.numConn = pnumConn;
        this.s = ps;
        t=new Thread(this, "MyConn");
        t.start();
        //t.setDaemon(true);
        //t.setPriority(NORM_PRIORITY);
    }
    public void run()
    {
        System.out.println("run conn ok");
        try
        {
            // из сокета клиента берём поток входящих данных
            InputStream is = s.getInputStream();
            // и оттуда же — поток данных от сервера к клиенту
            OutputStream os = s.getOutputStream();

            // буффер данных в 64 килобайта
            byte buf[] = new byte[64*1024];
            // читаем 64кб от клиента, результат —
            // кол-во реально принятых данных
            int r = is.read(buf);

            // создаём строку, содержащую полученную от клиента информацию
            String data = new String(buf, 0, r);

            // добавляем данные об адресе сокета:
            data = ""+this.numConn+": "+"\n"+data;

            // выводим данные:
            os.write(data.getBytes());
            //System.out.println(data.getBytes().toString());

            // завершаем соединение
            s.close();
        }
        catch(Exception e)
        {System.out.println("init error: "+e);} // вывод исключений
    }
}
