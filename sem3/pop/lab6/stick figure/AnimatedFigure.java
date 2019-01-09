import java.applet.*;
import java.awt.*;
public class AnimatedFigure extends Applet{

	private int index =0;
	private int horizmove=0;
	int[] horiz={45,40,35,30};
	int[] vert={70,75,80,80};
	private int sleep=100;
	public void start()
	{
		index=0;
		horizmove=0;
	}
	public void paint(Graphics g){
		g.drawLine(0,80,200,80);
		g.drawOval(15+horizmove,20,25,20);
		g.drawLine (30+horizmove,40,30+horizmove,60);
		g.drawLine (20+horizmove,50,40+horizmove,50);
     		g.drawLine (30+horizmove,60,30+horizmove,80);
     		//g.setColor (Color.GREEN);                     
     		//g.drawLine (30,60,horiz[index],vert[index]);

		++index;
		horizmove+=5;
		if(index==horiz.length)
			index=0;
		if(horizmove==150)
			horizmove=0;
		//g.setColor(Color.BLACK);

		g.drawLine(25+horizmove,60,horiz[index]+horizmove,vert[index]);
		try{
			Thread.sleep(sleep);
		}
		catch(InterruptedException e){
		}
		repaint();
	}
}
/* 
<applet code="AnimatedFigure.class" width="300" height="300"> 
</applet> 
*/