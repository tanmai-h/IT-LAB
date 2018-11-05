abstract class Shape {
	protected int l, b, h;
	protected double a, p, v;	

	Shape(int l, int b) {
		this.l = l; this.b = b;
	}
	Shape(int l, int b, int h) {
		this.l = l; this.b = b; this.h = h;
	}

	void print() {
		System.out.println("Shape Class");
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
	void print() {
		System.out.println("Rect");
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
	void print() {
		System.out.println("Square");
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
	void print() {
		System.out.println("Circle");
	}
	@Override
	double area() {
		a = (double)(pi * (r * r));
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

class inherit {
	public static void main(String args[]) {
		Shape s = new Rectangle(2,3);
		System.out.println("peri " + s.perimeter());
		s = new Square(2);
		System.out.println("area " + s.area());
		s = new Circle(1);
		System.out.println("circPeri: " + s.perimeter());
	}
}