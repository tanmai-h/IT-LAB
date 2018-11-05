class Car {

private int wheels;

private String color;

public Car() {

}

public String getColor() {

return color;

}

public void setColor(final String color) {

this.color = color;

}

public int getWheels() {

return wheels;

}

public void setWheels(final int wheels) {

this.wheels = wheels;

}

@Override

public String toString() {

return "Car [wheels = " + wheels + ", color = " + color + "]";

}

}

interface CarBuilder {

Car build();

CarBuilder setColor(String color);

CarBuilder setWheels(int wheels);

}

class CarBuilderImpl implements CarBuilder {

private Car car;

public CarBuilderImpl() {

car = new Car();

}

@Override

public Car build() {

return car;

}

@Override

public CarBuilder setColor(String color) {

car.setColor(color);

return this;

}

@Override

public CarBuilder setWheels( int wheels) {

car.setWheels(wheels);

return this;

}

}

public class CarBuildDirector {

private CarBuilder builder;

public CarBuildDirector(CarBuilder builder) {

this.builder = builder;

}

public Car construct() {

return builder.setWheels(5)

.setColor("Green")

.build();

}

public static void main(String[] arguments) {

CarBuilder builder = new CarBuilderImpl();

CarBuildDirector carBuildDirector = new CarBuildDirector(builder);

System.out.println(carBuildDirector.construct());

}

}