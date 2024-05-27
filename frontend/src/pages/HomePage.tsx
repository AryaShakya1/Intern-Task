import React, { useState } from 'react'
import WeatherCard from '../components/WeatherCard'

function HomePage() {
    const [location, setLocation] = useState('')
    const [weatherData, setWeatherData] = useState({} as WeatherType)
    const [isLoaded, setIsLoaded] = useState(false)
    const [errorMessage, setErrorMessage] = useState('')
    const baseUrl = "http://127.0.0.1:8000/api/"

    async function get_weather_data(location: string) {
        try {
            setErrorMessage('')
            if (location.length == 0) {
                setErrorMessage("Location cannot be Empty.")
                return
            }
            const response = await fetch(baseUrl, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ location: location })
            })
            if (response.ok) {
                const data = await response.json()
                setWeatherData(data)
                setIsLoaded(true)
            }
        } catch (error) {
            console.log(error);

        }
    }


    return (
        <div className='flex flex-col items-center justify-evenly p-4 bg-slate-300 min-h-screen'>
            <p className='text-black text-5xl font-extrabold'>Weather Data</p>
            <div className="flex flex-row justify-center min-w-full">
                <input type="text" name="location" id="location" placeholder='Enter location...' className='m-4 py-4 px-8 bg-gray-200 rounded-full focus:outline-none w-96' value={location} onChange={(e) => setLocation(e.target.value)} />
                <button type="button" className='bg-gray-600 text-white rounded-full m-4 px-6' onClick={async () => await get_weather_data(location)} >Search
                </button>

            </div>
            {isLoaded ? <WeatherCard weatherData={weatherData} /> : <></>}
            {errorMessage ? <p>{errorMessage}</p> : <></>}
        </div>
    )
}

export default HomePage