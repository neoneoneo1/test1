import com.sun.xml.internal.ws.util.ByteArrayBuffer;

import org.w3c.dom.*;
import javax.xml.parsers.*;
import javax.xml.transform.*;
import javax.xml.transform.dom.*;
import javax.xml.transform.stream.*;

import java.io.*;
import java.lang.reflect.Array;
import java.math.BigInteger;
import java.net.*;
import java.security.*;
import java.util.*;
class myConn implements Runnable
{
    Socket s;
    int numConn;
    public Thread t=null;
    ByteArrayBuffer bufMsg;
    myConn(){}
    public void init(int pnumConn,Socket ps)
    {
        bufMsg=new ByteArrayBuffer();
        this.numConn = pnumConn;
        this.s = ps;
        t=new Thread(this, "MyConn");
        t.start();
        //t.setDaemon(true);
        //t.setPriority(NORM_PRIORITY);
    }

    //Функция проверки пароля
    private boolean checkPass(byte[] msg)
    {
         try
        {
            //Контрольная сумма в виде md5 для сравнения с такой же полученной для авторизации
            //в каждой посылке должна быть, первые 20 байт
            String passPhrase="pass:"+"christian1980";
            byte passBytes[] = passPhrase.getBytes();
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] passDigest = md.digest(passBytes);
            //Сброс буфера для сообщений
            bufMsg.reset();
            //запись всего сообщения
            bufMsg.write(msg);//дописывает в конец буффера
            //Проверка пароля
            if(Arrays.equals(Arrays.copyOf(bufMsg.getRawData(),passDigest.length),passDigest))
                return true;
        }
        catch(Exception e)
        {
            System.out.println("init error: "+e);
        }
        return false;
    }

    private String getXmlRezAsString()
    {
        String xmlString="";
        try
        {
            /////////////////////////////
            // Creating an empty XML Document
            // We need a Document
            DocumentBuilderFactory dbfac = DocumentBuilderFactory.newInstance();
            DocumentBuilder docBuilder = dbfac.newDocumentBuilder();
            Document doc = docBuilder.newDocument();
            ////////////////////////
            // Creating the XML tree
            //создание рутового элемента
            Element root = doc.createElement("root");
            doc.appendChild(root);
            //создние комента
            Comment comment = doc.createComment("Just a thought");
            //прицепка комента к узлу рута
            root.appendChild(comment);

            //создание дочернего элемента
            Element child = doc.createElement("child");
            //задание атрибутов для дочернего узла
            child.setAttribute("name", "value");
            //прицепка дочернего элемента к руу
            root.appendChild(child);
            //создание текста для дочернего элемента
            Text text = doc.createTextNode("Filler, ... I could have had a foo!");
            //прицепка текста к дочернему элементу
            child.appendChild(text);
            /////////////////
            // Output the XML
            // set up a transformer
            TransformerFactory transfac = TransformerFactory.newInstance();
            Transformer trans = transfac.newTransformer();
            trans.setOutputProperty(OutputKeys.OMIT_XML_DECLARATION, "yes");
            trans.setOutputProperty(OutputKeys.INDENT, "yes");
            // create string from xml tree
            StringWriter sw = new StringWriter();
            StreamResult result = new StreamResult(sw);
            DOMSource source = new DOMSource(doc);
            trans.transform(source, result);
            xmlString = sw.toString();
            // print xml
            System.out.println("Here's the xml:\n\n" + xmlString);
            //System.out.println(doc.toString());
        }
        catch (Exception e)
        {
           System.out.println(e);
        }
        return xmlString;
    }

    private boolean doCommand()
    {
        String path="c:";
        String separ="\\";
        File f=new File(path+separ);
        //вывести все папки
        for(int i=0;i<f.list().length;i++)
        {
            File fl=new File(path+separ+f.list()[i]);
            if(fl.isDirectory())
                System.out.println(f.list()[i]+"\t\t==DIR==");
        }
        //вывести все НЕ папки
        for(int i=0;i<f.list().length;i++)
        {
            File fl=new File(path+separ+f.list()[i]);
            if(!fl.isDirectory())
                System.out.println(f.list()[i]+"====size:"+fl.length()/(1024)+"Kb");
        }
        return true;
    }

    //отправка файла клиенту
    private byte[] sendFile(String path,OutputStream os)
    {
        byte[] by=null;
        try
        {
            File f=new File(path);
            FileInputStream inp=new FileInputStream(f);
            by=new byte[1024];
            //Читать файл по 1024байта кусками, пока в нем есть байты
            //потом перейти на каналы
            while(inp.available()!=0)
            {
                System.out.println("читается, осталось:"+inp.available()+" байт");
                //Читаем из файла
                inp.read(by,0,by.length);
                //Пишем в сеть
                os.write(by);
            }
            System.out.println("Весь файл прочитан, осталось:"+inp.available()+" байт");
            inp.close();
        }
        catch(Exception e)
        {System.out.println("file: "+e);} // вывод исключений
        return by;
    }

    //приём файла от клиента, потом учесть метки пароля
    private boolean reciveFile(String path,InputStream is)
    {
        byte[] by=null;
        try
        {
            File f=new File(path);
            FileOutputStream outp=new FileOutputStream(f);
            //by=new byte[1024];
            by=new byte[32];
            //Читать файл по 1024байта кусками, пока в нем есть байты
            //потом перейти на каналы
            while(is.available()>0)
            {
                System.out.println("Пишеться файл, записалось:"+is.available()+" байт");
                is.read(by);
                outp.write(by);
            }
            System.out.println("Весь файл записан, осталось:"+is.available()+" байт");
            outp.close();
        }
        catch(Exception e)
        {System.out.println("file: "+e);} // вывод исключений
        return true;
    }

    public void run()
    {
        //doCommand();
        System.out.println("run conn ok");
        try
        {
            // из сокета клиента берём поток входящих данных
            InputStream is = s.getInputStream();
            // и оттуда же — поток данных от сервера к клиенту
            OutputStream os = s.getOutputStream();

            reciveFile("c:\\Archive.rar",is);
//            boolean bEnd=false;
//            while(!bEnd)
//            {
//                //Если есть байты для чтения, читаем
//                if(is.available()>0)
//                {
//                    byte[] msg = new byte[is.available()];
//                    is.read(msg);
//                    //Если пароль в сообщении в виде md5 подошёл
//                    if(checkPass(msg))
//                    {
//                        //to do
//                    }
//                }
//            }
            s.close();
//
//            // создаём строку, содержащую полученную от клиента информацию
//            String data = new String(buf, 0, r);
//
//            // добавляем данные об адресе сокета:
//            data = ""+this.numConn+": "+"\n"+data;
//
//            // выводим данные:
//            os.write(data.getBytes());
//
//            //byte[] bytesOfMessage = data.getBytes("UTF-8");
//            MessageDigest md = MessageDigest.getInstance("MD5");
//            byte[] thedigest = md.digest(buf);
//            //String digStr=new String(thedigest,0,thedigest.length);
//            System.out.println("md5:"+String.format("%x",new BigInteger(thedigest)));


//            thedigest = md.digest(buf);
//            digStr=new String(thedigest,0,thedigest.length);
//            System.out.println("md5:"+digStr);
            // завершаем соединение
            //s.close();



            //System.out.println(passDigest.length);
            //String digStr=new String(thedigest,0,thedigest.length);
            //System.out.println("md5:"+String.format("%x",new BigInteger(passDigest)));
        }
        catch(Exception e)
        {System.out.println("init error: "+e);} // вывод исключений
    }
}
