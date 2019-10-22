import java.applet.Applet;
import java.awt.*;

public class StickMan extends Applet
{
    public void paint(Graphics g)
    {
	   
       setBackground(Color.yellow);
       setForeground(Color.black);
       
       g.drawRect(5,5,190,190);
       g.drawOval(90,60,20,20);
       
       g.drawLine(100,80,100,120);
       
       g.drawLine(100,100,80,80);
       g.drawLine(100,100,120,75);
       
       g.drawLine(100,120,85,135);
       g.drawLine(100,120,115,135);

       // g.drawLine(90,60,85,55);
       // g.drawLine(90,60,82,60);

       g.drawString("Hello.Me StickMANNNNN", 20, 180);
    }    
}
