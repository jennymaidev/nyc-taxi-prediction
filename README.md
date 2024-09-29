# NYC Iconic Yellow Taxi Cost Estimation for Travellers

## Navigating NYC: Taxi Fare Insights & Travel Tips for Tourists

**Author**: Jenny Mai (mtqn0310@gmail.com)

## Introduction

In the bustling streets of New York City, where every minute counts and every block is a new adventure, the humble yellow taxi is more than just a mode of transportation—it's an essential part of the city's pulse. This report dives deep into NYC taxi data to provide comprehensive analysis and actionable insights that will empower tourists to make informed decisions, ensuring a smooth experience.

## Preprocessing

### Descriptive Statistics and Outlier Analysis

- **Trip Distance**: Initial data showed a mean trip distance of about 4.47 miles. Trips under 0.2 miles and over 75 miles were considered outliers.
- **Fare Amount**: Mean fare was $8.62, with outliers including negative fares and a maximum of $5901.74.
- **Passenger Count**: Average count was 1.38, with outliers from 0 to 9 passengers.

### Data Cleaning

- Missing data was handled by removing rows with missing values, resulting in the loss of about 500,000 entries.
- Outliers and invalid values were removed to ensure realistic and reliable data.

### Data Transformation

- Numerical features were standardized using the `StandardScaler`.
- Right-skewed numeric features like trip duration and distance were log-transformed.

### Feature Engineering

- **Temporal Features**: Extracted features like trip duration, pickup/dropoff hours, and day of the week.
- **Geospatial Features**: Identified if trips started or ended at key locations like airports.
- **Environmental Features**: Integrated weather data to analyze its influence on taxi trips.

## Analysis and Geospatial Visualisation

### Geospatial Analysis

- **Average Fare Amount by Drop-off Location**: Higher fares are concentrated in specific areas, such as southern Staten Island.
- **Trip Density by Pickup Location**: High concentrations in central Manhattan and JFK Airport.
- **Peak Pickup Hours by Location**: Varies by location, with business districts peaking from 3 PM to midnight.

### Temporal Analysis

- **Average Trip Duration by Hour of Day**: Peaks between 4 PM and 6 PM, coinciding with rush hours.
- **Trip Density and Fare Amount by Time of Day and Day of the Week**: Higher fares observed during early morning hours on Mondays and Tuesdays.

## Modelling

### Performance Metrics

The models were evaluated using metrics like RMSE, MAE, and R².

| Model                  | RMSE | MAE  | R²  |
|------------------------|------|------|-----|
| Linear Regression      | 7.46 | 3.82 | 0.78|
| Lasso Regression       | 7.58 | 3.94 | 0.77|
| Random Forest Regressor| 7.97 | 4.65 | 0.78|
| Gradient Boosted Trees | 3.96 | 1.88 | 0.94|

### Feature Analysis

- **Gradient Boosted Trees (GBT)** showed the best performance, being particularly reliable for predicting taxi fares due to its ability to handle complex interactions between features.

## Recommendations

1. **Plan for Higher Fares During Early Morning Airport Transfers**: Expect higher fares from 4 AM to 7 AM on weekdays.
2. **Avoid High-Density Times on Friday and Saturday Evenings**: Consider alternative transport from 5 PM to 8 PM.
3. **Utilize Off-Peak Times for Cheaper Rides and Leisure Activities**: Mid-morning hours and early afternoons on weekdays offer lower fares and less congestion.

## Conclusion

This report provides valuable insights into NYC taxi data, helping tourists make informed decisions and optimize their travel experiences. Through data preprocessing and analysis, we identified key factors affecting fares and trip durations, supported by robust modelling to predict fares accurately.

## References

- National Oceanic and Atmospheric Administration (NOAA), "Climate Data Online". Available at: [NOAA Climate Data](https://www.weather.gov/wrh/Climate?wfo=okx)
- Scikit-learn, "Scikit-learn: Machine Learning in Python". Available at: [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- New York City Taxi and Limousine Commission, "NYC Taxi and Limousine Service Trip Record Data". Available at: [NYC Taxi Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
