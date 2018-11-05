abstract class Shape {
	protected int l, b, h;
	protected double a, p, v;	

	Shape(int l, int b) {
		this.l = l; this.b = b;
	}
	Shape(int l, int b, int h) {
		this.l = l; this.b = b; this.h = h;
	}

	abstract double area();
	abstract double perimeter();
	abstract double volume();
}

class Rectangle extends Shape {
	Rectangle(int l, int b) {
		super(l, b);
	}

	@Override
	double area() {
		a = l*b;
		return a;
	}

	@Override
	double perimeter() {
		p = 2*(l+b);
		return p;
	}
	@Override
	double volume() {
		return v;
	}
}

class Square extends Rectangle {
	Square(int l) {
		super(l, l);
	}

	@Override
	double perimeter() {
		p = 4*l;
		return p;
	} 
}

class Circle extends Shape {
	final double pi = 3.14159;
	int r;
	Circle(int r) {
		super(0,0);
		this.r = r;
	}
	@Override
	double area() {
		a = (double)(pi * (r * r));
		System.out.println("arsdea " + a);
		return a;
	}

	@Override
	double perimeter() {
		p = (double)(2* pi * r);
		return p;
	}

	@Override
	double volume() {
		return 0;
	}
}
class crap {
	public static void main(String args[]) {
		Shape s = new Rectangle(2,3);
		System.out.println("area " + s.perimeter());
		s = new Square(2);
		System.out.println("area " + s.perimeter());
	}
}