import org.example.CurrentConditionsDisplay;
import org.example.ForecastDisplay;
import org.example.WeatherData;
import org.junit.jupiter.api.*;

public class WeatherTest {
    WeatherData weatherData = new WeatherData();
    CurrentConditionsDisplay currentDisplay = new CurrentConditionsDisplay(weatherData);
    ForecastDisplay forecastDisplay = new ForecastDisplay(weatherData);

    @BeforeAll
    public static void init() {
        System.out.println("Weather Station Testing");
    }

    @Test
    public void test1() {
        weatherData.setMeasurements(80, 65, 30.4f);
    }

    @Test
    public void test2() {
        weatherData.setMeasurements(300, 99, 17.3f);
    }

    @Test
    public void nullCheck() {

    }
}
