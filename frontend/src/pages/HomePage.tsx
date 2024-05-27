import React, { useState } from 'react'
import WeatherCard from '../components/WeatherCard'

function HomePage() {
    const [location, setLocation] = useState('')
    const date = new Date("2024-05-27")
    return (
        <div className='flex flex-col items-center justify-evenly p-4 bg-slate-300 min-h-screen'>
            <p className='text-black text-5xl font-extrabold'>Weather Data</p>
            <div className="flex flex-row justify-center min-w-full">
                <input type="text" name="location" id="location" placeholder='Enter location...' className='m-4 py-4 px-8 bg-gray-200 rounded-full focus:outline-none w-96' value={location} onChange={(e) => setLocation(e.target.value)} />
                <button type="button" className='bg-gray-600 text-white rounded-full m-4 px-6'>Search
                </button>

            </div>
            <WeatherCard weatherData={{
                location: {
                    lat: 0,
                    lon: 0,
                    name: 'Kathmandu',
                    region: '',
                    country: 'Nepal',
                    tz_id: '',
                    localtime_epoch: 0,
                    localtime: ''
                },
                last_updated: date,
                last_updated_epoch: 0,
                temp_c: 0,
                temp_f: 0,
                feelslike_c: 0,
                feelslike_f: 0,
                condition: {
                    text: 'Partly Cloudy',
                    icon: '//cdn.weatherapi.com/weather/64x64/day/116.png',
                    code: 1003
                },
                wind_mph: 0,
                wind_kph: 0,
                wind_degree: 0,
                wind_dir: '',
                pressure_mb: 0,
                pressure_in: 0,
                precip_mm: 0,
                precip_in: 0,
                humidity: 0,
                cloud: 0,
                is_day: 0,
                uv: 0,
                gust_mph: 0,
                gust_kph: 0
            }} />
        </div>
    )
}

export default HomePage