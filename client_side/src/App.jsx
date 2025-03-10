import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [array, setArray] = useState([])

  const fetchApi = async () => {
    const url = "http://127.0.0.1:8080/api/users";
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
      }
  
      const data = await response.json();
      setArray(data.users);
    } catch (error) {
      console.error(error.message);
    }

  }
  useEffect(() =>{
    fetchApi()
  },[])


  return (
    <>
  
        <p>
          {array.map((user, index) =>(
            <span key ={index}>
              <li>{user}</li>
            </span>
          ))}
      </p>
    </>
  )
}

export default App
