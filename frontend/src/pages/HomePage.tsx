import { useState } from 'react'
import WeatherCard from '../components/WeatherCard'
import ConnectionError from '../components/ConnectionError'

function HomePage() {
    const [location, setLocation] = useState('')
    const [weatherData, setWeatherData] = useState({} as WeatherType)
    const [isLoaded, setIsLoaded] = useState(false)
    const [errorMessage, setErrorMessage] = useState('')
    const [isConnected, setIsConnected] = useState(true)
    const baseUrl = "http://127.0.0.1:8000/api/"

    async function get_weather_data(location: string) {
        try {
            setErrorMessage('')
            if (location.length == 0) {
                setErrorMessage("Location cannot be Empty.")
                return
            }
            if (!navigator.onLine) {
                setIsConnected(false)
            }
            else { setIsConnected(true) }
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

    async function refresh_weather_data(location: string) {
        try {
            setErrorMessage('')
            if (location.length == 0) {
                setErrorMessage("Location cannot be Empty.")
                return
            }
            if (!navigator.onLine) {
                setIsConnected(false)
            }
            else { setIsConnected(true) }
            const response = await fetch(baseUrl + 'fetch/', {
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
        <div className='flex flex-col items-center justify-evenly p-4 bg-gradient-to-tr from-cyan-300 to-sky-600 min-h-screen'>
            <p className='text-black text-5xl font-extrabold'>Weather Data</p>
            <div className="flex flex-row justify-center min-w-full">
                <input type="text" name="location" id="location" placeholder='Enter location...' className='m-4 py-4 px-8 bg-gray-200 rounded-full focus:outline-none w-96' value={location} onChange={(e) => setLocation(e.target.value)} />
                <button type="button" className='bg-gray-600 text-white rounded-full m-4 px-6' onClick={async () => await get_weather_data(location)} >Search
                </button>

            </div>
            {isConnected ? <></> : <ConnectionError />}

            {isLoaded ? <div className='flex flex-row'>
                <WeatherCard weatherData={weatherData} />
                <button type="button" className='bg-gray-200 text-slate-800 rounded-full m-4 px-6 max-h-12' onClick={async () => await refresh_weather_data(location)}>Refresh</button>
            </div> : <></>}
            {errorMessage ? <p>{errorMessage}</p> : <></>}
        </div>
    )
}

export default HomePage