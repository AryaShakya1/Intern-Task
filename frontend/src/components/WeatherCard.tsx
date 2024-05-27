
function WeatherCard({ weatherData }: { weatherData: WeatherType }) {
    const lastUpdated = new Date(weatherData.last_updated).toLocaleString()
    return (
        <div className='flex flex-col bg-blue-200 rounded-xl p-4 m-2'>
            <p className='text-4xl p-2 font-bold'>{weatherData.location.name}, {weatherData.location.country}</p>
            <p className='text-3xl p-2'>{weatherData.temp_c}°C / {weatherData.temp_f}°F</p>
            <p className='text-xl p-2'>Feels like: {weatherData.feelslike_c}°C / {weatherData.feelslike_f}°F</p>
            <div className="flex flex-row">
                <p className='text-xl p-2'>Condition: {weatherData.condition.text}</p>
                <img src={weatherData.condition.icon} alt="Weather Icon" height={40} width={40} />
            </div>
            <p className='text-xl p-2'>Wind: {weatherData.wind_kph} kph / {weatherData.wind_mph} mph       {weatherData.wind_degree} {weatherData.wind_dir}</p>
            <p className='text-xl p-2'>Wind: {weatherData.wind_kph} kph / {weatherData.wind_mph} mph       {weatherData.wind_degree} {weatherData.wind_dir}</p>
            <p className='text-xl p-2'>UV: {weatherData.uv} </p>
            <div className="mt-4"></div>
            <p className='text-sm p-2 text-gray-700'>Updated at: {lastUpdated}</p>
        </div>

    )
}

export default WeatherCard