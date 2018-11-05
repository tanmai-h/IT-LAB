import java.awt.*;
import java.applet.*;
import java.awt.event.*;
public class calApplet extends Applet implements ActionListener{

	Button b1,b2,b3,b4,b5,b6,b7,b8,b9,b0,ba,bs,bd,bm,be,bp,bc,bde;
	TextField tf;
	static int op;
	Double a,b,res;

	public void init(){
		b1=new Button("1");
		b2=new Button("2");
		b3=new Button("3");
		b4=new Button("4");
		b5=new Button("5");
		b6=new Button("6");
		b7=new Button("7");
		b8=new Button("8");
		b9=new Button("9");
		b0=new Button("0");
		ba=new Button("+");
		bs=new Button("-");
		bm=new Button("*");
		bd=new Button("/");
		bp=new Button(".");
		be=new Button("=");
		bc=new Button("Clear");
		bde=new Button("delete");
		tf=new TextField();
		tf.setBounds(30,40,270,30);

		b1.setBounds(30,180,50,50);
		b2.setBounds(100,180,50,50);
		b3.setBounds(170,180,50,50);
		b4.setBounds(30,130,50,50);
		b5.setBounds(100,130,50,50);
		b6.setBounds(170,130,50,50);
		b7.setBounds(30,80,50,50);
		b8.setBounds(100,80,50,50);
		b9.setBounds(170,80,50,50);
		b0.setBounds(30,230,50,50);
		ba.setBounds(240,240,50,40);
		bs.setBounds(240,200,50,40);
		bm.setBounds(240,160,50,40);
		bd.setBounds(240,120,50,40);
		bp.setBounds(100,230,50,50);
		be.setBounds(170,230,50,50);
		bde.setBounds(240,80,50,40);
		bc.setBounds(30,290,80,40);

		add(b1);add(tf); 
add(b2);add(b3);add(b4);add(b5);add(b6);add(b7);add(b8);add(b9);add(b0);add(ba);add(bs);add(bm);add(bd);add(bc);add(bde);add(bp);add(be);
b1.addActionListener(this);
b2.addActionListener(this);
b3.addActionListener(this);
b4.addActionListener(this);
b5.addActionListener(this);
b6.addActionListener(this);
b7.addActionListener(this);
b8.addActionListener(this);
b9.addActionListener(this);
b0.addActionListener(this);
ba.addActionListener(this);
bs.addActionListener(this);
bm.addActionListener(this);
bd.addActionListener(this);
be.addActionListener(this);
bp.addActionListener(this);
bde.addActionListener(this);
bc.addActionListener(this);

 
setLayout(null); 
} 
 
 public void actionPerformed(ActionEvent e){ 
  if(e.getSource()==b1)
  tf.setText(tf.getText().concat("1"));
 if(e.getSource()==b2)
  tf.setText(tf.getText().concat("2"));
 if(e.getSource()==b3)
  tf.setText(tf.getText().concat("3"));
 if(e.getSource()==b4)
  tf.setText(tf.getText().concat("4"));
 if(e.getSource()==b5)
  tf.setText(tf.getText().concat("5"));
 if(e.getSource()==b6)
  tf.setText(tf.getText().concat("6"));
 if(e.getSource()==b7)
  tf.setText(tf.getText().concat("7"));
 if(e.getSource()==b8)
  tf.setText(tf.getText().concat("8"));
 if(e.getSource()==b9)
  tf.setText(tf.getText().concat("9"));
 if(e.getSource()==b0)
  tf.setText(tf.getText().concat("0"));
 if(e.getSource()==bp)
  tf.setText(tf.getText().concat("."));
 if(e.getSource()==ba){
     a=Double.parseDouble(tf.getText());
     op=1;
     tf.setText("");
 }
 if(e.getSource()==bs){
     a=Double.parseDouble(tf.getText());
     op=2;
     tf.setText("");
 }
 if(e.getSource()==bm){
     a=Double.parseDouble(tf.getText());
     op=3;
     tf.setText("");
 }
 if(e.getSource()==bd){
     a=Double.parseDouble(tf.getText());
     op=4;
     tf.setText("");
 }
 if(e.getSource()==be){
     b=Double.parseDouble(tf.getText());

 switch(op){
     case 1:res=a+b;
     break;
     case 2:res=a-b;
     break;
     case 3:res=a*b;
     break;
	 case 4:res=a/b;
     break;

 }
 tf.setText(""+res);
}
 if(e.getSource()==bc){
     tf.setText("");
 }
  if(e.getSource()==bde){
     String s=tf.getText();
     tf.setText("");
     for(int i=0;i<s.length()-1;i++)
     tf.setText(tf.getText()+s.charAt(i));
 }

 
 
  }
}
/*
<applet code="calApplet.class." width="330" height="360">
</applet>
*/
		
	