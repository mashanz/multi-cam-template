/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package multicaminterface;

import com.mysql.jdbc.Connection;
import com.mysql.jdbc.Statement;
import java.sql.DriverManager;
import java.sql.ResultSet;
import javax.swing.JOptionPane;

/**
 *
 * @author zalphe
 */
public class Database {
    private String dbuser = "root";
    private String dbpasswd = "op3nk3y";   
    public Connection con = null;
    public Statement stmt = null;
    public ResultSet rs = null;
    
    public Database(){
        systemDatabase();
    }
    
    public void systemDatabase(){
        try {
            Class.forName("com.mysql.jdbc.Driver");
            con = (Connection) DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/dbmulticam", dbuser, dbpasswd);
            stmt=(Statement) con.createStatement();
        } catch(Exception e){
            JOptionPane.showMessageDialog(null, "Error : "+e.getMessage(),"JDBC Driver Error",JOptionPane.WARNING_MESSAGE);
        }
                   
    }
}
