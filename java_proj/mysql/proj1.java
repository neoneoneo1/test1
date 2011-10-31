import java.sql.*;
public class proj1
{
    public static void main(String[] pars)
    {
        Connection con;
        try {
            // Название драйвера
            String driverName = "com.mysql.jdbc.Driver";
            Class.forName(driverName);
            con = DriverManager.getConnection("jdbc:mysql://localhost/test", "root", "pass");
            //System.out.println("is connect to DB" + connection);

            String query = "Select * FROM t1 LEFT JOIN t2 USING(key1) LEFT JOIN t3 ON t2.key2=t3.key2 WHERE t3.text_pole3 like 'pole444'";
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
            con.close();
        }
        catch (ClassNotFoundException e)
        {
            //e.printStackTrace();
            // Could not find the database driver
            System.out.println("Could not find the database driver");
        }
        catch (SQLException e)
        {
            //e.printStackTrace();
            System.out.println("Could not connect to the database");
            // Could not connect to the database
        }
    }
}

