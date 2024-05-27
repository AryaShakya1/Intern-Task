function timeAgo(date: Date) {
    const seconds = Math.floor((new Date().valueOf() - date.valueOf()) / 1000);

    const interval = Math.floor(seconds / 31536000);

    if (interval > 1) {
        return interval + " years ago";
    }
    if (interval === 1) {
        return interval + " year ago";
    }

    const months = Math.floor(seconds / 2628000);
    if (months > 1) {
        return months + " months ago";
    }
    if (months === 1) {
        return months + " month ago";
    }

    const days = Math.floor(seconds / 86400);
    if (days > 1) {
        return days + " days ago";
    }
    if (days === 1) {
        return days + " day ago";
    }

    const hours = Math.floor(seconds / 3600);
    if (hours > 1) {
        return hours + " hours ago";
    }
    if (hours === 1) {
        return hours + " hour ago";
    }

    const minutes = Math.floor(seconds / 60);
    if (minutes > 1) {
        return minutes + " minutes ago";
    }
    if (minutes === 1) {
        return minutes + " minute ago";
    }

    return "just now";
}


function WeatherCard({ weatherData }: { weatherData: WeatherType }) {
    const lastUpdatedDate = new Date(weatherData.last_updated)
    const lastUpdated = timeAgo(lastUpdatedDate)
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