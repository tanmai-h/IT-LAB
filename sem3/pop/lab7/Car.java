
import java.applet.*;
import java.awt.*;
import java.lang.*;
//Applet code
/*<applet code="AnimatedCar" height=800 width=700>
</applet> */
//Main Class
public class Car extends Applet
{ 
int a; 
int b; 
int c;
void car()                  
{
try 
{
Thread.sleep(200);
}  
catch(Exception ex) 
{      
}
}
public void init() 
{
b=30;
a=20;
}
//Draw moving car
public void paint(Graphics g) 
{            
setBackground(Color.white);            
c=getWidth();        
Color col1=new Color(0,204,204);        
Color col2=new Color(0,0,255);        
g.setColor(col1);       
//draw a line over which the car moves
g.drawLine(0,b+75,c,b+75); 
//Draw car       
g.setColor(col2);        
g.fillRoundRect(a,b+20,100,40,5,5);        
g.fillArc(a+90,b+20,20,40,270,180);        
g.setColor(col1);              
g.fillRoundRect(a+10,b,70,25,10,10);        
g.setColor(Color.red);                
g.fillRect(a+20,b+5,20,25);        
g.fillRect(a+50,b+5,20,25);        
g.setColor(Color.black);        
g.fillRoundRect(a+55,b+10,10,20,10,10);                  
g.fillOval(a+10,b+50,25,25);        
g.fillOval(a+60,b+50,25,25);        
g.setColor(Color.yellow);                  
g.fillOval(a+15,b+55,10,10);        
g.fillOval(a+65,b+55,10,10);         
a=a+10; 
car();           
if(a+100<c) 
{    
repaint(); 
}
else
{ 
repaint(); 
a=20; 
b+=30; 
}
}
}
