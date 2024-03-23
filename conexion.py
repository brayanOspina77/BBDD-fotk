



public class Conexion {
    
   
        
        try {
            Class.forName("com.mysql.jdbc.Driver"); 
            con = (Connection) DriverManager.getConnection(url, user, pass);
            System.out.println("Conexion Correcta");
            
            return con;
            
        
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(Conexion.class.getName()).log(Level.SEVERE, null, ex);
        } 
        
    
    
}
