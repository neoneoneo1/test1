import java.sql.*;
public class swing_bd
{
    public static Connection con;
    private static void doQuery(String query)
    {
        System.out.println(query);
        try
        {
            Statement stmt = con.createStatement();
            ResultSet rs = stmt.executeQuery(query);
            ResultSetMetaData meta = rs.getMetaData();
            int cols  = meta.getColumnCount();
            while (rs.next())
            {
                for(int i=0;i<cols;i++)
                    System.out.print(rs.getString(i+1)+" ");
                System.out.print("\n");
            }
            stmt.close();
            rs.close();
        }
        catch (SQLException e)
        {
            System.out.println("error "+e.getMessage());
        }
        System.out.println("\n");
    }
    private static void doUpdateQuery(String query)
    {
        System.out.println(query);
        try
        {
            Statement stmt = con.createStatement();
            int rows = stmt.executeUpdate(query);
                System.out.print("rows chenged/added "+rows+" \n");
            stmt.close();
        }
        catch (SQLException e)
        {
            System.out.println("error "+e.getMessage());
        }
        System.out.println("\n");
    }
    public static void main(String[] pars)
    {
        try {
            String driverName = "com.mysql.jdbc.Driver";
            Class.forName(driverName);
            con = DriverManager.getConnection("jdbc:mysql://localhost/test", "root", "pass");
            //удаление таблицы
            doUpdateQuery("DROP TABLE IF EXISTS t4");
            //создание таблицы t4
            doUpdateQuery("CREATE TABLE t4(key1 INT(10),pole1 TEXT)");
            //вставка записей в таблицу
            doUpdateQuery("INSERT INTO t4 VALUES(1,'text1'),(2,'text2'),(3,'text3'),(4,'text4')");
            doUpdateQuery(//"SET @c=0;\n" +
                    "DECLARE @c INT;" +
                    "SET @c=0;" +
                    "WHILE @c <= 1000;\n" +
                    "DO;\n" +
                    "BEGIN;\n" +
                    "INSERT INTO t4 VALUES(1,'text1');\n" +
                    "SET @c=@c+1;\n" +
                    "END;\n" +
                    "END WHILE");

            //простой join
            doQuery("SELECT * FROM t1,t2 WHERE t1.key1=t2.key1");
            //тройной join с условием
            doQuery("SELECT * FROM t1 LEFT JOIN t2 USING(key1) LEFT JOIN t3 ON t2.key2=t3.key2 WHERE t3.pole_t3 like 'pole444'");
            //выборка количеств строк с группировкой по полю
            doQuery("SELECT pole_t1, COUNT(*) FROM t1 GROUP BY(pole_t1)");
            //выборка количеств строк с группировкой по полю
            doQuery("SELECT pole_t1, COUNT(*) FROM t1 GROUP BY(pole_t1)");
            //выборка имен колонок из таблицы
            doQuery("SHOW COLUMNS FROM t1");
            //выборка имен таблиц из базы данных
            doQuery("SHOW TABLES FROM test");
            //выборка имен баз данных
            doQuery("SHOW DATABASES");

            //результат вернёт более 1 строки
            //doUpdateQuery("UPDATE t1 SET key1=(select key1 FROM t2 WHERE t2.key1 <3)");
            //doUpdateQuery("UPDATE t1 SET key1=(select key1 FROM t2 WHERE t2.key1 <2)");
            con.close();
        }
        catch (ClassNotFoundException e)
        {
            System.out.println("Could not find the database driver");
        }
        catch (SQLException e)
        {
            System.out.println("Could not connect to the database");
        }
    }
}

