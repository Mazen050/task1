# Weather CLI Application

This is a command-line interface (CLI) weather application that fetches and displays current weather information for a specified city using [weatherapi.com](https://www.weatherapi.com/).

## Features

- Fetch current weather data from WeatherAPI.
- Display weather information in a user-friendly format.
- Simple command-line interface.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Mazen050/task1.git
   ```

2. Navigate to the project directory:
   ```
   cd Task1
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Add your WeatherAPI key to a `.env` file:
   ```
   WEATHER_API_KEY="your_api_key"
   ```

## Usage

To run the application, use the following command:
```
python main.py
```

Follow the prompt to enter the city name for which you want to fetch the weather information.

## Dependencies

- requests: For making HTTP requests to the weather API.
- python-dotenv: For loading environment variables from `.env` file.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.