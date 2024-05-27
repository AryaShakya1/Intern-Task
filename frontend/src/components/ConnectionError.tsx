
function ConnectionError() {
    return (
        <div className='flex flex-col bg-red-200 rounded-xl p-4 m-2'>
            <p className='text-xl'>Connection Error!</p>
            <p> Not Connected to Internet</p>
            <p> Showing cached data if available</p>
        </div>

    )
}

export default ConnectionError